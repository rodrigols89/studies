# `Extraindo textos por tipo de arquivo`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Instalando as bibliotecas necessárias`](#installing-dependencies)
 - [`Extraindo conteúdo de arquivos .txt com Langchain`](#extracting-txt)
 - [`Extraindo conteúdo de arquivos .pdf com Langchain`](#extracting-pdf)
 - [`Extraindo conteúdo de arquivos .docx com Langchain`](#extracting-docx)
 - [`Extraindo texto de arquivos .HTML com Langchain`](#extracting-html)
 - [`Extraindo conteúdo de arquivos .xlsx com Langchain`](#extracting-excel)
 - [`Despachando a extração de texto de forma segura no pipeline RAG`](#detfspr)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

No RAG, você nunca embeda arquivos (.pdf, .docx, etc.).

> **Você embeda texto puro.**

Portanto, antes de `chunking` e `embeddings`, precisamos:

 - Abrir o arquivo físico
 - Extrair o texto corretamente (dependendo do tipo)
 - Retornar texto limpo
 - ⚠️ Garantir que nenhum dado de outro usuário entre no processo

















































---

<div id="installing-dependencies">

## `Instalando as bibliotecas necessárias`

Antes de começar as implementações, vamos *instalar* e *exportar* as bibliotecas necessárias:

> **⚠️ NOTE:**  
> Essas instalações devem ser feitas dentro do container e de lá nós exportamos as dependências para o `requirements.txt`.

```bash
poetry add langchain@latest
```

```bash
poetry add langchain-community@latest
```

```bash
poetry add  langchain-core@latest
```

```bash
poetry add pypdf@latest
```

```bash
poetry add beautifulsoup4@latest
```

```bash
poetry add docx2txt@latest
```

**A VERSÃO MAIS RECENTE ESTÁ DANDO CONFLITO COM O TASKIPY:**
```bash
poetry add "unstructured<0.21"
```

```bash
poetry add openpyxl@latest
```

```bash
poetry add networkx@latest
```

```bash
poetry add pandas@latest
```

```bash
poetry add msoffcrypto-tool@latest
```

Por fim, vamos exportar essas dependências para o `requirements.txt`:

```bash
poetry export \
--without-hashes \
--format=requirements.txt \
--output=requirements.txt
```















































---

<div id="extracting-txt"></div>

## `Extraindo conteúdo de arquivos .txt com Langchain`

> A função `extract_txt()` é responsável por carregar um arquivo `.txt` e convertê-lo em uma lista de objetos *Document* do LangChain, que é o formato nativo e ideal para pipelines de RAG.

> **Em termos simples:**  
> 👉 “Pegue um arquivo .txt do disco e transforme ele em Documents prontos para chunking, embeddings e busca semântica.”

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    TextLoader,
)
from langchain_core.documents import Document


def extract_txt(path: Path) -> List[Document]:

    loader = TextLoader(
        str(path),
        encoding="utf-8"
    )
    return loader.load()
```

#### `📘 Entendendo o retorno de extract_txt()`

```python
def extract_txt(path: Path) -> List[Document]:
    ...
```

> 👉 A assinatura já entrega uma pista importante:

```python
-> List[Document]
```

Ou seja:

* **não retorna um `Document`**
* **retorna uma LISTA de `Document`**

### `1️⃣ Por que `len(...) == 1` mas `docs[1]` dá erro?`

Imagine esse arquivo `example.txt`

```text
Olá mundo.
Esse é um arquivo TXT simples.
```

Agora você faz:

```python
docs = extract_txt(Path("example.txt"))

print(len(docs))
```

**OUTPUT:**
```text
1
```

Agora:

```python
docs[0]  # OK
docs[1]  # ❌ ERRO
```

**❌ Erro:**
```text
IndexError: list index out of range
```

> **Por quê?**

 - 📌 Porque a lista tem **1 elemento**:
   - Não significa que nós podemos iterar até o índice 1
 - 📌 E listas em Python começam em **0**:
   - Ou seja, só podemos ir até o índice 0

| Índice    | Existe? |
| --------- | ------- |
| `docs[0]` | ✅      |
| `docs[1]` | ❌      |

### `2️⃣ O que exatamente essa função retorna?`

Tipo real do retorno:

```python
type(docs)
```

**OUTPUT:**
```bash
<class 'list'>
```

Agora:

```python
type(docs[0])
```

**OUTPUT:**
```text
<class 'langchain.schema.document.Document'>
```

📌 Então temos:

```bash
List[Document]
```

> **O que é um `Document` no LangChain?**

Um `Document` é basicamente:

```python
Document(
    page_content="texto extraído",
    metadata={...}
)
```

### `3️⃣ Quais campos eu posso trabalhar?`

Campos principais do `Document`:

#### 🔹 `page_content`

O **texto puro** que será:

 - chunkado
 - embedado
 - enviado ao LLM

```python
docs[0].page_content
```

### Exemplo de saída:

```text
"Olá mundo.\nEsse é um arquivo TXT simples."
```


#### 🔹 `metadata`

Informações auxiliares sobre o documento.

```python
docs[0].metadata
```

### Saída típica:

```python
{
    'source': '/app/media/docs/example.txt'
}
```

### `4️⃣ Como manipular esse retorno?`

#### 🔹 Exemplo 1 — Iterar corretamente

Mesmo tendo só 1 item, **sempre trate como lista**:

```python
for doc in docs:
    print(doc.page_content)
```

#### 🔹 Exemplo 2 — Enriquecer metadata (muito comum em RAG)

```python
for doc in docs:
    doc.metadata["file_type"] = "txt"
    doc.metadata["user_id"] = 1
    doc.metadata["folder"] = "/workspace/docs"
```

Agora:

```python
docs[0].metadata
```

**OUTPUT:**
```python
{
    'source': '/app/media/docs/example.txt',
    'file_type': 'txt',
    'user_id': 1,
    'folder': '/workspace/docs'
}
```

> **NOTE:**  
> 🔥 Isso é ouro para **filtro por usuário no RAG**.

#### 🔹 Exemplo 3 — Criar múltiplos documentos manualmente

```python
from langchain.schema import Document

docs = [
    Document(page_content="Texto 1", metadata={"page": 1}),
    Document(page_content="Texto 2", metadata={"page": 2}),
]
```

### `5️⃣ O tamanho (`len`) pode mudar?`

✅ SIM — depende do loader

No seu caso (`TextLoader`):

```python
loader.load()
```

 - ➡️ **Sempre retorna uma lista com 1 `Document`**
 - ➡️ Mesmo que o TXT tenha 1 linha ou 1 milhão

> **NOTE:**  
>⚠️ Mas isso MUDA com outros loaders

#### Exemplo: `PyPDFLoader`

```python
loader = PyPDFLoader("arquivo.pdf")
docs = loader.load()
```

> 📌 Cada página vira um `Document`.

Exemplo de saída:

```text
len(docs) == 10
```

| Índice    | Conteúdo  |
| --------- | --------- |
| `docs[0]` | Página 1  |
| `docs[1]` | Página 2  |
| `docs[9]` | Página 10 |


















































---

<div id="extracting-pdf"></div>

## `Extraindo conteúdo de arquivos .pdf com Langchain`

> A função `extract_pdf()` é responsável por ler um *arquivo PDF* página por página e extrair todo o texto possível, retornando esse conteúdo como uma única string.

**NOTE:**  
Ela é usada no pipeline RAG quando o tipo de arquivo identificado é `.pdf`, permitindo que documentos PDF — que não são texto puro — possam ser transformados em texto indexável.

Porém, antes de começar a implementar essa função, primeiro nós vamos instalar a biblioteca `pdfplumber`:

```bash
poetry add pdfplumber
```

Agora, vamos atualizar os arquivos de dependências:

```bash
task exportdev
```

```bash
task exportprod
```

A nossa função `extract_pdf()` vai ficar da seguinte maneira:

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    PyPDFLoader,
)
from langchain_core.documents import Document


def extract_pdf(path: Path) -> List[Document]:
    loader = PyPDFLoader(str(path))
    return loader.load()
```

### `📘 Entendendo o retorno de extract_pdf()`

Assinatura importante:

```python
-> List[Document]
```

 - 📌 De novo: **sempre retorna uma lista de `Document`**
 - 📌 Mas **o tamanho dessa lista MUDA bastante aqui**


### `1️⃣ O que essa função retorna, de verdade?`

Tipo do retorno:

```python
docs = extract_pdf(Path("arquivo.pdf"))

type(docs)
```

**OUTPUT:**
```text
<class 'list'>
```

Agora:

```python
type(docs[0])
```

**OUTPUT:**
```bash
<class 'langchain_core.documents.Document'>
```

Resultado final:

```bash
List[Document]
```

### `2️⃣ Por que `len(docs)` pode ser 1, 10 ou 300?`

Regra fundamental do `PyPDFLoader`:

> **Cada página do PDF vira um `Document`**

Exemplo prático, PDF com 3 páginas:

```python
docs = extract_pdf(Path("contrato.pdf"))
print(len(docs))
```

**OUTPUT:**
```text
3
```

Agora os índices:

| Índice    | Conteúdo |
| --------- | -------- |
| `docs[0]` | Página 1 |
| `docs[1]` | Página 2 |
| `docs[2]` | Página 3 |

> **NOTE:**  
> 👉 Aqui **`docs[1]` EXISTE**, diferente do TXT.

PDF com 1 página:

```python
len(docs)
```

**OUTPUT:**
```bash
1
```

👉 Agora:

 - `docs[0]` ✅
 - `docs[1]` ❌ (`IndexError`)

> **NOTE:**  
> 📌 O tamanho depende *EXCLUSIVAMENTE* do número de páginas do PDF.

### `3️⃣ Quais campos existem em cada Document?`

Cada item da lista é assim:

```python
Document(
    page_content="texto da página",
    metadata={...}
)
```

#### 🔹 `page_content`

```python
docs[0].page_content
```

**OUTPUT:**
```bash
"CLÁUSULA PRIMEIRA – DO OBJETO
O presente contrato tem por objeto..."
```

📌 Isso é:

 - texto bruto da página
 - ainda **não chunkado**
 - ainda **não embedado**

#### 🔹 `metadata`

```python
docs[0].metadata
```

**OUTPUT:**
```python
{
    'source': '/app/media/docs/contrato.pdf',
    'page': 0
}
```

Campos padrão:

 - `source` → caminho do arquivo
 - `page` → número da página (**zero-based**)

> **NOTE:**  
> ⚠️ Página 1 do PDF = `page = 0`

### `4️⃣ Como manipular corretamente esse retorno?`

Forma CORRETA de iterar é nunca assumir uma quantidade fixa:

```python
for doc in docs:
    print(f"Página {doc.metadata['page']}")
    print(doc.page_content[:200])
```

### `5️⃣ Comparação direta: TXT vs PDF`

| Aspecto             | TXT (`TextLoader`)    | PDF (`PyPDFLoader`)    |
| ------------------- | --------------------- | ---------------------- |
| Retorno             | `List[Document]`      | `List[Document]`       |
| Quantidade inicial  | Sempre 1              | 1 por página           |
| Metadata padrão     | `source`              | `source`, `page`       |
| Uso de índice `[1]` | ❌ Quase sempre erro | ✅ Se houver +1 página |
| Ideal para RAG      | Sim                   | Sim (mais granular)    |

### `6️⃣ Erro comum (e como evitar)`

❌ Errado:

```python
docs[1]
```

✅ Correto:

```python
for doc in docs:
    process(doc)
```

Ou, se quiser a página 1 do PDF (segunda página):

```python
page_2 = next(
    doc for doc in docs if doc.metadata["page"] == 1
)
```


















































---

<div id="extracting-docx"></div>

## `Extraindo conteúdo de arquivos .docx com Langchain`

> A função `extract_docx()` é responsável por ler documentos do Microsoft Word (.docx) e extrair todo o texto contido nos parágrafos, retornando esse conteúdo como uma string única.

**NOTE:**  
Ela permite que arquivos `.docx`, muito comuns em ambientes corporativos, possam ser indexados e utilizados no pipeline RAG, assim como PDFs e arquivos de texto.

Porém, antes de começar a implementar essa função, primeiro nós vamos instalar a biblioteca `python-docx`:

```bash
poetry add python-docx
```

Agora, vamos atualizar os arquivos de dependências:

```bash
task exportdev
```

```bash
task exportprod
```

A nossa função `extract_docx()` vai ficar da seguinte maneira:

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    Docx2txtLoader,
)
from langchain_core.documents import Document


def extract_docx(path: Path) -> List[Document]:
    loader = Docx2txtLoader(str(path))
    return loader.load()
```

### `📘 Entendendo o retorno de extract_docx()`

Assinatura importante:

```python
-> List[Document]
```

 - 📌 De novo: **sempre retorna uma lista de `Document`**
 - 📌 Mas o **comportamento é diferente do PDF**

### `1️⃣ O que essa função retorna?`

Tipo real do retorno:

```python
docs = extract_docx(Path("relatorio.docx"))

type(docs)
```

**OUTPUT:**
```bash
<class 'list'>
```

```python
type(docs[0])
```

**OUTPUT:**
```bash
<class 'langchain_core.documents.Document'>
```

📌 Retorno final:

```bash
List[Document]
```

### `2️⃣ Quantos Document vêm nessa lista?`

Regra do `Docx2txtLoader`:

> **O arquivo DOCX inteiro vira UM único `Document`**.

Mesmo que:

 - tenha 20 páginas
 - tenha títulos, tabelas e parágrafos
 - tenha quebras de página

Exemplo prático de un `DOCX` grande:

```python
docs = extract_docx(Path("tese.docx"))
print(len(docs))
```

**OUTPUT:**
```text
1
```

Agora:

```python
docs[0]  # OK
docs[1]  # ❌ IndexError
```

> **NOTE:**  
> 📌 Comportamento **igual ao TXT**, **diferente do PDF**.

### `3️⃣ Quais campos existem no Document?`

Cada item é:

```python
Document(
    page_content="texto extraído do DOCX",
    metadata={...}
)
```

#### 🔹 `page_content`

```python
docs[0].page_content
```

**OUTPUT:**
```text
"RELATÓRIO FINAL\n\n1. INTRODUÇÃO\nEste documento tem como objetivo..."
```

Texto:

 - linearizado
 - sem noção de páginas
 - preserva parágrafos e quebras de linha

#### 🔹 `metadata`

```python
docs[0].metadata
```

**OUTPUT:**
```python
{
    'source': '/app/media/docs/relatorio.docx'
}
```

Diferente do PDF:

 - ❌ não há `page`
 - ❌ não há estrutura por seção
 - ✔️ apenas a origem

### `4️⃣ Como manipular corretamente?`

Iteração (mesmo com 1 item)

```python
for doc in docs:
    print(doc.page_content[:300])
```

### `5️⃣ O tamanho pode mudar depois?`

> ❌ No loader: NÃO

**SEMPRE:**
```python
len(docs) == 1
```

> ✅ Depois do splitter: SIM

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)
print(len(chunks))
```

**OUTPUT:**
```bash
42
```

 - 📌 DOCX grande → muitos chunks
 - 📌 DOCX pequeno → poucos chunks

### `6️⃣ Comparação direta: TXT × PDF × DOCX`

| Tipo | Loader           | Quantidade inicial | Metadata padrão  |
| ---- | ---------------- | ------------------ | ---------------- |
| TXT  | `TextLoader`     | 1                  | `source`         |
| PDF  | `PyPDFLoader`    | 1 por página       | `source`, `page` |
| DOCX | `Docx2txtLoader` | 1                  | `source`         |

### `7️⃣ Erros comuns (que você já está evitando)`

 - ❌ Assumir múltiplos documentos em DOCX
 - ❌ Acessar `docs[1]`
 - ❌ Não enriquecer metadata
 - ❌ Chunkar antes de padronizar metadata


















































---

<div id="extracting-html"></div>

## `Extraindo texto de arquivos .HTML com Langchain`

> A função `extract_html()` é responsável por ler um *arquivo HTML*, remover elementos que não representam conteúdo textual relevante (como scripts e estilos) e extrair apenas o texto visível, retornando tudo como uma string limpa.

A nossa função `extract_docx()` vai ficar da seguinte maneira:

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    BSHTMLLoader,
)
from langchain_core.documents import Document


def extract_html(path: Path) -> List[Document]:
    loader = BSHTMLLoader(str(path))
    return loader.load()
```

### `📘 Entendendo o retorno de extract_html()`

Assinatura importante:

```python
-> List[Document]
```

 - 📌 De novo: **sempre retorna uma lista de `Document`**
 - 📌 Mas **a quantidade e o conteúdo dependem da estrutura do HTML**

### `1️⃣ O que essa função retorna?`

Tipo do retorno:

```python
docs = extract_html(Path("pagina.html"))

type(docs)
```

**OUTPUT:**
```bash
<class 'list'>
```

```python
type(docs[0])
```

**OUTPUT:**
```bash
<class 'langchain_core.documents.Document'>
```

Resultado final:

**OUTPUT:**
```
List[Document]
```

### `2️⃣ Quantos Document vêm nessa lista?`

Regra do `BSHTMLLoader`:

> **Por padrão, o HTML inteiro vira UM `Document`**

Mesmo que o HTML tenha:

 - dezenas de `<section>`
 - múltiplos `<article>`
 - headers, footers, navbars

Exemplo simples de HTML básico:

```html
<html>
    <body>
        <h1>Título</h1>
        <p>Parágrafo 1</p>
        <p>Parágrafo 2</p>
    </body>
</html>
```

```python
docs = extract_html(Path("pagina.html"))
print(len(docs))
```

**OUTPUT:**
```bash
1
```

📌 Comportamento parecido com:

 - TXT
 - DOCX

### `3️⃣ O que vem dentro do Document?`

Cada item:

```python
Document(
    page_content="texto extraído do HTML",
    metadata={...}
)
```

#### 🔹 `page_content`

```python
docs[0].page_content
```

**OUTPUT:**
```text
"Título\n\nParágrafo 1\n\nParágrafo 2"
```

O loader:

 - remove tags HTML
 - ignora scripts e styles
 - lineariza o texto
 - preserva quebras lógicas

#### 🔹 `metadata`

```python
docs[0].metadata
```

**OUTPUT:**
```python
{
    'source': '/app/media/docs/pagina.html'
}
```

Igual a `TXT` e `DOCX`:

 - ❌ sem páginas
 - ❌ sem seções
 - ✔️ apenas origem

### `4️⃣ Como manipular corretamente?`

Iterar (mesmo com 1 item)

```python
for doc in docs:
    print(doc.page_content[:200])
```

### `5️⃣ O tamanho pode mudar?`

> ❌ No loader padrão: NÃO

```python
len(docs) == 1
```

> ✅ Depois do splitter: SIM

HTML geralmente **explode em chunks**, porque:

 - tem muito texto contínuo
 - pouca estrutura semântica explícita

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)
print(len(chunks))
```

**OUTPUT:**
```text
58
```

### `6️⃣ Ponto crítico: HTML é “barulhento”`

Problemas comuns:

 - menus
 - rodapés
 - breadcrumbs
 - textos repetidos

Exemplo ruim:

```text
Home | About | Contact
Copyright © 2025
```

> **NOTE:**  
> 👉 Isso vai para o embedding **se você não filtrar**.

### `7️⃣ Estratégias melhores (nível produção)`

> 🔥 Opção A — Pré-filtrar HTML

```python
loader = BSHTMLLoader(
    str(path),
    open_encoding="utf-8",
    features="lxml"
)
```

Ou usar um loader que permita:

 - selecionar tags
 - ignorar `<nav>`, `<footer>`

> 🔥 Opção B — Pós-processar `page_content`

```python
doc.page_content = clean_html_text(doc.page_content)
```

Removendo:

 - linhas muito curtas
 - textos repetidos
 - padrões inúteis

### `8️⃣ Comparação final (todos os loaders)`

| Tipo | Loader           | Docs iniciais | Metadata         |
| ---- | ---------------- | ------------- | ---------------- |
| TXT  | `TextLoader`     | 1             | `source`         |
| DOCX | `Docx2txtLoader` | 1             | `source`         |
| HTML | `BSHTMLLoader`   | 1             | `source`         |
| PDF  | `PyPDFLoader`    | 1 por página  | `source`, `page` |


















































---

<div id="extracting-excel"></div>

## `Extraindo conteúdo de arquivos .xlsx com Langchain`

> A função `extract_excel()` é responsável por carregar um arquivo `.xlsx` e convertê-lo em uma lista de objetos *Document* do LangChain, que é o formato nativo e ideal para pipelines de RAG.

A nossa função `extract_excel()` vai ficar da seguinte maneira:

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    UnstructuredExcelLoader,
)
from langchain_core.documents import Document


def extract_excel(path: Path) -> List[Document]:
    loader = UnstructuredExcelLoader(str(path))
    return loader.load()
```

### `📘 Entendendo o retorno de extract_html()`

Assinatura importante:

```python
-> List[Document]
```

 - 📌 De novo: **sempre retorna uma lista de `Document`**
 - 📌 **Mas o Excel é o loader mais variável em quantidade e estrutura**

### `1️⃣ O que essa função retorna?`

Tipo do retorno:

```python
docs = extract_excel(Path("dados.xlsx"))

type(docs)
```

**OUTPUT:**
```bash
<class 'list'>
```

```python
type(docs[0])
```

**OUTPUT:**
```bash
<class 'langchain_core.documents.Document'>
```

Resultado final:

**OUTPUT:**
```bash
List[Document]
```

### `2️⃣ Quantos Document vêm nessa lista?`

Regra do `UnstructuredExcelLoader`:

> **O Excel é dividido em múltiplos `Document` com base na estrutura interna**

Isso pode variar conforme:

 - número de abas (sheets)
 - quantidade de linhas
 - tipo de conteúdo (tabelas, texto, células vazias)


#### Exemplo 1 — Excel simples (1 aba)

| Nome | Idade |
| ---- | ----- |
| Ana  | 30    |
| João | 25    |

```python
docs = extract_excel(Path("pessoas.xlsx"))
print(len(docs))
```

**OUTPUT:**
```bash
1
```

> **NOTE:**  
> 📌 Tudo vira **um bloco textual**.

#### Exemplo 2 — Excel com várias abas

 - Aba 1: Clientes
 - Aba 2: Pedidos
 - Aba 3: Produtos

```python
len(docs)
```

**OUTPUT:**
```text
3
```

> **NOTE:**  
> 📌 **Cada aba pode virar um `Document`**.

#### Exemplo 3 — Excel grande e complexo

Planilha com:

 - 1 aba
 - 10.000 linhas

```text
len(docs) == 15
```

O loader pode:

 - quebrar por blocos
 - dividir por seções internas
 - gerar múltiplos documentos

> **NOTE:**  
> 👉 Não há garantia de quantidade fixa.

### `3️⃣ O que vem dentro de cada `Document`?`

Cada item é:

```python
Document(
    page_content="texto extraído da planilha",
    metadata={...}
)
```

#### 🔹 `page_content`

```python
docs[0].page_content
```

**OUTPUT:**
```bash
Sheet: Clientes

Nome | Idade
Ana  | 30
João | 25
```

Características:

 - tabela “linearizada” em texto
 - sem noção real de célula
 - perde fórmulas
 - perde tipos (número, data etc.)

> **NOTE:**  
> ⚠️ **Excel não é estruturado para LLM**, `é convertido à força`.

#### 🔹 `metadata`

```python
docs[0].metadata
```

**OUTPUT:**
```python
{
    'source': '/app/media/docs/dados.xlsx'
}
```

Às vezes inclui:

```python
{
    'source': '/app/media/docs/dados.xlsx',
    'sheet_name': 'Clientes'
}
```

(depende da versão do loader)

### `4️⃣ Como manipular corretamente?`

> 🔹 Nunca assuma posição fixa

**❌ Errado:**
```python
docs[0]
docs[1]
```

**✅ Correto:**
```python
for doc in docs:
    print(doc.page_content[:200])
```

### `5️⃣ O tamanho pode mudar?`

> **🔴 SIM — e muito.**

| Loader | Quantidade inicial |
| ------ | ------------------ |
| TXT    | Sempre 1           |
| DOCX   | Sempre 1           |
| HTML   | Sempre 1           |
| PDF    | 1 por página       |
| Excel  | ⚠️ Variável        |

**NOTE:**  
Excel é o **menos previsível** de todos.

> 🟢 Depois do splitter: muda ainda mais

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)
print(len(chunks))
```

**OUTPUT:**
```text
92
```

> **NOTE:**  
> 📌 Uma planilha grande pode gerar **centenas de chunks**.

### `6️⃣ Problemas clássicos com Excel no RAG`

 - ⚠️ Tabelas perdem semântica
 - ⚠️ Colunas ficam misturadas
 - ⚠️ Cabeçalhos se repetem
 - ⚠️ Dados numéricos não “explicam” nada sozinhos

Exemplo ruim para embedding:

```text
12 | 45 | 78
```

> **NOTE:**  
> Sem contexto, o LLM não entende nada.

### `7️⃣ Estratégias melhores (nível produção)`

> **🔥 Estratégia 1 — Converter tabela em frases**

Antes do embedding:

```text
O cliente Ana tem 30 anos.
O cliente João tem 25 anos.
```

Muito mais RAG-friendly.

> **🔥 Estratégia 2 — Enriquecer metadata por aba**

```python
doc.metadata["sheet"] = "Clientes"
```

Depois:

```python
filter={"sheet": "Clientes"}
```

### `8️⃣ Comparação FINAL de todos os loaders`

| Tipo  | Loader                    | Docs iniciais | Previsibilidade |
| ----- | ------------------------- | ------------- | --------------- |
| TXT   | `TextLoader`              | 1             | Alta            |
| DOCX  | `Docx2txtLoader`          | 1             | Alta            |
| HTML  | `BSHTMLLoader`            | 1             | Média           |
| PDF   | `PyPDFLoader`             | 1 por página  | Média           |
| Excel | `UnstructuredExcelLoader` | ⚠️ Variável   | Baixa           |


















































---

<div id="detfspr"></div>

## `Despachando a extração de texto de forma segura no pipeline RAG`

> A função `extract_text()` é o ponto central de extração de conteúdo textual no *pipeline RAG*.

 - Ela recebe um arquivo já autorizado
 - Decide qual extractor usar com base no tipo do arquivo
 - Devolve o texto bruto pronto para *chunking* e *embeddings*.

Vamos começar:

 - Definindo uma função chamada `extract_text()`
 - Importando os módulos/funções que vamos usar

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
from pathlib import Path


def extract_text(file_info):
    ...
```

Agora, nós vamos converter o caminho absoluto (string) do arquivo recebido (`file_info`) em um objeto `Path` que irá facilitar operações de leitura de arquivos:

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
def extract_text(file_info):

    file_path = Path(file_info["absolute_path"])
```

 - **🔹 Função utilizada: `Path()`**
   - **O que faz?**
     - Cria um objeto de caminho de arquivo
   - **Quais parâmetros recebe?**
     - Uma string representando o caminho
   - **O que retorna?**
     - Um objeto `pathlib.Path`

Agora, nós vamos pegar a extensão do arquivo:

> **NOTE:**  
> 📌 Essa padronização foi garantida anteriormente por `get_file_type()`.

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
def extract_text(file_info):

    ...

    file_type = file_info["file_type"]
```

Agora, nós vamos criar vários `ifs (dispatcher)` para decidir qual tipo de arquivo vamos extrair:

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
def extract_text(file_info):

    ...

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
```

> **E se for passado um tipo que nós não validamos ainda?**

Nesse, caso nós vamos precisar lançar uma exceção para isso:

[rag/services/ingestion/text_extraction.py](../../../rag/services/ingestion/text_extraction.py)
```python
def extract_text(file_info):

    ...

    raise ValueError(f"Tipo de arquivo não suportado: {file_type}")
```

 - **🔹 O que isso faz?**
   - Interrompe a execução se o tipo não for reconhecido
   - Evita:
     - comportamentos inesperados
     - leitura de formatos não previstos

### `Testando manualmente`

O código para testar se está tudo ok com essas funções é o seguinte:

```python
from pathlib import Path
from pprint import pprint

from rag.services.ingestion.text_extraction import extract_text


BASE_DIR = Path(__file__).resolve().parent
SAMPLES_DIR = BASE_DIR / "data" / "samples"


def build_file_info(path: Path):
    return {
        "absolute_path": str(path.resolve()),
        "file_type": path.suffix.lower(),
    }


def test_file(path: Path):
    print(f"\n📄 Testando: {path.name}")

    file_info = build_file_info(path)

    try:
        documents = extract_text(file_info)

        print(f"✅ Total de documentos: {len(documents)}")

        for i, doc in enumerate(documents, start=1):
            print(f"\n--- Documento {i} ---")
            print("Metadata:")
            pprint(doc.metadata)
            print("\nConteúdo (primeiros 300 chars):")
            print(doc.page_content[:300])

    except Exception as e:
        print(f"❌ Erro: {e}")


if __name__ == "__main__":

    for file_path in SAMPLES_DIR.iterdir():
        if file_path.is_file():
            test_file(file_path)
```

**OUTPUT:**
```bash
📄 Testando: RAG.txt
✅ Total de documentos: 1

--- Documento 1 ---
Metadata:
{'source': '/code/data/samples/RAG.txt'}

Conteúdo (primeiros 300 chars):
Introdução à Computação Moderna, Inteligência Artificial e Sistemas Distribuídos

A computação moderna passou por diversas transformações significativas ao longo das últimas décadas. Desde os primeiros computadores de grande porte, utilizados apenas por governos e instituições acadêmicas, até os dis

📄 Testando: RAG.pdf
✅ Total de documentos: 2

--- Documento 1 ---
Metadata:
{'author': '(anonymous)',
 'creationdate': '2026-01-28T09:56:27+00:00',
 'creator': '(unspecified)',
 'keywords': '',
 'moddate': '2026-01-28T09:56:27+00:00',
 'page': 0,
 'page_label': '1',
 'producer': 'ReportLab PDF Library - www.reportlab.com',
 'source': '/code/data/samples/RAG.pdf',
 'subject': '(unspecified)',
 'title': '(anonymous)',
 'total_pages': 2,
 'trapped': '/False'}

Conteúdo (primeiros 300 chars):
Introdução à Computação Moderna, Inteligência
Artificial e Sistemas Distribuídos
A computação moderna passou por diversas transformações significativas ao longo das
últimas décadas. Desde os primeiros computadores de grande porte, utilizados apenas por
governos e instituições acadêmicas, até os disp

--- Documento 2 ---
Metadata:
{'author': '(anonymous)',
 'creationdate': '2026-01-28T09:56:27+00:00',
 'creator': '(unspecified)',
 'keywords': '',
 'moddate': '2026-01-28T09:56:27+00:00',
 'page': 1,
 'page_label': '2',
 'producer': 'ReportLab PDF Library - www.reportlab.com',
 'source': '/code/data/samples/RAG.pdf',
 'subject': '(unspecified)',
 'title': '(anonymous)',
 'total_pages': 2,
 'trapped': '/False'}

Conteúdo (primeiros 300 chars):
Sistemas de recuperação de informação têm como objetivo encontrar informações relevantes
em grandes conjuntos de dados. Tradicionalmente, utilizavam abordagens baseadas em
palavras-chave, mas hoje evoluíram para buscas semânticas.
RAG – Retrieval-Augmented Generation
Retrieval-Augmented Generation c

📄 Testando: RAG.html
✅ Total de documentos: 1

--- Documento 1 ---
Metadata:
{'source': '/code/data/samples/RAG.html',
 'title': 'Introdução à Computação Moderna, IA e Sistemas Distribuídos'}

Conteúdo (primeiros 300 chars):



Introdução à Computação Moderna, IA e Sistemas Distribuídos



Introdução à Computação Moderna, Inteligência Artificial e Sistemas Distribuídos

A computação moderna passou por diversas transformações significativas ao longo das últimas décadas. Desde os primeiros computadores de grande porte, ut

📄 Testando: RAG.docx
✅ Total de documentos: 1

--- Documento 1 ---
Metadata:
{'source': '/code/data/samples/RAG.docx'}

Conteúdo (primeiros 300 chars):
Introdução à Computação Moderna, Inteligência Artificial e Sistemas Distribuídos

A computação moderna passou por diversas transformações significativas ao longo das últimas décadas. Desde os primeiros computadores de grande porte, utilizados apenas por governos e instituições acadêmicas, até os dis

📄 Testando: RAG.xlsm
✅ Total de documentos: 1

--- Documento 1 ---
Metadata:
{'source': '/code/data/samples/RAG.xlsm'}

Conteúdo (primeiros 300 chars):
CONTROLE DE GÁS (AGOSTO)

1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 11.0 12.0 13.0 14.0 15.0 16.0 17.0 18.0 19.0 20.0 21.0 22.0 23.0 24.0 25.0 26.0 27.0 28.0 29 30.0 31.0 TOTAL POR ESCOLA Secretaria de Educação 0 Rafael Clementino 2.0 1.0 3 Celso Carneiro 1.0 1.0 1 3 Creche Tia Tida 1.0 1.0 1.0 3 Cre

📄 Testando: RAG.md
✅ Total de documentos: 1

--- Documento 1 ---
Metadata:
{'source': '/code/data/samples/RAG.md'}

Conteúdo (primeiros 300 chars):

# Introdução à Computação Moderna, Inteligência Artificial e Sistemas Distribuídos

A computação moderna passou por diversas transformações significativas ao longo das últimas décadas. Desde os primeiros computadores de grande porte, utilizados apenas por governos e instituições acadêmicas, até os
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
