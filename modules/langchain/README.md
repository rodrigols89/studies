# Aprenda a usar LangChain

> Minnhas **notas** e **códigos** do livro [Aprende a usar a LangChain](https://learning.oreilly.com/library/view/aprende-a-usar/9798341637917/)

## Conteúdo

 - **1. Fundamentos de LLM com LangChain:**
   - [`O que é ChatOpenAI?`](#intro-to-chatopenai)
   - [`Métodos de Execução de Runnables no LangChain`](#runnables-methods-langchain)
   - [`Método .invoke()`](#invoke-method)
   - [`Modelo de Mensagens de Conversa no LangChain`](#messages-in-langchain)
   - [`"Templates de Prompt" no LangChain`](#templates-in-langchain)
 - **RAG Parte I: Indexar os teus dados:**
   - [`RAG (Retrieval-Augmented Generation)`](#intro-to-rag)
   - [`Chunks (chunk_size)`](#intro-to-chunks)
   - [`Overlap (chunk_overlap)`](#intro-to-overlap)
   - [`O que são Incorporações de Texto? (Text Embeddings)`](#text-embeddings)
   - [`Carregadores de Documentos (Document Loaders) no LangChain`](#document-loaders)
   - [`Divisão de Texto (Text Splitters) no LangChain`](#text-splitters)
   - [`Gerando Texto Incorporado (Text Embeddings)`](#making-embeddings)
   - [`Indexação de Conhecimento (Indexing) no LangChain`](#chp02-indexing)
   - [`PGVector: Banco de Dados Vetorial com PostgreSQL no LangChain`](#chp02-pgvector)
   - [`Exemplo Completo — Usando PGVector com LangChain`](#chp02-pgvector-exemplo)
 - **Configurações:**
   - [`Criando o ambiente virtual`](#create-env)
<!---
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
- Different topic = "200" Whitespace character.
--->









































































































<!--- ( 1. Fundamentos de LLM com LangChainn ) --->

---

<div id="intro-to-chatopenai"></div>

## `O que é ChatOpenAI?`

ChatOpenAI é a classe do LangChain responsável por conversar com os chat models da OpenAI, como:

 - gpt-3.5-turbo
 - gpt-4
 - gpt-4o
 - gpt-4.1

Ela implementa a interface de Chat Models, ou seja:

 - Recebe mensagens (strings ou objetos de mensagem)
 - Envia para a API da OpenAI
 - Retorna uma resposta estruturada (não apenas texto cru)

### `Que pacote é esse "langchain_openai"?`

A partir do LangChain `0.1 → 0.2`, o projeto foi dividido em pacotes menores.

**Antes (antigo ❌):**
```python
from langchain.chat_models import ChatOpenAI
```

**Agora (correto ✅):**
```python
from langchain_openai.chat_models import ChatOpenAI
```

### `O que significa "chat_models"?`

Dentro do pacote langchain_openai, existem vários módulos:

```bash
langchain_openai/
 ├── llms/          → modelos antigos (completion)
 ├── chat_models/   → modelos de chat (messages)
 ├── embeddings/    → embeddings OpenAI
```

### `Parâmetros da classe ChatOpenAI`

Os principais (os mais usados) parâmetros da classe ChatOpenAI são:

 - `model`
   - Define qual modelo da OpenAI será usado.
   - Exemplos:
     - "gpt-3.5-turbo"
     - "gpt-4"
     - "gpt-4o"
     - "gpt-4.1"
 - `temperature`
   - Controla a criatividade da resposta.
   - 0.0 ➔	Determinístico
   - 0.2 ➔	Mais preciso
   - 0.7 ➔	Criativo
   - 1.0+ ➔	Muito criativo
 - `max_tokens`
   - Limita o número máximo de tokens gerados na resposta.
 - `timeout`
   - Timeout da requisição (em segundos).
   - Exemplo: timeout=60
 - `verbose`
   - Mostra logs internos do LangChain.
   - Exemplo: verbose=True

Por exemplo:

[chapter01/ChatOpenAI-v1.py](codes/chapter01/ChatOpenAI-v1.py)
```python
from langchain_openai.chat_models import ChatOpenAI

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=100,
)
```

No exemplo acima nós temos:

 - `model = ChatOpenAI()`
   - Criamos uma instância da classe ChatOpenAI.
 - `model="gpt-3.5-turbo"`
   - Estamos dizendo que esse modelo vai utilizar o modelo `"gpt-3.5-turbo"` da OpenAI.
 - `temperature=0`
   - Aqui estamos dizendo que queremos uma resposta determinística.
   - **NOTE:** Ou seja, a resposta vai ser sempre a mesma, mesmo se o modelo for criativo.
 - `max_tokens=100`
   - Limitamos o número de tokens gerados na resposta.




















---

<div id="runnables-methods-langchain"></div>

## `Métodos de Execução de Runnables no LangChain`

A classe **ChatOpenAI** herda de **BaseChatModel** e implementa a interface **Runnable**, o que permite executar o modelo de diferentes formas:

```bash
ChatOpenAI
   └── BaseChatModel
         └── Runnable
               ├── invoke()
               ├── batch()
               ├── stream()
               └── ainvoke()
```

Ou seja, todos esses métodos servem para executar o modelo, mudando apenas a forma de execução:

 - `.invoke()` → execução síncrona (mais comum)
 - `.ainvoke()` → execução assíncrona (async)
 - `.stream()` → resposta em streaming
 - `.batch()` → múltiplas entradas de uma vez

### `1️⃣ O que todos eles têm em comum?`

Todos:

 - Executam um Runnable (ChatOpenAI, chain, prompt, RAG, etc.)
 - Usam a mesma lógica interna
 - Recebem o mesmo tipo de entrada
 - Produzem o mesmo tipo de saída final

> **📌 A diferença está em:**  
> **como** e **quando** a resposta é entregue.

### `2️⃣ .invoke() — execução síncrona (padrão)`

**Quando usar:**

 - Código simples
 - Scripts
 - Notebooks
 - Fluxo linear

**Exemplo:**
```python
response = chat.invoke("Explain LangChain in one sentence.")
print(response.content)
```

**Características:**

 - Bloqueia até a resposta chegar
 - Retorna um único resultado

### `.batch() — múltiplas entradas de uma vez`

**Quando usar:**

 - Processar muitos prompts
 - Ganhar performance
 - Reduzir overhead

**Exemplo:**
```python
inputs = [
    "Explain LangChain in one sentence.",
    "What is RAG?",
    "What is LCEL?"
]

responses = chat.batch(inputs)

for r in responses:
    print(r.content)
```

**Características:**

 - Recebe list[input]
 - Retorna list[output]
 - Pode rodar em paralelo (dependendo do backend)

### `4️⃣ .stream() — resposta em streaming (token a token)`

**Quando usar:**

 - Chat em tempo real
 - Interfaces web
 - UX melhor

**Exemplo:**
```python
for chunk in chat.stream("Explain LangChain in one sentence."):
    print(chunk.content, end="", flush=True)
```

**Características:**

 - Retorna um gerador
 - Entrega partes da resposta conforme são geradas
 - Ideal para interfaces interativas

### `.ainvoke() — execução assíncrona (async)`

**Quando usar:**

 - FastAPI
 - Apps web
 - Alta concorrência

**Exemplo:**
```python
import asyncio

async def run():
    response = await chat.ainvoke("Explain LangChain in one sentence.")
    print(response.content)

asyncio.run(run())
```

**Características:**

 - Não bloqueia a thread
 - Requer async/await

### `6️⃣ Comparação direta`

| Método       | Execução   | Entrada | Saída      | Uso típico            |
| ------------ | ---------- | ------- | ---------- | --------------------- |
| `.invoke()`  | Síncrona   | 1 item  | 1 resposta | Scripts / notebooks   |
| `.batch()`   | Paralela   | Lista   | Lista      | Processamento em lote |
| `.stream()`  | Streaming  | 1 item  | Gerador    | Chat em tempo real    |
| `.ainvoke()` | Assíncrona | 1 item  | 1 resposta | Web / APIs            |

### `7️⃣ 🧠 Resumo final`

 - ✅ Sim, eles são similares no propósito
 - ❌ Não são iguais no comportamento

Todos fazem a mesma coisa:

> **➡️ executam um Runnable.**  
> *Mas cada um é ideal para um cenário específico.*




















---

<div id="invoke-method"></div>

## `Método .invoke()`

O método `.invoke()` é a forma padrão e moderna de **executar um modelo no LangChain**.

> **📌 Em termos simples:**  
> `.invoke()` envia uma entrada para o modelo e retorna uma resposta estruturada.

### `Parâmetros input=... do método .invoke()`

 - Esse é o mais importante.
 - Ele pode assumir 3 formas principais.

**Forma 1 — String simples (mais comum):** [chapter01/invoke-01.py](codes/chapter01/invoke-01.py)
```python
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=100,
)

response = model.invoke("The sky is")
print(response.content)
```

**OUTPUT:**
```bash
blue and clear, with fluffy white clouds scattered across the horizon. The sun is shining brightly, casting a warm glow over everything below. It's a beautiful day to be outside and enjoy the beauty of nature.
```

> **NOTE:**  
> 📌 Aqui o *LangChain* converte automaticamente a string em:  
> `HumanMessage(content="The sky is")`

**Forma 2 — Lista de mensagens (chat explícito):** [chapter01/invoke-02.py](codes/chapter01/invoke-02.py)
```python
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=100,
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain LangChain in one sentence.")
]

response = model.invoke(messages)
print(response.content)
```

**OUTPUT:**
```bash
LangChain is a blockchain platform that aims to facilitate cross-border communication and collaboration by providing language translation services.
```

**📌 Use isso quando precisar de:**

 - system
 - assistant
 - histórico de conversa

**Forma 3 — Dicionário (com Prompt Template / LCEL):** [chapter01/invoke-03.py](codes/chapter01/invoke-03.py)
```python
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one sentence."
)

chain = prompt | model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=100,
)

response = chain.invoke({"topic": "LangChain"})
print(response.content)
```

**OUTPUT:**
```bash
LangChain is a blockchain platform that aims to facilitate cross-border communication and collaboration by providing language translation services.
```

**📌 Aqui:**

 - `.invoke()` recebe um dict
 - O prompt resolve as variáveis antes de chamar o modelo

### `O que o método .invoke() retorna?`

Sempre retorna um objeto:

```bash
AIMessage
```

Exemplo real:

```bash
AIMessage(
    content="LangChain is a framework for building LLM-powered apps.",
    additional_kwargs={},
    response_metadata={
        "model": "gpt-3.5-turbo",
        "token_usage": {...}
    }
)
```

### `Diferença entre .invoke() e .predict() (importante)`

| Método       | Status                  |
| ------------ | ----------------------- |
| `.invoke()`  | ✅ Padrão atual        |
| `.predict()` | ⚠️ Legacy / deprecated |

### `Erros comuns (⚠️)`

**❌ Erro 1 — esperar string:**
```python
text = chat.invoke("Hello")
print(text)  # errado
```

**✅ Correto:**
```python
print(text.content)
```




















---

<div id="messages-in-langchain"></div>

## `Modelo de Mensagens de Conversa no LangChain`

Para que serve `langchain_core.messages`?

```python
from langchain_core.messages import ...
```

Esse módulo define o formato padrão de mensagens que o LangChain usa para representar uma conversa entre:

 - sistema
 - usuário
 - modelo
 - ferramentas

### `1️⃣ Por que isso é importante?`

Porque modelos de chat não recebem texto solto, eles recebem listas de mensagens com papéis:

```bash
System → Human → AI → Tool → Human → AI
```

Se você entende isso, você entende:

 - chat
 - memória
 - RAG
 - agentes
 - tool calling

### `2️⃣ Imports mais utilizados

 - `SystemMessage`
   - Define regras e comportamento do modelo.

```python
SystemMessage(content="You are a helpful assistant.")
```

 - `HumanMessage`
   - Representa a mensagem do usuário.

```python
HumanMessage(content="What is LangChain?")
```

 - `AIMessage`
   - Representa respostas do modelo (útil para histórico).

```python
AIMessage(content="LangChain is a framework...")
```

 - `ToolMessage`
   - Representa a saída de uma ferramenta (agents / tools).

```python
ToolMessage(
    content="Result from search",
    tool_call_id="abc123"
)
```

### `3️⃣ Exemplo mínimo completo`

[chapter01/messages-01.py](codes/chapter01/messages-01.py)
```python
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

messages = [
    SystemMessage(content="You are a tutor."),
    HumanMessage(content="Explain LangChain in one sentence.")
]

response = chat.invoke(messages)
print(response.content)
```

**OUTPUT:**
```bash
LangChain is a blockchain platform that enables developers to build decentralized language-oriented applications.
```

### `5️⃣ Regra de ouro 🧠`

> **LangChain** é sobre **orquestrar mensagens**, não strings.

Se você domina `langchain_core.messages`, você domina:

 - conversas
 - contexto
 - histórico




















---

<div id="templates-in-langchain"></div>

## `"Templates de Prompt" no LangChain`

Para que serve `langchain_core.prompts`?

```python
from langchain_core.prompts import ...
```

> **NOTE:**  
> 📌 Esse módulo **define como você constrói prompts de forma estruturada**, reutilizável e segura no LangChain.

Ele existe para:

 - evitar concatenação manual de strings
 - organizar variáveis de entrada
 - padronizar prompts
 - integrar prompts com modelos via LCEL

> **📌 Em resumo:**  
> Prompts deixam de ser texto solto e passam a ser componentes.

## `1️⃣ Por que isso é importante?`

> **Modelos de linguagem não recebem código**, **"recebem prompts bem formados"**.

Sem templates:

 - mais erro
 - mais duplicação
 - difícil de manter

Com templates:

 - clareza
 - reutilização
 - fácil integração com *chains* e *RAG*

### 2️⃣ Imports mais utilizados

 - `PromptTemplate`
   - Usado para modelos que recebem texto simples (LLMs).

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Translate {text} to Portuguese."
)
```

 - `ChatPromptTemplate`
   - Usado para modelos de chat.

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one sentence."
)
```

 - `MessagesPlaceholder`
   - Usado para injetar histórico de conversa dinamicamente.

```python
from langchain_core.prompts import MessagesPlaceholder

ChatPromptTemplate.from_messages([
    ("system", "You are a tutor."),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])
```

 - `HumanMessagePromptTemplate`
   - Define explicitamente um template de mensagem humana.
 - `SystemMessagePromptTemplate`
   - Define regras do sistema como template.

### `3️⃣ Exemplo mínimo completo`

[chapter01/prompts-01.py](codes/chapter01/prompts-01.py)
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain {topic} in one sentence.")
])

chain = prompt | ChatOpenAI()

response = chain.invoke({"topic": "LangChain"})
print(response.content)
```

**OUTPUT:**
```bash
LangChain is a decentralized platform that connects businesses with language service providers for efficient and secure translation services.
```

### `5️⃣ Regra de ouro 🧠`

 - Use **prompts** para **definir estrutura**.
 - Use **messages** para **controlar conversa**.







































































































<!--- ( RAG Parte I: Indexar os teus dados ) --->

---
























---

<div id="intro-to-rag"></div>

## `RAG (Retrieval-Augmented Generation)`

Retrieval‑Augmented Generation (RAG) é uma técnica que combina:

 - Recuperação de documentos (retrieval);
 - Com modelos geradores de linguagem (generation).

Em vez de confiar apenas no conhecimento “embutido” nos parâmetros do modelo, o RAG permite que o sistema vá buscar trechos de texto relevantes em uma base externa (por exemplo, Wikipedia, banco de documentos corporativos) e use essas informações para gerar respostas mais precisas e contextualizadas.

![img](images/rag-01.png)  

### `Quando utilizar RAG?`

 - **Base de conhecimento grande e em constante atualização:**
   - Documentações, FAQs, bases científicas.
 - **Domínios técnicos/especializados:**
   - Jurídico, médico, pesquisadores que exigem precisão e citações.
 - **Sistemas de suporte ao cliente:**
   - Chatbots que precisam referenciar manuais, políticas, termos de serviço.

### `Quando não utilizar RAG?`

 - **Tarefas de conversação livre:**
   - Bate‑papo informal, criação de conteúdo criativo onde não há necessidade de buscar fatos externos.
 - **Restrições de latência:**
   - Se seu sistema exige respostas em tempo real (<100 ms) e não comporta o tempo extra de recuperação.
 - **Ambientes com poucos dados:**
   - Se a base de documentos for pequena e autossuficiente, pode ser mais simples usar um LLM puro ou até finetuning.





















---

<div id="intro-to-chunks"></div>

## `Chunks (chunk_size)`

> Imagina que você precisa criar um *RAG* que utiliza a **Constituição Federal** para auxiliar advogados.

Se, para uma pergunta sobre **direito do consumidor**, enviarmos *toda a constituição*, isso fará com que o modelo de IA não consiga processar todas as informações, já que, quanto maior o prompt, **menos precisa tende a ser a resposta**.

Para isso, utilizamos a técnica de **"chunks"**, onde, pegamos um arquivo geral e o quebramos em vários pequenos trechos:

![img](images/chunks-01.png)  

> **NOTE:**  
> 📌 Podemos usar um `chunk_size` para especificar quantos caracteres teremos por **chunk**.

A *Constituição Federal* possui **64.488 palavras**. Se definirmos um `chunk_size` como **100**, teremos **645 mini arquivos (64.488÷100)** da Constituição.

### 🧾 Exemplos:

 - **Art. 1º** A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos...
 - **Parágrafo único.** Todo o poder emana do povo, que o exerce por meio de representantes eleitos ou diretamente, nos termos desta Constituição...
 - **Art. 2º** São Poderes da União, independentes e harmônicos entre si, o Legislativo, o Executivo e o Judiciário...





















---

<div id="intro-to-overlap"></div>

## `Overlap (chunk_overlap)`

**Mas agora enfrentamos outro problema:**  
Ao separar o texto por chunks, pode ser que eles **fiquem sem sentido**, já que partes importantes da informação podem ser **cortadas (separadas)**.

> **NOTE:**  
> 📌 Para isso, usamos o parâmetro `chunk_overlap`.

 - Ele define quantos caracteres de sobreposição haverá entre um chunk e o próximo.
 - 👉 Isso é útil para manter o contexto entre pedaços consecutivos.

Por exemplo, Exemplo com `chunk_size = 500` e `chunk_overlap = 100`

```bash
[000 ... 499]
[400 ... 899]
[800 ... 1299]
```

Vejam que:

 - **Nosso primeiro chunk começa em 000 e termina em 499:**
   - Ou seja, as primeiras 500 palavras da Constituição.
 - **Nosso segundo chunk começa em 400 (por causa do "chunk_overlap = 100") e termina em 899:**
   - Ou seja, ele está pegando as 100 últimas palavras do chunk anterior.
   - **NOTE:** Isso é importante para evitar perda de contexto entre os chunks.

Por exemplo, imagine que nós temos o seguinte texto:

```bash
Python é uma excelente linguagem de programação para web e IA.
```

Se aplicarmos:

 - `chunk_size = 7`
 - `chunk_overlap = 3`

Vamos ter:

```bash
Python é uma excelente linguagem de programação para web e IA.
   |   |  |      |         |     |       |
   0   1  2      3         4     5       6
   ---------------------------------------
                chunk 1


Python é uma excelente linguagem de programação para web e IA.
                           |     |       |       |    |  |  |
                           1     2       3       4    5  6  7
                           -----------------------------------
                                        chunk 2
```

> **NOTE:**  
> 📌 Vejam que nós pegamos as **3 últimas palavras do chunk (overlap = 3)** para não perde contexto.





















---

<div id="text-embeddings"></div>

## `O que são Incorporações de Texto? (Text Embeddings)`

> As **incorporações de texto** são uma forma de **converter palavras ou frases do texto em dados numéricos que uma máquina pode entender**.

 - Pense nisso como se estivesse transformando o texto em uma lista de números, em que cada número captura uma parte do significado do texto.
 - Essa técnica ajuda as máquinas a entender o contexto e as relações entre as palavras.

![img](images/embeddings-01.png)  





















---

<div id="document-loaders"></div>

## `Carregadores de Documentos (Document Loaders) no LangChain`

Para que serve `langchain_community.document_loaders`?

```python
from langchain_community.document_loaders import ...
```

Esse módulo reúne **carregadores de documentos (document loaders)**, ou seja, classes responsáveis por:

 - ler arquivos ou fontes externas (PDF, TXT, CSV, HTML, URLs, etc.)
 - extrair o conteúdo
 - converter tudo para o formato padrão do LangChain: `Document`

> **📌 Em RAG, tudo começa aqui.**  
> Se o dado não foi carregado corretamente, o resto do pipeline falha.

### `1️⃣ O que é um Document?`

Todo *loader* retorna uma lista de objetos `Document`:

```python
Document(
    page_content="texto extraído",
    metadata={"source": "..."}
)
```

Esse formato é usado depois por:

 - text splitters
 - embeddings
 - vector stores
 - retrievers

### `2️⃣ Imports mais utilizados`

 - `TextLoader`
   - Carrega arquivos `.txt`

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/example.txt")
documents = loader.load()
```

> **📌 Uso comum:**  
> logs, textos simples, dumps.

 - `PyPDFLoader`
   - Extrai texto de arquivos PDF (página por página).

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/manual.pdf")
documents = loader.load()
```

> **NOTE:**  
> 📌 Cada página vira um Document.

 - `CSVLoader`
   - Lê arquivos .csv.

```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="data/users.csv",
    source_column="email"
)
documents = loader.load()
```

> **NOTE:**  
> 📌 Cada linha vira um Document.

 - `JSONLoader`
   - Carrega dados estruturados em `JSON`.

```python
from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="data/data.json",
    jq_schema=".items[]",
    text_content=False
)
documents = loader.load()
```

> **NOTE:**  
> 📌 Muito usado com APIs e dumps de dados.

 - `UnstructuredFileLoader`
   - Loader genérico para vários formatos.

```python
from langchain_community.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("data/report.docx")
documents = loader.load()
```

**📌 Funciona com:**

 - `.docx`
 - `.pptx`
 - `.html`
 - `.md`

 - `WebBaseLoader`
   - Carrega conteúdo direto de URLs.

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.langchain.com/")
documents = loader.load()
```

> **NOTE:**  
> 📌 Muito usado para *RAG* com *documentação online*.

 - `DirectoryLoader`
   - Carrega vários arquivos de uma pasta.

```python
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    "data/",
    glob="**/*.pdf"
)
documents = loader.load()
```

> **NOTE:**  
> 📌 Essencial para bases grandes de documentos.

### `Documentação do "Document loaders"`

> Aqui -> [Document loaders](https://docs.langchain.com/oss/python/integrations/document_loaders)





















---

<div id="text-splitters"></div>

## `Divisão de Texto (Text Splitters) no LangChain`

1️⃣ Para que serve langchain_text_splitters?

```python
from langchain_text_splitters import ...
```

Esse módulo contém os **Text Splitters**, responsáveis por **quebrar documentos grandes em pedaços menores (chunks)**.

📌 Isso é essencial porque:

 - LLMs têm limite de tokens
 - embeddings funcionam melhor com textos menores
 - buscas vetoriais ficam mais precisas

> **NOTE:**  
> 📌 Em *RAG*, o `splitter` é o coração da qualidade.

### `2️⃣ O problema que ele resolve`

 - **Sem splitter ❌:**
   - texto grande demais
   - perda de contexto
   - embeddings ruins
 - **Com splitter ✅:**
   - chunks consistentes
   - contexto preservado
   - melhor recuperação

### `3️⃣ Imports mais utilizados`

 - `RecursiveCharacterTextSplitter (mais usado)`
   - Divide texto de forma inteligente, tentando manter estrutura.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)
```

Parâmetros principais:

 - `chunk_size` → tamanho do chunk
 - `chunk_overlap` → sobreposição entre chunks
 - `separators` → lista de separadores (opcional)

> **NOTE:**  
> 📌 Padrão para RAG com texto natural.

 - `CharacterTextSplitter`
   - Divide texto de forma simples e direta.

```python
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=300,
    chunk_overlap=30
)
```

Parâmetros:

 - `separator` → caractere de divisão (\n, .)
 - `chunk_size`
 - `chunk_overlap`

> **NOTE:**  
> 📌 Bom para textos bem estruturados.

 - `TokenTextSplitter`
   - Divide baseado em tokens, não caracteres.

```python
from langchain_text_splitters import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=256,
    chunk_overlap=25
)
```

Parâmetros:

 - `chunk_size` → tokens por chunk
 - `chunk_overlap`
 - `encoding_name` → tokenizer (ex: "cl100k_base")

> **NOTE:**  
> 📌 Ideal quando você precisa respeitar limite exato de tokens.

### `4️⃣ Regra de ouro 🧠`

Escolha o `splitter` de acordo com o tipo de dado, não por moda.

 - texto livre → `RecursiveCharacterTextSplitter`
 - tokens exatos → `TokenTextSplitter`
 - markdown → `MarkdownTextSplitter`
 - HTML → `HTMLTextSplitter`





















---

<div id="making-embeddings"></div>

## `Gerando Texto Incorporado (Text Embeddings)`

O LangChain tem várias API para se trabalhar com Textos Incorporados (Text Embeddings) e vocês podem escolhar qualquer um deles de acordo com a sua necessidade.

> Aqui está a documentação oficial -> [Embedding models](https://docs.langchain.com/oss/python/integrations/text_embedding)

Por exemplo, vamos utilizar a classe `OpenAIEmbeddings` da OpenAI:

[chapter02/text-embeddings-01.py](codes/chapter02/text-embeddings-01.py)
```python
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings()

embeddings = model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!",
    ]
)
```

Se você desse um print() o resultado seria algo parecido com isso (não vou mostrar porque é muito grande):

**OUTPUT:**
```bash
[
  [
    -0.004845875, 0.004899438, -0.016358767, -0.024475135, -0.017341806,
      0.012571548, -0.019156644, 0.009036391, -0.010227379, -0.026945334,
      0.022861943, 0.010321903, -0.023479493, -0.0066544134, 0.007977734,
    0.0026371893, 0.025206111, -0.012048521, 0.012943339, 0.013094575,
    -0.010580265, -0.003509951, 0.004070787, 0.008639394, -0.020631202,
    ... 1511 more items
  ]
  [
      -0.009446913, -0.013253193, 0.013174579, 0.0057552797, -0.038993083,
      0.0077763423, -0.0260478, -0.0114384955, -0.0022683728, -0.016509168,
      0.041797023, 0.01787183, 0.00552271, -0.0049789557, 0.018146982,
      -0.01542166, 0.033752076, 0.006112323, 0.023872782, -0.016535373,
      -0.006623321, 0.016116094, -0.0061090477, -0.0044155475, -0.016627092,
    ... 1511 more items
  ]
  ... 3 more items
]
```





















---

<div id="chp02-indexing"></div>

## `Indexação de Conhecimento (Indexing) no LangChain (+Indexing vs. Retrieval)`

### `1️⃣ O que é Indexing no LangChain?`

> O termo `Indexing` se refere ao processo de **transformar dados brutos (documentos)** em uma estrutura **pesquisável por similaridade semântica**.

Em termos práticos, é quando você:

 - carrega documentos
 - divide em chunks
 - gera embeddings
 - armazena tudo em um Vector Store

> **NOTE:**  
> 📌 Sem `indexação`, não existe *RAG*.

### `2️⃣ Por que a indexação é necessária?`

LLMs:

 - não “lembram” de documentos
 - não pesquisam sozinhas
 - não acessam arquivos diretamente

> **NOTE:**  
> 📌 A `indexação` *cria uma memória externa consultável*.

### `3️⃣ Fluxo completo de Indexing`

No processo de indexação, o LangChain segue o seguinte fluxo:

```bash
Dados brutos
   ↓
DocumentLoader
   ↓
TextSplitter
   ↓
Embeddings
   ↓
VectorStore (Index)
```

> **NOTE:**  
> 📌 O resultado final é o índice vetorial.

### `4️⃣ Exemplo mínimo de indexação`

**Passo 1 — Carregar documentos:**
```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/manual.txt")
documents = loader.load()
```

**Passo 2 — Dividir o texto:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)
```

**Passo 3 — Gerar embeddings:**
```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
```

**Passo 4 — Criar o índice (Vector Store):**
```python
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)
```

> **NOTE:**  
> 📌 Aqui nasce o índice.

### `5️⃣ Consultando o índice (busca semântica)`

> Porém, ainda falta fazer a consulta semântica nesse índice.

Para isso nós vamos utilizar o conceito de **"Text Similarity"**:

```python
results = vectorstore.similarity_search(
    "How does indexing work?",
    k=3
)

for doc in results:
    print(doc.page_content)
```

### `6️⃣ Indexing vs Retrieval`

| Conceito    | Quando acontece | O que faz         |
| ----------- | --------------- | ----------------- |
| `Indexing`  | Antes do uso    | Cria o índice     |
| `Retrieval` | Em runtime      | Consulta o índice |

### `7️⃣ Persistindo e Carregando o índice`

> Nós também precisamos persistir e carregar o índice de algum Banco de Dados.

**Persistindo o índice:**
```python
vectorstore.save_local("faiss_index")
```

**Carregando o índice:**
```python
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)
```





















---

<div id="chp02-pgvector"></div>

## `PGVector: Banco de Dados Vetorial com PostgreSQL no LangChain`

### `1️⃣ O que é PGVector?`

PGVector é uma extensão do PostgreSQL que permite armazenar e buscar embeddings (vetores) diretamente no banco de dados.

**📌 Em outras palavras:**

> PostgreSQL + vetores = Vector Store persistente e robusto

### `2️⃣ Por que PGVector entra nesse contexto?`

Até agora nós vimos:

```bash
DocumentLoader
→ TextSplitter
→ Embeddings
→ VectorStore
```

O `PGVector` é o `VectorStore` — só que:

 - persistente
 - escalável
 - SQL
 - pronto para produção

> **NOTE:**  
> 📌 Diferente de FAISS (memória/local), o PGVector vive em um banco real.

### `3️⃣ Criando um container docker com PGVector`

```bash
docker run \
    --name pgvector \
    -e POSTGRES_USER=lcuser \
    -e POSTGRES_PASSWORD=lcpass \
    -e POSTGRES_DB=lcdb \
    -p 6024:5432 \
    -d pgvector/pgvector:pg16
```

 - `docker run`
   - Inicia um container Docker.
 - `--name pgvector`
   - Define o nome do container como pgvector.
   - Facilita: *"docker ps"*, *"docker stop pgvector"*
 - `-e POSTGRES_USER=lcuser`
 - `-e POSTGRES_PASSWORD=lcpass`
 - `-e POSTGRES_DB=lcdb`
   - Variáveis de ambiente do PostgreSQL
   - Criam automaticamente:
     - `POSTGRES_USER` -> usuário: langchain
     - `POSTGRES_PASSWORD` -> senha: langchain
     - `POSTGRES_DB` -> banco: langchain
 - `-p 6024:5432`
   - Mapeamento de porta
   - 5432 → porta interna do PostgreSQL no container
   - 6024 → porta acessível na sua máquina
   - Conexão externa:
     - *postgresql://langchain:langchain@localhost:6024/langchain*
 - `-d`
   - Roda o container em background.
 - `pgvector/pgvector:pg16`
   - Isso é:
     - PostgreSQL 16
     - extensão pgvector já instalada
   - 📌 Você não precisa instalar nada manualmente. 

### `4️⃣ O que acontece quando esse container sobe?`

Internamente, o PostgreSQL:

 - inicia normalmente
 - ativa a extensão pgvector
 - fica pronto para criar colunas do tipo vector

Exemplo SQL real:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### `5️⃣ Como o PGVector armazena embeddings?`

Cada embedding vira algo assim:

```sql
vector(1536)
```

Onde:

 - 1536 = dimensão do embedding (OpenAI small)

📌 Um registro típico:

```bash
id | content | embedding | metadata
```





















---

<div id="chp02-pgvector-exemplo"></div>

## `Exemplo Completo — Usando PGVector com LangChain`

**📦 Pré-requisitos:**

 - Container do PGVector rodando (o Docker que você já subiu)
 - Variável de ambiente OPENAI_API_KEY configurada
 - Pacotes instalados:
   - `pip install langchain langchain-community langchain-openai psycopg2-binary`

Vamos começar criando uma instância de `load_dotenv()` que vai ser responsável por carregar as variáveis de ambiente:

[chapter02/pgvector-01.py](codes/chapter02/pgvector-01.py)
```python
from dotenv import load_dotenv

load_dotenv()
```

Continuando, agora vamos implementar a **String de Conexão com PostgreSQL (PGVector) no LangChain**:

[chapter02/pgvector-01.py](codes/chapter02/pgvector-01.py)
```python
CONNECTION_STRING = (
    "postgresql+psycopg2://"
    "lcuser:lcpass@localhost:6024/lcdb"
)
```

 - `postgresql`
   - Define o tipo de banco de dados.
   - O LangChain usa isso para saber:
     - que é PostgreSQL
     - que suporta pgvector
 - `+psycopg2`
   - Define o driver Python usado para conectar ao banco.
   - Por quê?
     - PostgreSQL não fala Python diretamente
     - o driver faz essa ponte
   - Biblioteca necessária:
     - `pip install psycopg2-binary`
 - `://`
   - Separador padrão entre:
     - tipo de conexão
     - credenciais
 - `lcuser:lcpass`
   - Credenciais -> username:password
   - Isso vem diretamente do Docker:
     - `-e POSTGRES_USER=lcuser`
     - `-e POSTGRES_PASSWORD=lcpass`
 - `@localhost`
   - Define **onde o banco está rodando**.
   - localhost → sua máquina
   - poderia ser:
     - IP
     - nome do container
     - hostname de produção
 -  `:6024`
   - Porta externa mapeada pelo Docker:
     - `-p 6024:5432`
     - 📌 Importante:
       - 5432 → porta interna do PostgreSQL
       - 6024 → porta que você acessa
 - `/lcdb`
   - Nome do banco de dados.
   - Criado automaticamente pelo Docker:
     - `-e POSTGRES_DB=lcdb`

Ótimo, agora vamos implementar um `loader de arquivos` de texto que vai ler um arquivo `.txt`:

[chapter02/pgvector-01.py](codes/chapter02/pgvector-01.py)
```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/example.txt")
```

> **O que tem na variável `loader`?**

```python
loader = TextLoader("data/example.txt")
print(loader)
print(type(loader))
```

**OUTPUT:**
```bash
<langchain_community.document_loaders.text.TextLoader object at 0x7fed2d540890>
<class 'langchain_community.document_loaders.text.TextLoader'>
```

Vejam que nós temos apenas objetos da classe `langchain_community.document_loaders.text.TextLoader`.

> **E como eu acesso meus dados? (Meu texto em `data/example.txt`)?**

Para isso nós precisamos utilizar o método `load()` da classe `TextLoader` que é responsável por ler o arquivo:

[chapter02/pgvector-01.py](codes/chapter02/pgvector-01.py)
```python
loader = TextLoader("data/example.txt")
text = loader.load()

print("\nType:", type(text))
print("\nContent:", text)
```

**OUTPUT:**
```bash
Type: <class 'list'>

Content: [Document(metadata={'source': 'data/example.txt'}, page_content='LangChain is a framework designed to simplify the development of applications powered by large language models (LLMs).\n\nIt provides building blocks for common use cases such as chatbots, question answering systems, and retrieval-augmented generation (RAG).\n\nOne of the core ideas of LangChain is to connect language models with external data sources.\n\nThis is achieved by loading documents, splitting them into smaller chunks, generating embeddings, and storing them in vector databases.\n\nVector databases allow semantic search, meaning that queries are matched based on meaning rather than exact keywords.\n\nPGVector is a PostgreSQL extension that enables storing and searching vector embeddings directly in a relational database.\n\nUsing PGVector with LangChain allows developers to build production-ready RAG systems with persistence, scalability, and SQL support.\n\nIndexing is the process of transforming raw documents into searchable vector representations.\n\nRetrieval is the process of querying those vectors to find the most relevant information for a user question.\n')]
```

Ótimo, vejam que agora nós temos:

 - **Um objeto lista:**
   - `<class 'list'>`
 - **Uma tupla `Document()`:**
   - Representando um único documento.
   - Essa tupla tem os seguintes campos:
     - `page_content`
     - `metadata`

Por exemplo, vamos ver o conteúdo (`page_content`) e os metadados (`metadata`) do nosso documento (`Document`):

```python
for index, document in enumerate(text):
    print(f"\n------------ Document {index} ------------")
    print("\n[PAGE CONTENT]\n", document.page_content)
    print("\[nMETADATA]\n", document.metadata)
```

**OUTPUT:**
```bash
------------ Document 0 ------------

[PAGE CONTENT]
 LangChain is a framework designed to simplify the development of applications powered by large language models (LLMs).

It provides building blocks for common use cases such as chatbots, question answering systems, and retrieval-augmented generation (RAG).

One of the core ideas of LangChain is to connect language models with external data sources.

This is achieved by loading documents, splitting them into smaller chunks, generating embeddings, and storing them in vector databases.

Vector databases allow semantic search, meaning that queries are matched based on meaning rather than exact keywords.

PGVector is a PostgreSQL extension that enables storing and searching vector embeddings directly in a relational database.

Using PGVector with LangChain allows developers to build production-ready RAG systems with persistence, scalability, and SQL support.

Indexing is the process of transforming raw documents into searchable vector representations.

Retrieval is the process of querying those vectors to find the most relevant information for a user question.


[METADATA]
 {'source': 'data/example.txt'}
```

Continuando na nossa implementação vamos dividir os dados do nosso arquivo `.txt` em 500 palavras (chunk_size=500) com 50 palavras de overlap (chunk_overlap=50):

[chapter02/pgvector-01.py](codes/chapter02/pgvector-01.py)
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

> **O que tem na variável `splitter`?**

```python
print(splitter)
print(type(splitter))
```

**OUTPUT:**
```bash
<langchain_text_splitters.character.RecursiveCharacterTextSplitter object at 0x751f76613170>
<class 'langchain_text_splitters.character.RecursiveCharacterTextSplitter'>
```

 - Novamente, temos objetos LangChain, `langchain_text_splitters.character.RecursiveCharacterTextSplitter` nesse caso.
 - Bem, se nós temos objetos eles tem (ou podem ter) métodos e nós podemos utilizar esses métodos.
 - A classe `RecursiveCharacterTextSplitter` tem o método `split_documents()` que divide os dados em chunks:

> **NOTE:**  
> 📌 Lembrando que quando nós criamos uma instância de `RecursiveCharacterTextSplitter()` nós definimos a quantidade de pedaços (chunks) e a quantidade de overlap (chunk_overlap).

[chapter02/pgvector-01.py](codes/chapter02/pgvector-01.py)
```python
chunks = splitter.split_documents(text)
```

> **O que tem na variável `chunks`?**

```python
print("\nType:", type(chunks))
print("\nContent:", chunks)
```

**OUTPUT:**
```bash
Type: <class 'list'>

Content: [Document(metadata={'source': 'data/example.txt'}, page_content='LangChain is a framework designed to simplify the development of applications powered by large language models (LLMs).\n\nIt provides building blocks for common use cases such as chatbots, question answering systems, and retrieval-augmented generation (RAG).\n\nOne of the core ideas of LangChain is to connect language models with external data sources.\n\nThis is achieved by loading documents, splitting them into smaller chunks, generating embeddings, and storing them in vector databases.'), Document(metadata={'source': 'data/example.txt'}, page_content='Vector databases allow semantic search, meaning that queries are matched based on meaning rather than exact keywords.\n\nPGVector is a PostgreSQL extension that enables storing and searching vector embeddings directly in a relational database.\n\nUsing PGVector with LangChain allows developers to build production-ready RAG systems with persistence, scalability, and SQL support.\n\nIndexing is the process of transforming raw documents into searchable vector representations.'), Document(metadata={'source': 'data/example.txt'}, page_content='Retrieval is the process of querying those vectors to find the most relevant information for a user question.')]
```

> **Ué, é a mesma coisa que o nosso `text = loader.load()` tem?**  
> Não, não!

 - **Primeiro, se vocês prestarem atenção verão que nós temos 3 objetos `Document()`:**
   - Lembram que nós definimos 500 palavras por divisão (chunk_size)?
   - Então, cada `Document()` tem 500 palavras.

Por exemplo, vamos ver separadamente esses `Document()`:

```python
for index, document in enumerate(chunks):
    print(f"\n------------ Document {index} ------------")
    print("\n[PAGE CONTENT]\n", document.page_content)
    print("\n[METADATA]\n", document.metadata)
```

**OUTPUT:**
```bash
------------ Document 0 ------------

[PAGE CONTENT]
 LangChain is a framework designed to simplify the development of applications powered by large language models (LLMs).

It provides building blocks for common use cases such as chatbots, question answering systems, and retrieval-augmented generation (RAG).

One of the core ideas of LangChain is to connect language models with external data sources.

This is achieved by loading documents, splitting them into smaller chunks, generating embeddings, and storing them in vector databases.

[METADATA]
 {'source': 'data/example.txt'}

------------ Document 1 ------------

[PAGE CONTENT]
 Vector databases allow semantic search, meaning that queries are matched based on meaning rather than exact keywords.

PGVector is a PostgreSQL extension that enables storing and searching vector embeddings directly in a relational database.

Using PGVector with LangChain allows developers to build production-ready RAG systems with persistence, scalability, and SQL support.

Indexing is the process of transforming raw documents into searchable vector representations.

[METADATA]
 {'source': 'data/example.txt'}

------------ Document 2 ------------

[PAGE CONTENT]
 Retrieval is the process of querying those vectors to find the most relevant information for a user question.

[METADATA]
 {'source': 'data/example.txt'}
```

**Ótimo, entendendo tudo isso agora vamos transformar esses chunks em vetores:**  
Para isso, primeiro vamos importar e instanciar a classe `OpenAIEmbeddings`:

[chapter02/pgvector-01.py](codes/chapter02/pgvector-01.py)
```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
```

Vejam que aqui nós estamos utilizando o modelo pré-treinado `text-embedding-3-small` da OpenAI.

> **Agora é só pegar nossos chunks (textos divididos) e transformar em vetores (embeddings)?**  
> Não nesse nosso exemplo!

**Lembram que nós criamos um container com PostgreSQL que dá suporte a pgvector?**  
Então, aqui vamos criar uma instância da classe `PGVector` que vai:

 - Receber os nossos chunks (textos divididos);
 - A instancia (classe responsável) que vai gerar os embeddings;
 - Conexão com o banco de dados (string de conexão);
 - Um nome para a nossa coleção:
   - Nome lógico da *coleção de vetores*.

[chapter02/pgvector-01.py](codes/chapter02/pgvector-01.py)
```python
from langchain_community.vectorstores import PGVector


vectorstore = PGVector.from_documents(
    documents=chunks,
    embedding=embeddings,
    connection_string=CONNECTION_STRING,
    collection_name="ex01_documents"
)
```

**O que acontece internamente?**  
Quando esse código roda, o *LangChain*:

```bash
1. Conecta no PostgreSQL
2. Cria tabelas se não existirem
3. Para cada chunk:
      - lê page_content
      - gera embedding
      - salva vetor + metadata
4. Cria ou reutiliza a coleção
```

> **O que temos na variável `vectorstore`?**

É um objeto que sabe:

 - onde estão os vetores
 - como buscá-los
 - como calcular similaridade

> **O que esse código (até esse momento) NÃO faz?**

 - ❌ Não responde perguntas
 - ❌ Não chama LLM
 - ❌ Não faz RAG completo
 - **NOTE:** Ele apenas cria a memória.

> **NOTE:**  
> 📌 Novamente, se nós temos uma instância de uma classe (`vectorstore`), essa instância tem (ou pode ter) um método.

Isso mesmo, aqui nossa instância `vectorstore` pode utilizar o método `similarity_search` para buscar vetores similares:

[chapter02/pgvector-01.py](codes/chapter02/pgvector-01.py)
```python
results = vectorstore.similarity_search(
    query="What is LangChain?",
    k=3
)
```

O código acima faz uma **busca semântica no índice vetorial** e **retorna os 3 textos mais relevantes**, com base no significado da pergunta.

 - 📌 Não é busca por palavra-chave
 - 📌 Não é SQL tradicional
 - 📌 É busca por similaridade de significado

> **O que temos na variável `query_results`?**

```python
query_results = vectorstore.similarity_search(
    query="What is LangChain?",
    k=3
)

print("\nType:", type(query_results))
print("\nContent:", query_results)
```

**OUTPUT:**
```bash
Type: <class 'list'>

Content: [Document(metadata={'source': 'data/example.txt'}, page_content='LangChain is a framework designed to simplify the development of applications powered by large language models (LLMs).\n\nIt provides building blocks for common use cases such as chatbots, question answering systems, and retrieval-augmented generation (RAG).\n\nOne of the core ideas of LangChain is to connect language models with external data sources.\n\nThis is achieved by loading documents, splitting them into smaller chunks, generating embeddings, and storing them in vector databases.'), Document(metadata={'source': 'data/example.txt'}, page_content='LangChain is a framework designed to simplify the development of applications powered by large language models (LLMs).\n\nIt provides building blocks for common use cases such as chatbots, question answering systems, and retrieval-augmented generation (RAG).\n\nOne of the core ideas of LangChain is to connect language models with external data sources.\n\nThis is achieved by loading documents, splitting them into smaller chunks, generating embeddings, and storing them in vector databases.'), Document(metadata={'source': 'data/example.txt'}, page_content='Vector databases allow semantic search, meaning that queries are matched based on meaning rather than exact keywords.\n\nPGVector is a PostgreSQL extension that enables storing and searching vector embeddings directly in a relational database.\n\nUsing PGVector with LangChain allows developers to build production-ready RAG systems with persistence, scalability, and SQL support.\n\nIndexing is the process of transforming raw documents into searchable vector representations.')]
```

Se vocês prestarem bem atenção verão que nós temos uma lista (`<class 'list'>`) com 3 Documents, por exemplo vamos exibir o `page_content` e `metadata` desses `Document()``, separadamente:

```python
query_results = vectorstore.similarity_search(
    query="What is LangChain?",
    k=3
)

for index, document in enumerate(query_results):
    print(f"\n------------ Document {index} ------------")
    print("\n[PAGE CONTENT]\n", document.page_content)
    print("\n[METADATA]\n", document.metadata)
```

**OUTPUT:**
```bash
------------ Document 0 ------------

[PAGE CONTENT]
 LangChain is a framework designed to simplify the development of applications powered by large language models (LLMs).

It provides building blocks for common use cases such as chatbots, question answering systems, and retrieval-augmented generation (RAG).

One of the core ideas of LangChain is to connect language models with external data sources.

This is achieved by loading documents, splitting them into smaller chunks, generating embeddings, and storing them in vector databases.

[METADATA]
 {'source': 'data/example.txt'}

------------ Document 1 ------------

[PAGE CONTENT]
 LangChain is a framework designed to simplify the development of applications powered by large language models (LLMs).

It provides building blocks for common use cases such as chatbots, question answering systems, and retrieval-augmented generation (RAG).

One of the core ideas of LangChain is to connect language models with external data sources.

This is achieved by loading documents, splitting them into smaller chunks, generating embeddings, and storing them in vector databases.

[METADATA]
 {'source': 'data/example.txt'}

------------ Document 2 ------------

[PAGE CONTENT]
 LangChain is a framework designed to simplify the development of applications powered by large language models (LLMs).

It provides building blocks for common use cases such as chatbots, question answering systems, and retrieval-augmented generation (RAG).

One of the core ideas of LangChain is to connect language models with external data sources.

This is achieved by loading documents, splitting them into smaller chunks, generating embeddings, and storing them in vector databases.

[METADATA]
 {'source': 'data/example.txt'}
```










































































































<!--- ( ??? ) --->










































































































<!--- ( Configurações ) --->

---

<div id="create-env"></div>

## `Criando o ambiente virtual`

**NOTE:**  
Antes de criar o ambiente virtual, crie um arquivo chamado [.env](.env) e depois insira a sua chave de API da OpenAI:

[.env](.env)
```bash
OPENAI_API_KEY=your_api_key
```

Continuando...

**CRIA O AMBIENTE VIRTUAL:**  
```bash
python3 -m venv environment
```

**ATIVA O AMBIENTE VIRTUAL (WINDOWS):**  
```bash
source environment/Scripts/activate
```

**ATIVA O AMBIENTE VIRTUAL (LINUX):**  
```bash
source environment/bin/activate
```

**ATUALIZA O PIP:**
```bash
python -m pip install --upgrade pip --require-virtualenv
```

**INSTALA AS DEPENDÊNCIAS:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**LISTA AS DEPENDÊNCIAS:**
```bash
pip list --require-virtualenv
```

**SALVA AS DEPENDÊNCIAS:**
```bash
pip freeze > requirements.txt --require-virtualenv
```

**Now, Be Happy!!!** 😬

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
