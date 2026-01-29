# `Extraindo textos por tipo de arquivo`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Extraindo conteúdo de arquivos TXT e Markdown`](#extracting-txt-md)
 - [`Extraindo texto de arquivos PDF (extract_pdf)`](#extracting-pdf)
 - [`Extraindo texto de arquivos DOCX (extract_docx)`](#extracting-word)
 - [`Extraindo texto de arquivos HTML (extract_html)`](#extracting-html)
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

Portanto, antes de ``chunking`` e `embeddings`, precisamos:

 - Abrir o arquivo físico
 - Extrair o texto corretamente (dependendo do tipo)
 - Retornar texto limpo
 - ⚠️ Garantir que nenhum dado de outro usuário entre no processo


















































---

<div id="installing-dependencies">

## `Instalando as bibliotecas necessárias`

Antes de começar as implementações, vamos *instalar* e *exportar* as bibliotecas necessárias:

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
poetry add openpyxl@latest
```

```bash
poetry add xlrd@latest
```


















































---

<div id="extracting-txt"></div>

## `Extraindo conteúdo de arquivos .txt com Langchain`

> A função `extract_txt()` é responsável por carregar um arquivo `.txt` e convertê-lo em uma lista de objetos *Document* do LangChain, que é o formato nativo e ideal para pipelines de RAG.

> **Em termos simples:**  
> 👉 “Pegue um arquivo .txt do disco e transforme ele em Documents prontos para chunking, embeddings e busca semântica.”

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    TextLoader,
)
from langchain_core.documents import Document


def extract_txt(path: Path) -> List[Document]:
    """Extract text from a TXT file using LangChain."""
    loader = TextLoader(
        str(path),
        encoding="utf-8"
    )
    return loader.load()
```

 - **O que essa função faz?**
   - Lê um arquivo `.txt`
   - Usa o `TextLoader` do LangChain
   - Retorna uma lista de `Document`
   - Cada Document contém:
     - `page_content` → texto
     - `metadata` → informações do arquivo

Para entendermos melhor essa função, vamos utilizar ela para extrair o conteúdo de um arquivo `.txt`:

[rag/services/driver_text_extraction.py](../../rag/services/driver_text_extraction.py)
```python
from pathlib import Path

from text_extraction import extract_txt


# Caminho para o arquivo rag.txt
rag_path = Path("../../data/samples/RAG.txt")

# Extraindo os documentos
documents = extract_txt(rag_path)
```

Vamos começar entendendo qual o tipo da nossa variável `documents`, ou seja, o que foi retornado da função `extract_txt()`:

```python
print(f"Type: {type(documents)}")
```

**OUTPUT:**
```bash
Type: <class 'list'>
```

Ótimo, temos uma lista como retorno!

> **Mas qual o tamanho da nossa lista?**

```python
print(f"Length: {len(documents)}")
```

**OUTPUT:**
```bash
Length: 1
```

> **Hum.. Por que 1?**  

Porque nós estamos utilizando o `TextLoader`, e ele funciona assim:

> Um arquivo TXT inteiro = um único Document

**Resultado real:**
```bash
[
    Document(
        page_content="conteúdo completo do RAG.txt...",
        metadata={"source": ".../RAG.txt"}
    )
]
```

> **Poderia ser mais de 1 documento?**

Sim:

 - 1️⃣ Você faz chunking (mais comum em RAG)
 - 2️⃣ Loader que já divide o conteúdo
 - 3️⃣ Você mesmo cria vários Document

Vamos, ver o exemplo 3️⃣ na prática:

```python
from langchain_core.documents import Document

docs = [
    Document(
        page_content="Parte 1",
        metadata={}
    ),
    Document(
        page_content="Parte 2",
        metadata={}
    ),
    Document(
        page_content="Parte 3",
        metadata={}
    ),
]
```

**Resultado real:**
```bash
[
    <Document page_content='Parte 1' metadata={}>,
    <Document page_content='Parte 2' metadata={}>,
    <Document page_content='Parte 3' metadata={}>
]
```

**NOTE:**  
Então, pense comigo eu tenho uma lista como retorno da função `extract_txt()` e essa lista tem os atributos `page_content` e `metadata`.

> **Eu posso ver esses atributos individualmente?**  
> SIM!





```python

```

**OUTPUT:**
```bash

```




































---

<div id="extracting-pdf"></div>

## `Extraindo texto de arquivos PDF (extract_pdf)`

> A função `extract_pdf()` é responsável por ler um *arquivo PDF* página por página e extrair todo o texto possível, retornando esse conteúdo como uma única string.

**NOTE:**  
Ela é usada no pipeline RAG quando o tipo de arquivo identificado é `.pdf`, permitindo que documentos PDF — que não são texto puro — possam ser transformados em texto indexável.

Porém, antes de começar a implementar essa função, primeiro nós vamos instalar a biblioteca `pdfplumber`:

```bash
poetry add pdfplumber@latest
```

Agora, vamos atualizar os arquivos de dependências:

```bash
task exportdev
```

```bash
task exportprod
```

Ótimo, agora partindo para a implementação vamos importar a biblioteca `pdfplumber` e definir a função `extract_pdf(path: Path)`:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
import pdfplumber


def extract_pdf(path):
    ...
```

Continuando, agora nós vamos criar uma lista vazia para armazenar os textos das páginas:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_pdf(path):

    text_parts = []
```

 - **🔹 O que isso faz?**
   - Cria uma lista vazia para armazenar:
     - o texto extraído de cada página
 - **🔹 Por que usar uma lista?**
   - Strings são imutáveis em Python
   - Acumular em `lista + join()` é:
     - mais eficiente
     - mais limpo
     - mais performático

Agora, nós vamos utilizar `pdfplumber.open(path)` com `with` para abrir o PDF:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_pdf(path):

    text_parts = []

    with pdfplumber.open(path) as pdf:
        ...
```

 - **🔹 O que isso faz?**
   - Abre o arquivo PDF usando um context manager
   - Garante que o arquivo será fechado corretamente
 - **Função utilizada: `pdfplumber.open(path)`**
   - **O que faz?**
     - Abre um arquivo PDF para leitura
   - **Quais parâmetros recebe?**
     - `path` - Caminho do arquivo PDF
   - **O que retorna?**
     - Um objeto PDF do *pdfplumber*

Ótimo, sabendo que dentro desse bloco (with) nós teremos o PDF aberto, vamos iterar página por página:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_pdf(path):

    ...

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
```

 - **🔹 O que isso faz?**
   - Percorre todas as páginas do PDF
 - **🔹 Atributo utilizado: `pdf.pages`**
   - **O que é?**
     - Uma lista de objetos `Page`
     - Cada `Page` representa:
       - *uma página individual do PDF*

> **Mas o que fazer em cada página lida?**

Então, em cada página nós vamos:

 - **Extrair o texto da página atual:**
   - `page_text = page.extract_text()`
 - **Verificar se o texto extraído tem conteúdo, ou seja é diferente de `None`:**
   - `if page_text`
     - **Se ele for `True`, então adicionar o conteúdo na lista:**
       - `text_parts.append(page_text)`
     - **Se `page_text` for `None`, não adicionaremos nada na lista `text_parts`.**

Nosso código ficará assim:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_pdf(path):

    text_parts = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
```

Por fim, vamos retornar nossa lista, porém, juntando todos os textos das páginas separando por uma quebra de linha `(\n)`:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_pdf(path):

    ...

    return "\n".join(text_parts)
```


















































---

<div id="extracting-word"></div>

## `Extraindo texto de arquivos DOCX (extract_docx)`

> A função `extract_docx()` é responsável por ler documentos do Microsoft Word (.docx) e extrair todo o texto contido nos parágrafos, retornando esse conteúdo como uma string única.

**NOTE:**  
Ela permite que arquivos `.docx`, muito comuns em ambientes corporativos, possam ser indexados e utilizados no pipeline RAG, assim como PDFs e arquivos de texto.

Porém, antes de começar a implementar essa função, primeiro nós vamos instalar a biblioteca `python-docx`:

```bash
poetry add python-docx@latest
```

Agora, vamos atualizar os arquivos de dependências:

```bash
task exportdev
```

```bash
task exportprod
```

Ótimo, agora partindo para a implementação vamos importar o módulo `Document` e definir a função `extract_docx(path)`:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_docx(path):
```

 - **🔹 O que essa função faz?**
   - Abre um arquivo `.docx`
   - Extrai o texto de todos os parágrafos
   - Ignora parágrafos vazios
   - Retorna o texto consolidado
 - **🔹 O que ela retorna?**
   - Uma `str` com todo o texto do documento
   - Cada parágrafo separado por uma quebra de linha `(\n)`

Agora, nós vamos utilizar a função `Document(path)` para abrir o documento:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_docx(path):
    """Extract text from a DOCX file."""

    document = Document(path)
```

 - **🔹 O que essa linha faz?**
   - Carrega o arquivo `.docx` em memória
 - **🔹 Função utilizada: `Document()`**
   - **O que faz?**
     - Abre e interpreta um arquivo `.docx`
   - **Quais parâmetros recebe?**
     - `path` - Caminho do arquivo
   - **O que retorna?**
     - Um objeto `Document`, representando o documento Word

Continuando, agora nós vamos criar uma *list comprehension* para:

 - Percorre todos os parágrafos do documento
 - Extrai apenas o texto (`p.text`)
 - Ignora parágrafos vazios

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_docx(path):
    """Extract text from a DOCX file."""

    document = Document(path)
    paragraphs = [p.text for p in document.paragraphs if p.text]
```

Por fim, nós vamos juntar todos os parágrafos em uma string, separando-os por uma quebra de linha `(\n)` e enviar como retorno:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_docx(path):
    """Extract text from a DOCX file."""

    document = Document(path)
    paragraphs = [p.text for p in document.paragraphs if p.text]
    
    return "\n".join(paragraphs)
```


















































---

<div id="extracting-html"></div>

## `Extraindo texto de arquivos HTML (extract_html)`

> A função `extract_html()` é responsável por ler um *arquivo HTML*, remover elementos que não representam conteúdo textual relevante (como scripts e estilos) e extrair apenas o texto visível, retornando tudo como uma string limpa.

Porém, antes de começar a implementar essa função, primeiro nós vamos instalar a biblioteca `beautifulsoup4`:

```bash
poetry add beautifulsoup4@latest
```

Agora, vamos atualizar os arquivos de dependências:

```bash
task exportdev
```

```bash
task exportprod
```

Ótimo, agora partindo para a implementação vamos importar a biblioteca `BeautifulSoup` e definir a função `extract_html(path: Path)`:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
from bs4 import BeautifulSoup

def extract_html(path):
    ...
```

Continuando, agora nós vamos ler todo o arquivo HTML como texto e ignorar caracteres inválidos:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_html(path):

    html = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )
```

 - **🔹 Função utilizada: `Path.read_text()`**
   - **O que faz?**
     - Lê o conteúdo de um arquivo de texto
   - **Quais parâmetros recebe?**
     - `encoding="utf-8"` - Codificação
     - `errors="ignore"` - Ignora erros
   - **O que retorna?**
     - Uma `str` com o conteúdo do arquivo

> **NOTE:**  
> 📌 Essa abordagem garante robustez contra HTMLs malformados ou com encoding inconsistente.

Continuando, agora nós vamos converter o HTML em um objeto `BeautifulSoup`, que nada mais é que uma estrutura navegável de elementos HTML:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_html(path):

    ...

    soup = BeautifulSoup(
        html,
        "html.parser"
    )
```

 - **🔹 Função utilizada: `BeautifulSoup()`**
   - **O que faz?**
     - Analisa o HTML e cria uma árvore de nós
   - **Quais parâmetros recebe?**
     - `markup (str)` → HTML bruto
     - `parser (str)` → "html.parser"
   - **O que retorna?**
     - Um objeto *BeautifulSoup*

Agora, nós vamos remover `tags HTML` que nós consideramos irrelevantes, como `scripts` e `estilos`:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_html(path):

    ...

    for tag in soup(["script", "style"]):
        tag.decompose()
```

 - **🔹 O que esse bloco faz?**
   - Localiza todas as tags `<script>` e `<style>`
   - Remove completamente essas tags da árvore
 - `soup(["script", "style"])`
   - **O que faz?**
     - Busca todas as tags com esses nomes
   - **Quais parâmetros recebe?**
     - Uma lista de nomes de tags
   - **O que retorna?**
     - Uma lista de elementos encontrados
 - `tag.decompose()`
   - **O que faz?**
     - Remove a tag e todo o seu conteúdo da árvore
   - **Quais parâmetros recebe?**
     - Nenhum
   - **O que retorna?**
     - `None`

> **NOTE:**  
> 📌 Isso evita que códigos JavaScript, regras de CSS entrem no texto indexado.

Agora, nós vamos:

 - Extrair todo o texto visível do HTML
 - Separar por blocos de texto com quebras de linha (`\n`)
 - Por fim, enviar como retorno da função

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_html(path):

    ...

    return soup.get_text(separator="\n")
```

 - **🔹 Função utilizada: `soup.get_text()`**
   - **O que faz?**
     - Coleta todo o texto da árvore HTML
   - **Quais parâmetros recebe?**
     - `separator="\n"` - Define como os blocos de texto serão separados
   - **O que retorna?**
     - Uma `str` com o texto final


















































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

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
from pathlib import Path


def extract_text(file_info):
    ...
```

Agora, nós vamos converter o caminho absoluto (string) do arquivo recebido (`file_info`) em um objeto `Path` que irá facilitar operações de leitura de arquivos:

[rag/services/extraction.py](../../rag/services/extraction.py)
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

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_text(file_info):

    ...

    file_type = file_info["file_type"]
```

Agora, nós vamos criar vários `ifs (dispatcher)` para decidir qual tipo de arquivo vamos extrair:

[rag/services/extraction.py](../../rag/services/extraction.py)
```python
def extract_text(file_info):

    ...

    if file_type == ".txt":
        return extract_txt(file_path)

    if file_type == ".pdf":
        return extract_pdf(file_path)

    if file_type == ".docx":
        return extract_docx(file_path)

    if file_type == ".md":
        return extract_md(file_path)

    if file_type == ".html":
        return extract_html(file_path)
```

> **E se for passado um tipo que nós não validamos ainda?**

Nesse, caso nós vamos precisar lançar uma exceção para isso:

[rag/services/extraction.py](../../rag/services/extraction.py)
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

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
