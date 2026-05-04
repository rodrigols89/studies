# `Criando o app RAG e planejando sua estrutura`

## Conteúdo

 - [`Criando o app RAG e instalando nas configurações do projeto`](#create-rag-app)
 - [`Estrutura do App RAG (ingestion, retrieval e generation)`](#app-structure)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="create-rag-app"></div>

## `Criando o app RAG e instalando nas configurações do projeto`

De início aqui vamos criar o nosso App RAG:

```bash
python manage.py startapp rag
```

Agora vamos registrar esse app nas configurações do projeto:

[settings.py](../../../core/settings.py)
```python
INSTALLED_APPS = [

    ...

    # Seus apps
    "rag"
]
```


















































---

<div id="app-structure"></div>

## `Estrutura do App RAG (ingestion, retrieval e generation)`

Uma abordagem utilizada em sistemas RAG consiste em dividir o trabalho nos seguintes grupo:

 - `services/ingestion`
   - Responsável por transformar arquivos brutos em embeddings armazenados no banco (descobrir arquivos, extrair texto, dividir em chunks e gerar vetores).
 - `services/retrieval`
   - Responsável por buscar os chunks mais relevantes para uma pergunta, usando embeddings e busca vetorial.
 - `services/generation`
   - Responsável por montar o contexto e gerar a resposta final do LLM a partir dos chunks recuperados.

A estrutura do nosso app RAG vai ficar da seguinte maneira:

```bash
rag/
├── services/
│   ├── generation/
│   |      ├── answer_generator.py
│   |      |     ├── _get_llm()
│   |      |     └── generate_answer()
│   |      └── context_builder.py
│   |            └── build_context()
|   |
│   ├── ingestion/
│   |      ├── chunking.py
│   |      |     └── chunk_text()
│   |      ├── embeddings.py
│   |      |     ├── get_embedding_model()
│   |      |     └── generate_embeddings()
│   |      ├── file_discovery.py
│   |      |     ├── get_file_type()
│   |      |     ├── get_folder_path()
│   |      |     ├── map_file()
│   |      |     └── discover_workspace_files()
│   |      ├── ingestion_pipeline.py
│   |      |     └── ingest_workspace()
│   |      ├── text_extraction.py
│   |      |     ├── extract_txt()
│   |      |     ├── extract_md()
│   |      |     ├── extract_pdf()
│   |      |     ├── extract_docx()
│   |      |     ├── extract_html()
│   |      |     ├── extract_excel()
│   |      |     └── extract_text()
|   |      └── vector_store.py
|   |            └── store_embeddings()
│   |
│   └── retrieval/
│          └── embed_query.py
│          |
│          └── vector_search.py
│                └── vector_search()
|
├── qa_service.py
└── models.py
      └── DocumentEmbedding()
```


















































---
