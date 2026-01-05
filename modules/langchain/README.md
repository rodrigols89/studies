# Aprende a usar a LangChain

> Minnhas **notas** e **códigos** do livro [Aprende a usar a LangChain](https://learning.oreilly.com/library/view/aprende-a-usar/9798341637917/)

## Conteúdo

 - **1. Fundamentos de LLM com LangChain:**
   - [`O que é ChatOpenAI?`](#intro-to-chatopenai)
   - [`Métodos de Execução de Runnables no LangChain`](#runnables-methods-langchain)
   - [`Método .invoke()`](#invoke-method)
   - [`Modelo de Mensagens de Conversa no LangChain`](#messages-in-langchain)
   - [`"Templates de Prompt" no LangChain`](#templates-in-langchain)
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
> Esse módulo **define como você constrói prompts de forma estruturada**, reutilizável e segura no LangChain.

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
