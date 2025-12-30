# langchain-ai

> Meus estudos sobre o projeto [langchain-ai](https://github.com/langchain-ai)

## Conteúdo

 - **Configurações:**
   - [`Criando o ambiente virtual`](#create-env)
   - [`Instalando o LangChain`](#install-langchain)
 - [**REFERÊNCIAS**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "200" Whitespace character.
--->









































































































<!--- ( Configurações ) --->

---

<div id="create-env"></div>

## `Criando o ambiente virtual`

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source environment/Scripts/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source environment/bin/activate
```

**UPDATE PIP:**
```bash
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**Now, Be Happy!!!** 😬










---

<div id="install-langchain"></div>

## `Instalando o LangChain`

Para instalar o pacote LangChain:

**1️⃣ langchain (o “LangChain normal”)**
```bash
pip install -U langchain
# Requires Python 3.10+
```

Hoje, o langchain **NÃO instala automaticamente integração com nenhum LLM** (OpenAI, Anthropic, etc.).

Ele fornece principalmente:

 - **🧠 Core abstractions:**
   - Chains
   - Prompt templates
   - Memory
   - Output parsers
   - Runnables
- **🧱 Infraestrutura para orquestrar LLMs**
- **🔌 Interfaces genéricas (sem dependência de fornecedor)**

> **📌 Importante:**  
> Sem instalar um pacote de integração, você não consegue usar nenhum modelo.

**2️⃣ langchain-openai:**
```bash
pip install -U langchain-openai
```

Este pacote adiciona suporte específico aos modelos da OpenAI.

 - **O que ele instala?**
   - **Classes como:**
     - ChatOpenAI
     - OpenAIEmbeddings
   - **Integração com:**
     - GPT-4.x
     - GPT-3.5
     - Embeddings da OpenAI
   - **Dependência do SDK oficial da OpenAI**

**3️⃣ langchain-anthropic:**
```bash
pip install -U langchain-anthropic
```

Este pacote adiciona suporte aos modelos Claude (Anthropic).

 - **O que ele fornece?**
   - **Classe:**
     - ChatAnthropic
   - **Integração com:**
     - Claude 3 (Opus, Sonnet, Haiku)
   - **Dependência do SDK da Anthropic**

> 📌 Sem esse pacote, o LangChain não sabe falar com a Anthropic.

### Consulte a aba Integrações para obter uma lista completa das integrações disponíveis.

[LangChain integrations packages](https://docs.langchain.com/oss/python/integrations/providers/overview)










<!--- ( REFERÊNCIAS ) --->

---

<div id="ref"></div>

## `REFERÊNCIAS`

 - **Configurações:**
   - [Install LangChain](https://docs.langchain.com/oss/python/langchain/install)
