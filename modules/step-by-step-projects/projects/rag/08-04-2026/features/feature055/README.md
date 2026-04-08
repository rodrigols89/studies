# `Criando o mecanismo de separação de treinamento por pastas`

## Conteúdo

 - [`Criando e configurando o app "train" nas configurações do Django`](#create-train-app)
 - [`Atualizando o modelo DocumentEmbedding()`](#update-document-embedding-model)
 - [`Atualizando o rag/services/ingestion/file_discovery.py`](#update-file-discovery)
 - [`Atualizando o módulo rag/services/ingestion/vector_store.py`](#update-vector-store)
 - [`Atualizando o módulo rag/services/retrieval/vector_search.py`](#update-vector-search)
 - [`Atualizando o módulo rag/services/qa_services.py`](#update-qa-services)
 - [`Criando o módulo workspace/browser.py`](#create-workspace-browser)
 - [`Atualizando a view workspace/view.py`](#update-workspace-view)
 - [`Atualizando o template workspace_home.html`](#update-workspace-home-template)
 - [`Criando os modelos de treino train/models.py`](#create-train-models)
 - [`Registrando os modelos de treino train/models.py no Django Admin`](#registre-train-models)
 - [`Criando o train/utils.py`](#create-train-utils)
 - [`Criando o rag/services/ingestion/embedding_pipeline.py`](#embedding-pipeline)
 - [`Criando a view train/view.py`](#create-train-view)
 - [`Mapeando a ROTA/URL para a view train_view()`](#map-url-to-view)
 - [`Atualizando o sidebar`](#update-sidebar)
 - [`Criando o template train_home.html`](#create-train-home-template)
 - [`Criando o template training_model_detail.html`](#create-training-model-template)
 - [`Atualizando a view users/views.py`](#update-users-views)
 - [`Atualizando a view chat/views.py`](#update-chat-views)
 - [`Atualizando o template home.html`](#update-home-template)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="create-train-app"></div>

## `Criando e configurando o app "train" nas configurações do Django`

Para começar vamos criar o app `train` que será responsável por toda a lógia de treinamento:

```bash
python manage.py startapp train
```

Agora, vamos adicionar esse app nos app instalados:

[core/settings.py](../../../core/settings.py)
```python
INSTALLED_APPS = [

    ...

    # Seus apps
    ...
    "train",
]
```


















































---

<div id="update-document-embedding-model"></div>

## `Atualizando o modelo DocumentEmbedding()`

Antes de trabalhar nas novas views, vamos atualizar o nosso modelo `DocumentEmbedding()`:

[rag/models.py](../../../rag/models.py)
```python
from django.db import models
from pgvector.django import VectorField


class DocumentEmbedding(models.Model):

    user_id: models.PositiveIntegerField = (
        models.PositiveIntegerField(
            db_index=True,
        )
    )

    file_id: models.PositiveIntegerField = (
        models.PositiveIntegerField(
            db_index=True,
        )
    )

    folder: models.CharField = (
        models.CharField(
            max_length=255,
            db_index=True,
        )
    )

    path: models.CharField = (
        models.CharField(
            max_length=500,
            db_index=True,
        )
    )

    chunk_index: models.PositiveIntegerField = (
        models.PositiveIntegerField()
    )

    content: models.TextField = (
        models.TextField()
    )

    embedding: VectorField = (
        VectorField(
            dimensions=3072,
        )
    )

    metadata: models.JSONField = (
        models.JSONField(
            default=dict,
        )
    )

    created_at: models.DateTimeField = (
        models.DateTimeField(
            auto_now_add=True,
        )
    )

    training_model = models.ForeignKey(
        "train.TrainingModel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="embeddings",
    )

    class Meta:
        indexes = [
            models.Index(fields=["user_id"]),
            models.Index(fields=["file_id"]),
            models.Index(fields=["folder"]),
        ]
```


















































---

<div id="update-file-discovery"></div>

## `Atualizando o rag/services/ingestion/file_discovery.py`

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
import os
from collections import deque
from typing import Any, Dict, List, Optional

from workspace.models import File, Folder


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

    if file.folder:
        workspace_path = f"{file.folder.full_path}/{file.name}"
    else:
        workspace_path = f"workspace/{file.name}"

    return {
        "file_id": file.id,
        "name": file.name,
        "file_type": get_file_type(file.name),
        "folder": folder_path,
        "folder_id": file.folder_id,
        "workspace_path": workspace_path,
        "absolute_path": file.file.path,
    }


def _folder_ids_with_descendants(
    user: Any,
    root_ids: List[int],
) -> List[int]:
    """
    Expande IDs de pastas para incluir todas as subpastas (BFS).
    Apenas pastas do usuário e não deletadas entram.
    """
    if not root_ids:
        return []

    seen: set[int] = set()
    queue: deque[int] = deque()

    for rid in root_ids:
        if rid not in seen:
            seen.add(rid)
            queue.append(rid)

    while queue:
        cur = queue.popleft()
        children = Folder.objects.filter(
            parent_id=cur,
            owner=user,
            is_deleted=False,
        ).values_list("id", flat=True)
        for cid in children:
            if cid not in seen:
                seen.add(cid)
                queue.append(cid)

    return list(seen)


def _inventory_from_queryset(queryset: Any) -> List[Dict[str, Any]]:
    inventory: List[Dict[str, Any]] = []
    for file_obj in queryset:
        try:
            inventory.append(map_file(file_obj))
        except Exception:
            continue
    return inventory


def discover_all_workspace_files(*, user: Any) -> List[Dict[str, Any]]:
    """
    Todos os arquivos do usuário no workspace (raiz e todas as pastas),
    sem filtrar por pasta.
    """
    if user is None:
        raise ValueError(
            "Usuário é obrigatório para descobrir arquivos do workspace"
        )
    queryset = (
        File.objects.filter(uploader=user, is_deleted=False)
        .order_by("id")
    )
    return _inventory_from_queryset(queryset)


def discover_workspace_files(
    *,
    user: Any,
    folder_id: Optional[int] = None,
    folder_ids: Optional[List[int]] = None,
) -> List[Dict[str, Any]]:
    """
    Returns a list of mapped files from the user's workspace.

    - Se folder_ids for informado e não vazio → arquivos em qualquer
      dessas pastas ou subpastas (árvore completa).
    - Se folder_id for None e folder_ids vazio/ausente → todos os arquivos
    - Se folder_id for informado (sem folder_ids) → filtra só essa pasta
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

    # 📁 Filtro por várias pastas (inclui subpastas)
    if folder_ids:
        valid_roots = list(
            Folder.objects.filter(
                id__in=folder_ids,
                owner=user,
                is_deleted=False,
            ).values_list("id", flat=True)
        )
        expanded = _folder_ids_with_descendants(user, list(valid_roots))
        if not expanded:
            return []
        queryset = queryset.filter(folder_id__in=expanded)
    elif folder_id:
        queryset = queryset.filter(folder_id=folder_id)

    queryset = queryset.order_by("id")
    return _inventory_from_queryset(queryset)
```


















































---

<div id="update-vector-store"></div>

## `Atualizando o módulo rag/services/ingestion/vector_store.py`

[rag/services/ingestion/vector_store.py](../../../rag/services/ingestion/vector_store.py)
```python
from typing import Any, Dict, List, Set

from rag.models import DocumentEmbedding


def get_processed_file_ids(
    *,
    user_id: int,
    training_model_id: int,
) -> Set[int]:
    """
    Retorna file_ids já processados para aquele modelo de treino.
    """
    return set(
        DocumentEmbedding.objects.filter(
            user_id=user_id,
            training_model_id=training_model_id,
        )
        .values_list("file_id", flat=True)
        .distinct()
    )


def store_embeddings(
    *,
    embedded_chunks: List[Dict[str, Any]],
    training_model_id: int,
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

    # 🔎 Descobrir quais arquivos já foram processados neste modelo
    processed_file_ids = get_processed_file_ids(
        user_id=user_id,
        training_model_id=training_model_id,
    )

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
                training_model_id=training_model_id,
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

<div id="update-vector-search"></div>

## `Atualizando o módulo rag/services/retrieval/vector_search.py`

[rag/services/retrieval/vector_search.py](../../../rag/services/retrieval/vector_search.py)
```python
from typing import List, Optional

from pgvector.django import CosineDistance

from rag.models import DocumentEmbedding


def vector_search(
    *,
    user_id: int,
    query_vector: List[float],
    top_k: int = 5,
    training_model_id: Optional[int] = None,
) -> List[DocumentEmbedding]:
    """
    Busca os chunks mais similares à pergunta do usuário
    utilizando cosine distance.

    Se ``training_model_id`` for informado, restringe a esse modelo.
    Se for None, usa apenas embeddings legados (sem modelo associado).
    """

    qs = DocumentEmbedding.objects.filter(user_id=user_id)

    if training_model_id is not None:
        qs = qs.filter(training_model_id=training_model_id)
    else:
        qs = qs.filter(training_model_id__isnull=True)

    results = (
        qs.annotate(
            distance=CosineDistance(
                "embedding",
                query_vector,
            )
        )
        .order_by("distance")[:top_k]
    )

    return list(results)
```


















































---

<div id="update-qa-services"></div>

## `Atualizando o módulo rag/services/qa_services.py`

[rag/services/qa_service.py](../../../rag/services/qa_service.py)
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


















































---

<div id="create-workspace-browser"></div>

## `Criando o módulo workspace/browser.py`

[workspace/browser.py](../../../workspace/browser.py)
```python
"""
Listagem e breadcrumbs do workspace (reutilizável por várias views).
"""

from typing import Any

from django.shortcuts import get_object_or_404

from .models import File, Folder


def build_breadcrumbs(folder: Folder | None) -> list[Folder]:
    """
    Lista de pastas do caminho (raiz -> atual).
    """
    breadcrumbs: list[Folder] = []
    while folder:
        breadcrumbs.insert(0, folder)
        folder = folder.parent
    return breadcrumbs


def get_workspace_browser_context(
    *,
    user: Any,
    folder_id: str | None,
) -> dict[str, Any]:
    """
    Contexto para listar pastas e arquivos na raiz ou dentro de uma pasta.
    """
    if folder_id:
        current_folder = get_object_or_404(
            Folder,
            id=folder_id,
            owner=user,
        )
        folders = Folder.objects.filter(
            parent=current_folder,
            owner=user,
            is_deleted=False,
        ).order_by("name")
        files = File.objects.filter(
            folder=current_folder,
            uploader=user,
            is_deleted=False,
        ).order_by("name")
        breadcrumbs = build_breadcrumbs(current_folder)
    else:
        current_folder = None
        folders = Folder.objects.filter(
            owner=user,
            parent__isnull=True,
            is_deleted=False,
        ).order_by("name")
        files = File.objects.filter(
            uploader=user,
            folder__isnull=True,
            is_deleted=False,
        ).order_by("name")
        breadcrumbs = []

    return {
        "current_folder": current_folder,
        "folders": folders,
        "files": files,
        "breadcrumbs": breadcrumbs,
    }
```


















































---

<div id="update-workspace-view"></div>

## `Atualizando a view workspace/view.py`

[workspace/views.py](../../../workspace/views.py)
```python
import json
import logging
import os
import traceback
from collections import Counter
from dataclasses import dataclass
from typing import Any

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from utils.messages import (
    WORKSPACE_EMPTY_FOLDER_NAME,
    WORKSPACE_FILE_MOVED_TO_TRASH,
    WORKSPACE_FILE_SENT_SUCCESS,
    WORKSPACE_FOLDER_CREATED_SUCCESS,
    WORKSPACE_FOLDER_DELETED_SUCCESS,
    WORKSPACE_FOLDER_UPLOADED_SUCCESS,
    WORKSPACE_MANY_FILES_SENT_SUCCESS,
    WORKSPACE_MORE_FILES_WITH_ERROR,
    WORKSPACE_NO_FILE_PROCESSED,
    WORKSPACE_NO_FILE_SENT,
    WORKSPACE_NO_FOLDER_SELECTED,
)

from .browser import build_breadcrumbs, get_workspace_browser_context
from .forms import FolderForm
from .models import File, Folder
from .validators import validate_file

MAX_ERROR_MESSAGES_UPLOAD_FILE = 3
MAX_ERROR_MESSAGES_UPLOAD_FOLDER = 5


@dataclass
class FolderUploadParams:
    """Parâmetros para processamento de upload de pasta."""
    user: Any
    uploaded_files: list[Any]
    file_paths_list: list[str]
    folder_name: str
    main_folder: Folder
    folders_cache: dict[str, Folder]


@dataclass
class FileUploadParams:
    """Parâmetros para processamento de upload de arquivo."""
    user: Any
    uploaded_file: Any
    file_path: str
    folder_name: str
    target_folder: Folder
    folders_cache: dict[str, Folder]


@dataclass
class UploadResults:
    """Resultados do upload de pasta."""
    request: HttpRequest
    main_folder: Folder
    folder_name: str
    uploaded_count: int
    error_count: int
    error_messages: list[str]


@login_required(login_url="/")
def workspace_home(request: HttpRequest) -> HttpResponse:
    """
    View principal do workspace.

    Exibe as pastas e arquivos do usuário, suportando navegação
    hierárquica através do parâmetro 'folder' na query string.

    Args:
        request: Objeto HttpRequest do Django

    Returns:
        HttpResponse: Renderiza o template workspace_home.html
    """
    folder_id = request.GET.get("folder")
    context = get_workspace_browser_context(
        user=request.user,
        folder_id=folder_id,
    )
    return render(request, "pages/workspace_home.html", context)


def _check_folder_name_exists(
    user: Any,
    folder_name: str,
    parent_folder: Folder | None,
    exclude_id: int | None = None,
) -> bool:
    """
    Verifica se já existe uma pasta com o nome especificado no mesmo nível.

    Args:
        user: Usuário proprietário
        folder_name: Nome da pasta a verificar
        parent_folder: Pasta pai (None para raiz)
        exclude_id: ID da pasta a excluir da verificação (opcional)

    Returns:
        bool: True se o nome já existe, False caso contrário
    """
    query = Folder.objects.filter(
        owner=user,
        name__iexact=folder_name,
        parent=parent_folder,
        is_deleted=False
    )
    if exclude_id:
        query = query.exclude(id=exclude_id)
    return query.exists()


def _check_file_name_exists(
    user: Any,
    file_name: str,
    folder: Folder | None,
    exclude_id: int | None = None,
) -> bool:
    """
    Verifica se já existe um arquivo com o mesmo nome no diretório.

    Args:
        user: Usuário proprietário
        file_name: Nome do arquivo a verificar
        folder: Pasta de destino (None para raiz)
        exclude_id: ID do arquivo a excluir da verificação (opcional)

    Returns:
        bool: True se o nome já existe, False caso contrário
    """
    query = File.objects.filter(
        uploader=user,
        name__iexact=file_name,
        folder=folder,
        is_deleted=False
    )
    if exclude_id:
        query = query.exclude(id=exclude_id)
    return query.exists()


@login_required(login_url="/")
def create_folder(request: HttpRequest) -> HttpResponse:
    """
    View para criação de nova pasta.

    Valida o nome e verifica duplicação no mesmo nível hierárquico.
    Suporta criação de pastas dentro de outras pastas.

    Args:
        request: Objeto HttpRequest do Django

    Returns:
        HttpResponse: Redireciona ou renderiza template com erros
    """
    if request.method == "POST":
        form = FolderForm(request.POST)

        parent_id = request.POST.get("parent")
        parent_folder = None
        if parent_id:
            parent_folder = get_object_or_404(
                Folder,
                id=parent_id,
                owner=request.user
            )

        if form.is_valid():
            name = form.cleaned_data["name"]

            if _check_folder_name_exists(request.user, name, parent_folder):
                form.add_error(
                    "name",
                    "Já existe uma pasta com esse nome nesse diretório."
                )
            else:
                new_folder = form.save(commit=False)
                new_folder.owner = request.user
                new_folder.parent = parent_folder
                new_folder.save()

                messages.success(
                    request,
                    WORKSPACE_FOLDER_CREATED_SUCCESS.format(name=name)
                )
                return redirect(
                    request.POST.get("next", "workspace_home")
                )

        if parent_folder:
            folders = Folder.objects.filter(
                parent=parent_folder,
                is_deleted=False
            )
            files = File.objects.filter(
                folder=parent_folder,
                is_deleted=False
            )
            breadcrumbs = build_breadcrumbs(parent_folder)
        else:
            folders = Folder.objects.filter(
                owner=request.user,
                parent__isnull=True,
                is_deleted=False
            )
            files = File.objects.filter(
                uploader=request.user,
                folder__isnull=True,
                is_deleted=False
            )
            breadcrumbs = []

        context = {
            "form": form,
            "current_folder": parent_folder,
            "folders": folders,
            "files": files,
            "breadcrumbs": breadcrumbs,
            "show_modal": True,
        }

        return render(request, "pages/workspace_home.html", context)

    return redirect("workspace_home")


def _validate_uploaded_file(uploaded_file: Any) -> str | None:
    """
    Valida um arquivo enviado e retorna mensagem de erro se houver.
    """
    try:
        validate_file(uploaded_file)
        return None
    except Exception as e:
        error_message = _extract_error_message(e)  # ✅ Remove os colchetes
        return error_message  # ✅ Retorna apenas a mensagem, sem prefixo


def _generate_unique_filename(
    user: Any, folder: Folder | None, original_name: str
) -> str:
    """
    Gera um nome de arquivo único para evitar duplicatas.
    """
    base, ext = os.path.splitext(original_name)
    new_name = original_name
    counter = 1

    while _check_file_name_exists(user, new_name, folder):
        new_name = f"{base} ({counter}){ext}"
        counter += 1

    return new_name


def _create_file_instance(
    user: Any,
    folder: Folder | None,
    uploaded_file: Any,
    new_name: str,
) -> bool:
    """
    Cria uma instância de File no banco de dados.
    Retorna True se bem-sucedido, False caso contrário.
    """
    try:
        File.objects.create(
            name=new_name,
            file=uploaded_file,
            folder=folder,
            uploader=user,
        )
        return True
    except Exception:
        return False


def _process_single_file_upload(
    user: Any, folder: Folder | None, uploaded_file: Any
) -> tuple[bool, str | None]:
    """
    Processa o upload de um único arquivo.
    Retorna (success, error_message).
    """
    error_msg = _validate_uploaded_file(uploaded_file)
    if error_msg:
        return (False, error_msg)

    new_name = _generate_unique_filename(
        user, folder, uploaded_file.name
    )

    if _create_file_instance(user, folder, uploaded_file, new_name):
        return (True, None)

    return (False, f"{uploaded_file.name}: Erro ao salvar arquivo")


@login_required(login_url="/")
def upload_file(request: HttpRequest) -> HttpResponse:
    """
    View para upload de arquivos (um ou múltiplos).

    Realiza validações de extensão e tamanho, além de renomear
    automaticamente arquivos duplicados. Suporta upload de
    um ou múltiplos arquivos.

    Args:
        request: Objeto HttpRequest do Django

    Returns:
        HttpResponse: Redireciona após upload ou exibe erros
    """
    if request.method == "POST":
        uploaded_files = request.FILES.getlist("file")
        next_url = request.POST.get("next", "workspace_home")
        folder_id = request.POST.get("folder")
        folder = None

        if folder_id:
            folder = get_object_or_404(
                Folder,
                id=folder_id,
                owner=request.user
            )

        if not uploaded_files:
            messages.error(request, WORKSPACE_NO_FILE_SENT)
            return redirect(next_url)

        uploaded_count = 0
        error_count = 0
        error_messages = []

        for uploaded_file in uploaded_files:
            success, error_message = _process_single_file_upload(
                request.user, folder, uploaded_file
            )

            if success:
                uploaded_count += 1
            else:
                error_count += 1
                error_messages.append(error_message)

        if uploaded_count > 0:
            if uploaded_count == 1:
                messages.success(request, WORKSPACE_FILE_SENT_SUCCESS)
            else:
                messages.success(
                    request,
                    WORKSPACE_MANY_FILES_SENT_SUCCESS.format(count=uploaded_count)
                )

        if error_count > 0:
            for error_msg in error_messages[:MAX_ERROR_MESSAGES_UPLOAD_FILE]:
                messages.error(request, error_msg)
            if len(error_messages) > MAX_ERROR_MESSAGES_UPLOAD_FILE:
                max_err = MAX_ERROR_MESSAGES_UPLOAD_FILE
                remaining = len(error_messages) - max_err
                messages.warning(
                    request,
                    WORKSPACE_MORE_FILES_WITH_ERROR.format(remaining=remaining)
                )

        return redirect(next_url)

    return redirect("workspace_home")


def _determine_folder_name(
    uploaded_files: list[Any], folder_name: str
) -> str:
    """
    Determina o nome da pasta a partir dos arquivos ou nome fornecido.
    """
    if folder_name:
        return folder_name

    first_dirs = []
    for uploaded_file in uploaded_files:
        file_path = uploaded_file.name
        path_parts = file_path.split("/")
        if len(path_parts) > 1 and path_parts[0].strip():
            first_dirs.append(path_parts[0].strip())

    if not first_dirs:
        timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
        return f"Pasta Upload {timestamp}"

    unique_first_dirs = set(first_dirs)
    if len(unique_first_dirs) == 1:
        return list(unique_first_dirs)[0]

    if len(unique_first_dirs) > 1:
        dir_counter = Counter(first_dirs)
        return dir_counter.most_common(1)[0][0]

    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
    return f"Pasta Upload {timestamp}"


def _ensure_unique_folder_name(
    user: Any, parent_folder: Folder | None, folder_name: str
) -> str:
    """
    Garante que o nome da pasta seja único no mesmo nível hierárquico.
    """
    if not _check_folder_name_exists(user, folder_name, parent_folder):
        return folder_name

    base_name = folder_name
    counter = 1
    while _check_folder_name_exists(user, folder_name, parent_folder):
        folder_name = f"{base_name} ({counter})"
        counter += 1

    return folder_name


def _setup_folder_upload(
    user: Any,
    uploaded_files: list[Any],
    folder_name_input: str,
    parent_folder: Folder | None,
) -> tuple[Folder, str]:
    """
    Configura o upload de pasta: determina nome e cria pasta principal.
    Retorna (main_folder, folder_name).
    """
    folder_name = _determine_folder_name(uploaded_files, folder_name_input)
    folder_name = _ensure_unique_folder_name(
        user, parent_folder, folder_name
    )

    main_folder = Folder.objects.create(
        name=folder_name,
        owner=user,
        parent=parent_folder
    )

    return (main_folder, folder_name)


def _prepare_file_paths(
    uploaded_files: list[Any], file_paths_json: str
) -> list[str]:
    """
    Prepara a lista de caminhos de arquivos a partir dos arquivos
    enviados e do JSON opcional.
    """

    file_paths_list = []

    if file_paths_json:
        try:
            file_paths_list = json.loads(file_paths_json)
        except json.JSONDecodeError:
            pass

    if not file_paths_list:
        file_paths_list = [
            uploaded_file.name for uploaded_file in uploaded_files
        ]

    return file_paths_list


def _normalize_path_parts(file_path: str, folder_name: str) -> list[str]:
    """
    Normaliza os path_parts removendo o primeiro diretório se for igual ao
    folder_name.
    """
    path_parts = file_path.split("/")
    if len(path_parts) > 1:
        first_dir = path_parts[0].strip()
        if (folder_name and
                first_dir.lower() == folder_name.strip().lower()):
            path_parts = path_parts[1:]
    return path_parts


def _collect_folder_paths(
    file_paths_list: list[str], folder_name: str
) -> list[str]:
    """
    Coleta todos os caminhos de pastas a partir dos caminhos dos arquivos.
    """
    all_folder_paths = set()
    for file_path in file_paths_list:
        if not file_path:
            continue

        path_parts = _normalize_path_parts(file_path, folder_name)
        if len(path_parts) <= 1:
            continue

        folder_path = "/".join(path_parts[:-1])
        if not folder_path or not folder_path.strip():
            continue

        all_folder_paths.add(folder_path.strip())
        path_components = folder_path.split("/")
        for i in range(1, len(path_components) + 1):
            intermediate_path = "/".join(path_components[:i])
            if intermediate_path and intermediate_path.strip():
                all_folder_paths.add(intermediate_path.strip())

    return sorted(all_folder_paths, key=lambda x: (x.count("/"), x))


def _create_subfolders(
    user: Any, main_folder: Folder, sorted_paths: list[str]
) -> dict[str, Folder]:
    """
    Cria todas as subpastas necessárias e retorna um cache de pastas.
    """
    folders_cache = {}
    folders_cache[""] = main_folder

    for folder_path in sorted_paths:
        if folder_path in folders_cache:
            continue

        current_path = ""
        current_parent = main_folder

        for raw_subfolder_name in folder_path.split("/"):
            cleaned_name = raw_subfolder_name.strip()
            if not cleaned_name:
                continue

            if current_path:
                current_path = f"{current_path}/{cleaned_name}"
            else:
                current_path = cleaned_name

            if current_path in folders_cache:
                current_parent = folders_cache[current_path]
                continue

            existing_folder = Folder.objects.filter(
                owner=user,
                parent=current_parent,
                name=cleaned_name,
                is_deleted=False
            ).first()

            if existing_folder:
                folders_cache[current_path] = existing_folder
                current_parent = existing_folder
            else:
                new_folder = Folder.objects.create(
                    name=cleaned_name,
                    owner=user,
                    parent=current_parent
                )
                folders_cache[current_path] = new_folder
                current_parent = new_folder

    return folders_cache


def _get_target_folder(
    user: Any,
    main_folder: Folder,
    path_parts: list[str],
    folders_cache: dict[str, Folder],
) -> Folder:
    """
    Obtém a pasta de destino para um arquivo baseado em seu caminho.
    """
    if len(path_parts) <= 1:
        return main_folder

    folder_path = "/".join(path_parts[:-1])
    if not folder_path or not folder_path.strip():
        return main_folder

    folder_path_stripped = folder_path.strip()
    if folder_path_stripped in folders_cache:
        return folders_cache[folder_path_stripped]

    path_components = folder_path_stripped.split("/")
    current_parent = main_folder
    for subfolder_name in path_components:
        if not subfolder_name:
            continue
        existing_folder = Folder.objects.filter(
            owner=user,
            parent=current_parent,
            name=subfolder_name,
            is_deleted=False
        ).first()
        if existing_folder:
            current_parent = existing_folder
        else:
            break

    return current_parent


def _extract_error_message(exception: Exception) -> str:
    """
    Extrai a mensagem de erro de uma exceção.
    """
    if isinstance(exception, ValidationError):
        if hasattr(exception, 'messages') and exception.messages:
            return str(exception.messages[0])
        if hasattr(exception, 'message'):
            return str(exception.message)
        return str(exception)

    if hasattr(exception, 'message'):
        return str(exception.message)

    return str(exception)


def _extract_error_detail(exception: Exception) -> str:
    """
    Extrai detalhes de erro de uma exceção para logging.
    """
    error_detail = str(exception)
    if isinstance(exception, ValidationError):
        if hasattr(exception, 'messages') and exception.messages:
            error_detail = str(exception.messages[0])
        elif hasattr(exception, 'message_dict'):
            error_detail = str(exception.message_dict)
    return error_detail


def _process_file_upload(
    params: FileUploadParams,
) -> tuple[bool, str | None, str]:
    """
    Processa o upload de um arquivo individual.
    Retorna (success, error_message, file_name).
    """
    if not params.file_path:
        params.file_path = params.uploaded_file.name

    path_parts = _normalize_path_parts(
        params.file_path, params.folder_name
    )
    file_name = path_parts[-1]

    target_folder = _get_target_folder(
        params.user, params.target_folder, path_parts, params.folders_cache
    )

    try:
        validate_file(params.uploaded_file)
    except Exception as e:
        error_message = _extract_error_message(e)
        return (False, error_message, file_name)

    base, ext = os.path.splitext(file_name)
    new_name = file_name
    counter = 1

    while _check_file_name_exists(params.user, new_name, target_folder):
        new_name = f"{base} ({counter}){ext}"
        counter += 1

    try:
        File.objects.create(
            name=new_name,
            file=params.uploaded_file,
            folder=target_folder,
            uploader=params.user,
        )
        return (True, None, file_name)
    except Exception as e:
        error_detail = _extract_error_detail(e)
        if settings.DEBUG:
            logger = logging.getLogger(__name__)
            logger.error(
                f"Erro ao salvar arquivo {file_name}: {error_detail}"
            )
            logger.error(traceback.format_exc())
        error_message = (
            f"{file_name}: Erro ao salvar arquivo - {error_detail}"
        )
        return (False, error_message, file_name)


def _process_folder_uploads(
    params: FolderUploadParams,
) -> tuple[int, int, list[str]]:
    """
    Processa todos os uploads de arquivos em uma pasta.
    Retorna (uploaded_count, error_count, error_messages).
    """
    files_with_paths = []
    for i, uploaded_file in enumerate(params.uploaded_files):
        file_path = (
            params.file_paths_list[i]
            if i < len(params.file_paths_list)
            else uploaded_file.name
        )
        files_with_paths.append((uploaded_file, file_path))

    uploaded_count = 0
    error_count = 0
    error_messages = []

    for uploaded_file, file_path in files_with_paths:
        file_params = FileUploadParams(
            user=params.user,
            uploaded_file=uploaded_file,
            file_path=file_path,
            folder_name=params.folder_name,
            target_folder=params.main_folder,
            folders_cache=params.folders_cache
        )
        success, error_message, file_name = _process_file_upload(
            file_params
        )

        if success:
            uploaded_count += 1
        else:
            error_count += 1
            error_messages.append(error_message)

    return (uploaded_count, error_count, error_messages)


def _process_folder_upload_complete(
    user: Any,
    uploaded_files: list[Any],
    file_paths_json: str,
    folder_name: str,
    main_folder: Folder,
) -> tuple[int, int, list[str]]:
    """
    Processa completamente o upload de pasta: cria subpastas e arquivos.
    Retorna (uploaded_count, error_count, error_messages).
    """
    file_paths_list = _prepare_file_paths(uploaded_files, file_paths_json)
    sorted_paths = _collect_folder_paths(file_paths_list, folder_name)
    folders_cache = _create_subfolders(
        user, main_folder, sorted_paths
    )

    folder_params = FolderUploadParams(
        user=user,
        uploaded_files=uploaded_files,
        file_paths_list=file_paths_list,
        folder_name=folder_name,
        main_folder=main_folder,
        folders_cache=folders_cache
    )

    return _process_folder_uploads(folder_params)


def _handle_upload_results(results: UploadResults) -> None:
    """
    Processa os resultados do upload e exibe mensagens apropriadas.
    """
    if results.uploaded_count == 0 and results.error_count > 0:
        results.main_folder.delete()
        max_errors = MAX_ERROR_MESSAGES_UPLOAD_FOLDER
        for error_msg in results.error_messages[:max_errors]:
            messages.error(results.request, error_msg)
        if len(results.error_messages) > max_errors:
            remaining = len(results.error_messages) - max_errors
            messages.warning(
                results.request,
                f"E mais {remaining} arquivo(s) com erro."
            )
    elif results.error_count == 0 and results.uploaded_count > 0:
        messages.success(
            results.request,
            WORKSPACE_FOLDER_UPLOADED_SUCCESS.format(folder_name=results.folder_name)
        )
    elif results.uploaded_count > 0 and results.error_count > 0:
        max_errors = MAX_ERROR_MESSAGES_UPLOAD_FOLDER
        for error_msg in results.error_messages[:max_errors]:
            messages.error(results.request, error_msg)
        if len(results.error_messages) > max_errors:
            remaining = len(results.error_messages) - max_errors
            messages.warning(
                results.request,
                f"E mais {remaining} arquivo(s) com erro."
            )
    else:
        results.main_folder.delete()
        messages.error(results.request, WORKSPACE_NO_FILE_PROCESSED)


@login_required(login_url="/")
def upload_folder(request: HttpRequest) -> HttpResponse:
    """
    View para upload de pastas inteiras.

    Cria a pasta principal e todas as subpastas detectadas.
    Não processa arquivos.

    Args:
        request: Objeto HttpRequest do Django

    Returns:
        HttpResponse: Redireciona após criar as pastas
    """
    if request.method != "POST":
        return redirect("workspace_home")

    uploaded_files = request.FILES.getlist("files")
    next_url = request.POST.get("next", "workspace_home")
    folder_id = request.POST.get("folder")
    parent_folder = None

    if folder_id:
        parent_folder = get_object_or_404(
            Folder,
            id=folder_id,
            owner=request.user
        )

    if not uploaded_files:
        messages.error(request, WORKSPACE_NO_FOLDER_SELECTED)
        return redirect(next_url)

    folder_name_input = request.POST.get("folder_name", "").strip()
    main_folder, folder_name = _setup_folder_upload(
        request.user, uploaded_files, folder_name_input, parent_folder
    )

    file_paths_json = request.POST.get("file_paths", "")
    uploaded_count, error_count, error_messages = (
        _process_folder_upload_complete(
            request.user,
            uploaded_files,
            file_paths_json,
            folder_name,
            main_folder
        )
    )

    results = UploadResults(
        request=request,
        main_folder=main_folder,
        folder_name=folder_name,
        uploaded_count=uploaded_count,
        error_count=error_count,
        error_messages=error_messages
    )
    _handle_upload_results(results)

    return redirect(next_url)


@login_required(login_url="/")
def delete_file(request: HttpRequest, file_id: int) -> HttpResponse:
    """
    View para exclusão de arquivo (soft delete).

    Marca o arquivo como deletado sem removê-lo fisicamente do banco.
    Retorna para a pasta onde estava ou para a raiz.

    Args:
        request: Objeto HttpRequest do Django
        file_id: ID do arquivo a ser deletado

    Returns:
        HttpResponseRedirect: Redireciona após exclusão
    """
    file = get_object_or_404(
        File,
        id=file_id,
        uploader=request.user
    )

    folder = file.folder

    file.is_deleted = True
    file.deleted_at = timezone.now()
    file.save()

    messages.success(
        request,
        WORKSPACE_FILE_MOVED_TO_TRASH.format(file_name=file.name)
    )

    if folder:
        return redirect(f"/workspace?folder={folder.id}")

    return redirect("workspace_home")


@login_required(login_url="/")
def delete_folder(request: HttpRequest, folder_id: int) -> HttpResponse:
    """
    View para exclusão de pasta (soft delete).

    Marca a pasta como deletada sem removê-la fisicamente do banco.
    Retorna para a pasta pai ou para a raiz.

    Args:
        request: Objeto HttpRequest do Django
        folder_id: ID da pasta a ser deletada

    Returns:
        HttpResponseRedirect: Redireciona após exclusão
    """
    if request.method != "POST":
        return redirect("workspace_home")

    folder = get_object_or_404(
        Folder,
        id=folder_id,
        owner=request.user
    )

    parent = folder.parent

    folder.is_deleted = True
    folder.deleted_at = timezone.now()
    folder.save()

    messages.success(
        request,
        WORKSPACE_FOLDER_DELETED_SUCCESS.format(folder_name=folder.name)
    )

    if parent:
        return redirect(f"/workspace?folder={parent.id}")

    return redirect("workspace_home")


@login_required(login_url="/")
def rename_folder(request: HttpRequest, folder_id: int) -> HttpResponse:
    """
    View para renomear pasta.

    Valida o novo nome e verifica duplicação no mesmo nível hierárquico.

    Args:
        request: Objeto HttpRequest do Django
        folder_id: ID da pasta a ser renomeada

    Returns:
        HttpResponseRedirect: Redireciona após renomeação
    """
    folder = get_object_or_404(
        Folder,
        id=folder_id,
        owner=request.user,
        is_deleted=False
    )

    if request.method != "POST":
        return redirect("workspace_home")

    new_name = request.POST.get("name", "").strip()
    next_url = request.POST.get("next", "workspace_home")

    if not new_name:
        messages.error(
            request,
            WORKSPACE_EMPTY_FOLDER_NAME
        )
        return redirect(next_url)

    if _check_folder_name_exists(
        request.user, new_name, folder.parent, exclude_id=folder.id
    ):
        messages.error(
            request,
            "Já existe uma pasta com esse nome nesse diretório."
        )
        return redirect(next_url)

    old_name = folder.name
    folder.name = new_name
    folder.save()
    messages.success(
        request,
        f"Pasta '{old_name}' foi renomeada para '{new_name}'."
    )
    return redirect(next_url)


@login_required(login_url="/")
def rename_file(request: HttpRequest, file_id: int) -> HttpResponse:
    """
    View para renomear arquivo.

    Valida o novo nome e verifica duplicação no mesmo diretório.

    Args:
        request: Objeto HttpRequest do Django
        file_id: ID do arquivo a ser renomeado

    Returns:
        HttpResponseRedirect: Redireciona após renomeação
    """
    file = get_object_or_404(
        File,
        id=file_id,
        uploader=request.user,
        is_deleted=False
    )

    if request.method != "POST":
        return redirect("workspace_home")

    new_name = request.POST.get("name", "").strip()
    next_url = request.POST.get("next", "workspace_home")

    if not new_name:
        messages.error(
            request,
            "O nome do arquivo não pode ser vazio."
        )
        return redirect(next_url)

    if _check_file_name_exists(
        request.user, new_name, file.folder, exclude_id=file.id
    ):
        messages.error(
            request,
            "Já existe um arquivo com esse nome neste diretório."
        )
        return redirect(next_url)

    old_name = file.name
    file.name = new_name
    file.save()
    messages.success(
        request,
        f"Arquivo '{old_name}' foi renomeado para '{new_name}'."
    )
    return redirect(next_url)


def _is_descendant(folder: Folder, potential_parent: Folder | None) -> bool:
    """
    Helper para evitar mover uma pasta para ela mesma ou seus filhos.

    Verifica se a pasta potencial pai é descendente da pasta atual,
    o que criaria um ciclo na hierarquia.

    Args:
        folder: Pasta que está sendo movida
        potential_parent: Pasta que seria o novo pai

    Returns:
        bool: True se potential_parent é descendente de folder
    """
    current = potential_parent
    while current:
        if current == folder:
            return True
        current = current.parent
    return False


@login_required(login_url="/")
def move_item(request: HttpRequest) -> JsonResponse:  # noqa: PLR0911
    """
    View para mover pastas ou arquivos (via AJAX).

    Suporta mover itens entre pastas ou para a raiz.
    Retorna JSON para requisições AJAX.

    Args:
        request: Objeto HttpRequest do Django

    Returns:
        JsonResponse: Resposta JSON com sucesso ou erro
    """
    if request.method != "POST":
        return JsonResponse(
            {"error": "Método inválido."},
            status=405
        )

    item_type = request.POST.get("item_type")
    item_id = request.POST.get("item_id")
    target_folder_id = request.POST.get("target_folder") or None

    if not item_type or not item_id:
        return JsonResponse(
            {"error": "Dados insuficientes para mover o item."},
            status=400
        )

    target_folder = None
    if target_folder_id:
        target_folder = get_object_or_404(
            Folder,
            id=target_folder_id,
            owner=request.user,
            is_deleted=False,
        )

    if item_type == "folder":
        folder = get_object_or_404(
            Folder,
            id=item_id,
            owner=request.user,
            is_deleted=False,
        )

        if target_folder and _is_descendant(folder, target_folder):
            error_message = (
                "Não é possível mover a pasta para dentro dela mesma."
            )
            return JsonResponse(
                {"error": error_message},
                status=400,
            )

        # Verifica se já existe uma pasta com o mesmo nome no destino
        if _check_folder_name_exists(
            request.user, folder.name, target_folder, exclude_id=folder.id
        ):
            error_message = (
                f"Já existe uma pasta com o nome '{folder.name}' "
                "no diretório de destino."
            )
            return JsonResponse(
                {"error": error_message},
                status=400,
            )

        folder.parent = target_folder
        folder.save()
        return JsonResponse({"success": True})

    elif item_type == "file":
        file = get_object_or_404(
            File,
            id=item_id,
            uploader=request.user,
            is_deleted=False,
        )

        # Verifica se já existe um arquivo com o mesmo nome no destino
        if _check_file_name_exists(
            request.user, file.name, target_folder, exclude_id=file.id
        ):
            error_message = (
                f"Já existe um arquivo com o nome '{file.name}' "
                "no diretório de destino."
            )
            return JsonResponse(
                {"error": error_message},
                status=400,
            )

        file.folder = target_folder
        file.save()
        return JsonResponse({"success": True})

    return JsonResponse(
        {"error": "Tipo de item inválido."},
        status=400
    )


@login_required
def folder_view(request: HttpRequest, folder_id: int) -> HttpResponse:
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


















































---

<div id="update-workspace-home-template"></div>

## `Atualizando o template workspace_home.html`

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
{% extends "base.html" %}
{% load static %}


{% block title %}Workspace{% endblock %}


{% block head %}
    <link
        rel="stylesheet"
        href="{% static 'workspace/css/workspace_home.css' %}">
{% endblock head %}


{% block content %}
    <!-- Container principal -->
    <div class="flex h-screen bg-gray-100">


        <!-- 🧱 Sidebar -->
        {% include "partials/sidebar.html" with current_page="workspace" %}


        <!-- 💼 Área principal do Workspace -->
        <main class="flex-1 p-8 overflow-y-auto">


            <!-- Header -->
            <header class="bg-white shadow px-6 py-4">
                <h1 class="text-2xl font-semibold text-gray-800">
                    Bem-vindo, {{ request.user.username }}!
                </h1>
            </header>


            <!-- 🧭 Breadcrumbs -->
            <nav class="text-sm text-gray-600 my-4 flex items-center
                space-x-2">

                {% if current_folder %}

                    {% if breadcrumbs|length > 1 %}
                        {% with prev_folder=breadcrumbs|slice:"-2:-1"|first %}
                            <a href="?folder={{ prev_folder.id }}"
                               class="text-blue-600 hover:underline
                                   breadcrumb-drop"
                               data-folder-id="{{ prev_folder.id }}">
                                ← Voltar</a>
                        {% endwith %}
                    {% else %}
                        <a href="{% url 'workspace_home' %}"
                           class="text-blue-600 hover:underline
                               breadcrumb-drop"
                           data-folder-id="">← Voltar à raiz</a>
                    {% endif %}

                    <span>/</span>

                    <a href="{% url 'workspace_home' %}"
                       class="hover:underline breadcrumb-drop"
                       data-folder-id="">📁 Raiz</a>

                    <span>/</span>

                    {% for folder in breadcrumbs %}
                        {% if not forloop.last %}
                            <a href="?folder={{ folder.id }}"
                               class="hover:underline breadcrumb-drop"
                               data-folder-id="{{ folder.id }}">
                                {{ folder.name }}</a>
                            <span>/</span>
                        {% else %}
                            <span class="font-semibold breadcrumb-drop"
                                  data-folder-id="{{ folder.id }}">
                                {{ folder.name }}
                            </span>
                        {% endif %}
                    {% endfor %}

                {% else %}
                    <span class="text-gray-400 italic breadcrumb-drop"
                          data-folder-id="">
                        📁 Raiz
                    </span>
                {% endif %}

            </nav> <!-- 🧭 Breadcrumbs -->


            <!-- Mensagens -->
            {% if messages %}
                <ul class="mb-4">
                    {% for message in messages %}
                        <li class="px-4 py-2 rounded 
                            {% if message.tags == 'success' %}
                                bg-green-100 text-green-700
                            {% else %}bg-red-100 text-red-700{% endif %}">
                                {{ message }}
                        </li>
                    {% endfor %}
                </ul>
            {% endif %} <!-- /Mensagens -->


            <!-- 📌 Botões -->
            <div class="
                        mb-6
                        flex
                        justify-between
                        gap-3
                        flex-wrap"
                        data-preserve-selection="true">

                <!-- 🔹 BOTÕES ESQUERDO -->
                <div class="flex items-center gap-3 flex-wrap">

                    <!-- 📌 Botão de Criar Pasta -->
                    <button
                        command="show-modal"
                        commandfor="create_folder_modal"
                        class="inline-block
                                bg-green-600
                                hover:bg-green-700
                                text-white
                                px-4
                                py-2
                                rounded">
                        ➕ Nova Pasta
                    </button> <!-- 📌 /Botão de Criar Pasta -->



                    <!-- Dropdown de Upload (Botão de Upload) -->
                    <div class="relative inline-block">
                        <button 
                            type="button"
                            id="upload_button"
                            class="
                                inline-block
                                bg-blue-600
                                hover:bg-blue-700
                                text-white
                                px-4
                                py-2
                                rounded
                                cursor-pointer">
                            📤 Fazer Upload
                        </button>
                        
                        <div
                            id="upload_menu" 
                            class="
                                hidden
                                absolute
                                left-0
                                mt-2
                                w-48
                                bg-white
                                rounded-md
                                shadow-lg
                                z-50
                                border
                                border-gray-200">
                            <div class="py-1">
                                <label
                                    for="file_input"
                                    class="
                                        block
                                        px-4
                                        py-2
                                        text-sm
                                        text-gray-700
                                        hover:bg-gray-100
                                        cursor-pointer">
                                    📄 Arquivo
                                </label>
                                <label
                                    for="folder_input"
                                    class="
                                        block
                                        px-4
                                        py-2
                                        text-sm
                                        text-gray-700
                                        hover:bg-gray-100
                                        cursor-pointer">
                                    📁 Pasta
                                </label>
                            </div>
                        </div>
                    </div> <!-- /Dropdown de Upload (Botão de Upload) -->

                    <!-- Formulário para upload de arquivo -->
                    <form method="post"
                        id="upload_file_form"
                        action="{% url 'upload_file' %}"
                        enctype="multipart/form-data"
                        class="hidden">

                        {% csrf_token %}

                        <input 
                            type="hidden" 
                            name="next" 
                            value="{{ request.get_full_path }}">
                        <input 
                            type="hidden" 
                            name="folder" 
                            value="{{ current_folder.id|default_if_none:'' }}">
                        <input 
                            type="hidden" 
                            name="upload_type" 
                            value="file">
                        <input 
                            type="file" 
                            name="file" 
                            id="file_input"
                            multiple 
                            class="hidden" 
                            onchange="checkFileSizeAndSubmit(this)">
                    </form> <!-- /Formulário para upload de arquivo -->

                    <!-- Formulário para upload de pasta -->
                    <form method="post"
                        id="upload_folder_form"
                        action="{% url 'upload_folder' %}"
                        enctype="multipart/form-data"
                        class="hidden">
                        {% csrf_token %}
                        <input 
                            type="hidden" 
                            name="next" 
                            value="{{ request.get_full_path }}">
                        <input 
                            type="hidden" 
                            name="folder" 
                            value="{{ current_folder.id|default_if_none:'' }}">
                        <input 
                            type="file" 
                            name="files" 
                            id="folder_input"
                            webkitdirectory 
                            directory 
                            multiple 
                            class="hidden"
                            required>
                        <input 
                            type="hidden" 
                            name="folder_name" 
                            id="detected_folder_name">
                        <input 
                            type="hidden" 
                            name="file_paths" 
                            id="file_paths_json">
                    </form> <!-- /Formulário para upload de pasta -->

                    <!-- 📌 Botão de Remover Itens Selecionados -->
                    <button
                        id="delete_selected"
                        class="
                            inline-block
                            bg-red-600
                            hover:bg-red-700
                            text-white
                            px-4
                            py-2
                            rounded
                            disabled:opacity-50
                            disabled:cursor-not-allowed"
                            disabled>
                        🗑 Remover
                    </button> <!-- 📌 /Botão de Remover Itens Selecionados -->

                    <!-- Formulário para remoção de itens -->
                    <form
                        id="delete_form"
                        method="post"
                        class="hidden">
                        {% csrf_token %}
                    </form> <!-- Formulário para remoção de itens -->

                    <!-- 📌 Botão de Renomear Item Selecionado -->
                    <button
                        id="rename_selected"
                        class="
                            inline-block
                            bg-yellow-500
                            hover:bg-yellow-600
                            text-white
                            px-4
                            py-2
                            rounded
                            disabled:opacity-50
                            disabled:cursor-not-allowed"
                            disabled>
                        ✏ Renomear
                    </button> <!-- 📌 /Botão de Renomear Item Selecionado -->

                    <!-- MODAL Renomear Item -->
                    <dialog
                        id="rename_modal"
                        aria-labelledby="rename-title"
                        data-preserve-selection="true"
                        class="
                            fixed inset-0
                            size-auto
                            max-h-none
                            max-w-none
                            overflow-y-auto
                            bg-transparent
                            backdrop:bg-transparent">
                        <div
                            tabindex="0"
                            class="
                                flex
                                min-h-full
                                items-center
                                justify-center
                                p-4
                                text-center
                                sm:p-0">
                            <div
                                class="
                                    relative
                                    transform
                                    rounded-lg
                                    bg-white
                                    shadow-xl
                                    transition-all
                                    sm:w-full
                                    sm:max-w-md
                                    p-6">
                                <form id="rename_form" method="post">
                                    {% csrf_token %}
                                    <input
                                        type="hidden"
                                        name="next"
                                        value="{{ request.get_full_path }}">
                                    <h3
                                        id="rename-title"
                                        class="
                                            text-lg
                                            font-semibold
                                            text-gray-900
                                            mb-4">
                                        Renomear item
                                    </h3>
                                    <div>
                                        <label
                                            for="rename_input"
                                            class="
                                                block
                                                text-sm
                                                font-medium
                                                text-gray-700">
                                            Novo nome
                                        </label>
                                        <input
                                            type="text"
                                            id="rename_input"
                                            name="name"
                                            required
                                            class="
                                                mt-1
                                                block
                                                w-full
                                                px-4 py-2
                                                border
                                                rounded-lg"
                                            autocomplete="off">
                                        <p
                                            id="rename-error"
                                            class="
                                                text-sm
                                                text-red-500
                                                mt-1
                                                hidden"
                                        ></p>
                                    </div>
                                    <div
                                        class="
                                            mt-6
                                            flex
                                            justify-end
                                            space-x-2">
                                        <button
                                            type="submit"
                                            class="
                                                px-4
                                                py-2
                                                bg-yellow-500
                                                hover:bg-yellow-600
                                                text-white
                                                rounded">
                                            Salvar
                                        </button>
                                        <button
                                            type="button"
                                            id="rename_cancel"
                                            class="
                                                px-4
                                                py-2
                                                bg-gray-200
                                                hover:bg-gray-300
                                                rounded">
                                            Cancelar
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </dialog> <!-- /MODAL Renomear Item -->
                </div> <!-- 🔹 /BOTÕES ESQUERDO -->

            </div> <!-- 📌 /Botões -->



            <!-- MODAL Criar Pasta -->
            <el-dialog>
                <dialog
                    id="create_folder_modal"
                    aria-labelledby="modal-title"
                    {% if show_modal %}data-auto-open="true"{% endif %}
                    class="
                        fixed
                        inset-0
                        size-auto
                        max-h-none
                        max-w-none
                        overflow-y-auto
                        bg-transparent
                        backdrop:bg-transparent">

                    <el-dialog-backdrop
                        class="
                            fixed
                            inset-0
                            bg-gray-900/50
                            transition-opacity">
                    </el-dialog-backdrop>

                    <div
                        tabindex="0"
                        class="
                            flex
                            min-h-full
                            items-center
                            justify-center
                            p-4
                            text-center
                            sm:p-0">
                        <el-dialog-panel
                            class="
                                relative
                                transform
                                rounded-lg
                                bg-white
                                shadow-xl
                                transition-all
                                sm:w-full
                                sm:max-w-md
                                p-6">
                            <form method="post" action="{% url 'create_folder' %}">
                                {% csrf_token %}
                                <input 
                                    type="hidden" 
                                    name="next" 
                                    value="{{ request.get_full_path }}">
                                <input
                                    type="hidden" 
                                    name="parent" 
                                    value="{{ current_folder.id|default_if_none:'' }}">

                                <h3 id="modal-title" class="text-lg font-semibold text-gray-900 mb-4">
                                    Criar nova pasta
                                </h3>

                                <div>
                                    <label
                                        for="folder_name"
                                        class="
                                            block
                                            text-sm
                                            font-medium
                                            text-gray-700">
                                        Nome da pasta
                                    </label>
                                    <input
                                        type="text"
                                        name="name"
                                        id="folder_name"
                                        required
                                        class="
                                            mt-1 block
                                            w-full
                                            px-4
                                            py-2
                                            border
                                            rounded-lg"
                                        autocomplete="off"
                                        value="{{ form.name.value|default:'' }}">

                                    {% if form.name.errors %}
                                        <p
                                            id="server-error"
                                            class="
                                                text-sm
                                                text-red-500
                                                mt-1"
                                        >
                                            {{ form.name.errors.0 }}
                                        </p>
                                    {% else %}
                                        <p
                                            id="server-error"
                                            class="
                                                text-sm
                                                text-red-500
                                                mt-1
                                                hidden"
                                        ></p>
                                    {% endif %}
                                </div>

                                <div class="mt-6 flex justify-end space-x-2">

                                    <button
                                        type="submit"
                                        id="create_folder_btn"
                                        class="
                                            px-4
                                            py-2
                                            bg-green-600
                                            hover:bg-green-700
                                            text-white
                                            rounded">
                                        Criar
                                    </button>

                                    <button
                                        type="button"
                                        command="close"
                                        commandfor="create_folder_modal"
                                        class="
                                            px-4
                                            py-2
                                            bg-gray-200
                                            hover:bg-gray-300
                                            rounded">
                                        Cancelar
                                    </button>
                                </div>
                            </form>
                        </el-dialog-panel>
                    </div>
                </dialog>

            </el-dialog> <!-- MODAL Criar Pasta -->



            <!-- 📁 Listagem de pastas e arquivos -->
            {% if folders or files %}

                <!-- Lista de pastas e arquivos -->
                <ul class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">



                    <!-- Pastas -->
                    {% for folder in folders %}
                        <li class="
                                bg-white
                                border
                                rounded-lg
                                p-4
                                cursor-pointer
                                transition
                                transform
                                hover:scale-102
                                hover:bg-gray-200
                                selectable-item"
                            data-url="?folder={{ folder.id }}"
                            data-target="_self"
                            data-kind="folder"
                            data-id="{{ folder.id }}"
                            draggable="true">
                                <div class="block">
                                    <span class="text-gray-800
                                                font-semibold flex
                                                items-center space-x-2">
                                        <span>📁</span>
                                        <span>{{ folder.name }}</span>
                                    </span>
                                </div>
                        </li>
                    {% endfor %} <!-- 📁 /Pastas -->



                    <!-- Arquivos -->
                    {% for file in files %}
                        <li class="
                                bg-white
                                border
                                rounded-lg
                                p-4
                                cursor-pointer
                                transition
                                transform
                                hover:scale-102
                                hover:bg-gray-200
                                selectable-item"
                            data-url="{{ file.file.url }}"
                            data-target="_blank"
                            data-kind="file" data-id="{{ file.id }}"
                            draggable="true">
                                <div class="block">
                                    <span class="
                                                text-gray-800
                                                font-semibold
                                                flex items-center
                                                space-x-2">
                                        <span>📄</span>
                                        <span>{{ file.name }}</span>
                                    </span>
                                </div>
                        </li>
                    {% endfor %} <!-- 📁 /Arquivos -->

                </ul> <!-- 📁 /Lista de pastas e arquivos -->

            <!-- Else - Se não houver pastas ou arquivos -->
            {% else %}
                <p class="pt-4 text-gray-500 italic">
                    Nenhum item encontrado neste diretório.
                </p>
            {% endif %} <!-- /else - Se não houver pastas ou arquivos -->



        </main> <!-- Área principal do Workspace -->



    </div> <!-- /Container principal -->
{% endblock %}


{% block scripts %}
    <script src="{% static 'workspace/js/workspace_home.js' %}"></script>
    <script>
        function checkFileSizeAndSubmit(input) {
            const maxSize = 100 * 1024 * 1024; // 100 MB in bytes
            const files = input.files;
            for (let i = 0; i < files.length; i++) {
                if (files[i].size > maxSize) {
                    alert(`O arquivo "${files[i].name}" é muito grande. O tamanho máximo permitido é 100 MB.`);
                    input.value = ''; // Clear the input
                    return;
                }
            }
            input.form.submit();
        }
    </script>
{% endblock scripts %}
```


















































---

<div id="create-train-models"></div>

## `Criando os modelos de treino train/models.py`

[train/models.py](../../../train/models.py)
```python
from django.conf import settings
from django.db import models


class TrainingModel(models.Model):
    """Modelo lógico de treino (nome escolhido pelo usuário)."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="training_models",
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        constraints = [
            models.UniqueConstraint(
                fields=("user", "name"),
                name="train_trainingmodel_user_name_uniq",
            ),
        ]

    def __str__(self) -> str:
        return self.name


class TrainingModelFile(models.Model):
    """Snapshot dos arquivos usados em um treino (para exibição)."""

    training_model = models.ForeignKey(
        TrainingModel,
        on_delete=models.CASCADE,
        related_name="source_files",
    )
    file_id = models.PositiveIntegerField()
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(
        max_length=1024,
        blank=True,
        default="",
        help_text=(
            "Caminho lógico no workspace "
            "(ex.: workspace/pasta/arquivo.pdf)."
        ),
    )
    workspace_folder_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=(
            "ID da pasta que contém o arquivo "
            "(para link no workspace); vazio = raiz."
        ),
    )

    class Meta:
        ordering = ["file_name"]
        constraints = [
            models.UniqueConstraint(
                fields=("training_model", "file_id"),
                name="train_trainingmodelfile_model_file_uniq",
            ),
        ]
```


















































---

<div id="registre-train-models"></div>

## `Registrando os modelos de treino train/models.py no Django Admin`

[train/admin.py](../../../train/admin.py)
```python
from django.contrib import admin

from train.models import TrainingModel, TrainingModelFile


class TrainingModelFileInline(admin.TabularInline):
    model = TrainingModelFile
    extra = 0
    readonly_fields = (
        "file_id",
        "file_name",
        "file_path",
        "workspace_folder_id",
    )


@admin.register(TrainingModel)
class TrainingModelAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "updated_at")
    list_filter = ("updated_at",)
    search_fields = ("name", "user__username")
    inlines = (TrainingModelFileInline,)


@admin.register(TrainingModelFile)
class TrainingModelFileAdmin(admin.ModelAdmin):
    list_display = ("file_name", "file_id", "training_model")
    search_fields = ("file_name",)
```


















































---

<div id="create-train-utils"></div>

## `Criando o train/utils.py`

[train/utils.py](../../../train/utils.py)
```python
from __future__ import annotations

from django.http import HttpRequest

from train.models import TrainingModel


def resolve_active_training_model_id(
    request: HttpRequest,
    user_id: int,
) -> int | None:
    """
    Modelo usado no chat: sessão (se válido), senão o último treino do usuário.
    Se não houver modelo treinado, retorna None (apenas embeddings legados
    com training_model nulo entram na busca).
    """
    sid = request.session.get("active_training_model_id")
    if sid is not None:
        try:
            sid_int = int(sid)
        except (TypeError, ValueError):
            sid_int = None
        if sid_int is not None:
            if TrainingModel.objects.filter(
                id=sid_int,
                user_id=user_id,
            ).exists():
                return sid_int

    latest = (
        TrainingModel.objects.filter(user_id=user_id)
        .order_by("-updated_at")
        .first()
    )
    return latest.id if latest else None
```


















































---

<div id="embedding-pipeline"></div>

## `Criando o rag/services/ingestion/embedding_pipeline.py`

[rag/services/ingestion/embedding_pipeline.py](../../../rag/services/ingestion/embedding_pipeline.py)
```python
"""
Pipeline compartilhada: extrair texto, limpar, chunkar, dicts para embeddings.

Usada pelo treinamento de modelos e por outros fluxos de ingestão equivalentes.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

from rag.services.ingestion.chunking import chunk_text
from rag.services.ingestion.text_extraction import extract_text

DEFAULT_CHUNK_SIZE = 300
DEFAULT_CHUNK_OVERLAP = 30
DEFAULT_EMBED_MAX_WORKERS = 4


def clean_texts_for_embedding(texts: list[Any]) -> list[str]:
    """Filtra e normaliza strings não vazias."""
    cleaned: list[str] = []
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


def text_to_embedding_chunks(
    text: str,
    *,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[str]:
    """
    Divide texto em chunks; se o splitter vier vazio, usa o texto inteiro.
    """
    chunks = chunk_text(
        text=text,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    if not chunks:
        print("⚠️ Fallback aplicado (1 chunk criado)")
        return [text]
    return chunks


def embedded_chunks_from_file(
    file_info: dict[str, Any],
    user_id: int,
    *,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[dict[str, Any]]:
    """
    Processa um arquivo mapeado (file_discovery.map_file) e retorna dicts
    prontos para generate_embeddings.
    """
    embedded_chunks: list[dict[str, Any]] = []
    try:
        texts = extract_text(file_info)
        print(f"\n📄 Arquivo: {file_info['name']}")
        print(f"🧾 Textos extraídos: {len(texts) if texts else 0}")
        if not texts:
            return []
        cleaned_texts = clean_texts_for_embedding(texts)
        for text in cleaned_texts:
            chunks = text_to_embedding_chunks(
                text,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
            )
            print(f"🧩 Chunks gerados: {len(chunks)}")
            for index, chunk in enumerate(chunks):
                embedded_chunks.append(
                    {
                        "user_id": user_id,
                        "file_id": file_info["file_id"],
                        "folder": file_info["folder"],
                        "path": file_info["absolute_path"],
                        "chunk_index": index,
                        "content": chunk,
                    }
                )
    except Exception as e:
        print(f"❌ Erro no arquivo {file_info['name']}: {e}")
    return embedded_chunks


def embedded_chunks_from_files_parallel(
    files: list[dict[str, Any]],
    user_id: int,
    *,
    max_workers: int = DEFAULT_EMBED_MAX_WORKERS,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[dict[str, Any]]:
    """Processa vários arquivos em paralelo (thread pool)."""
    embedded_chunks: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(
                embedded_chunks_from_file,
                f,
                user_id,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
            )
            for f in files
        ]
        for future in as_completed(futures):
            result = future.result()
            if result:
                embedded_chunks.extend(result)
    return embedded_chunks
```


















































---

<div id="create-train-view"></div>

## `Criando a view train/view.py`

[train/views.py](../../../train/views.py)
```python
from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from rag.models import DocumentEmbedding
from rag.services.ingestion.embedding_pipeline import (
    DEFAULT_EMBED_MAX_WORKERS,
    embedded_chunks_from_files_parallel,
)
from rag.services.ingestion.embeddings import (
    generate_embeddings,
    get_embedding_model,
)
from rag.services.ingestion.file_discovery import (
    discover_all_workspace_files,
    discover_workspace_files,
)
from rag.services.ingestion.vector_store import store_embeddings
from train.models import TrainingModel, TrainingModelFile
from utils.messages import (
    RAG_NO_FILES_FOUND,
    RAG_NO_VALID_CONTENT_FOUND,
    RAG_TRAINING_COMPLETED,
    RAG_TRAINING_ERROR,
    RAG_TRAINING_MODEL_DELETED,
    RAG_TRAINING_MODEL_NAME_REQUIRED,
)
from workspace.browser import get_workspace_browser_context
from workspace.models import Folder

# ==============================
# 🔹 Constantes / Helpers
# ==============================

TRAINING_MODEL_NAME_MAX_LEN = 255


def _collect_folder_ids_from_post(
    request: HttpRequest,
    user: Any,
) -> list[int]:
    raw_folder_ids = request.POST.getlist("folder_ids")
    selected_folder_ids: list[int] = []
    for raw in raw_folder_ids:
        try:
            selected_folder_ids.append(int(raw))
        except ValueError:
            continue

    if request.POST.get("include_current_folder") == "1":
        cur = request.POST.get("current_folder_id")
        if cur:
            try:
                selected_folder_ids.append(int(cur))
            except ValueError:
                pass

    selected_folder_ids = list(dict.fromkeys(selected_folder_ids))

    if not selected_folder_ids:
        return []

    allowed = set(
        Folder.objects.filter(
            id__in=selected_folder_ids,
            owner=user,
            is_deleted=False,
        ).values_list("id", flat=True)
    )
    return [fid for fid in selected_folder_ids if fid in allowed]


def _discover_files_for_training(
    user: Any,
    selected_folder_ids: list[int],
) -> list[dict[str, Any]]:
    if selected_folder_ids:
        return discover_workspace_files(
            user=user,
            folder_ids=selected_folder_ids,
        )
    return discover_all_workspace_files(user=user)


def _persist_training_model_file_rows(
    training_model: TrainingModel,
    files: list[dict[str, Any]],
) -> None:
    seen_file_ids: set[int] = set()
    file_rows: list[TrainingModelFile] = []
    max_name = TRAINING_MODEL_NAME_MAX_LEN
    for f in files:
        fid = f["file_id"]
        if fid in seen_file_ids:
            continue
        seen_file_ids.add(fid)
        ws_path = (f.get("workspace_path") or "").strip()
        if not ws_path:
            folder_label = f.get("folder") or "workspace"
            ws_path = f"{folder_label}/{f['name']}".replace("//", "/")
        path_str = str(ws_path)[:1024]
        folder_id_val = f.get("folder_id")
        if folder_id_val is not None:
            try:
                folder_id_int = int(folder_id_val)
            except (TypeError, ValueError):
                folder_id_int = None
        else:
            folder_id_int = None
        file_rows.append(
            TrainingModelFile(
                training_model=training_model,
                file_id=fid,
                file_name=f["name"][:max_name],
                file_path=path_str,
                workspace_folder_id=folder_id_int,
            )
        )
    if file_rows:
        TrainingModelFile.objects.bulk_create(file_rows)


def _handle_train_post(request: HttpRequest) -> HttpResponse:
    user = request.user
    next_default = request.POST.get("next", "train_home")

    model_name = (request.POST.get("model_name") or "").strip()
    if not model_name:
        messages.error(request, RAG_TRAINING_MODEL_NAME_REQUIRED)
        return redirect(next_default)
    if len(model_name) > TRAINING_MODEL_NAME_MAX_LEN:
        messages.error(
            request,
            f"O nome do modelo é muito longo "
            f"(máx. {TRAINING_MODEL_NAME_MAX_LEN}).",
        )
        return redirect(next_default)

    selected_folder_ids = _collect_folder_ids_from_post(request, user)

    try:
        training_model, _ = TrainingModel.objects.get_or_create(
            user=user,
            name=model_name,
        )

        DocumentEmbedding.objects.filter(
            training_model_id=training_model.id
        ).delete()
        TrainingModelFile.objects.filter(training_model=training_model).delete()

        print(
            f"🧹 Embeddings anteriores removidos "
            f"(modelo: {training_model.name!r})"
        )

        files = _discover_files_for_training(user, selected_folder_ids)

        if not files:
            messages.warning(request, RAG_NO_FILES_FOUND)
            return redirect(next_default)

        embedded_chunks = embedded_chunks_from_files_parallel(
            files,
            user.id,
            max_workers=DEFAULT_EMBED_MAX_WORKERS,
        )

        print(f"\n🚀 Total de chunks: {len(embedded_chunks)}")

        if not embedded_chunks:
            messages.warning(request, RAG_NO_VALID_CONTENT_FOUND)
            return redirect(next_default)

        embed_model = get_embedding_model()
        embedded_chunks = generate_embeddings(
            embedding_model=embed_model,
            chunks=embedded_chunks,
        )

        store_embeddings(
            embedded_chunks=embedded_chunks,
            training_model_id=training_model.id,
        )

        _persist_training_model_file_rows(training_model, files)

        TrainingModel.objects.filter(pk=training_model.pk).update(
            updated_at=timezone.now()
        )

        request.session["active_training_model_id"] = training_model.id

        messages.success(
            request,
            RAG_TRAINING_COMPLETED.format(count=len(files)),
        )

    except Exception as e:
        messages.error(request, RAG_TRAINING_ERROR.format(error=str(e)))

    return redirect(next_default)


# ==============================
# 🔥 Views
# ==============================


@login_required
def train_home(request: HttpRequest) -> HttpResponse:
    """Exibe a página de treinamento."""
    folder_id = request.GET.get("folder")
    context = get_workspace_browser_context(
        user=request.user,
        folder_id=folder_id,
    )
    context["training_models"] = list(
        TrainingModel.objects.filter(user=request.user).order_by("-updated_at")[
            :100
        ]
    )
    return render(request, "pages/train_home.html", context)


@login_required
def training_model_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """Remove um modelo de treino e embeddings associados (CASCADE)."""
    if request.method != "POST":
        return redirect("train_home")

    tm = get_object_or_404(TrainingModel, pk=pk, user=request.user)
    name = tm.name

    active = request.session.get("active_training_model_id")
    if active is not None:
        try:
            if int(active) == pk:
                request.session.pop("active_training_model_id", None)
        except (TypeError, ValueError):
            pass

    tm.delete()
    messages.success(request, RAG_TRAINING_MODEL_DELETED.format(name=name))
    return redirect("train_home")


@login_required
def training_model_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Lista arquivos usados em um treino."""
    tm = get_object_or_404(
        TrainingModel,
        pk=pk,
        user=request.user,
    )
    source_files = tm.source_files.all().order_by("file_name")
    return render(
        request,
        "pages/training_model_detail.html",
        {
            "training_model": tm,
            "source_files": source_files,
        },
    )


@login_required
def set_active_training_model(request: HttpRequest) -> HttpResponse:
    """Define qual modelo o chat deve usar (sessão)."""
    if request.method != "POST":
        return redirect("train_home")

    raw = request.POST.get("training_model_id")
    next_url = request.POST.get("next", "") or ""

    if not raw:
        request.session.pop("active_training_model_id", None)
    else:
        try:
            tid = int(raw)
        except (TypeError, ValueError):
            tid = None

        if tid is not None and TrainingModel.objects.filter(
            id=tid,
            user=request.user,
        ).exists():
            request.session["active_training_model_id"] = tid

    if next_url.startswith("/"):
        return redirect(next_url)
    return redirect("train_home")


@login_required
def train_view(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return redirect("train_home")
    return _handle_train_post(request)
```


















































---

<div id="map-url-to-view"></div>

## `Mapeando a ROTA/URL para a view train_view()`

Agora, nós vamos criar uma rota para essa view:

[core/urls.py](../../../core/urls.py)
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    ...

    path(
        "",
        include("train.urls")
    ),
]
```

[train/urls.py](../../../train/urls.py)
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


















































---

<div id="update-sidebar"></div>

## `Atualizando o sidebar`

[templates/partials/sidebar.html](../../../templates/partials/sidebar.html)
```html
<!--
    Sidebar para páginas autenticadas (home, workspace, lixeira).

    Variável: current_page — 'home' | 'workspace' | 'train' | 'trash' (destaque ativo).
-->
<aside class="
            flex
            w-64
            shrink-0
            flex-col
            justify-between
            bg-gray-900
            text-white
            min-h-0">

    <!-- Botões (links) principais -->
    <div class="
            p-2
            border-gray-700
            flex flex-col
            gap-1">

        <!--- Estilo para o botão (link) /home/ -->
        <div class="
            p-1
            border-b
            border-gray-700
            flex
            flex-col
            gap-1">
            <a
                href="{% url 'home' %}"
                class="flex items-center justify-between p-2 rounded
                    {% if current_page == 'home' %}
                        bg-gray-500
                    {% else %}
                        hover:bg-gray-800
                    {% endif %}">
                Home / Chat
            </a>
        </div>
        <!--- /Estilo para o botão (link) /home/ -->

        <!--- Estilo para o botão (link) /workspace/ -->
        <div class="
            p-1">
            <a
                href="{% url 'workspace_home' %}"
                class="flex items-center justify-between p-2 rounded
                    {% if current_page == 'workspace' %}
                        bg-gray-500
                    {% else %}
                        hover:bg-gray-800
                    {% endif %}">
                Workspace
            </a>
        </div>
        <!--- /Estilo para o botão (link) /workspace/ -->

        <!--- Estilo para o botão (link) /train/ -->
        <div class="
            p-1">
            <a
                href="{% url 'train_home' %}"
                class="flex items-center justify-between p-2 rounded
                    {% if current_page == 'train' %}
                        bg-gray-500
                    {% else %}
                        hover:bg-gray-800
                    {% endif %}">
                Treinamento
            </a>
        </div>
        <!--- /Estilo para o botão (link) /train/ -->

    </div>
    <!-- /Botões (links) principais -->

    <!-- Espaço flexível para empurrar os botões secundários para baixo -->
    <div class="flex-1 min-h-0"></div>

    <!-- Botões (links) secundários -->
    <div>

        <div class="
                p-2
                border-t
                border-gray-700
                flex flex-col
                gap-1">
            
            <!--- Estilo para o botão (link) /trash/ -->
            <a
                href="{% url 'trash_home' %}"
                class="flex items-center justify-between p-2 rounded
                    {% if current_page == 'trash' %}
                        bg-gray-500
                    {% else %}
                        hover:bg-gray-800
                    {% endif %}">
                Lixeira
            </a>
            <!--- /Estilo para o botão (link) /trash/ -->
        </div>

        <!-- Botão de sair -->
        <div class="p-4 border-t border-gray-700">
            <a href="{% url 'logout' %}"
                class="block text-center text-red-400 hover:text-red-300">
                Sair
            </a>
        </div>
        <!-- /Botão de sair -->

    </div>
    <!-- Botões (links) secundários -->

</aside>
```


















































---

<div id="create-train-home"></div>

## `Criando o template train_home.html`

[train/templates/pages/train_home.html](../../../train/templates/pages/train_home.html)
```html
{% extends "base.html" %}
{% load static %}


{% block title %}Treinamento{% endblock %}


{% block head %}
    <link
        rel="stylesheet"
        href="{% static 'workspace/css/workspace_home.css' %}">
{% endblock head %}


{% block content %}
    <!-- Container principal -->
    <div class="flex h-screen bg-gray-100">


        <!-- 🧱 Sidebar -->
        {% include "partials/sidebar.html" with current_page="train" %}


        <!-- 💼 Área principal do Workspace -->
        <main class="flex-1 p-8 overflow-y-auto">


            <!-- Header -->
            <header class="bg-white shadow px-6 py-4">
                <h1 class="text-2xl font-semibold text-gray-800">
                    Treinamento — {{ request.user.username }}
                </h1>
                <p class="text-sm text-gray-600 mt-2 max-w-3xl">
                    Marque as pastas abaixo para treinar apenas o conteúdo delas
                    (inclui subpastas). Se nenhuma estiver marcada, o treino usa
                    todo o workspace.
                </p>
            </header>

            <!-- Formulário oculto: checkboxes da lista usam form="train-form" -->
            <form
                id="train-form"
                method="post"
                action="{% url 'train' %}"
                class="hidden"
                aria-hidden="true">
                {% csrf_token %}
                <input
                    type="hidden"
                    name="next"
                    value="{{ request.get_full_path }}">
                {% if current_folder %}
                    <input
                        type="hidden"
                        name="current_folder_id"
                        value="{{ current_folder.id }}">
                {% endif %}
            </form>


            <!-- 🧭 Breadcrumbs -->
            <nav class="text-sm text-gray-600 my-4 flex items-center
                space-x-2">

                {% if current_folder %}

                    {% if breadcrumbs|length > 1 %}
                        {% with prev_folder=breadcrumbs|slice:"-2:-1"|first %}
                            <a href="?folder={{ prev_folder.id }}"
                               class="text-blue-600 hover:underline
                                   breadcrumb-drop"
                               data-folder-id="{{ prev_folder.id }}">
                                ← Voltar</a>
                        {% endwith %}
                    {% else %}
                        <a href="{% url 'train_home' %}"
                           class="text-blue-600 hover:underline
                               breadcrumb-drop"
                           data-folder-id="">← Voltar à raiz</a>
                    {% endif %}

                    <span>/</span>

                    <a href="{% url 'train_home' %}"
                       class="hover:underline breadcrumb-drop"
                       data-folder-id="">📁 Raiz</a>

                    <span>/</span>

                    {% for folder in breadcrumbs %}
                        {% if not forloop.last %}
                            <a href="?folder={{ folder.id }}"
                               class="hover:underline breadcrumb-drop"
                               data-folder-id="{{ folder.id }}">
                                {{ folder.name }}</a>
                            <span>/</span>
                        {% else %}
                            <span class="font-semibold breadcrumb-drop"
                                  data-folder-id="{{ folder.id }}">
                                {{ folder.name }}
                            </span>
                        {% endif %}
                    {% endfor %}

                {% else %}
                    <span class="text-gray-400 italic breadcrumb-drop"
                          data-folder-id="">
                        📁 Raiz
                    </span>
                {% endif %}

            </nav> <!-- 🧭 Breadcrumbs -->


            <!-- Mensagens -->
            {% if messages %}
                <ul class="mb-4">
                    {% for message in messages %}
                        <li class="px-4 py-2 rounded 
                            {% if message.tags == 'success' %}
                                bg-green-100 text-green-700
                            {% else %}bg-red-100 text-red-700{% endif %}">
                                {{ message }}
                        </li>
                    {% endfor %}
                </ul>
            {% endif %} <!-- /Mensagens -->


            <!-- 📌 Botões -->
            <div class="
                        mb-6
                        flex
                        justify-between
                        gap-3
                        flex-wrap"
                        data-preserve-selection="true">

                <!-- 🔹 BOTÕES ESQUERDO -->
                <div class="flex flex-col gap-3 sm:flex-row sm:items-center flex-wrap">


                    <!-- 🤖 Treinar (abre modal de nome do modelo) -->
                    <div class="flex flex-wrap items-center gap-3">
                        <button
                            type="button"
                            command="show-modal"
                            commandfor="train_model_modal"
                            class="
                                bg-purple-600
                                hover:bg-purple-700
                                text-white
                                px-5
                                py-2
                                rounded
                                font-semibold
                                shadow">
                            🤖 Treinar
                        </button>
                        {% if current_folder %}
                            <label class="inline-flex items-center gap-2 text-sm text-gray-700 cursor-pointer">
                                <input
                                    type="checkbox"
                                    name="include_current_folder"
                                    value="1"
                                    form="train-form"
                                    class="h-4 w-4 rounded border-gray-300 text-purple-600">
                                <span>Incluir esta pasta no treino (com subpastas)</span>
                            </label>
                        {% endif %}
                    </div>
                    <!-- 🤖 /Treinar -->

                </div> <!-- 🔹 /BOTÕES ESQUERDO -->


                <!-- 🔸 Lado DIREITO -->
                <div class="flex items-center">

                </div> <!-- 🔸 Lado DIREITO -->

            </div> <!-- 📌 /Botões -->



            <!-- MODAL Criar Pasta -->
            <el-dialog>
                <dialog
                    id="create_folder_modal"
                    aria-labelledby="modal-title"
                    {% if show_modal %}data-auto-open="true"{% endif %}
                    class="
                        fixed
                        inset-0
                        size-auto
                        max-h-none
                        max-w-none
                        overflow-y-auto
                        bg-transparent
                        backdrop:bg-transparent">

                    <el-dialog-backdrop
                        class="
                            fixed
                            inset-0
                            bg-gray-900/50
                            transition-opacity">
                    </el-dialog-backdrop>

                    <div
                        tabindex="0"
                        class="
                            flex
                            min-h-full
                            items-center
                            justify-center
                            p-4
                            text-center
                            sm:p-0">
                        <el-dialog-panel
                            class="
                                relative
                                transform
                                rounded-lg
                                bg-white
                                shadow-xl
                                transition-all
                                sm:w-full
                                sm:max-w-md
                                p-6">
                            <form method="post" action="{% url 'create_folder' %}">
                                {% csrf_token %}
                                <input 
                                    type="hidden" 
                                    name="next" 
                                    value="{{ request.get_full_path }}">
                                <input
                                    type="hidden" 
                                    name="parent" 
                                    value="{{ current_folder.id|default_if_none:'' }}">

                                <h3 id="modal-title" class="text-lg font-semibold text-gray-900 mb-4">
                                    Criar nova pasta
                                </h3>

                                <div>
                                    <label
                                        for="folder_name"
                                        class="
                                            block
                                            text-sm
                                            font-medium
                                            text-gray-700">
                                        Nome da pasta
                                    </label>
                                    <input
                                        type="text"
                                        name="name"
                                        id="folder_name"
                                        required
                                        class="
                                            mt-1 block
                                            w-full
                                            px-4
                                            py-2
                                            border
                                            rounded-lg"
                                        autocomplete="off"
                                        value="{{ form.name.value|default:'' }}">

                                    {% if form.name.errors %}
                                        <p
                                            id="server-error"
                                            class="
                                                text-sm
                                                text-red-500
                                                mt-1"
                                        >
                                            {{ form.name.errors.0 }}
                                        </p>
                                    {% else %}
                                        <p
                                            id="server-error"
                                            class="
                                                text-sm
                                                text-red-500
                                                mt-1
                                                hidden"
                                        ></p>
                                    {% endif %}
                                </div>

                                <div class="mt-6 flex justify-end space-x-2">

                                    <button
                                        type="submit"
                                        id="create_folder_btn"
                                        class="
                                            px-4
                                            py-2
                                            bg-green-600
                                            hover:bg-green-700
                                            text-white
                                            rounded">
                                        Criar
                                    </button>

                                    <button
                                        type="button"
                                        command="close"
                                        commandfor="create_folder_modal"
                                        class="
                                            px-4
                                            py-2
                                            bg-gray-200
                                            hover:bg-gray-300
                                            rounded">
                                        Cancelar
                                    </button>
                                </div>
                            </form>
                        </el-dialog-panel>
                    </div>
                </dialog>

            </el-dialog> <!-- MODAL Criar Pasta -->


            <!-- MODAL Nome do modelo / treino -->
            <el-dialog>
                <dialog
                    id="train_model_modal"
                    aria-labelledby="train-model-title"
                    class="
                        fixed
                        inset-0
                        size-auto
                        max-h-none
                        max-w-none
                        overflow-y-auto
                        bg-transparent
                        backdrop:bg-transparent">

                    <el-dialog-backdrop
                        class="
                            fixed
                            inset-0
                            bg-gray-900/50
                            transition-opacity">
                    </el-dialog-backdrop>

                    <div
                        tabindex="0"
                        class="
                            flex
                            min-h-full
                            items-center
                            justify-center
                            p-4
                            text-center
                            sm:p-0">
                        <el-dialog-panel
                            class="
                                relative
                                transform
                                rounded-lg
                                bg-white
                                shadow-xl
                                transition-all
                                sm:w-full
                                sm:max-w-md
                                p-6
                                text-left">

                            <h3
                                id="train-model-title"
                                class="text-lg font-semibold text-gray-900 mb-2">
                                Nome do modelo
                            </h3>
                            <p class="text-sm text-gray-600 mb-4">
                                Escolha um nome para identificar este treino. Você pode
                                reutilizar o mesmo nome para substituir o treino anterior.
                            </p>

                            <div>
                                <label
                                    for="train_model_name_input"
                                    class="block text-sm font-medium text-gray-700">
                                    Nome do modelo
                                </label>
                                <input
                                    type="text"
                                    name="model_name"
                                    id="train_model_name_input"
                                    form="train-form"
                                    required
                                    maxlength="255"
                                    autocomplete="off"
                                    class="
                                        mt-1 block w-full px-4 py-2 border rounded-lg
                                        border-gray-300 focus:ring-purple-500
                                        focus:border-purple-500">
                            </div>

                            <div class="mt-6 flex justify-end space-x-2">
                                <button
                                    type="submit"
                                    form="train-form"
                                    class="
                                        px-4 py-2
                                        bg-purple-600
                                        hover:bg-purple-700
                                        text-white
                                        rounded">
                                    Iniciar treino
                                </button>
                                <button
                                    type="button"
                                    command="close"
                                    commandfor="train_model_modal"
                                    class="
                                        px-4 py-2
                                        bg-gray-200
                                        hover:bg-gray-300
                                        rounded">
                                    Cancelar
                                </button>
                            </div>
                        </el-dialog-panel>
                    </div>
                </dialog>
            </el-dialog> <!-- /MODAL Nome do modelo -->



            <!-- 📁 Listagem de pastas e arquivos -->
            {% if folders or files %}

                <!-- Lista de pastas e arquivos -->
                <ul class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">



                    <!-- Pastas -->
                    {% for folder in folders %}
                        <li class="
                                bg-white
                                border
                                rounded-lg
                                p-4
                                cursor-pointer
                                transition
                                transform
                                hover:scale-102
                                hover:bg-gray-200
                                selectable-item"
                            data-url="?folder={{ folder.id }}"
                            data-target="_self"
                            data-kind="folder"
                            data-id="{{ folder.id }}"
                            draggable="true">
                                <div class="flex items-start gap-3 w-full">
                                    <input
                                        type="checkbox"
                                        name="folder_ids"
                                        value="{{ folder.id }}"
                                        form="train-form"
                                        title="Incluir esta pasta no treinamento"
                                        class="train-folder-checkbox mt-1 h-4 w-4 shrink-0 rounded border-gray-300 text-purple-600 focus:ring-purple-500"
                                        onclick="event.stopPropagation()">
                                    <div class="block flex-1 min-w-0">
                                        <span class="text-gray-800
                                                    font-semibold flex
                                                    items-center space-x-2">
                                            <span>📁</span>
                                            <span>{{ folder.name }}</span>
                                        </span>
                                    </div>
                                </div>
                        </li>
                    {% endfor %} <!-- 📁 /Pastas -->



                    <!-- Arquivos -->
                    {% for file in files %}
                        <li class="
                                bg-white
                                border
                                rounded-lg
                                p-4
                                cursor-pointer
                                transition
                                transform
                                hover:scale-102
                                hover:bg-gray-200
                                selectable-item"
                            data-url="{{ file.file.url }}"
                            data-target="_blank"
                            data-kind="file" data-id="{{ file.id }}"
                            draggable="true">
                                <div class="block">
                                    <span class="
                                                text-gray-800
                                                font-semibold
                                                flex items-center
                                                space-x-2">
                                        <span>📄</span>
                                        <span>{{ file.name }}</span>
                                    </span>
                                </div>
                        </li>
                    {% endfor %} <!-- 📁 /Arquivos -->

                </ul> <!-- 📁 /Lista de pastas e arquivos -->

            <!-- Else - Se não houver pastas ou arquivos -->
            {% else %}
                <p class="pt-4 text-gray-500 italic">
                    Nenhum item encontrado neste diretório.
                </p>
            {% endif %} <!-- /else - Se não houver pastas ou arquivos -->


            {% if training_models %}
                <section
                    class="
                        mt-10
                        bg-white
                        shadow
                        rounded-lg
                        p-6
                        border border-gray-200">
                    <h2 class="text-lg font-semibold text-gray-800 mb-4">
                        Modelos treinados
                    </h2>
                    <p class="text-sm text-gray-600 mb-4">
                        Clique no nome para ver os arquivos usados em cada treino.
                    </p>
                    <ul class="divide-y divide-gray-200">
                        {% for tm in training_models %}
                            <li class="
                                    py-3
                                    flex flex-wrap
                                    items-center
                                    justify-between
                                    gap-3">
                                <div class="flex flex-wrap items-center gap-3 min-w-0">
                                    <a
                                        href="{% url 'training_model_detail' tm.pk %}"
                                        class="
                                            text-purple-700
                                            hover:underline
                                            font-medium
                                            truncate">
                                        {{ tm.name }}
                                    </a>
                                    <span class="text-xs text-gray-500 shrink-0">
                                        {{ tm.updated_at|date:"d/m/Y H:i" }}
                                    </span>
                                </div>
                                <form
                                    method="post"
                                    action="{% url 'training_model_delete' tm.pk %}"
                                    class="shrink-0"
                                    onsubmit="return confirm('Excluir este modelo e todos os embeddings associados?');">
                                    {% csrf_token %}
                                    <button
                                        type="submit"
                                        class="
                                            inline-block bg-red-600
                                            hover:bg-red-700 text-white
                                            text-sm px-4 py-2 rounded">
                                        Excluir
                                    </button>
                                </form>
                            </li>
                        {% endfor %}
                    </ul>
                </section>
            {% endif %}



        </main> <!-- Área principal do Workspace -->



    </div> <!-- /Container principal -->
{% endblock %}


{% block scripts %}
    <script src="{% static 'workspace/js/workspace_home.js' %}"></script>
    <script>
        function checkFileSizeAndSubmit(input) {
            const maxSize = 100 * 1024 * 1024; // 100 MB in bytes
            const files = input.files;
            for (let i = 0; i < files.length; i++) {
                if (files[i].size > maxSize) {
                    alert(`O arquivo "${files[i].name}" é muito grande. O tamanho máximo permitido é 100 MB.`);
                    input.value = ''; // Clear the input
                    return;
                }
            }
            input.form.submit();
        }
    </script>
{% endblock scripts %}
```


















































---

<div id="create-training-model-template"></div>

## `Criando o template training_model_detail.html`

[train/templates/pages/training_model_detail.html](../../../train/templates/pages/training_model_detail.html)
```html
{% extends "base.html" %}
{% load static %}

{% block title %}{{ training_model.name }} — Treinamento{% endblock %}

{% block head %}
    <link
        rel="stylesheet"
        href="{% static 'workspace/css/workspace_home.css' %}">
{% endblock head %}

{% block content %}
    <div class="flex h-screen bg-gray-100">

        {% include "partials/sidebar.html" with current_page="train" %}

        <main class="flex-1 p-8 overflow-y-auto">

            <header class="bg-white shadow px-6 py-4 mb-6">
                <p class="text-sm text-gray-500 mb-1">
                    <a href="{% url 'train_home' %}" class="text-purple-600 hover:underline">
                        ← Treinamento
                    </a>
                </p>
                <h1 class="text-2xl font-semibold text-gray-800">
                    Modelo: {{ training_model.name }}
                </h1>
                <p class="text-sm text-gray-600 mt-2">
                    Atualizado em {{ training_model.updated_at|date:"d/m/Y H:i" }}
                </p>
                <p class="text-sm text-gray-500 mt-3">
                    Escolha o modelo na
                    <a href="{% url 'home' %}" class="text-purple-600 hover:underline">Home</a>
                    para o chat usar este conjunto de documentos.
                </p>
            </header>

            {% if messages %}
                <ul class="mb-4">
                    {% for message in messages %}
                        <li class="px-4 py-2 rounded
                            {% if message.tags == 'success' %}
                                bg-green-100 text-green-700
                            {% else %}bg-red-100 text-red-700{% endif %}">
                            {{ message }}
                        </li>
                    {% endfor %}
                </ul>
            {% endif %}

            <section class="bg-white shadow rounded-lg p-6">
                <h2 class="text-lg font-semibold text-gray-800 mb-4">
                    Arquivos usados neste treino
                </h2>
                {% if source_files %}
                    <ul class="divide-y divide-gray-200">
                        {% for sf in source_files %}
                            <li class="py-3 text-gray-800">
                                <div class="flex flex-wrap items-baseline gap-2">
                                    <span class="text-gray-500 shrink-0">📄</span>
                                    <span class="font-medium">{{ sf.file_name }}</span>
                                    <span class="text-xs text-gray-400">(id {{ sf.file_id }})</span>
                                </div>
                                {% if sf.file_path %}
                                    <p class="mt-1 text-sm pl-7">
                                        <a
                                            href="{% url 'workspace_home' %}{% if sf.workspace_folder_id %}?folder={{ sf.workspace_folder_id }}{% endif %}"
                                            class="text-purple-700 hover:underline break-all">
                                            {{ sf.file_path }}
                                        </a>
                                    </p>
                                {% else %}
                                    <p class="mt-1 text-sm text-gray-400 italic pl-7">
                                        Caminho não registrado (treino anterior à gravação do caminho).
                                    </p>
                                {% endif %}
                            </li>
                        {% endfor %}
                    </ul>
                {% else %}
                    <p class="text-gray-500 italic">Nenhum arquivo registrado para este modelo.</p>
                {% endif %}
            </section>

        </main>
    </div>
{% endblock %}
```


















































---

<div id="update-users-views"></div>

## `Atualizando a view users/views.py`

[users/views.py](../../../users/views.py)
```python
"""
Views da aplicação 'users'.

Este módulo contém todas as views relacionadas à autenticação
e gerenciamento de usuários, incluindo login, logout, criação
de conta e página inicial.
"""
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from chat.history import get_chat_history_dicts
from train.models import TrainingModel
from users.forms import CustomUserCreationForm
from utils.messages import (
    USERS_ACCOUNT_CREATED,
    USERS_FIX_FORM_ERRORS,
    USERS_INVALID_CREDENTIALS,
)


def create_account(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = CustomUserCreationForm()
        return render(
            request,
            "pages/create-account.html",
            {"form": form}
        )

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, USERS_ACCOUNT_CREATED)
            return redirect("/")

        messages.error(request, USERS_FIX_FORM_ERRORS)
        return render(
            request,
            "pages/create-account.html",
            {"form": form}
        )


@login_required(login_url="/")
def home_view(request: HttpRequest) -> HttpResponse:
    chat_history = get_chat_history_dicts(request.user)
    training_models = list(
        TrainingModel.objects.filter(user=request.user).order_by("-updated_at")[:100]
    )
    raw_active = request.session.get("active_training_model_id")
    try:
        active_training_model_id = (
            int(raw_active) if raw_active is not None else None
        )
    except (TypeError, ValueError):
        active_training_model_id = None

    valid_ids = {m.id for m in training_models}
    if training_models:
        if (
            active_training_model_id is not None
            and active_training_model_id in valid_ids
        ):
            selected_training_model_id = active_training_model_id
        else:
            selected_training_model_id = training_models[0].id
    else:
        selected_training_model_id = None

    return render(
        request,
        "pages/home.html",
        {
            "chat_history": chat_history,
            "training_models": training_models,
            "selected_training_model_id": selected_training_model_id,
        },
    )


def login_view(request: HttpRequest) -> HttpResponse:
    # Se o usuário já estiver logado, envia direto pra home
    if request.user.is_authenticated:
        return redirect("home")

    # GET → renderiza pages/index.html (form de login)
    if request.method == "GET":
        return render(request, "pages/index.html")

    # POST → processa credenciais
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        messages.error(request, USERS_INVALID_CREDENTIALS)
        return render(
            request,
            "pages/index.html"
        )


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("/")
```


















































---

<div id="update-chat-views"></div>

## `Atualizando a view chat/views.py`

[chat/views.py](../../../chat/views.py)
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


















































---

<div id="update-home-template"></div>

## `Atualizando o template home.html`

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
                    {% if not training_models %}
                        <p class="text-sm text-gray-500 mt-2">
                            <a href="{% url 'train_home' %}" class="text-blue-600 hover:underline">
                                Treine um modelo
                            </a>
                            para o chat usar seus documentos.
                        </p>
                    {% endif %}
                </header>

                {% if messages %}
                    <ul class="shrink-0 space-y-2">
                        {% for message in messages %}
                            <li class="px-4 py-2 rounded-lg text-sm
                                {% if message.tags == 'success' %}
                                    bg-green-100 text-green-800
                                {% else %}
                                    bg-red-100 text-red-800
                                {% endif %}">
                                {{ message }}
                            </li>
                        {% endfor %}
                    </ul>
                {% endif %}

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
                                        <div class="bg-gray-100 p-3 rounded-lg overflow-hidden">
                                            
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
                                                        Fontes:
                                                    </div>
                                                    <div class="flex flex-wrap items-center gap-2 text-xs">
                                                        {% for source in message.sources %}
                                                            {% if source.folder_id %}
                                                                <a
                                                                    href="{% url 'workspace_home' %}?folder={{ source.folder_id }}&file={{ source.file_id }}"
                                                                    class="
                                                                        inline-flex items-center gap-1
                                                                        rounded-full px-2 py-1
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
                                                                    href="{% url 'workspace_home' %}?file={{ source.file_id }}"
                                                                    class="
                                                                        inline-flex items-center gap-1
                                                                        rounded-full px-2 py-1
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

                <!-- Limpar + pergunta + modelo + enviar -->
                <div class="shrink-0 flex flex-wrap items-center gap-2">

                    <!-- Botão Limpar -->
                    <form method="post" action="{% url 'clear_chat' %}">
                        {% csrf_token %}
                        <button
                            type="submit"
                            class="
                                px-3 py-2
                                rounded-lg
                                border border-gray-300
                                bg-white text-gray-800
                                hover:bg-gray-50
                                whitespace-nowrap
                                text-sm
                            "
                        >
                            Limpar
                        </button>
                    </form>

                    <!-- Form vazio: campos associados via atributo form -->
                    <form id="ask-form" method="post" action="{% url 'ask' %}">
                        {% csrf_token %}
                    </form>

                    <div class="flex flex-1 min-w-[12rem] gap-2 items-center">
                        <input
                            type="text"
                            name="question"
                            form="ask-form"
                            placeholder="Digite sua pergunta..."
                            required
                            autocomplete="off"
                            class="
                                flex-1 min-w-0
                                border border-gray-300 rounded-lg
                                px-3 py-2 text-sm
                            "
                        >

                        {% if training_models %}
                            <form
                                method="post"
                                action="{% url 'train_set_active' %}"
                                class="flex items-center shrink-0">
                                {% csrf_token %}
                                <input type="hidden" name="next" value="{% url 'home' %}">
                                <label for="chat-model-select" class="sr-only">Modelo</label>
                                <select
                                    name="training_model_id"
                                    id="chat-model-select"
                                    title="Modelo do chat"
                                    onchange="this.form.submit()"
                                    class="
                                        w-[4.67rem] sm:w-[6.33rem]
                                        text-xs py-1.5 pl-1.5 pr-5
                                        border border-gray-300 rounded-md
                                        bg-white text-gray-800
                                        focus:ring-1 focus:ring-blue-500 focus:border-blue-500
                                    ">
                                    {% for tm in training_models %}
                                        <option
                                            value="{{ tm.pk }}"
                                            {% if selected_training_model_id == tm.id %}selected{% endif %}>
                                            {{ tm.name }}
                                        </option>
                                    {% endfor %}
                                </select>
                            </form>
                        {% endif %}

                        <button
                            type="submit"
                            form="ask-form"
                            class="
                                px-4 py-2 rounded-lg shrink-0
                                bg-blue-600 text-white text-sm
                                hover:bg-blue-700
                            ">
                            Enviar
                        </button>
                    </div>
                </div>

            </div>
            <!-- /Área do chat -->
        </main>
    </div>
{% endblock %}

{% block scripts %}
    <script src="{% static 'users/js/home.js' %}"></script>
{% endblock scripts %}
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
