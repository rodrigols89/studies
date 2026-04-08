# `Criando o processo de treinamento/salvamento de embeddings no banco`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Criando o botão de treinar`](#train-button)
 - [`Atualizando o módulo de mapeamento de arquivos: file_discovery.py`](#update-file-discovery)
 - [`Atualizando o módulo de extração de textos: text_extraction.py`](#update-text-extraction)
 - [`Atualizando o módulo responsável por armazenar embeddings no banco: vector_store.py`](#update-vector-store)
 - [`Criando a view (ação) de treinamento: train_view()`](#train-view)
 - [`Criando/Relacionando a ROTA/URL de Treinamento: train/`](#training-url)
 - [`Criando/relacionando a ROTA/URL train: front(template) <--> back(view)`](#mapping-front-back)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

Aqui nós vamos criar o seguinte processo:

```bash
🤖 Treinar (Botão)
   ↓
🧹 Apaga tudo do usuário (Todos os Embeddings salvos no banco)
   ↓
📂 Lê todos arquivos
   ↓
✂️ Chunking
   ↓
🧠 Embeddings (Gera Embeddings novamente)
   ↓
💾 Salva limpo (Salva os Embeddings no Banco)
```

 - **💪 VANTAGENS:**
   - ✔ 100% confiável
   - ✔ zero erro de constraint
   - ✔ fácil de debugar
   - ✔ ideal pra fase atual
 - **⚠️ DESVANTAGEM (aceitável agora)**
   - ❌ reprocessa tudo sempre (custo maior)

**⚠️ NOTE:**  
Porém, essa é só uma versão inicial do processo de treinamento. Depois nós vamos atualizar para só treinar os arquivos novos.

Para aplicar os  conceitos listados acima nós vamos precisar de um botão "🤖 Treinar" que tenha uma view (ação) relacionada (`train_view()`) que:

 - Localize, filtre e mapei todos os arquivos do *Workspace* que pertencem exclusivamente ao usuário logado utilizando a função [rag/services/ingestion/file_discovery.py::discover_workspace_files()](../../../rag/services/ingestion/file_discovery.py)
 - Utilize as funções adequadas para extração de textos do módulo [rag/services/ingestion/text_extraction.py::extract_text()](../../../rag/services/ingestion/text_extraction.py)
 - Transforme os arquivos/textos em chunks com a função [rag/services/ingestion/chunking.py::chunk_text()](../../../rag/services/ingestion/chunking.py)
 - Gere os vetores de embedding a partir dos chunks com a função [rag/services/ingestion/embedding.py::generate_embeddings()](../../../rag/services/ingestion/embeddings.py)
 - Salve esses vetores de embedding no banco de dados [rag/services/ingestion/vector_store.py::store_embeddings()](../../../rag/services/ingestion/vector_store.py)



















































---

<div id="train-button"></div>

## `Criando o botão de treinar`

> Aqui, nós vamos criar um botão que vai ser responsável `Treinar` os embeddings com os nossos dados do Workspace atual (usuário logado).

O botão de `Treinar` vai ficar da seguinte maneira:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
                </div> <!-- 🔹 /BOTÕES ESQUERDO -->


                <!-- 🔸 Lado DIREITO -->
                <div class="flex items-center">

                    <!-- 🤖 Botão Treinar -->
                    {% if not current_folder %}
                        <form method="post"
                            action="">
                            
                            {% csrf_token %}

                            <input 
                                type="hidden" 
                                name="folder" 
                                value="{{ current_folder.id|default_if_none:'' }}">

                            <input 
                                type="hidden" 
                                name="next" 
                                value="{{ request.get_full_path }}">

                            <button
                                type="submit"
                                class="
                                    bg-purple-600
                                    hover:bg-purple-700
                                    text-white
                                    mr-2
                                    px-5
                                    py-2
                                    rounded
                                    font-semibold
                                    shadow">
                                🤖 Treinar
                            </button>
                        </form><!-- 🤖 /Botão Treinar -->
                    {% endif %}

                </div> <!-- 🔸 Lado DIREITO -->

            </div> <!-- 📌 /Botões -->
```

> **NOTE:**  
> Vejam que esse botão só vai aparecer quando estivermos na raiz do Workspace (`current_folder`).


















































---

<div id="update-file-discovery"></div>

## `Atualizando o módulo de mapeamento de arquivos: file_discovery.py`

Seguindo a lógica listada acima o primeiro módulo que nós vamos precisar atualizar para satisfazer nossas necessidades é o módulo [rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)

### `CÓDIGO ANTIGO`

O módulo `file_discovery.py` (completa) estava da seguinte maneira:

```python
import os

from workspace.models import File


def get_file_type(filename):
    """Returns the file type from the file name"""

    _, ext = os.path.splitext(filename)
    return ext.lower()


def get_folder_path(file):
    """Returns the folder path from the file path"""

    if not file.folder:
        raise ValueError(
            f"Arquivo {file.id} sem pasta associada (inconsistência de dados)"
        )

    return file.folder.full_path


def map_file(file):
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


def discover_workspace_files(user):
    """Returns a list of files from the workspace"""

    if user is None:
        raise ValueError(
            "Usuário é obrigatório para descobrir arquivos do workspace"
        )

    files = File.objects.filter(
        uploader=user,
        is_deleted=False
    )

    inventory = []

    for file in files:
        inventory.append(map_file(file))

    return inventory
```

### `CÓDIGO NOVO (ATUALIZADO)`

O módulo `file_discovery.py` (completa) vai ficar da seguinte maneira:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
import os
from typing import List, Optional, Dict, Any

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


















































---

<div id="update-text-extraction"></div>

## `Atualizando o módulo de extração de textos: text_extraction.py`

Agora, nós vamos atualizar o módulo de extração de textos para satisfazer nossas necessidades.

### `CÓDIGO ANTIGO`

O módulo `text_extraction.py` (completa) estava da seguinte maneira:

```python
from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    BSHTMLLoader,
    Docx2txtLoader,
    PyPDFLoader,
    TextLoader,
    UnstructuredExcelLoader,
)
from langchain_core.documents import Document


def extract_txt(path: Path) -> List[Document]:
    """Extract text from a TXT file using LangChain."""

    loader = TextLoader(
        str(path),
        encoding="utf-8"
    )
    return loader.load()


def extract_md(path: Path) -> List[Document]:
    """Extract text from a Markdown file using LangChain."""
    loader = TextLoader(
        str(path),
        encoding="utf-8"
    )
    return loader.load()


def extract_pdf(path: Path) -> List[Document]:
    """Extract text from a PDF file using LangChain."""
    loader = PyPDFLoader(str(path))
    return loader.load()


def extract_docx(path: Path) -> List[Document]:
    """Extract text from a DOCX file using LangChain."""
    loader = Docx2txtLoader(str(path))
    return loader.load()


def extract_html(path: Path) -> List[Document]:
    """Extract text from an HTML file using LangChain."""
    loader = BSHTMLLoader(str(path))
    return loader.load()


def extract_excel(path: Path) -> List[Document]:
    """
    Extract text from an Excel file using LangChain.

    Cada planilha vira um ou mais Documents.
    """
    loader = UnstructuredExcelLoader(str(path))
    return loader.load()


def extract_text(file_info) -> List[Document]:
    """
    Extrai texto de um arquivo do workspace já autorizado.

    ⚠️ Controle de acesso:
    - file_info SEMPRE vem do discover_workspace_files(user)
    - Nunca recebe caminhos arbitrários
    - Nunca mistura dados de usuários
    """

    file_path = Path(file_info["absolute_path"])
    file_type = file_info["file_type"]

    if file_type == ".txt":
        return extract_txt(file_path)

    if file_type == ".md":
        return extract_md(file_path)

    if file_type == ".pdf":
        return extract_pdf(file_path)

    if file_type == ".docx":
        return extract_docx(file_path)

    if file_type == ".html":
        return extract_html(file_path)

    if file_type.startswith(".xls"):
        return extract_excel(file_path)

    raise ValueError(f"Tipo de arquivo não suportado: {file_type}")
```

### `CÓDIGO NOVO (ATUALIZADO)`

O módulo `text_extraction.py` (completa) vai ficar da seguinte maneira:

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    BSHTMLLoader,
    Docx2txtLoader,
    PyPDFLoader,
    TextLoader,
    UnstructuredExcelLoader,
)
from langchain_core.documents import Document


def extract_txt(path: Path) -> List[Document]:
    loader = TextLoader(str(path), encoding="utf-8")
    return loader.load()


def extract_md(path: Path) -> List[Document]:
    loader = TextLoader(str(path), encoding="utf-8")
    return loader.load()


def extract_pdf(path: Path) -> List[Document]:
    loader = PyPDFLoader(str(path))
    return loader.load()


def extract_docx(path: Path) -> List[Document]:
    loader = Docx2txtLoader(str(path))
    return loader.load()


def extract_html(path: Path) -> List[Document]:
    loader = BSHTMLLoader(str(path))
    return loader.load()


def extract_excel(path: Path) -> List[Document]:
    loader = UnstructuredExcelLoader(str(path))
    return loader.load()


def extract_text(file_info) -> List[str]:
    """
    Extrai texto e retorna LISTA DE STRINGS (corrigido).
    """

    file_path = Path(file_info["absolute_path"])
    file_type = file_info["file_type"]

    if file_type == ".txt":
        docs = extract_txt(file_path)

    elif file_type == ".md":
        docs = extract_md(file_path)

    elif file_type == ".pdf":
        docs = extract_pdf(file_path)

    elif file_type == ".docx":
        docs = extract_docx(file_path)

    elif file_type == ".html":
        docs = extract_html(file_path)

    elif file_type.startswith(".xls"):
        docs = extract_excel(file_path)

    else:
        raise ValueError(f"Tipo de arquivo não suportado: {file_type}")

    texts: List[str] = []

    for doc in docs:
        if not isinstance(doc, Document):
            continue

        content = doc.page_content

        if content and content.strip():
            texts.append(content.strip())

    return texts
```


















































---

<div id="update-vector-store"></div>

## `Atualizando o módulo responsável por armazenar embeddings no banco: vector_store.py`

Outro módulo importante que nós vamos precisar atualizar é o `vector_store.py`.

### `CÓDIGO ANTIGO`

O módulo `vector_store.py` (completa) estava da seguinte maneira:

```python
from typing import Any, Dict, List

from rag.models import DocumentEmbedding


def store_embeddings(
    *,
    embedded_chunks: List[Dict[str, Any]],
) -> None:
    """
    Persiste embeddings no PostgreSQL com pgvector.
    """

    objects: List[DocumentEmbedding] = []

    for chunk in embedded_chunks:
        objects.append(
            DocumentEmbedding(
                user_id=chunk["user_id"],
                file_id=chunk["file_id"],
                folder=chunk["folder"],
                path=chunk["path"],
                chunk_index=chunk["chunk_index"],
                content=chunk["content"],
                embedding=chunk["embedding"],
                metadata={
                    "source": "upload",
                },
            )
        )

    DocumentEmbedding.objects.bulk_create(objects)
```

### `CÓDIGO NOVO (ATUALIZADO)`

O módulo `vector_store.py` (completa) vai ficar da seguinte maneira:

[rag/services/ingestion/vector_store.py](../../../rag/services/ingestion/vector_store.py)
```python
from typing import Any, Dict, List, Set

from rag.models import DocumentEmbedding


def get_processed_file_ids(*, user_id: int) -> Set[int]:
    """
    Retorna todos os file_ids que já possuem embeddings
    para o usuário (controle incremental).
    """
    return set(
        DocumentEmbedding.objects.filter(user_id=user_id)
        .values_list("file_id", flat=True)
        .distinct()
    )


def store_embeddings(
    *,
    embedded_chunks: List[Dict[str, Any]],
) -> None:
    """
    Persiste embeddings no PostgreSQL com pgvector.

    Agora com proteção contra duplicação:
    - Não insere embeddings se o arquivo já foi processado
    """

    if not embedded_chunks:
        return

    # 🔐 Garantir isolamento por usuário
    user_id = embedded_chunks[0]["user_id"]

    # 🔎 Descobrir quais arquivos já foram processados
    processed_file_ids = get_processed_file_ids(user_id=user_id)

    objects: List[DocumentEmbedding] = []

    for chunk in embedded_chunks:

        # 🚫 Skip se já foi processado
        if chunk["file_id"] in processed_file_ids:
            continue

        objects.append(
            DocumentEmbedding(
                user_id=chunk["user_id"],
                file_id=chunk["file_id"],
                folder=chunk["folder"],
                path=chunk["path"],
                chunk_index=chunk["chunk_index"],
                content=chunk["content"],
                embedding=chunk["embedding"],
                metadata={
                    "source": "upload",
                },
            )
        )

    # 🚀 Inserção em lote (rápido)
    if objects:
        DocumentEmbedding.objects.bulk_create(objects, batch_size=1000)
```


















































---

<div id="train-view"></div>

## `Criando a view (ação) de treinamento: train_view()`

Agora, nós vamos criar (implementar) a view (ação) `train_view()`:

[rag/views.py](../../../rag/views.py)
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from rag.models import DocumentEmbedding
from rag.services.ingestion.chunking import chunk_text
from rag.services.ingestion.embeddings import (
    generate_embeddings,
    get_embedding_model,
)
from rag.services.ingestion.file_discovery import discover_workspace_files
from rag.services.ingestion.text_extraction import extract_text
from rag.services.ingestion.vector_store import store_embeddings

# ==============================
# 🔹 Helpers
# ==============================


def _clean_texts(texts):
    cleaned = []

    for text in texts:
        if not isinstance(text, str):
            print("⚠️ Ignorado: não é string")
            continue

        cleaned_text = text.strip()

        if not cleaned_text:
            print("⚠️ Ignorado: texto vazio")
            continue

        cleaned.append(cleaned_text)

    return cleaned


def _generate_chunks_from_text(text):
    chunks = chunk_text(
        text=text,
        chunk_size=300,
        chunk_overlap=30,
    )

    if not chunks:
        print("⚠️ Fallback aplicado (1 chunk criado)")
        return [text]

    return chunks


def _process_file(file, user_id):
    """Executa pipeline de 1 arquivo (thread-safe)."""
    embedded_chunks = []

    try:
        texts = extract_text(file)

        print(f"\n📄 Arquivo: {file['name']}")
        print(f"🧾 Textos extraídos: {len(texts) if texts else 0}")

        if not texts:
            return []

        cleaned_texts = _clean_texts(texts)

        for text in cleaned_texts:
            chunks = _generate_chunks_from_text(text)

            print(f"🧩 Chunks gerados: {len(chunks)}")

            for index, chunk in enumerate(chunks):
                embedded_chunks.append(
                    {
                        "user_id": user_id,
                        "file_id": file["file_id"],
                        "folder": file["folder"],
                        "path": file["absolute_path"],
                        "chunk_index": index,
                        "content": chunk,
                    }
                )

    except Exception as e:
        print(f"❌ Erro no arquivo {file['name']}: {e}")

    return embedded_chunks


# ==============================
# 🔥 View com paralelismo
# ==============================

@login_required
def train_view(request):

    if request.method != "POST":
        return redirect("workspace_home")

    user = request.user
    folder_id = request.POST.get("folder")
    folder_id = int(folder_id) if folder_id else None

    try:
        # 🔥 Reset total
        DocumentEmbedding.objects.filter(
            user_id=user.id
        ).delete()

        print("🧹 Embeddings antigos removidos (reset total)")

        # 🔍 Descobrir arquivos
        files = discover_workspace_files(
            user=user,
            folder_id=folder_id
        )

        if not files:
            messages.warning(request, "Nenhum arquivo encontrado.")
            return redirect(request.POST.get("next", "workspace_home"))

        embedded_chunks = []

        # ⚡ Paralelismo aqui
        MAX_WORKERS = 4  # pode ajustar (4 ~ 8 ideal)

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [
                executor.submit(_process_file, file, user.id)
                for file in files
            ]

            for future in as_completed(futures):
                result = future.result()
                if result:
                    embedded_chunks.extend(result)

        print(f"\n🚀 Total de chunks: {len(embedded_chunks)}")

        if not embedded_chunks:
            messages.warning(
                request,
                "Nenhum conteúdo válido encontrado após processamento."
            )
            return redirect(request.POST.get("next", "workspace_home"))

        # 🧠 Embeddings (mantido sequencial — mais seguro)
        model = get_embedding_model()

        embedded_chunks = generate_embeddings(
            embedding_model=model,
            chunks=embedded_chunks,
        )

        # 💾 Persistência
        store_embeddings(
            embedded_chunks=embedded_chunks
        )

        messages.success(
            request,
            f"Treinamento concluído! {len(files)} arquivos processados."
        )

    except Exception as e:
        messages.error(request, f"Erro no treinamento: {str(e)}")

    return redirect(request.POST.get("next", "workspace_home"))
```


















































---

<div id="training-url"></div>

## `Criando/Relacionando a ROTA/URL de Treinamento: train/`

Agora, nós vamos:

 - Criar uma ROTA/URL `train` no app `RAG`
 - Relacionar essa ROTA/URL com as rotas gerais do projeto: `core/urls.py`
 - Relacionar essa ROTA/URL com a view (ação) `train_view()`

Vamos começar criando a ROTA/URL `train` e relacionando ela com a nossa view (ação) `train_view()`:

[rag/urls.py](../../../rag/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [
    path(
        route="train",
        view=views.train_view,
        name="train"
    )
]
```

Agora, vamos relacionar as ROTAS/URLs do app `RAG` com as rotas do projeto:

[core/urls.py](../../../core/urls.py)
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    ...

    path(
        "",
        include("rag.urls")
    ),
]
```


















































---

<div id="mapping-front-back"></div>

## `Criando/relacionando a ROTA/URL train: front(template) <--> back(view)`

Por fim, nós vamos referenciar a ROTA/URL `train` no botão `"🤖 Treinar"`, no template `workspace_home`:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<!-- 🤖 Botão Treinar -->
{% if not current_folder %}
    <form method="post"
        action="{% url 'train' %}">

        ...

    </form>
{% endif %}
```

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
