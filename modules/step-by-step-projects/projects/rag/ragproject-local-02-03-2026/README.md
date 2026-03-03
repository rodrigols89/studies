# RAG Project

 - [**Introdução e Objetivos do Projeto**](#intro-to-the-project)
 - [**Configurando o projeto localmente**](#local-settings)
 - [**Como este projeto foi desenvolvido (passo a passo)**](docs)
<!---
[WHITESPACE RULES]
- Different topic = "50" Whitespace character.
--->




















































---

<div id="intro-to-the-project"></div>

## Introdução e Objetivos do Projeto

O **RAG Project** foi desenvolvido para solucionar um problema recorrente na *Secretaria de Educação*, onde trabalho (Remígio-PB):

> A **"ausência de um mecanismo de consulta"** em um grande número de pastas, arquivos e formatos.

Para enfrentar esse desafio, o projeto adota uma arquitetura baseada em *Retrieval-Augmented Generation (RAG)*, integrando técnicas de *Processamento de Linguagem Natural (NLP)*, *modelos de linguagem (LLMs)* e *mecanismos de busca vetorial*. O sistema permite transformar dados institucionais estáticos em um repositório consultável e responsivo.

### 🎯 Objetivos Técnicos

 - Centralizar documentos institucionais de forma estruturada.
 - Indexar arquivos através de embeddings semânticos.
 - Realizar consultas híbridas (vetorial + keyword).
 - Fornecer respostas geradas por LLMs baseadas exclusivamente nos dados indexados.
 - Garantir rastreabilidade e auditoria das fontes utilizadas nas respostas.

### 🏗️ Arquitetura do Sistema

A solução é dividida em *quatro camadas* principais:

 - **1. Ingestão de Dados:**
   - Extração de conteúdo de PDFs, DOCXs, planilhas e documentos administrativos.
   - Normalização de texto e limpeza semântica.
   - Pipeline automatizado de pré-processamento (fragmentação, tokenização, chunking).
 - **2. Indexação e Armazenamento:**
   - Geração de embeddings com modelo compatível com LLM escolhido.
   - Armazenamento em banco vetorial.
 - **3. Recuperação da Informação (Retrieval):**
   - Recuperação baseada em similaridade vetorial.
   - Suporte a filtros estruturados (metadata filtering).
   - Opcional: rerankers para melhorar precisão do top-k.
 - **4. Geração da Resposta (LLM Layer):**
   - Pipeline RAG com prompt engineering focado em:
     - grounding em documentos institucionais;
     - citar fontes;
     - evitar alucinações;
     - manter conformidade administrativa.
   - Respostas são geradas usando LLMs locais ou hospedados (OpenAI, Azure, vLLM, etc.).




















































---

<div id="local-settings"></div>

## Configurando o projeto localmente

> Por mais que este projeto tenha sido projetado para rodar em contêiners e a maioria das configurações sejam feita neles, precisamos de um ambiente virtual local (em nossa máquina), que será responsável por gerenciar esses contêineres localmente.

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
pip install -U -v --require-virtualenv -r requirements-local.txt
```

**LISTA AS DEPENDÊNCIAS:**
```bash
pip list --require-virtualenv
```

**Now, Be Happy!!!** 😬

Depois, que o ambiente estiver criado é só utilizar os comandos Taskipy:

 - task start_compose
 - task opendb

> **⚠️ NOTE:**  
> Você poderá ver todos os comandos disponíveis em [pyproject.toml](pyproject.toml) na seção `[tool.taskipy.tasks]`.

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
