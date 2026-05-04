# `Convertendo funções/views síncronas em assíncronas (async/await)`

## Conteúdo

 - [`O que é async/await?`](#what-is-async)
 - [`Atualizando a função rag/services/retrieval/embed_query.py::embed_query() para assíncrona`](#update-embed-query)
 - [`Atualizando a função rag/services/generation/answer_generator.py::generate_answer() para assíncrona`](#update-generate-answer)
 - [`Atualizando a view chat/views.py::ask_view() para assíncrona`](#update-ask-view)
 - [`Atualizando a função rag/services/ingestion/embeddings.py::generate_embeddings() para assíncrona`](#update-generate-embeddings)
 - [`Atualizando a função rag/services/qa_service.py::ask() para assíncrona`](#update-qa-ask)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="what-is-async"></div>

## `O que é async/await?`

> Imagine que você está em um restaurante com **um único garçom**.

 - **Modo “síncrono” (tradicional):**
   - O garçom anota o pedido da mesa 1, vai à cozinha e **fica parado** até o prato ficar pronto. Só depois ele atende a mesa 2.
 - **Modo “assíncrono” (async):**
   - O garçom anota o pedido da mesa 1, leva para a cozinha e **volta** para anotar o pedido da mesa 2 enquanto a cozinha trabalha. Quando o prato 1 estiver pronto, ele retoma aquele pedido.

`async` e `await` em Python são **ferramentas de linguagem** para escrever esse segundo estilo de forma organizada: você marca funções que podem “pausar” em operações que demoram (rede, disco, banco) sem precisar bloquear o resto do programa da forma mais ingênua.

 - `async def minha_funcao()`
   - “esta função pode ser interrompida e retomada em pontos de espera”.
 - `await alguma_coisa()`
   - “aqui costuma haver espera; em sistemas bem configurados, podemos **aproveitar** esse tempo para outras coisas úteis”.

Com **async/await** bem aplicado (principalmente nas camadas que falam com **rede** ou **banco** com drivers assíncronos), você pode:

 - Atender **mais requisições leves** no mesmo servidor quando há muita espera de I/O.
 - Preparar o terreno para **SSE/WebSockets** ou endpoints que “empurram” pedaços de resposta (streaming), se no futuro o produto exigir.

> **⚠️ Cuidado:**  
> Partes que usam **PyTorch**, **transformers** ou chamadas bloqueantes pesadas precisam de estratégia extra (thread pool, processo separado, fila em background — ver Parte 3).


















































---

<div id="update-embed-query"></div>

## `Atualizando a função rag/services/retrieval/embed_query.py::embed_query() para assíncrona`

Até então a nossa função [rag/services/retrieval/embed_query.py::embed_query()](../../../rag/services/retrieval/embed_query.py) estava síncrona:

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

Agora, nós vamos atualizar para uma versão assíncrona:

[rag/services/retrieval/embed_query.py::embed_query()](../../../rag/services/retrieval/embed_query.py)
```python
from typing import List

from rag.services.ingestion.embeddings import (
    get_embedding_model,
)


async def embed_query(
    *,
    question: str,
) -> List[float]:
    """
    Converte a pergunta do usuário em um vetor
    de embedding utilizando o mesmo modelo
    usado na ingestão dos documentos.
    """

    model = get_embedding_model()

    query_vector: List[float] = await model.aembed_query(
        question
    )

    return query_vector
```

> **O que mudou?**

 - `async def embed_query(...)`
   - 👉 Isso significa que:
     - A função não executa imediatamente
     - Ela retorna uma `corrotina`
     - Precisa ser chamada com `await`
 - `Uso de await` ➔ `query_vector = await model.aembed_query(question)`
   - 👉 Aqui está a principal mudança:
     - `embed_query()` → síncrono (bloqueia execução)
     - `aembed_query()` → assíncrono (não bloqueia)
 - `Mudança no comportamento (o mais importante)`
   - **🔴 Antes (síncrono):**
     - A thread fica bloqueada até o embedding ser gerado
     - Se estiver em uma API (ex: Django), cada request espera terminar
   - **🟢 Agora (assíncrono):**
     - A execução pode ser suspensa enquanto espera a resposta
     - Libera o event loop para outras tarefas
     - Melhor uso de concorrência (especialmente em APIs)

> **E agora quem precisar desta função é só chamar?**  
> Não exatamente!

Por exemplo, a função [rag/services/qa_service.py::ask()](../../../rag/services/qa_service.py) chamava essa função da seguinte maneira:

```python
def ask(...) -> Dict[str, Any]:

    ...

    # 1️⃣ Gerar embedding da pergunta
    query_vector = embed_query(
        question=question
    )
```

> **👉 Problema:**  
> Código *síncrono* não pode usar `await` diretamente.

Para resolver esse problema, vamos utilizar o adaptador `async_to_sync (do asgiref)`:

[rag/services/qa_service.py::ask()](../../../rag/services/qa_service.py)
```python
from asgiref.sync import async_to_sync


def ask(...) -> Dict[str, Any]:

    # 1️⃣ Gerar embedding da pergunta
    query_vector = async_to_sync(embed_query)(
        question=question
    )

    ...
```

Isso faz:

 - Criar um loop assíncrono *"por baixo dos panos"*
 - Executa `embed_query`
 - Espera o resultado
 - Retorna como se fosse síncrono

### `🔄 Fluxo mental`

**Antes:**
```bash
sync → sync → sync
```

**Agora:**
```bash
sync → (ponte) → async → (espera) → volta sync
```


















































---

<div id="update-generate-answer"></div>

## `Atualizando a função rag/services/generation/answer_generator.py::generate_answer() para assíncrona`

Até então o nosso módulo [rag/services/generation/answer_generator.py::generate_answer()](../../../rag/services/generation/answer_generator.py) estava síncrona:

```python
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

Agora, nós vamos atualizar para uma versão assíncrona:

```python
async def generate_answer(
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

    response: Any = await llm.ainvoke(formatted_prompt)

    return response.content.strip()
```

> **O que mudou?**

👉 Aqui está a mudança principal:

| Método    | Tipo       | Comportamento         |
| --------- | ---------- | --------------------- |
| `invoke`  | síncrono   | bloqueia até resposta |
| `ainvoke` | assíncrono | não bloqueia          |

### `🧠 O que isso significa na prática?`

 - **🔴 Antes (síncrono):**
   - `Sua aplicação → chama LLM → fica parada esperando resposta`
   - Thread bloqueada
   - Não atende outras requisições
   - Escala pior
 - **🟢 Agora (assíncrono):**
   - `Sua aplicação → chama LLM → "pausa" → atende outras coisas → volta com resposta`
   - Libera o event loop
   - Melhor concorrência
   - Melhor uso de recursos

> **⚠️ NOTE:**  
> Igualmente, se uma função síncrona chamar `async def generate_answer()`, precisará utilizar o adaptador `async_to_sync()`.


















































---

<div id="update-ask-view"></div>

## `Atualizando a view chat/views.py::ask_view() para assíncrona`

Até então a nossa view [chat/views.py::ask_view()](../../../chat/views.py) estava síncrona:

```python
from typing import Any, Dict, List

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

from chat.history import (
    append_exchange,
    clear_chat_for_user,
)
from rag.services.qa_service import ask
from train.utils import resolve_active_training_model_id
from utils.messages import (
    CHAT_INTERNAL_ERROR,
    CHAT_QUESTION_REQUIRED,
)


@login_required(login_url="/")
def ask_view(request: HttpRequest) -> HttpResponse:

    # Redireciona GETs para home (evita acesso direto à URL)
    if request.method == "GET":
        return redirect("home")

    # Obtém e valida a pergunta do formulário
    question: str = request.POST.get("question", "").strip()

    # Se não há pergunta, avisa o usuário e redireciona
    if not question:
        messages.warning(request, CHAT_QUESTION_REQUIRED)
        return redirect("home")

    user_id: int = request.user.id
    training_model_id = resolve_active_training_model_id(request, user_id)

    # Processa a pergunta via serviço RAG
    try:
        result: Dict[str, Any] = ask(
            user_id=user_id,
            question=question,
            training_model_id=training_model_id,
        )

        answer: str = result.get("answer", "")
        sources: List[Dict[str, str]] = result.get("sources", [])

    # Trata erros no processamento da pergunta
    except Exception as error:
        print("ERRO RAG:", error)
        answer = "Erro ao processar sua pergunta."
        sources = []
        messages.error(request, CHAT_INTERNAL_ERROR)

    # Salva a troca no histórico do chat
    try:
        append_exchange(
            user=request.user,
            question=question,
            answer=answer,
            sources=sources,
        )
        print(f"✅ Pergunta salva: {question[:50]}...")
    except Exception as e:
        print(f"❌ Erro ao salvar pergunta: {e}")
        # Mesmo com erro no histórico, continua o fluxo

    # SEMPRE redireciona para home
    print("🔄 Redirecionando para home...")
    return redirect("home")


@login_required(login_url="/")
def clear_chat_view(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return redirect("home")

    clear_chat_for_user(request.user)

    return redirect("home")
```

Agora, nós vamos atualizar para uma versão assíncrona:

[chat/views.py::ask_view()](../../../chat/views.py)
```python
from typing import Any, Dict, List

from asgiref.sync import sync_to_async
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

from chat.history import (
    append_exchange,
    clear_chat_for_user,
)
from rag.services.qa_service import ask
from train.utils import resolve_active_training_model_id
from utils.messages import (
    CHAT_INTERNAL_ERROR,
    CHAT_QUESTION_REQUIRED,
)


def _post_question_stripped(request: HttpRequest) -> str:
    return request.POST.get("question", "").strip()


def _authenticated_user_id(request: HttpRequest) -> int:
    return request.user.id


def _flash_warning_question_required(request: HttpRequest) -> HttpResponse:
    messages.warning(request, CHAT_QUESTION_REQUIRED)
    return redirect("home")


def _flash_error_rag(request: HttpRequest) -> None:
    messages.error(request, CHAT_INTERNAL_ERROR)


def _append_exchange_from_request(
    request: HttpRequest,
    question: str,
    answer: str,
    sources: List[Dict[str, Any]],
) -> None:
    append_exchange(
        user=request.user,
        question=question,
        answer=answer,
        sources=sources,
    )


@login_required(login_url="/")
async def ask_view(request: HttpRequest) -> HttpResponse:

    if request.method == "GET":
        return await sync_to_async(redirect)("home")

    question = await sync_to_async(_post_question_stripped)(request)

    if not question:
        return await sync_to_async(_flash_warning_question_required)(request)

    user_id = await sync_to_async(_authenticated_user_id)(request)
    training_model_id = await sync_to_async(resolve_active_training_model_id)(
        request,
        user_id,
    )

    try:
        result: Dict[str, Any] = await ask(
            user_id=user_id,
            question=question,
            training_model_id=training_model_id,
        )

        answer: str = result.get("answer", "")
        sources: List[Dict[str, Any]] = result.get("sources", [])

    except Exception as error:
        print("ERRO RAG:", error)
        answer = "Erro ao processar sua pergunta."
        sources = []
        await sync_to_async(_flash_error_rag)(request)

    try:
        await sync_to_async(_append_exchange_from_request)(
            request,
            question,
            answer,
            sources,
        )
        print(f"✅ Pergunta salva: {question[:50]}...")
    except Exception as e:
        print(f"❌ Erro ao salvar pergunta: {e}")

    print("🔄 Redirecionando para home...")
    return await sync_to_async(redirect)("home")


@login_required(login_url="/")
def clear_chat_view(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return redirect("home")

    clear_chat_for_user(request.user)

    return redirect("home")
```


















































---

<div id="update-generate-embeddings"></div>

## `Atualizando a função rag/services/ingestion/embeddings.py::generate_embeddings() para assíncrona`

Até então o nosso módulo [rag/services/ingestion/embeddings.py::generate_embeddings()](../../../rag/services/ingestion/embeddings.py) estava síncrono:

```python
import os
from typing import Any, Dict, List

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


def get_embedding_model() -> OpenAIEmbeddings:
    """
    Initialize and return the embedding model using OpenAI,
    loading API key from .env file.
    """

    # Carrega variáveis do .env
    load_dotenv()

    # Recupera a chave
    api_key: str | None = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY não encontrada no .env")

    embedding_model: OpenAIEmbeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        openai_api_key=api_key,
    )

    return embedding_model


def generate_embeddings(
    *,
    embedding_model: OpenAIEmbeddings,
    chunks: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Generate embeddings for the given chunks
    using the provided embedding model.
    """

    texts: List[str] = [
        chunk["content"]
        for chunk in chunks
    ]

    vectors: List[List[float]] = (
        embedding_model.embed_documents(texts)
    )

    embedded_chunks: List[Dict[str, Any]] = []

    for chunk, vector in zip(chunks, vectors):
        embedded_chunks.append({
            **chunk,
            "embedding": vector,
        })

    return embedded_chunks
```

Agora, nós vamos atualizar para uma versão assíncrona:

[rag/services/ingestion/embeddings.py::generate_embeddings()](../../../rag/services/ingestion/embeddings.py)
```python
import os
from typing import Any, Dict, List

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


def get_embedding_model() -> OpenAIEmbeddings:
    """
    Initialize and return the embedding model using OpenAI,
    loading API key from .env file.
    """

    # Carrega variáveis do .env
    load_dotenv()

    # Recupera a chave
    api_key: str | None = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY não encontrada no .env")

    embedding_model: OpenAIEmbeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        openai_api_key=api_key,
    )

    return embedding_model


async def generate_embeddings(
    *,
    embedding_model: OpenAIEmbeddings,
    chunks: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Generate embeddings for the given chunks
    using the provided embedding model.
    """

    texts: List[str] = [
        chunk["content"]
        for chunk in chunks
    ]

    vectors: List[List[float]] = await embedding_model.aembed_documents(
        texts
    )

    embedded_chunks: List[Dict[str, Any]] = []

    for chunk, vector in zip(chunks, vectors):
        embedded_chunks.append({
            **chunk,
            "embedding": vector,
        })

    return embedded_chunks
```


















































---

<div id="update-qa-ask"></div>

## `Atualizando a função rag/services/qa_service.py::ask() para assíncrona`

Até então o nosso módulo [rag/services/qa_service.py::ask()](../../../rag/services/qa_service.py) estava síncrono:

```python
from typing import Any, Dict, Optional

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
    training_model_id: Optional[int] = None,
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
        training_model_id=training_model_id,
    )

    if not chunks:
        default_answer = (
            "Não encontrei informações relevantes "
            "nos seus documentos."
        )
        return {
            "answer": default_answer,
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

Agora, nós vamos atualizar para uma versão assíncrona:

[rag/services/qa_service.py::ask()](../../../rag/services/qa_service.py)
```python
from typing import Any, Dict, Optional

from asgiref.sync import sync_to_async

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


async def ask(
    *,
    user_id: int,
    question: str,
    top_k: int = 5,
    training_model_id: Optional[int] = None,
) -> Dict[str, Any]:

    # 1️⃣ Gerar embedding da pergunta
    query_vector = await embed_query(
        question=question
    )

    # 2️⃣ Buscar chunks mais relevantes
    chunks = await sync_to_async(vector_search)(
        user_id=user_id,
        query_vector=query_vector,
        top_k=top_k,
        training_model_id=training_model_id,
    )

    if not chunks:
        default_answer = (
            "Não encontrei informações relevantes "
            "nos seus documentos."
        )
        return {
            "answer": default_answer,
            "sources": [],
        }

    # 3️⃣ Construir contexto + fontes
    context, sources = await sync_to_async(build_context)(
        chunks=chunks,
        user_id=user_id,
    )

    # 4️⃣ Gerar resposta com LLM
    answer = await generate_answer(
        question=question,
        context=context,
    )

    # 5️⃣ Retorno padronizado
    return {
        "answer": answer,
        "sources": sources,
    }
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
