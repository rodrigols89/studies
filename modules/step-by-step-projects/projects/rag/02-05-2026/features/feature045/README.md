# `Gerando Vetores de Embeddings a partir de chunks de texto`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Instalando as bibliotecas necessárias`](#installing-dependencies)
 - [`Criando uma função para instanciar (e retornar) um modelo de embeddings: get_embedding_model()`](#get-embedding-model)
 - [`Gerando embeddings a partir dos chunks de texto: generate_embeddings()`](#generate-embeddings)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

> 🧠 **Aqui a IA entra de verdade.**

Até agora, nós só **preparamos texto**:

* extraímos conteúdo
* dividimos em chunks
* mantivemos contexto semântico

> **⚠️ Nada disso é IA ainda.**

Neste passo, cada *chunk* de texto vira um **vetor numérico** que representa o *significado* daquele texto.

Isso nos permitirá:

* busca semântica
* perguntas em linguagem natural
* respostas inteligentes no RAG

### `Exemplo Visual (entendimento intuitivo)`

Texto original:

```bash
"Python é uma linguagem de programação muito usada em IA."
```

Depois do embedding:

```bash
[0.021, -0.334, 0.887, 0.104, ..., -0.552]
```

Agora imagine **milhares** desses vetores armazenados.

Quando o usuário pergunta:

> “Qual linguagem é usada em inteligência artificial?”

> **NOTE:**  
> *A pergunta também vira um vetor.*

🔍 O banco vetorial compara:

* vetor da pergunta
* vetores dos chunks
* retorna os **mais semanticamente próximos**

### `Conceito-chave desse passo`

* 📄 **Entrada:** chunks de texto
* 🧠 **Processo:** modelo de embeddings
* 🔢 **Saída:** vetores numéricos (listas de floats)
* 🔐 **Regra de ouro:**
  **Todo embedding precisa carregar `user_id`**


















































---

<div id="installing-dependencies">

## `Instalando e configurando as bibliotecas necessárias`

Antes de começar as implementações, vamos *instalar*, *configurar* e *exportar* as bibliotecas necessárias:

```bash
poetry add langchain-openai@latest
```

[.env](../../../.env)
```bash
OPENAI_API_KEY=sk-...
```

Por fim, vamos exportar essas dependências para o `requirements.txt`:

```bash
poetry export \
--without-hashes \
--format=requirements.txt \
--output=requirements.txt
```


















































---

<div id="get-embedding-model"></div>

## `Criando uma função para instanciar (e retornar) um modelo de embeddings: get_embedding_model()`

> Aqui vamos criar uma função responsável por **instanciar e retornar um modelo de embeddings**.

Esse modelo será usado para:

> **Transformar textos (chunks) em vetores numéricos.**

### `Código Completo`

A nossa função `get_embedding_model()` (completa) vai ficar da seguinte maneira:

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python
import os

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
```

### `Testando manualmente`

Agora, vamos criar alguns códigos que serão responsáveis por testar (manualmente) se a função `get_embedding_model()` consegue instanciar um modelo de embeddings:

```python
from rag.services.ingestion.embeddings import get_embedding_model


def main() -> None:
    print("🔄 Inicializando modelo de embeddings...")

    model = get_embedding_model()

    print("✅ Modelo carregado com sucesso!")

    # Texto de teste
    text = "Olá mundo, isso é um teste de embeddings."

    print(f"\n📌 Gerando embedding para: {text}")

    embedding = model.embed_query(text)

    print("\n📊 Resultado:")
    print(f"Tamanho do vetor: {len(embedding)}")
    print(f"Primeiros 5 valores: {embedding[:5]}")


if __name__ == "__main__":
    main()
```

**OUPUT:**
```bash
🔄 Inicializando modelo de embeddings...
✅ Modelo carregado com sucesso!

📌 Gerando embedding para: Olá mundo, isso é um teste de embeddings.

📊 Resultado:
Tamanho do vetor: 3072
Primeiros 5 valores: [-0.006936306599527597, 0.045991335064172745, -0.00898377038538456, -0.002698613330721855, -0.0006032706587575376]
```

Vejam que nós:

 - **Conseguimos instanciar o modelo `text-embedding-3-large` que foi definido na função `get_embedding_model()`**
 - **Conseguimos gerar um embedding para um texto qualquer! (fake)**


















































---

<div id="generate-embeddings"></div>

## `Gerando embeddings a partir dos chunks de texto: generate_embeddings()`

> Agora entramos no **coração do pipeline de RAG**.

Nesta etapa, vamos pegar:

* chunks de texto já processados (resultado do chunking)
* um modelo de embeddings já carregado (`get_embedding_model()`)

E transformar cada chunk em:

* um **vetor numérico**
* mantendo todos os metadados originais
* adicionando o campo `"embedding"`

> **⚠️ NOTE:**  
> O resultado final será uma estrutura **pronta para ser salva em um banco vetorial**.

### `Código Completo`

A nossa função `generate_embeddings()` (completa) vai ficar da seguinte maneira:

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python

from typing import Any, Dict, List


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

### `Explicação passo a passo (Step-by-Step)`

Vamos começar importando as tipagens necessárias:

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python
from typing import Any, Dict, List
```

 - `Any`
   - Permite qualquer tipo de valor
 - `Dict`
   - Representa dicionários tipados
 - `List`
   - Representa listas tipadas

Continuando, agora vamos definir nossa função `generate_embeddings()`:

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python
def generate_embeddings(
    *,
    embedding_model: OpenAIEmbeddings,
    chunks: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
```

---

 - **O que essa função faz (ou vai fazer)?**
   - Recebe uma lista de chunks de texto e:
     - Extrai apenas o conteúdo textual
     - Gera embeddings para cada chunk
     - Reanexa o embedding ao chunk original
     - Retorna os chunks enriquecidos com vetores
 - **Parâmetros da função:**
   - `*`
     - O `*` obriga que os argumentos sejam passados **explicitamente por nome**.
     - Exemplo correto:
       - `embedding_model=model`
       - `chunks=chunks`
     - *👉 Isso evita erros de ordem e deixa o código mais legível*
   - `embedding_model: OpenAIEmbeddings`
     - Modelo de embeddings previamente carregado
     - Responsável por converter texto → vetor numérico
     - 📌 É o mesmo modelo retornado por `get_embedding_model()`.
   - `chunks: List[Dict[str, Any]]`
     - Cada item da lista representa um chunk e normalmente contém algo como
     - 👉 O formato é flexível, desde que exista a chave `"content"`.
 - **O que essa função retorna?**
   - `-> List[Dict[str, Any]]`
   - Uma nova lista onde cada chunk contém **todos os dados originais**, mais:
     - `"embedding": [0.0123, 0.9845, ...]`

Continuando na implementação agora nós vamos extrair apenas o texto de cada chunk:

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python
def generate_embeddings(...) -> List[Dict[str, Any]]:

    ...

    texts: List[str] = [
        chunk["content"]
        for chunk in chunks
    ]
```

 - **O que esse código faz?**
   - Cria uma lista contendo **somente o texto** de cada chunk.
 - **Explicando o que está acontecendo passo a passo:**
   - Iteramos sobre `chunks`
   - Para cada `chunk`:
     - acessamos `chunk["content"]`
   - O resultado é uma lista de strings

Exemplo de saída:

```python
[
    "Primeiro pedaço do texto",
    "Segundo pedaço do texto",
    "Terceiro pedaço do texto",
]
```

Ótimo, agora nós vamos gerar os vetores de embeddings:

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python
def generate_embeddings(...) -> List[Dict[str, Any]]:

    ...

    vectors: List[List[float]] = (
        embedding_model.embed_documents(texts)
    )
```

Vejam que no código acima:

 - **Estamos criando um vetor tipado: `vectors: List[List[float]]`:** 
   - Esse vetor vai ser uma lista de floats
 - **O que a função `embed_documents()` faz?**
   - Recebe uma lista de textos e converte cada texto em um vetor numérico.
   - **Quais parâmetros ela recebe?**
     - `texts: List[str]`
       - Lista de textos (chunks)
   - **O que ela retorna?**
     - `List[List[float]]`
 - **Aqui:**
   - Cada texto vira um vetor
   - Cada vetor é uma lista de números (`float`)
   - Todos os vetores têm o **mesmo tamanho** (ex: 384 dimensões)
 - **📌 Importante:**
   - A ordem dos vetores **corresponde exatamente** à ordem dos textos
   - Isso é crucial para o próximo passo

Recaptulando, o que nós temos até então:

 - `texts`
   - Lista de textos (chunks)
 - `vectors`
   - Lista de vetores numéricos dos chunks

Ótimo, sabendo disso o que nós vamos fazer agora vai ser, **inicializa uma lista vazia que armazenará**:

 - o chunk original
 - mais o campo `"embedding"`

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python
def generate_embeddings(...) -> List[Dict[str, Any]]:

    ...

    embedded_chunks: List[Dict[str, Any]] = []
```

Agora, nós vamos utilizar a função `zip()` para associar cada chunk ao seu respectivo embedding:

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python
def generate_embeddings(...) -> List[Dict[str, Any]]:

    ...

    for chunk, vector in zip(chunks, vectors):
        ...
```

 - `zip()`
   - **O que a função `zip()` faz?**
     - Combina múltiplas listas, iterando sobre elas **em paralelo**.
   - **Quais parâmetros ela recebe?**
     - `chunks`
     - `vectors`
   - **O que ela retorna?**
     - Um iterador de tuplas, como:
       - `(chunk_1, vector_1)`
       - `(chunk_2, vector_2)`
       - `(chunk_3, vector_3)`

Sabendo que a função `zip()` vai iterar em paralelo sobre as listas `chunks` e `vectors`, vamos fazer ela salvar o chunk atual com o seu respectivo embedding na lista `embedded_chunks` (com a função .append() da classe `List`):

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python
def generate_embeddings(...) -> List[Dict[str, Any]]:

    ...

    for chunk, vector in zip(chunks, vectors):
        embedded_chunks.append({
            **chunk,
            "embedding": vector,
        })
```

Por fim, nós vamos retornar o `embedded_chunks` que vai conter todos os chunks com seus respectivos embeddings:

[rag/services/embeddings.py](../../../rag/services/ingestion/embeddings.py)
```python
def generate_embeddings(...) -> List[Dict[str, Any]]:

    ...

    return embedded_chunks
```

> **O que isso faz?**

Retorna a lista completa de chunks:

 - já vetorizados
 - com metadados preservados
 - prontos para:
   - salvar no banco vetorial
   - associar por `user_id`
   - realizar busca semântica

### `Testando manualmente`

Para testar a função `generate_embeddings()` usando dados reais do **media/workspace**, o ideal é montar um `driver.py` que execute todas as funções que nós já implementamos, na ordem correta:

```bash
Workspace
   ↓
discover_workspace_files()
   ↓
extract_text()
   ↓
chunk_text()
   ↓
generate_embeddings()
```

Assim nós validamos o pipeline completo antes de salvar no banco vetorial:

```python
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model

from rag.services.ingestion.chunking import chunk_text
from rag.services.ingestion.embeddings import (
    generate_embeddings,
    get_embedding_model,
)
from rag.services.ingestion.file_discovery import discover_workspace_files
from rag.services.ingestion.text_extraction import extract_text

User = get_user_model()


def test_embedding_pipeline(user_id: int):

    print("\n🔎 Buscando usuário...")
    user = User.objects.get(id=user_id)
    print(f"Usuário encontrado: {user}")

    print("\n📂 Descobrindo arquivos do workspace...\n")
    inventory = discover_workspace_files(user)
    print(f"Arquivos encontrados: {len(inventory)}\n")

    embedding_model = get_embedding_model()

    for file_info in inventory:
        print("📄 Arquivo:", file_info["name"])
        print("📦 Tipo:", file_info["file_type"])
        try:
            # -----------------------------------
            # 1️⃣ EXTRAÇÃO DE TEXTO
            # -----------------------------------
            documents = extract_text(file_info)

            all_chunks = []

            for doc in documents:
                text = doc.page_content
                # -----------------------------------
                # 2️⃣ CHUNKING
                # -----------------------------------
                chunks = chunk_text(
                    text=text,
                    chunk_size=500,
                    chunk_overlap=50,
                )

                for chunk in chunks:
                    all_chunks.append({
                        "content": chunk,
                        "file_id": file_info["file_id"],
                        "source": file_info["name"],
                        "folder": file_info["folder"],
                    })

            print(f"🧩 Chunks gerados: {len(all_chunks)}")

            # -----------------------------------
            # 3️⃣ EMBEDDINGS
            # -----------------------------------
            embedded_chunks = generate_embeddings(
                embedding_model=embedding_model,
                chunks=all_chunks,
            )

            print(f"🧠 Embeddings gerados: {len(embedded_chunks)}")
            if embedded_chunks:
                print("\n📊 Exemplo de chunk com embedding:\n")

                example = embedded_chunks[0]

                print("Conteúdo:")
                print(example["content"][:200])

                print("\nDimensão do vetor:", len(example["embedding"]))
                print("Valor do vetor (primeiras 10 dimensões):")
                print(example["embedding"][:10])
        except Exception as e:
            print("❌ ERRO:", e)
        print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    test_embedding_pipeline(user_id=1)
```

**OUTPUT:**
```bash
🔎 Buscando usuário...
Usuário encontrado: drigols

📂 Descobrindo arquivos do workspace...

Arquivos encontrados: 40


📄 Arquivo: TERMO DE EMPRÉSTIMO DE BEM MÓVEL.docx
📦 Tipo: .docx
🧩 Chunks gerados: 9
🧠 Embeddings gerados: 9

📊 Exemplo de chunk com embedding:

Conteúdo:
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

Dimensão do vetor: 384
Valor do vetor (primeiras 10 dimensões):
[0.036749519407749176, 0.04102740436792374, -0.020422374829649925, -0.003431542543694377, -0.08255966752767563, 0.03698539733886719, -0.009754789061844349, 0.021472293883562088, 0.040164198726415634, 0.05117522552609444]

======================================================================

📄 Arquivo: Poliana.docx
📦 Tipo: .docx
🧩 Chunks gerados: 9
🧠 Embeddings gerados: 9

📊 Exemplo de chunk com embedding:

Conteúdo:
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

Dimensão do vetor: 384
Valor do vetor (primeiras 10 dimensões):
[0.036749519407749176, 0.04102740436792374, -0.020422374829649925, -0.003431542543694377, -0.08255966752767563, 0.03698539733886719, -0.009754789061844349, 0.021472293883562088, 0.040164198726415634, 0.05117522552609444]

======================================================================

📄 Arquivo: Paloma.docx
📦 Tipo: .docx
🧩 Chunks gerados: 9
🧠 Embeddings gerados: 9

📊 Exemplo de chunk com embedding:

Conteúdo:
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

Dimensão do vetor: 384
Valor do vetor (primeiras 10 dimensões):
[0.036749519407749176, 0.04102740436792374, -0.020422374829649925, -0.003431542543694377, -0.08255966752767563, 0.03698539733886719, -0.009754789061844349, 0.021472293883562088, 0.040164198726415634, 0.05117522552609444]

======================================================================

📄 Arquivo: Nice.docx
📦 Tipo: .docx
🧩 Chunks gerados: 9
🧠 Embeddings gerados: 9

📊 Exemplo de chunk com embedding:

Conteúdo:
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

Dimensão do vetor: 384
Valor do vetor (primeiras 10 dimensões):
[0.036749519407749176, 0.04102740436792374, -0.020422374829649925, -0.003431542543694377, -0.08255966752767563, 0.03698539733886719, -0.009754789061844349, 0.021472293883562088, 0.040164198726415634, 0.05117522552609444]

======================================================================

📄 Arquivo: Estabilizador.docx
📦 Tipo: .docx
🧩 Chunks gerados: 9
🧠 Embeddings gerados: 9

📊 Exemplo de chunk com embedding:

Conteúdo:
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

Dimensão do vetor: 384
Valor do vetor (primeiras 10 dimensões):
[0.036749519407749176, 0.04102740436792374, -0.020422374829649925, -0.003431542543694377, -0.08255966752767563, 0.03698539733886719, -0.009754789061844349, 0.021472293883562088, 0.040164198726415634, 0.05117522552609444]


    ...
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
