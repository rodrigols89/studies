# `Criando (implementando) o chat da aplicação`

## Conteúdo

 - [`Criando o app chat`](#create-chat-app)
 - [`Convertendo a pergunta do usuário em um embedding: embed_query.py`](#embed-query)
 - [`Buscando os chunks mais similares (em relação a pergunta do usuário) com "Cosine Distance": vector_search.py`](#vector-search)
 - [`Criando (implementando) o services/qa_service.py`](#create-qa-service)
 - [`Criando (implementando) a view (ação): ask_view()`](#create-ask-view)
 - [`Criando a ROTA/URL ask e relacionando com a view (ação) ask_view() + projeto`](#create-ask-url)
 - [`Atualizando o módulo answer_generator.py`](#update-answer-generator)
 - [`Atualizando o módulo context_builder.py`](#update-context-builder)
 - [`Atualizando a criação do inventário (file_directory.py)`](#update-file-directory)
 - [`Atualizando a view (ação) users/views.py::home_view()`](#update-home-view)
 - [`Criando a view (ação) workspace/views.py::folder_view()`](#create-folder-view)
 - [`Criando o HTML (e JavaScript) necessário para criar o chat`](#create-chat-html-js)
<!---
[WHITESPACE RULES]
- 50
--->



















































---

<div id="create-chat-app"></div>

## `Criando o app chat`

> Uma coisa importante no desenvolvimento de software é dividir as responsabilidades.

Sabendo disso, vamos criar um app chamado `chat` que será responsável por lidar com as perguntas e respostas do nosso chatbot:

```bash
python manage.py startapp chat
```



















































---

<div id="embed-query"></div>

## `Convertendo a pergunta do usuário em um embedding: embed_query.py`

> Quando o usuário faz uma pergunta, primeiro é necessário transformar essa pergunta em `embedding`, para só depois fazer uma *Busca de Similaridade (tipo, uma comparação)*.

**Exemplo:**
```bash
"Como funciona o Docker?"

↓

[0.18, -0.24, 0.72, 0.10, ...]
```

### `Código Completo`

A nossa função `embed_query()` (completa) vai ficar da seguinte maneira:

[retrieval/embed_query.py](../../../rag/services/retrieval/embed_query.py)
```python
from typing import List

from rag.services.ingestion.embeddings import (
    get_embedding_model,
)


def embed_query(
    *,
    question: str,
) -> List[float]:
    """
    Converte a pergunta do usuário em um vetor
    de embedding utilizando o mesmo modelo
    usado na ingestão dos documentos.
    """

    model = get_embedding_model()

    query_vector: List[float] = model.embed_query(
        question
    )

    return query_vector
```



















































---

<div id="vector-search"></div>

## `Buscando os chunks mais similares (em relação a pergunta do usuário) com "Cosine Distance": vector_search.py`

Agora, nós vamos criar o módulo que busca os chunks mais similares em relação a pergunta do usuário com `Cosine Distance`.

> **⚠️ NOTE:**  
> Ou seja, este módulo será responsável pela fase de recuperação semântica (retrieval).

### `Exemplo visual de busca vetorial`

Imagine que o banco possui embeddings de documentos:

```bash
Doc 1 → "Docker containers..."
Doc 2 → "Kubernetes orchestration..."
Doc 3 → "Python virtual environments..."
```

Pergunta do usuário:

```bash
"Como funciona container Docker?"
```

Vetores comparados:

```bash
Docker doc      → distância 0.08
Kubernetes doc  → distância 0.27
Python doc      → distância 0.71
```

**RESULTADO:**
```bash
1️⃣ Docker doc
2️⃣ Kubernetes doc
```

Esses documentos serão usados para montar o contexto do LLM.

### `Código Completo`

A nossa função `vector_search()` (completa) vai ficar da seguinte maneira:

[retrieval/vector_search.py](../../../rag/services/retrieval/vector_search.py)
```python
from typing import List

from pgvector.django import CosineDistance

from rag.models import DocumentEmbedding


def vector_search(
    *,
    user_id: int,
    query_vector: List[float],
    top_k: int = 5,
) -> List[DocumentEmbedding]:
    """
    Busca os chunks mais similares à pergunta do usuário
    utilizando cosine distance.
    """

    results = (
        DocumentEmbedding.objects
        .filter(user_id=user_id)
        .annotate(
            distance=CosineDistance(
                "embedding",
                query_vector,
            )
        )
        .order_by("distance")[:top_k]
    )

    return list(results)
```

### `Testando manualmente`

Agora, vamos criar alguns códigos que serão responsáveis por testar (manualmente) se a função `vector_search()` mostrar os textos (chunks) mais similares:

```python
import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "core.settings"
)

django.setup()

from rag.services.retrieval.embed_query import embed_query
from rag.services.retrieval.vector_search import vector_search

question = "Quem é a secretária de educação do município de Remígio?"

query_vector = embed_query(
    question=question
)

chunks = vector_search(
    user_id=1,
    query_vector=query_vector,
    top_k=5,
)

for chunk in chunks:
    print(chunk.content)
```

**OUTPUT:**
```bash
Secretária Municipal de Educação Remígio-PB
Roseluce dos Santos Souza

Secretária Municipal de Educação
Articulador Municipal do Selo UNICEF 2025-2028

Comissão Intersetorial do SELO UNICEF



_____________________________________________________

Luis Cláudio Régis Marinho

Prefeito(a) Municipal de Remígio
Articulador Municipal do Selo UNICEF 2025-2028

Comissão Intersetorial do SELO UNICEF



_____________________________________________________

Luis Cláudio Régis Marinho

Prefeito(a) Municipal de Remígio
Remígio-PB

                Telefone: (83) 3364-1700

                e-mail: secsauderemigio@gmail.com


RECIBO DE ENTREGA DE CHAVES

Declaro que recebi nesta data, 03/02/2025, da Secretaria de Educação de Remígio, os seguintes materiais:

Chaves da ESCOLA MUNICIPAL DE ENSINO FUNDAMENTAL MANOEL JOCA.
```

> **⚠️ NOTE:**  
> Aqui nós utilizamos `chunk.content`, mas poderia ser qualquer campo em [DocumentEmbedding()](../../../rag/models.py).



















































---

<div id="create-qa-service"></div>

## `Criando (implementando) o services/qa_service.py`

 - O arquivo `qa_service.py` é a interface principal do nosso sistema RAG.
 - Ele conecta todos os módulos do pipeline de pergunta-resposta e expõe uma única função pública para o resto da aplicação.
 - Na prática, ele transforma uma pergunta do usuário em uma resposta utilizando os documentos do workspace.

### `Implementando a função ask()`

Aqui, nós vamos implementar a função `ask()` que vai receber:

 - o `user_id` (para garantir isolamento do workspace)
 - a pergunta do usuário

Depois ela vai:

 - 1️⃣ gera o embedding da pergunta
 - 2️⃣ busca os chunks mais relevantes
 - 3️⃣ monta o contexto
 - 4️⃣ envia o contexto para o LLM
 - 5️⃣ retorna a resposta final

**O papel do qa_service.py:**
| Arquivo           | Responsabilidade  |
| ----------------- | ----------------- |
| `embed_query`     | vetor da pergunta |
| `vector_search`   | busca semântica   |
| `build_context`   | monta contexto    |
| `generate_answer` | gera resposta     |
| `qa_service`      | conecta tudo      |

> **O que nós ganhamos com isso?**

Agora, o nosso sistema inteiro pode ser usado assim:

```python
answer = ask(user_id=1, question="O que é Docker?")
```

### `Código Completo`

A nossa função `ask()` (completa) vai ficar da seguinte maneira:

[rag/services/qa_service.py](../../../rag/services/qa_service.py)
```python
from typing import Any, Dict

from rag.services.generation.answer_generator import (
    generate_answer,
)
from rag.services.generation.context_builder import (
    build_context,
)
from rag.services.retrieval.embed_query import (
    embed_query,
)
from rag.services.retrieval.vector_search import (
    vector_search,
)


def ask(
    *,
    user_id: int,
    question: str,
    top_k: int = 5,
) -> Dict[str, Any]:

    # 1️⃣ Gerar embedding da pergunta
    query_vector = embed_query(
        question=question
    )

    # 2️⃣ Buscar chunks mais relevantes
    chunks = vector_search(
        user_id=user_id,
        query_vector=query_vector,
        top_k=top_k,
    )

    if not chunks:
        return {
            "answer": (
                "Não encontrei informações relevantes nos seus documentos.",
            ),
            "sources": [],
        }

    # 3️⃣ Construir contexto + fontes
    context, sources = build_context(
        chunks=chunks,
        user_id=user_id,
    )

    # 4️⃣ Gerar resposta com LLM
    answer = generate_answer(
        question=question,
        context=context,
    )

    # 5️⃣ Retorno padronizado
    return {
        "answer": answer,
        "sources": sources,
    }
```

### `Testando manualmente`

Agora, vamos criar alguns códigos que serão responsáveis por testar (manualmente) se a função `ask()` consegue responder corretamente:

```python
import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "core.settings"
)

django.setup()

from rag.services.qa_service import ask

question = "Quem é a secretária de educação do município de Remígio?"

answer = ask(
    user_id=1,
    question=question,
    top_k=5
)

print("Type:", type(answer))
print(answer)
```

**OUTPUT:**
```bash
Type: <class 'dict'>
{'answer': 'A secretária de educação do município de Remígio é Roseluce dos Santos Souza.', 'sources': [{'file_id': 32, 'file_name': 'RECIBO DE ENTREGA DE DOCUMENTOS.docx', 'folder_id': 22}, {'file_id': 17, 'file_name': 'Aline - Gabinete.docx', 'folder_id': 17}, {'file_id': 23, 'file_name': 'Ubiratan Marques - selo unicef.docx', 'folder_id': 14}, {'file_id': 22, 'file_name': 'Conselho.docx', 'folder_id': 14}, {'file_id': 30, 'file_name': 'RECIBO DE CHAVES.docx', 'folder_id': 22}]}
```

Vejam que nós temos um dicionário (dict) que tem:

 - A resposta (answer)
 - Fontes (sources)

Uma visão mais estrutura desse dicionário é a seguinte:

```python
{
    'answer': 'A secretária de educação do município de Remígio é Roseluce dos Santos Souza.',
    'sources': [
         {
            'file_id': 32,
            'file_name': 'RECIBO DE ENTREGA DE DOCUMENTOS.docx',
            'folder_id': 22
        },
        {
            'file_id': 17,
            'file_name': 'Aline - Gabinete.docx',
            'folder_id': 17
        },
        {
            'file_id': 23,
            'file_name': 'Ubiratan Marques - selo unicef.docx',
            'folder_id': 14
        },
        {
            'file_id': 22,
            'file_name': 'Conselho.docx',
            'folder_id': 14
        },
        {
            'file_id': 30,
            'file_name': 'RECIBO DE CHAVES.docx',
            'folder_id': 22
        }
    ]
}
```

















































---

<div id="create-ask-view"></div>

## `Criando (implementando) a view (ação): ask_view()`

> Agora, nós vamos criar uma view (ação) que **vai receber a pergunta do usuário** e **retornar a resposta**.

### `Código Completo`

A nossa view (ação) `ask_view()` (completa) vai ficar da seguinte maneira:

[chat/views.py](../../../chat/views.py)
```python
from typing import Any, Dict, List

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from rag.services.qa_service import ask


@login_required(login_url="/")
def ask_view(request: HttpRequest) -> HttpResponse:

    chat_history: List[Dict[str, Any]] = request.session.get(
        "chat_history",
        [],
    )

    if request.method != "POST":
        context: Dict[str, Any] = {
            "chat_history": chat_history,
        }
        return render(request, "pages/home.html", context)

    question: str = request.POST.get("question", "").strip()

    if not question:
        context: Dict[str, Any] = {
            "chat_history": chat_history,
        }
        return render(request, "pages/home.html", context)

    user_id: int = request.user.id

    try:
        # 🔥 AGORA O ASK DEVE RETORNAR UM DICT
        result: Dict[str, Any] = ask(
            user_id=user_id,
            question=question,
        )

        answer: str = result.get("answer", "")
        sources: List[Dict[str, str]] = result.get("sources", [])

    except Exception as error:
        print("ERRO RAG:", error)
        answer = "Erro ao processar sua pergunta."
        sources = []

    # 👤 mensagem do usuário
    user_message: Dict[str, Any] = {
        "role": "user",
        "content": question,
    }

    # 🤖 mensagem do assistente (COM FONTES)
    assistant_message: Dict[str, Any] = {
        "role": "assistant",
        "content": answer,
        "sources": sources,  # 🔥 NOVO
    }

    chat_history.append(user_message)
    chat_history.append(assistant_message)

    request.session["chat_history"] = chat_history
    request.session.modified = True

    context: Dict[str, Any] = {
        "chat_history": chat_history,
    }

    return render(request, "pages/home.html", context)
```



















































---

<div id="create-ask-url"></div>

## `Criando a ROTA/URL ask e relacionando com a view (ação) ask_view() + projeto`

Aqui, vamos começar criando a ROTA/URL `ask` nas URLs do app `chat`:

[chat/urls.py](../../../chat/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [
    path(
        route="ask/",
        view=views.ask_view,
        name="ask"
    ),
]
```

Agora, vamos vamos relacionar as ROTAS do projeto com as URLs do app `chat`:

[core/urls.py](../../../core/urls.py)
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    ...

    path(
        "",
        include("chat.urls")
    ),
]
```



















































---

<div id="update-answer-generator"></div>

## `Atualizando o módulo answer_generator.py`

A nossa versão antiga do módulo `answer_generator.py` dizia para mostrar as fontes do treinamento na resposta, mas nessa nossa versão nós vamos tratar isso no frontend passando o `sources` para o template `home.html`.

### `Código Completo`

A versão corrigida do módulo `answer_generator.py` vai ficar da seguinte maneira:

[rag/services/generation/answer_generator.py](../../../rag/services/generation/answer_generator.py)
```python
from typing import Any

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


def _get_llm() -> ChatOpenAI:
    """
    Retorna o LLM da OpenAI configurado.
    """

    return ChatOpenAI(
        model="gpt-4o-mini",  # rápido e barato (recomendado para RAG)
        temperature=0.0,
    )


def generate_answer(
    *,
    question: str,
    context: str,
) -> str:

    template: str = """
Use apenas o contexto abaixo para responder.

Se a resposta não estiver no contexto,
diga que não encontrou informação suficiente.

Responda de forma direta e objetiva.
NÃO mencione arquivos, caminhos ou fontes na resposta.

Contexto:
{context}

Pergunta:
{question}

Resposta:
    """

    prompt: PromptTemplate = PromptTemplate(
        template=template.strip(),
        input_variables=["context", "question"],
    )

    formatted_prompt: str = prompt.format(
        context=context,
        question=question,
    )

    llm: ChatOpenAI = _get_llm()

    response: Any = llm.invoke(formatted_prompt)

    return response.content.strip()
```



















































---

<div id="update-context-builder"></div>

## `Atualizando o módulo context_builder.py`

O nosso módulo `context_builder.py` está da seguinte maneira:

### `CÓDIGO ANTIGO`

```python
from typing import List

from rag.models import DocumentEmbedding


def build_context(
    *,
    chunks: List[DocumentEmbedding],
) -> str:

    context_parts: List[str] = []

    for chunk in chunks:
        source: str = (
            f"[{chunk.folder}/{chunk.path}]"
        )

        text: str = chunk.content.strip()

        formatted: str = (
            f"{source}\n\"{text}\""
        )

        context_parts.append(formatted)

    context: str = "\n\n".join(context_parts)

    return context
```

### `CÓDIGO NOVO (ATUALIZADO)`

O módulo `context_builder.py` vai precisar ficar da seguinte maneira para satisfazer as nossas novas necessidades:

[rag/services/generation/context_builder.py](../../../rag/services/generation/context_builder.py)
```python
import os
from typing import Any, Dict, List, Tuple

from rag.models import DocumentEmbedding
from workspace.models import File


def build_context(
    *,
    chunks: List[DocumentEmbedding],
    user_id: int,
) -> Tuple[str, List[Dict[str, Any]]]:

    context_parts: List[str] = []
    sources_by_file: Dict[int, Dict[str, Any]] = {}

    for chunk in chunks:
        text: str = (chunk.content or "").strip()

        if text:
            context_parts.append(text)

        fid = chunk.file_id
        if fid in sources_by_file:
            continue

        file_row = (
            File.objects.filter(
                id=fid,
                uploader_id=user_id,
                is_deleted=False,
            )
            .select_related("folder")
            .first()
        )

        if file_row:
            sources_by_file[fid] = {
                "file_id": fid,
                "file_name": file_row.name,
                "folder_id": file_row.folder_id,
            }
        else:
            basename = os.path.basename((chunk.path or "").strip()) or "Arquivo"
            sources_by_file[fid] = {
                "file_id": fid,
                "file_name": basename,
                "folder_id": None,
            }

    context: str = "\n\n".join(context_parts)

    return context, list(sources_by_file.values())
```



















































---

<div id="update-file-directory"></div>

## `Atualizando a criação do inventário (file_directory.py)`

Outro módulo que nós vamos precisar atualizar para satisfazer as nossas novas necessidades é o módulo `file_directory.py`.

### `CÓDIGO ANTIGO`

```python
import os
from typing import Any, Dict, List, Optional

from workspace.models import File


def get_file_type(filename: str) -> str:
    """Returns the file type from the file name"""

    _, ext = os.path.splitext(filename)
    return ext.lower()


def get_folder_path(file: File) -> str:
    """Returns the folder path from the file path"""

    if not file.folder:
        raise ValueError(
            f"Arquivo {file.id} sem pasta associada (inconsistência de dados)"
        )

    return file.folder.full_path


def map_file(file: File) -> Dict[str, Any]:
    """Maps a file object to a dictionary with relevant information"""

    if not file.file or not file.file.path:
        raise ValueError(
            f"Arquivo inválido ou sem caminho físico (id={file.id})"
        )

    return {
        "file_id": file.id,
        "name": file.name,
        "file_type": get_file_type(file.name),
        "folder": get_folder_path(file),
        "absolute_path": file.file.path,
    }


def discover_workspace_files(
    *,
    user,
    folder_id: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """
    Returns a list of mapped files from the user's workspace.

    - Se folder_id for None → retorna todos os arquivos do usuário
    - Se folder_id for informado → filtra pela pasta
    """

    if user is None:
        raise ValueError(
            "Usuário é obrigatório para descobrir arquivos do workspace"
        )

    # 🔐 Sempre filtrar por usuário
    queryset = File.objects.filter(
        uploader=user,
        is_deleted=False,
    )

    # 📁 Filtro opcional por pasta
    if folder_id:
        queryset = queryset.filter(folder_id=folder_id)

    inventory: List[Dict[str, Any]] = []

    for file in queryset:
        try:
            inventory.append(map_file(file))
        except Exception:
            # ⚠️ evita quebrar o pipeline por arquivo corrompido
            continue

    return inventory
```

### `CÓDIGO NOVO (ATUALIZADO)`

O módulo `file_directory.py` vai precisar ficar da seguinte maneira para satisfazer as nossas novas necessidades:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
import os
from typing import Any, Dict, List, Optional

from workspace.models import File


def get_file_type(filename: str) -> str:
    """Returns the file type from the file name"""

    _, ext = os.path.splitext(filename)
    return ext.lower()


def map_file(file: File) -> Dict[str, Any]:
    """Maps a file object to a dictionary with relevant information"""

    if not file.file or not file.file.path:
        raise ValueError(
            f"Arquivo inválido ou sem caminho físico (id={file.id})"
        )

    folder_path = file.folder.full_path if file.folder else "workspace"

    return {
        "file_id": file.id,
        "name": file.name,
        "file_type": get_file_type(file.name),
        "folder": folder_path,
        "folder_id": file.folder_id,
        "absolute_path": file.file.path,
    }


def discover_workspace_files(
    *,
    user,
    folder_id: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """
    Returns a list of mapped files from the user's workspace.

    - Se folder_id for None → retorna todos os arquivos do usuário
    - Se folder_id for informado → filtra pela pasta
    """

    if user is None:
        raise ValueError(
            "Usuário é obrigatório para descobrir arquivos do workspace"
        )

    # 🔐 Sempre filtrar por usuário
    queryset = File.objects.filter(
        uploader=user,
        is_deleted=False,
    )

    # 📁 Filtro opcional por pasta
    if folder_id:
        queryset = queryset.filter(folder_id=folder_id)

    inventory: List[Dict[str, Any]] = []

    for file in queryset:
        try:
            inventory.append(map_file(file))
        except Exception:
            # ⚠️ evita quebrar o pipeline por arquivo corrompido
            continue

    return inventory
```



















































---

<div id="update-home-view"></div>

## `Atualizando a view (ação) users/views.py::home_view()`

A nossa versão antiga da view (ação) `home_view()` só mostrava o nosso template `home.html` para o usuário:

### `CÓDIGO ANTIGO`

```python
@login_required(login_url="/")
def home_view(request):
    return render(request, "pages/home.html")
```

### `CÓDIGO NOVO (ATUALIZADO)`

A nossa nova versão dessa view (ação) também vai precisar mostrar o histórico sempre que o template `home.html` for renderizado:

[users/views.py](../../../users/views.py)
```python
@login_required(login_url="/")
def home_view(request):
    chat_history = request.session.get("chat_history", [])
    return render(
        request,
        "pages/home.html",
        {"chat_history": chat_history},
    )
```



















































---

<div id="create-folder-view"></div>

## `Criando a view (ação) workspace/views.py::folder_view()`

Aqui, vamos implementar a view (ação) `folder_view()` que será responsável por exibir o conteúdo de uma pasta específica.

[workspace/views.py](../../../workspace/views.py)
```python
@login_required
def folder_view(request, folder_id):
    """
    View para exibir o conteúdo de uma pasta específica.

    Args:
        request: Objeto HttpRequest do Django
        folder_id: ID da pasta a ser exibida

    Returns:
        HttpResponse: Resposta HTTP com o conteúdo da pasta
    """

    folder = Folder.objects.get(
        id=folder_id,
        owner=request.user
    )

    files = File.objects.filter(
        folder=folder,
        uploader=request.user,
        is_deleted=False,
    )

    return render(
        request,
        "pages/folder.html",
        {
            "folder": folder,
            "files": files,
        }
    )
```

Outra coisa importante aqui vai ser criar uma ROTA/URL para essa view (ação):

[workspace/urls.py](../../../workspace/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [

    ...

    path(
        "workspace/folder/<int:folder_id>/",
        views.folder_view,
        name="workspace_folder",
    ),
]
```



















































---

<div id="create-chat-html-js"></div>

## `Criando o HTML (e JavaScript) necessário para criar o chat`

> Aqui, nós vamos criar o *HTML* e o *JavaScript* necessários para nosso `chat` funcionar corretamente.

### `Atualização do template (HTML) sidebar.html`

[templates/partials/sidebar.html](../../../templates/partials/sidebar.html)
```html
<!--
    Template parcial para a sidebar de navegação.
    
    Este componente é usado em páginas autenticadas (home e workspace)
    e contém:
    - Link de navegação entre Home e Workspace
    - Link de logout
    
    Variáveis esperadas:
    - current_page: 'home' ou 'workspace' (opcional, usado para
      destacar o link ativo)
-->
<aside class="
            flex
            w-64
            shrink-0
            flex-col
            justify-between
            bg-gray-900
            text-white">

    <!-- Link de navegação -->
    <div class="p-2 border-b border-gray-700">
        {% if current_page == 'home' %}
            <a class="flex items-center justify-between p-2 
                      hover:bg-gray-800 rounded"
               href="{% url 'workspace_home' %}">
                Workspace
            </a>
        {% else %}
            <a href="{% url 'home' %}"
               class="flex items-center justify-between 
                      p-2 hover:bg-gray-800 rounded">
                Home
            </a>
        {% endif %}
    </div>

    <!-- Link de Logout -->
    <div class="p-4 border-t border-gray-700">
        <a href="{% url 'logout' %}"
           class="block text-center text-red-400 
                  hover:text-red-300">
           Sair
        </a>
    </div>

</aside>
```

### `Atualização do template (HTML) home.html`

[users/templates/pages/home.html](../../../users/templates/pages/home.html)
```html
{% extends "base.html" %}
{% load static %}

{% block title %}Home{% endblock %}

{% block content %}
    <div class="flex h-screen min-h-0 overflow-hidden bg-gray-100">

        <!-- Sidebar -->
        {% include "partials/sidebar.html" with current_page="home" %}

        <!-- Área principal: min-h-0 permite o filho flex encolher e rolar -->
        <main class="flex min-h-0 min-w-0 flex-1 flex-col overflow-hidden">

            <!-- Área do chat -->
            <div class="flex min-h-0 flex-1 flex-col gap-4 p-6">

                <!-- Header -->
                <header class="shrink-0 bg-white shadow px-6 py-4">
                    <h1 class="text-2xl font-semibold text-gray-800">
                        Bem-vindo, {{ request.user.username }}!
                    </h1>
                </header>

                <!-- Histórico (rolagem interna; JS mantém a vista no fim = mensagens recentes) -->
                <div
                    id="chat-history"
                    class="
                    min-h-0
                    flex-1
                    overflow-y-auto
                    overscroll-y-contain
                    bg-white
                    rounded-lg
                    shadow
                    p-6
                    space-y-4">

                    {% if chat_history %}

                        {% for message in chat_history %}

                            <!-- USUÁRIO -->
                            {% if message.role == "user" %}
                                <div class="flex justify-end">
                                    <div class="max-w-xl">
                                        <div class="bg-blue-100 p-3 rounded-lg">
                                            <strong class="flex justify-end">
                                                {{ request.user.username }}:
                                            </strong>
                                            {{ message.content }}
                                        </div>
                                    </div>
                                </div>

                            <!-- ASSISTENTE -->
                            {% elif message.role == "assistant" %}
                                <div class="flex justify-start">
                                    <div class="max-w-xl">
                                        <div class="bg-gray-100 p-3 rounded-lg">
                                            
                                            <strong class="flex">
                                                Assistente:
                                            </strong>

                                            <!-- Resposta -->
                                            <div>
                                                {{ message.content }}
                                            </div>

                                            {% if message.sources %}
                                                <div class="mt-3 pt-3 border-t border-gray-200">
                                                    <div class="text-xs text-gray-500 mb-2">
                                                        Fontes
                                                    </div>
                                                    <div class="flex flex-wrap items-center gap-2 text-sm">
                                                        {% for source in message.sources %}
                                                            {% if source.folder_id %}
                                                                <a
                                                                    href="{% url 'workspace_home' %}?folder={{ source.folder_id }}"
                                                                    class="
                                                                        inline-flex items-center gap-1
                                                                        rounded-full px-3 py-1.5
                                                                        bg-white border border-gray-300
                                                                        text-gray-800
                                                                        hover:bg-gray-50 hover:border-gray-400
                                                                        whitespace-nowrap
                                                                    "
                                                                >
                                                                    📄 {{ source.file_name }}
                                                                </a>
                                                            {% else %}
                                                                <a
                                                                    href="{% url 'workspace_home' %}"
                                                                    class="
                                                                        inline-flex items-center gap-1
                                                                        rounded-full px-3 py-1.5
                                                                        bg-white border border-gray-300
                                                                        text-gray-800
                                                                        hover:bg-gray-50 hover:border-gray-400
                                                                        whitespace-nowrap
                                                                    "
                                                                >
                                                                    📄 {{ source.file_name }}
                                                                </a>
                                                            {% endif %}
                                                        {% endfor %}
                                                    </div>
                                                </div>
                                            {% endif %}

                                        </div>
                                    </div>
                                </div>

                            <!-- SISTEMA -->
                            {% else %}
                                <div class="flex justify-center">
                                    <div class="max-w-xl">
                                        <div class="bg-yellow-100 p-3 rounded-lg">
                                            {{ message.content }}
                                        </div>
                                    </div>
                                </div>
                            {% endif %}

                        {% endfor %}

                    {% else %}
                        <div class="text-center text-gray-500">
                            Nenhuma mensagem ainda. Faça uma pergunta!
                        </div>
                    {% endif %}

                </div>
                <!-- /Histórico -->

                <!-- Formulário -->
                <div class="shrink-0 bg-white shadow rounded-lg p-4">
                    <form method="POST" action="{% url 'ask' %}">
                        {% csrf_token %}

                        <div class="flex gap-3">
                            <input
                                type="text"
                                name="question"
                                placeholder="Digite sua pergunta..."
                                required
                                class="peer flex-1 border rounded-lg px-4 py-2"
                            >

                            <button
                                type="submit"
                                class="
                                    px-6 py-2 rounded-lg
                                    bg-blue-600 text-white
                                    opacity-50
                                    pointer-events-none
                                    peer-valid:opacity-100
                                    peer-valid:pointer-events-auto
                                ">
                                Enviar
                            </button>
                        </div>
                    </form>
                </div>
                <!-- /Formulário -->

            </div>
        </main>
    </div>
{% endblock %}

{% block scripts %}
    <script src="{% static 'users/js/home.js' %}"></script>
{% endblock scripts %}
```

### `Criação do JavaScript static/users/js/home.js`

[static/users/js/home.js](../../../static/users/js/home.js)
```js
(function () {
    function scrollChatToBottom() {
        var el = document.getElementById("chat-history");
        if (el) {
            el.scrollTop = el.scrollHeight;
        }
    }
    document.addEventListener("DOMContentLoaded", function () {
        scrollChatToBottom();
        requestAnimationFrame(function () {
            requestAnimationFrame(scrollChatToBottom);
        });
    });
})();
```

> **⚠️ NOTE:**  
> Como o foco aqui não é o front-end, não vou explicar passo a passo o que foi implementado.

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
