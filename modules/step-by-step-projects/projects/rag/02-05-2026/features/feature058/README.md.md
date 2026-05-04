# `Mapa de funções do projeto (RAG / Django)`

Este documento resume **como as principais funções se relacionam** nos apps Django (`users`, `workspace`, `train`, `chat`, `trash`, `rag`) e no núcleo (`core`). Os diagramas usam [Mermaid](https://mermaid.js.org/) (renderizam em GitHub, GitLab e muitos editores Markdown).

---

## 1. Visão geral por camada

Fluxo de alto nível: HTTP → views → serviços → ORM / Celery / APIs externas.

```mermaid
flowchart TB
  subgraph HTTP["Camada HTTP"]
    UV[users.views]
    WV[workspace.views]
    TV[train.views]
    CV[chat.views]
    TRV[trash.views]
  end

  subgraph Shared["Helpers compartilhados"]
    WB[get_workspace_browser_context / build_breadcrumbs]
    TH[train.training_helpers / train.utils]
    CH[chat.history]
  end

  subgraph RAG["Serviços RAG"]
    QA[qa_service.ask]
    EQ[retrieval.embed_query]
    VS[retrieval.vector_search]
    CB[generation.build_context]
    GA[generation.generate_answer]
    RUN[train.runner.execute_training_job]
    TASK[train.tasks.run_training_task]
  end

  subgraph Data["Persistência"]
    ORM[(Django ORM: File, Folder, ChatMessage, TrainingModel, DocumentEmbedding)]
  end

  WV --> WB
  TV --> WB
  TV --> TASK
  TASK --> RUN
  CV --> CH
  CV --> QA
  CV --> TH
  UV --> CH
  QA --> EQ
  QA --> VS
  QA --> CB
  QA --> GA
  RUN --> ORM
  VS --> ORM
  CB --> ORM
  CH --> ORM
  WV --> ORM
  TV --> ORM
  TRV --> ORM
```

---

## 2. Rotas → views (entrada HTTP)

Montagem em `core/urls.py`: admin, `allauth`, depois apps sem prefixo próprio.

```mermaid
flowchart LR
  ROOT[core.urls]

  ROOT --> U[apps.users.urls]
  ROOT --> W[apps.workspace.urls]
  ROOT --> T[apps.train.urls]
  ROOT --> C[apps.chat.urls]
  ROOT --> TR[apps.trash.urls]

  U --> index_view
  U --> create_account
  U --> login_view
  U --> logout_view
  U --> home_view

  W --> workspace_home
  W --> create_folder
  W --> upload_file
  W --> upload_folder
  W --> delete_file
  W --> delete_folder
  W --> rename_folder
  W --> rename_file
  W --> move_item
  W --> folder_view

  T --> train_home
  T --> train_view
  T --> training_models_status_api
  T --> training_model_delete
  T --> training_model_detail
  T --> set_active_training_model

  C --> ask_view
  C --> clear_chat_view

  TR --> trash_home
  TR --> permanent_delete_file
  TR --> permanent_delete_folder
  TR --> empty_trash
```

*(Nomes exatos das rotas URL estão em cada `urls.py`; o diagrama foca nas **funções-view** ligadas.)*

---

## 3. Pipeline de chat + RAG (`ask_view` → `ask`)

```mermaid
sequenceDiagram
  participant V as chat.views.ask_view
  participant R as train.utils.resolve_active_training_model_id
  participant A as rag.services.qa_service.ask
  participant E as retrieval.embed_query
  participant S as retrieval.vector_search
  participant B as generation.build_context
  participant G as generation.generate_answer
  participant H as chat.history.append_exchange

  V->>R: sessão / modelo READY
  V->>A: user_id, question, training_model_id
  A->>E: question
  E-->>A: query_vector
  A->>S: user_id, query_vector, training_model_id
  S-->>A: chunks DocumentEmbedding
  alt sem chunks
    A-->>V: resposta padrão + sources vazias
  else com chunks
    A->>B: chunks, user_id
    B-->>A: context, sources
    A->>G: question, context
    G-->>A: answer
    A-->>V: answer, sources
  end
  V->>H: persistir pergunta + resposta
```

---

## 4. Treinamento assíncrono (Celery → runner → ingestão)

```mermaid
flowchart TD
  POST[train.views._handle_train_post]
  DELAY[train.tasks.run_training_task.delay]
  EXEC[train.runner.execute_training_job]

  DISC[training_helpers.discover_files_for_training]
  DISC_F[file_discovery.discover_workspace_files]
  DISC_A[file_discovery.discover_all_workspace_files]

  PIPE[embedding_pipeline.embedded_chunks_from_files_parallel]
  GEM[ingestion.embeddings.get_embedding_model]
  GEN[ingestion.embeddings.generate_embeddings]
  STORE[ingestion.vector_store.store_embeddings]
  PERSIST[training_helpers.persist_training_model_file_rows]

  POST --> DELAY
  DELAY --> EXEC

  DISC --> DISC_F
  DISC --> DISC_A

  EXEC --> DISC
  EXEC --> PIPE
  EXEC --> GEM
  EXEC --> GEN
  EXEC --> STORE
  EXEC --> PERSIST

  EXEC --> TM[(TrainingModel READY / FAILED)]
  STORE --> DE[(DocumentEmbedding)]
  PERSIST --> TMF[(TrainingModelFile)]
```

---

## 5. Workspace: upload de pasta (funções encadeadas)

Subconjunto das helpers em `workspace.views` que formam o fluxo de upload em árvore.

```mermaid
flowchart TD
  UF[upload_folder]

  SU[_setup_folder_upload]
  DF[_determine_folder_name]
  EU[_ensure_unique_folder_name]
  CF[_check_folder_name_exists]

  PC[_process_folder_upload_complete]
  PF[_prepare_file_paths]
  COL[_collect_folder_paths]
  NS[_normalize_path_parts]
  CS[_create_subfolders]

  PROC[_process_folder_uploads]
  PFU[_process_file_upload]
  GT[_get_target_folder]
  VF[validators.validate_file]

  HR[_handle_upload_results]

  UF --> SU
  SU --> DF
  SU --> EU
  EU --> CF

  UF --> PC
  PC --> PF
  PC --> COL
  COL --> NS
  PC --> CS
  PC --> PROC
  PROC --> PFU
  PFU --> NS
  PFU --> GT
  PFU --> VF

  UF --> HR
```

---

## 6. Utilidades transversais

```mermaid
flowchart LR
  subgraph Users
    home_view
    get_chat_history_dicts
  end

  subgraph Train_UI
    train_home
    set_active_training_model
  end

  subgraph Chat
    ask_view
    resolve_active_training_model_id
  end

  WB[get_workspace_browser_context]

  train_home --> WB
  workspace_home --> WB

  home_view --> get_chat_history_dicts
  set_active_training_model --> Session[(session active_training_model_id)]
  ask_view --> resolve_active_training_model_id
  resolve_active_training_model_id --> Session
  resolve_active_training_model_id --> TM[(TrainingModel READY)]
```

---

## 7. Lixeira vs workspace (soft delete vs hard delete)

```mermaid
flowchart LR
  subgraph Workspace
    delete_file
    delete_folder
  end

  subgraph Trash
    trash_home
    permanent_delete_file
    permanent_delete_folder
    empty_trash
  end

  delete_file -->|is_deleted True| DBF[(File trashed)]
  delete_folder -->|is_deleted True| DBFo[(Folder trashed)]

  trash_home --> DBF
  trash_home --> DBFo

  permanent_delete_file -->|File.delete| GoneF[(removido)]
  permanent_delete_folder -->|Folder.delete CASCADE| GoneFo[(removido)]
  empty_trash --> GoneF
  empty_trash --> GoneFo
```

---

## Referência rápida de arquivos-chave

| Área | Módulo principal | Funções de entrada |
|------|------------------|-------------------|
| CLI Django | `manage.py` | `main` → `execute_from_command_line` |
| URLs | `core/urls.py` | `urlpatterns` |
| Chat | `apps/chat/views.py` | `ask_view`, `clear_chat_view` |
| RAG pergunta | `apps/rag/services/qa_service.py` | `ask` |
| Treino | `apps/train/views.py`, `tasks.py`, `runner.py` | `train_view` / `_handle_train_post`, `run_training_task`, `execute_training_job` |
| Workspace | `apps/workspace/views.py` | `workspace_home`, uploads, rename, move, delete |
| Histórico | `apps/chat/history.py` | `get_chat_history_dicts`, `append_exchange`, `clear_chat_for_user` |

---

*Gerado a partir da estrutura atual do repositório; ao adicionar views ou serviços, atualize os diagramas correspondentes.*
