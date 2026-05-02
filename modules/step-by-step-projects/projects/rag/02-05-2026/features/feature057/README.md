# `Atualizando o treinamento para usar Celery com Redis`

## Conteúdo

 - [`O que é concorrência?`](#what-is-concurrency)
 - [`O que é uma tarefa em background?`](#what-is-background-job)
 - [`Entendendo e instalando o HTTPX`](#what-is-httpx)
 - [`Entendendo e instalando o Celery`](#what-is-celery)
 - [`Entendendo e Instalando/configurando o Redis`](#what-is-redis)
 - [`Configurando o Celery nas configurações do projeto /core`](#configuring-celery-in-core-settings)
 - [`Atualizando o modelo train/models.py`](#updating-the-model-trainingmodel)
 - [`Criando o helper train/training_helpers.py`](#creating-the-training_helpers-helper)
 - [`Criando o train/runner.py`](#creating-the-train-runner)
 - [`Criando o train/tasks.py`](#creating-the-train-tasks)
 - [`Atualizando o train/utils.py`](#updating-the-utils)
 - [`Atualiza a view (ação) train/views.py`](#updating-the-train-views)
 - [`Atualizando a view (ação) users/views.py`](#updating-the-users-views)
 - [`Atualizando o train/admin.py`](#updating-the-train-admin)
 - [`Atualizando o template train_home.html`](#updating-the-train-home-template)
 - [`Atualizando o template training_model_detail.html`](#updating-the-training-model-detail-template)
 - [`Instalando o Flower`](#install-flower)
<!---
[WHITESPACE RULES]
- 50
--->









































---

<div id="what-is-concurrency"></div>

## `O que é concorrência?`

`Concorrência` é ter **várias linhas de trabalho em andamento** no mesmo período de tempo. Elas podem ser:

 - **Alternadas rapidamente** num único núcleo (como um chef que corta cebola, volta ao fogão, volta à cebola)
 - **Ao mesmo tempo de verdade** em vários núcleos (**paralelismo**)

Muita gente usa `“concorrência”` no sentido amplo: *o sistema lida com vários usuários/pedidos sem um travar todos os outros de forma desnecessária*.

**Visual: um servidor atendendo vários usuários**
```bash
        Usuário 1          Usuário 2          Usuário 3
            │                  │                  │
            ▼                  ▼                  ▼
     ┌──────────────────────────────────────────────────┐
     │           Servidor Django / ASGI / workers       │
     │   (vários pedidos “em progresso” ao longo do     │
     │    tempo — concorrência entre requisições)       │
     └──────────────────────────────────────────────────┘
```

**Formas comuns de concorrência (mapa mental):**
| Ideia | Analogia rápida | Onde costuma aparecer |
|--------|-----------------|------------------------|
| **Vários workers/processos** | Vários garçons | Gunicorn com vários workers |
| **Threads** | Um garçom com duas mãos ocupadas | Operações bloqueantes liberadas em pool |
| **Async** | Garçom que não fica parado na cozinha | Muito I/O, muitas conexões |
| **Filas (jobs)** | Pedidos em papel na parede da cozinha | Treinar, indexar documentos, enviar e-mail |


















































---

<div id="what-is-background-job"></div>

## `O que é uma tarefa em background?`

> Uma **tarefa em background** é um trabalho que o usuário **não precisa esperar na mesma tela** para terminar.

O servidor (ou outro serviço) continua processando **depois** que a resposta HTTP já foi enviada.

**🧠 Analogia:**  
Você pede um bolo na confeitaria. A atendente te dá o **comprovante** na hora (**resposta rápida**); o bolo assa **nos bastidores** (**background**); quando fica pronto, você recebe aviso ou busca o pedido.

### `Exemplos que costumam ir para background neste tipo de projeto`

 - **Indexar / fatiar documentos** depois de upload no workspace.
 - **Treinar ou atualizar embeddings** em lote.
 - **Gerar relatórios** ou exportações grandes.
 - **Chamar APIs externas** com retry quando não precisa segurar o usuário na página.



















































---

<div id="what-is-httpx"></div>

## `Entendendo e instalando o HTTPX`

**HTTPX** é um cliente HTTP para Python com API parecida com a de `requests`, mas com duas vantagens importantes para o nosso cenário:

 1. **Suporte nativo a `async`/`await`** — você pode usar `AsyncClient` e fazer várias requisições sem bloquear o *event loop* (útil com ASGI/Uvicorn).
 2. **HTTP/1.1 e HTTP/2** — útil se no futuro vocês falarem com APIs que beneficiam disso.

**Instalando o HTTPX:**
```bash
poetry add httpx@latest
```

**Exportando para as dependências do desenvolvimento:**
```bash
task exportdev
```

**Exportando para as dependências do produção:**
```bash
task exportprod
```


















































---

<div id="what-is-celery"></div>

## `Entendendo e instalando o Celery`

**Celery** é um sistema de **filas de tarefas** para Python: você **enfileira jobs** (funções assíncronas em relação ao request HTTP) e **workers** separados do processo web os executam em segundo plano, com retry, agendamento e integração com Django.

> **⚠️ NOTE:**  
> Precisa de um **message broker** (quase sempre **Redis** ou **RabbitMQ**) para o worker “puxar” as tarefas; opcionalmente um **result backend** (muitas vezes o próprio Redis) para guardar status/resultado.

> **Como isso se encaixa nas tarefas do nosso projeto?**

No seu cenário (upload, treino RAG pesado, possível reindexação), o Celery entra onde **não faz sentido** manter o usuário esperando na mesma requisição:

| Tarefa planejada | Papel do Celery |
|------------------|-----------------|
| **Primeiro job em background** | Ex.: após upload, disparar `extrair texto → chunks → embeddings → gravar no pgvector` em uma task `@shared_task`. |
| **Treino / reindexação longa** | Mover o que hoje roda em `train/views` (pipeline pesado) para uma **task**; a view só valida, grava “pendente” e retorna rápido. |
| **HTTP 202 + id** | A view enfileira a task, devolve **202** (ou redirect) com **id do job**; o worker processa depois. |
| **Modelo de status** | O worker atualiza `processando` → `concluído` / `erro`; a UI pode fazer polling. |
| **Confiabilidade** | **Retries**, fila de dead-letter (com configuração), logs com **task id** — alinhado à lista de “retries, DLQ, alertas de fila”. |
| **Deploy** | Um processo **celery worker** (e opcionalmente **beat** para agendamentos) ao lado do Uvicorn/Gunicorn; Redis como serviço na infra. |

> **O que o Celery **não** resolve sozinho?**

 - **Chat pergunta/resposta em tempo real** pode continuar síncrono (ou streaming) até vocês decidirem UX; Celery é para trabalho **demorado e desacoplado** do clique.
 - **Gargalo de API OpenAI ou CPU** continua existindo: a fila evita **travar o web**, não aumenta o limite da API.

**Em uma frase:**  
**Celery é o mecanismo em que o Django “manda trabalhar” tarefas pesadas para processos dedicados**, encaixando diretamente no roteiro de filas, status, 202 e workers em produção.

**Instalando o Celery:**
```bash
poetry add celery@latest
```

**Exportando para as dependências do desenvolvimento:**
```bash
task exportdev
```

**Exportando para as dependências do produção:**
```bash
task exportprod
```


















































---

<div id="what-is-Redis"></div>

## `Entendendo e Instalando/configurando o Redis`

**Redis** é um armazenamento **em memória** (com opção de persistência em disco), muito rápido, usado como **estruturas de dados** na rede: `filas`, `cache`, `contadores`, `locks leves`, `pub/sub`.

> **Como isso se encaixa nas tarefas do nosso projeto?**

| Uso | Papel do Redis |
|-----|----------------|
| **Celery** | **Broker** (e às vezes **result backend**): o web enfileira jobs; o worker lê da fila no Redis e executa. |
| **Cache Django** (opcional) | Respostas repetidas ou fragmentos de sessão com `django-redis`. |
| **Rate limiting** (opcional) | Contagem de requisições por usuário/IP com janelas de tempo. |
| **Não substitui** | PostgreSQL continua sendo o banco principal; Redis é **auxiliar** para concorrência, filas e cache. |

> **⚠️ NOTE:**  
> Em produção é comum proteger Redis com **senha** e **rede interna**; em desenvimento local o serviço abaixo expõe `6379` para o app na máquina host.

Vamos começar instalando ele para que seja possível usar ele em desenvolvimento:

**Instalando o Redis:**
```bash
poetry add redis@latest
```

**Exportando para as dependências do desenvolvimento:**
```bash
task exportdev
```

**Exportando para as dependências do produção:**
```bash
task exportprod
```

Antes de atualizar o [docker-compose.yml](../../../docker-compose.yml) para ter o serviços Redis, vamos criar as variáveis de ambiente para esse container:

[.env](../../../.env)
```bash
# ======================
# Redis
# ======================
REDIS_PASSWORD=substitua_por_uma_senha_forte_e_longa
# Opcional: teto de RAM do Redis (default no compose se omitir: 512mb)
REDIS_MAXMEMORY=512mb

# Opcional: onde o app na MÁQUINA HOST enxerga o Redis (bind 127.0.0.1:6379 no compose)
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_DB=0

# Quando integrar Celery/RQ/django-redis, use a MESMA senha (troque o trecho da senha)
REDIS_URL=redis://:substitua_por_uma_senha_forte_e_longa@127.0.0.1:6379/0
CELERY_BROKER_URL=redis://:substitua_por_uma_senha_forte_e_longa@127.0.0.1:6379/0
CELERY_RESULT_BACKEND=redis://:substitua_por_uma_senha_forte_e_longa@127.0.0.1:6379/1
```

Agora, o nosso [docker-compose.yml](../../../docker-compose.yml) vai ficar da seguinte maneira:

[docker-compose.yml](../../../docker-compose.yml)
```yaml
services:
  db:
    image: pgvector/pgvector:pg15
    container_name: postgresql
    restart: always
    env_file: .env
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./docker/postgres/init:/docker-entrypoint-initdb.d
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    container_name: redis
    restart: always
    env_file: .env
    environment:
      # Autentica o redis-cli no healthcheck (Redis 6+)
      REDISCLI_AUTH: ${REDIS_PASSWORD}
    ports:
      # Produção: não publica Redis na interface pública; só na máquina local.
      # Se o worker Django/Celery rodar noutro host, use rede privada/VPN ou remova
      # o bind e fale com o serviço pelo nome `redis` na rede do Compose.
      - "127.0.0.1:6379:6379"
    volumes:
      - redis_data:/data
    command: >
      redis-server
      --appendonly yes
      --appendfsync everysec
      --requirepass ${REDIS_PASSWORD}
      --maxmemory ${REDIS_MAXMEMORY:-512mb}
      --maxmemory-policy allkeys-lru
      --tcp-keepalive 300
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5
      start_period: 5s

  nginx:
    image: nginx:1.27
    container_name: nginx
    restart: always
    env_file: .env
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf
      - ./staticfiles:/code/staticfiles
      - ./media:/code/media
      # 🔐 Certificados
      - ./certbot/conf:/etc/letsencrypt
      # 📁 Webroot ACME
      - ./certbot/www:/var/www/certbot
    extra_hosts:
      - "host.docker.internal:host-gateway"

volumes:
  postgres_data:
  redis_data:
```

Para subir o Redis é só executar o seguinte comando:

```bash
docker compose up -d redis
```


















































---

<div id="configuring-celery-in-core-settings"></div>

## `Configurando o Celery nas configurações do projeto /core`

[core/settings.py](../../../core/settings.py)
```python
##############################################################################
# Celery (Redis broker)                                                      #
##############################################################################

def _celery_redis_url() -> str:
    """
    URL do broker/result backend.
    Preferir CELERY_BROKER_URL no .env; senão monta a partir de REDIS_*.
    """
    explicit = os.getenv("CELERY_BROKER_URL", "").strip()
    if explicit:
        return explicit
    password = os.getenv("REDIS_PASSWORD", "").strip()
    host = os.getenv("REDIS_HOST", "127.0.0.1").strip()
    port = os.getenv("REDIS_PORT", "6379").strip()
    db = os.getenv("REDIS_CELERY_DB", "0").strip() or "0"
    if password:
        return f"redis://:{password}@{host}:{port}/{db}"
    return f"redis://{host}:{port}/{db}"


CELERY_BROKER_URL = _celery_redis_url()
CELERY_RESULT_BACKEND = os.getenv(
    "CELERY_RESULT_BACKEND",
    CELERY_BROKER_URL,
).strip() or CELERY_BROKER_URL
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = int(os.getenv("CELERY_TASK_TIME_LIMIT", str(4 * 3600)))
CELERY_TASK_SOFT_TIME_LIMIT = int(
    os.getenv("CELERY_TASK_SOFT_TIME_LIMIT", str(3 * 3600))
)
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
```

[core/celery.py](../../../core/celery.py)
```python
import os

from celery import Celery

try:
    import redis  # noqa: F401 — garante que Kombu tenha o cliente se Redis for usado
except ImportError:
    redis = None  # type: ignore[assignment, misc]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


def _require_redis_client_if_urls_use_redis() -> None:
    """
    Kombu deixa o módulo redis como None se `pip install redis` não foi feito;
    o worker quebra com: 'NoneType' object has no attribute 'Redis'.
    """
    broker = str(app.conf.broker_url or "")
    backend = str(app.conf.result_backend or "")
    if not (broker.startswith("redis") or backend.startswith("redis")):
        return
    if redis is None:
        raise ImportError(
            "Celery usa Redis como broker ou result backend, mas o pacote "
            "Python 'redis' não está instalado no mesmo ambiente do worker. "
            "Execute: pip install -r requirements.txt (ou pip install redis)."
        )


_require_redis_client_if_urls_use_redis()
```

[core/__init__.py](../../../core/__init__.py)
```python
from .celery import app as celery_app

__all__ = ("celery_app",)
```


















































---

<div id="updating-the-model-trainingmodel"></div>

## `Atualizando o modelo train/models.py`

[train/models.py](../../../train/models.py)
```python
from django.conf import settings
from django.db import models


class TrainingModel(models.Model):
    """Modelo lógico de treino (nome escolhido pelo usuário)."""

    class Status(models.TextChoices):
        WORKING = "working", "Em andamento"
        READY = "ready", "Pronto"
        FAILED = "failed", "Falhou"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="training_models",
    )
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.READY,
        db_index=True,
    )
    error_message = models.TextField(
        blank=True,
        default="",
        help_text="Detalhes quando o treino falha (para exibição no painel).",
    )
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

<div id="creating-the-training_helpers-helper"></div>

## `Criando o helper train/training_helpers.py`

[train/training_helpers.py](../../../train/training_helpers.py)
```python
from typing import Any, List

from rag.services.ingestion.file_discovery import (
    discover_all_workspace_files,
    discover_workspace_files,
)
from train.models import TrainingModel, TrainingModelFile

TRAINING_MODEL_NAME_MAX_LEN = 255


def discover_files_for_training(
    user: Any,
    selected_folder_ids: List[int],
) -> List[dict[str, Any]]:
    if selected_folder_ids:
        return discover_workspace_files(
            user=user,
            folder_ids=selected_folder_ids,
        )
    return discover_all_workspace_files(user=user)


def persist_training_model_file_rows(
    training_model: TrainingModel,
    files: List[dict[str, Any]],
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
```


















































---

<div id="creating-the-train-runner"></div>

## `Criando o train/runner.py`

[train/runner.py](../../../train/runner.py)
```python
from __future__ import annotations

from typing import List

from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
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
from rag.services.ingestion.vector_store import store_embeddings
from train.models import TrainingModel, TrainingModelFile
from train.training_helpers import (
    discover_files_for_training,
    persist_training_model_file_rows,
)
from utils.messages import (
    RAG_NO_FILES_FOUND,
    RAG_NO_VALID_CONTENT_FOUND,
)


def _truncate_error(msg: str, max_len: int = 2000) -> str:
    msg = (msg or "").strip()
    if len(msg) <= max_len:
        return msg
    return msg[: max_len - 1] + "…"


def _fail_training_model(training_model_id: int, message: str) -> None:
    TrainingModel.objects.filter(pk=training_model_id).update(
        status=TrainingModel.Status.FAILED,
        error_message=_truncate_error(message),
        updated_at=timezone.now(),
    )


def execute_training_job(
    *,
    training_model_id: int,
    user_id: int,
    selected_folder_ids: List[int],
) -> None:
    User = get_user_model()
    user = User.objects.filter(pk=user_id).first()
    if user is None:
        return

    tm = TrainingModel.objects.filter(
        pk=training_model_id,
        user_id=user_id,
    ).first()
    if tm is None:
        return
    if tm.status != TrainingModel.Status.WORKING:
        return

    try:
        DocumentEmbedding.objects.filter(
            training_model_id=tm.id,
        ).delete()
        TrainingModelFile.objects.filter(training_model_id=tm.id).delete()

        files = discover_files_for_training(user, selected_folder_ids)
        if not files:
            _fail_training_model(tm.id, RAG_NO_FILES_FOUND)
            return

        embedded_chunks = embedded_chunks_from_files_parallel(
            files,
            user.id,
            max_workers=DEFAULT_EMBED_MAX_WORKERS,
        )
        if not embedded_chunks:
            _fail_training_model(
                tm.id,
                RAG_NO_VALID_CONTENT_FOUND,
            )
            return

        embed_model = get_embedding_model()
        embedded_chunks = async_to_sync(generate_embeddings)(
            embedding_model=embed_model,
            chunks=embedded_chunks,
        )

        store_embeddings(
            embedded_chunks=embedded_chunks,
            training_model_id=tm.id,
        )

        persist_training_model_file_rows(tm, files)

        TrainingModel.objects.filter(pk=tm.pk).update(
            status=TrainingModel.Status.READY,
            error_message="",
            updated_at=timezone.now(),
        )
    except Exception as exc:
        _fail_training_model(tm.id, str(exc))
```


















































---

<div id="creating-the-train-tasks"></div>

## `Criando o train/tasks.py`

[train/tasks.py](../../../train/tasks.py)
```python
from celery import shared_task

from train.runner import execute_training_job


@shared_task(bind=True, ignore_result=True)
def run_training_task(
    self,
    training_model_id: int,
    user_id: int,
    selected_folder_ids: list,
) -> None:
    execute_training_job(
        training_model_id=training_model_id,
        user_id=user_id,
        selected_folder_ids=list(selected_folder_ids or []),
    )
```


















































---

<div id="updating-the-utils"></div>

## `Atualizando o train/utils.py`

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
                status=TrainingModel.Status.READY,
            ).exists():
                return sid_int

    latest = (
        TrainingModel.objects.filter(
            user_id=user_id,
            status=TrainingModel.Status.READY,
        )
        .order_by("-updated_at")
        .first()
    )
    return latest.id if latest else None
```


















































---

<div id="updating-the-train-views"></div>

## `Atualiza a view (ação) train/views.py`

[train/views.py](../../../train/views.py)
```python
from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from train.models import TrainingModel
from train.tasks import run_training_task
from train.training_helpers import TRAINING_MODEL_NAME_MAX_LEN
from utils.messages import (
    RAG_TRAINING_ALREADY_RUNNING,
    RAG_TRAINING_MODEL_DELETED,
    RAG_TRAINING_MODEL_NAME_REQUIRED,
    RAG_TRAINING_QUEUED,
)
from workspace.browser import get_workspace_browser_context
from workspace.models import Folder


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

    already_running = False
    training_model: TrainingModel | None = None

    try:
        with transaction.atomic():
            training_model = (
                TrainingModel.objects.select_for_update()
                .filter(
                    user=user,
                    name=model_name,
                )
                .first()
            )
            if training_model is None:
                training_model = TrainingModel.objects.create(
                    user=user,
                    name=model_name,
                    status=TrainingModel.Status.WORKING,
                    error_message="",
                )
            elif training_model.status == TrainingModel.Status.WORKING:
                already_running = True
            else:
                training_model.status = TrainingModel.Status.WORKING
                training_model.error_message = ""
                training_model.save(
                    update_fields=["status", "error_message", "updated_at"],
                )
    except Exception as e:
        messages.error(request, f"Erro ao preparar treinamento: {e}")
        return redirect(next_default)

    if already_running:
        messages.error(
            request,
            RAG_TRAINING_ALREADY_RUNNING.format(name=model_name),
        )
        return redirect(next_default)

    assert training_model is not None

    try:
        run_training_task.delay(
            training_model.id,
            user.id,
            selected_folder_ids,
        )
    except Exception as e:
        TrainingModel.objects.filter(pk=training_model.pk).update(
            status=TrainingModel.Status.FAILED,
            error_message=str(e)[:2000],
            updated_at=timezone.now(),
        )
        messages.error(request, f"Erro ao enfileirar treinamento: {e}")
        return redirect(next_default)

    messages.success(
        request,
        RAG_TRAINING_QUEUED.format(name=model_name),
    )
    return redirect(next_default)


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
def training_models_status_api(request: HttpRequest) -> JsonResponse:
    """JSON para atualizar status dos modelos no painel (polling)."""
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    rows = (
        TrainingModel.objects.filter(user=request.user)
        .order_by("-updated_at")
        .values("id", "name", "status", "error_message", "updated_at")[:100]
    )
    models = []
    for row in rows:
        models.append(
            {
                "id": row["id"],
                "name": row["name"],
                "status": row["status"],
                "error_message": row["error_message"] or "",
                "updated_at": (
                    timezone.localtime(row["updated_at"]).isoformat()
                    if row["updated_at"]
                    else ""
                ),
            }
        )
    return JsonResponse({"models": models})


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
            status=TrainingModel.Status.READY,
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

<div id="updating-the-users-views"></div>

## `Atualizando a view (ação) users/views.py`

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
        TrainingModel.objects.filter(
            user=request.user,
            status=TrainingModel.Status.READY,
        ).order_by("-updated_at")[:100]
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

<div id="updating-the-train-admin"></div>

## `Atualizando o train/admin.py`

[train/admin.py](../../../train/admin.py)
```python
from django.contrib import admin
from django.utils.html import format_html

from train.models import TrainingModel, TrainingModelFile

_ERROR_PREVIEW_MAX_LEN = 80


class TrainingModelFileInline(admin.TabularInline):
    model = TrainingModelFile
    extra = 0
    readonly_fields = (
        "file_id",
        "file_name",
        "file_path",
        "workspace_folder_id",
    )
    can_delete = False


@admin.register(TrainingModel)
class TrainingModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "status_badge",
        "created_at",
        "updated_at",
        "error_preview",
    )
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("name", "user__username", "user__email", "error_message")
    readonly_fields = ("created_at", "updated_at")
    list_select_related = ("user",)
    ordering = ("-updated_at",)
    inlines = (TrainingModelFileInline,)
    fieldsets = (
        (None, {"fields": ("user", "name", "status")}),
        (
            "Erro (se falhou)",
            {
                "fields": ("error_message",),
                "classes": ("collapse",),
            },
        ),
        (
            "Datas",
            {"fields": ("created_at", "updated_at")},
        ),
    )

    @admin.display(description="Status")
    @staticmethod
    def status_badge(obj: TrainingModel) -> str:
        colors = {
            TrainingModel.Status.WORKING: "#ca8a04",
            TrainingModel.Status.READY: "#16a34a",
            TrainingModel.Status.FAILED: "#dc2626",
        }
        labels = dict(TrainingModel.Status.choices)
        color = colors.get(obj.status, "#6b7280")
        label = labels.get(obj.status, obj.status)
        return format_html(
            '<span style="font-weight:600;color:{};">{}</span>',
            color,
            label,
        )

    @admin.display(description="Erro (prévia)")
    @staticmethod
    def error_preview(obj: TrainingModel) -> str:
        if not obj.error_message:
            return "—"
        text = obj.error_message.strip().replace("\n", " ")
        if len(text) > _ERROR_PREVIEW_MAX_LEN:
            text = text[: _ERROR_PREVIEW_MAX_LEN - 3] + "…"
        return text


@admin.register(TrainingModelFile)
class TrainingModelFileAdmin(admin.ModelAdmin):
    list_display = (
        "file_name",
        "file_id",
        "training_model",
        "workspace_folder_id",
    )
    list_filter = ("training_model",)
    search_fields = ("file_name", "file_path")
    raw_id_fields = ("training_model",)
```


















































---

<div id="updating-the-train-home-template"></div>

## `Atualizando o template train_home.html`

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
                            <li
                                class="
                                    py-3
                                    flex flex-wrap
                                    items-center
                                    justify-between
                                    gap-3"
                                data-training-model-row="{{ tm.pk }}">
                                <div class="flex flex-col gap-1 min-w-0 flex-1">
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
                                        <span
                                            class="training-status-badge shrink-0 inline-flex items-center rounded px-2 py-0.5 text-xs font-medium
                                            {% if tm.status == 'working' %}
                                                bg-yellow-100 text-yellow-800
                                            {% elif tm.status == 'ready' %}
                                                bg-green-100 text-green-800
                                            {% else %}
                                                bg-red-100 text-red-800
                                            {% endif %}"
                                            data-status="{{ tm.status }}">
                                            {% if tm.status == 'working' %}
                                                Em andamento
                                            {% elif tm.status == 'ready' %}
                                                Pronto
                                            {% else %}
                                                Falhou
                                            {% endif %}
                                        </span>
                                        <span class="text-xs text-gray-500 shrink-0">
                                            {{ tm.updated_at|date:"d/m/Y H:i" }}
                                        </span>
                                    </div>
                                    {% if tm.status == 'failed' and tm.error_message %}
                                        <p class="training-status-error text-xs text-red-600 break-words pl-0 max-w-xl">
                                            {{ tm.error_message|truncatechars:280 }}
                                        </p>
                                    {% else %}
                                        <p class="training-status-error text-xs text-red-600 break-words pl-0 max-w-xl hidden"></p>
                                    {% endif %}
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
        (function () {
            const statusUrl = "{% url 'training_models_status' %}";

            const labelFor = (status) => {
                if (status === "working") return "Em andamento";
                if (status === "ready") return "Pronto";
                return "Falhou";
            };

            const badgeClass = (status) => {
                if (status === "working") {
                    return "training-status-badge shrink-0 inline-flex items-center rounded px-2 py-0.5 text-xs font-medium bg-yellow-100 text-yellow-800";
                }
                if (status === "ready") {
                    return "training-status-badge shrink-0 inline-flex items-center rounded px-2 py-0.5 text-xs font-medium bg-green-100 text-green-800";
                }
                return "training-status-badge shrink-0 inline-flex items-center rounded px-2 py-0.5 text-xs font-medium bg-red-100 text-red-800";
            };

            function applyModel(m) {
                const row = document.querySelector("[data-training-model-row=\"" + m.id + "\"]");
                if (!row) return;
                const badge = row.querySelector(".training-status-badge");
                const errEl = row.querySelector(".training-status-error");
                if (badge) {
                    badge.setAttribute("data-status", m.status);
                    badge.className = badgeClass(m.status);
                    badge.textContent = labelFor(m.status);
                }
                if (errEl) {
                    if (m.status === "failed" && m.error_message) {
                        errEl.textContent = m.error_message.length > 280
                            ? m.error_message.slice(0, 277) + "…"
                            : m.error_message;
                        errEl.classList.remove("hidden");
                    } else {
                        errEl.textContent = "";
                        errEl.classList.add("hidden");
                    }
                }
            }

            async function pollOnce() {
                try {
                    const r = await fetch(statusUrl, {
                        headers: { Accept: "application/json" },
                        credentials: "same-origin",
                    });
                    if (!r.ok) return;
                    const data = await r.json();
                    let anyWorking = false;
                    for (const m of data.models || []) {
                        applyModel(m);
                        if (m.status === "working") anyWorking = true;
                    }
                    if (anyWorking) {
                        window.setTimeout(pollOnce, 3000);
                    }
                } catch (e) {
                    window.setTimeout(pollOnce, 8000);
                }
            }

            if (document.querySelector("[data-training-model-row]")) {
                const badgeWorking = document.querySelector('.training-status-badge[data-status="working"]');
                if (badgeWorking) {
                    window.setTimeout(pollOnce, 2000);
                }
            }
        })();

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

<div id="updating-the-training-model-detail-template"></div>

## `Atualizando o template training_model_detail.html`

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
                <p class="text-sm mt-2">
                    <span
                        class="inline-flex items-center rounded px-2 py-0.5 text-xs font-medium
                        {% if training_model.status == 'working' %}
                            bg-yellow-100 text-yellow-800
                        {% elif training_model.status == 'ready' %}
                            bg-green-100 text-green-800
                        {% else %}
                            bg-red-100 text-red-800
                        {% endif %}">
                        {% if training_model.status == 'working' %}
                            Em andamento
                        {% elif training_model.status == 'ready' %}
                            Pronto
                        {% else %}
                            Falhou
                        {% endif %}
                    </span>
                </p>
                {% if training_model.status == 'failed' and training_model.error_message %}
                    <p class="text-sm text-red-600 mt-2 break-words">
                        {{ training_model.error_message }}
                    </p>
                {% endif %}
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
                    {% if training_model.status == 'working' %}
                        <p class="text-gray-500 italic">
                            Treino em andamento. A lista de arquivos aparece quando o treino terminar.
                        </p>
                    {% else %}
                        <p class="text-gray-500 italic">Nenhum arquivo registrado para este modelo.</p>
                    {% endif %}
                {% endif %}
            </section>

        </main>
    </div>
{% endblock %}
```


















































---

<div id="install-flower"></div>

## `Instalando o Flower`

Nós não “vemos” o worker como uma página mágica só com Celery + Redis:

> **O que existe são *logs*, *comandos de inspeção*.**

Para resolver esse problemas nós vamos utilizar a ferramenta `Flower`:

**Instalando o Flower:**
```bash
poetry add --group dev flower@latest
```

**Exportando para as dependências do desenvolvimento:**
```bash
task exportdev
```

**Exportando para as dependências do produção:**
```bash
task exportprod
```

**Rodando o Flower:**
```bash
celery -A core flower
```

O comando acima irá abrir algo como `http://localhost:5555` (porta padrão).

> **⚠️ NOTE:**  
> **Em produção:** não exponha sem autenticação/rede fechada.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
