# `Geração da resposta com contexto controlado (RAG)`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Preparando o contexto textual: build_context()`](#build-context)
 - [`Gerando Respostas com LLM utilizando Contexto Recuperado: generate_answer()`](#generate-answer)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

> **🧠 O LLM só é confiável quando você limita o que ele pode usar.**

Se você apenas perguntar:

```bash
"O que diz sobre autenticação?"
```

O modelo pode:

 - inventar informações
 - usar conhecimento externo
 - misturar fatos

Mas se você disser:

```bash
Use apenas o contexto abaixo.
```

Você está controlando o comportamento.

Neste passo, vamos:

- Montar o contexto com chunks recuperados
- Incluir metadados (pasta + arquivo)
- Criar um prompt restritivo
- Exigir que o modelo cite as fontes


















































---

<div id="build-context"></div>

## `Preparando o contexto textual: build_context()`

> Aqui, vamos implementar a função `build_context()` que terar como objetivo montar o contexto textual que será enviado para o modelo de linguagem (LLM) durante uma consulta em um sistema *RAG (Retrieval-Augmented Generation)*.

Ela recebe uma lista de chunks recuperados do banco vetorial, representados por objetos `DocumentEmbedding`, e transforma esses trechos em um único texto estruturado.

Cada `chunk` é formatado incluindo:

 - A origem do trecho (pasta e caminho do arquivo)
 - O conteúdo do texto extraído

> **⚠️ NOTE:**  
> Ao final, todos os trechos são concatenados em um único bloco de texto, separados por linhas em branco. Esse texto final é o contexto que será usado pelo modelo de IA para gerar uma resposta baseada nos documentos do workspace do usuário.

Em resumo, a função:

 - Recebe os chunks recuperados da busca vetorial.
 - Formata cada chunk com sua fonte e conteúdo.
 - Junta todos os trechos em um único contexto textual.
 - Retorna esse contexto para ser enviado ao modelo de linguagem.

### `Código Completo`

A nossa função `build_context()` (completa) vai ficar da seguinte maneira:

[rag/services/generation/context_builder.py](../../../rag/services/generation/context_builder.py)
```python
from typing import List

from rag.models import DocumentEmbedding


def build_context(
    *,
    chunks: List[DocumentEmbedding],
) -> str:

    context_parts: List[str] = []

    for chunk in chunks:
        source: str = (
            f"[{chunk.folder}/{chunk.path}]"
        )

        text: str = chunk.content.strip()

        formatted: str = (
            f"{source}\n\"{text}\""
        )

        context_parts.append(formatted)

    context: str = "\n\n".join(context_parts)

    return context
```

### `Testando manualmente`

O nosso teste manual para a função `build_context()` vai seguir o seguinte fluxo:

```bash
Pergunta
   ↓
Gerar embedding da pergunta
   ↓
Buscar chunks similares no pgvector
   ↓
build_context(chunks)
   ↓
Mostrar contexto final
```

```python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from pgvector.django import CosineDistance

from rag.models import DocumentEmbedding
from rag.services.ingestion.embeddings import get_embedding_model
from rag.services.generation.context_builder import build_context


def test_context_builder(user_id: int, question: str):

    print("\n🔎 Pergunta:")
    print(question)

    embedding_model = get_embedding_model()

    query_vector = embedding_model.embed_query(question)

    print("\n🧠 Embedding da pergunta gerou")

    chunks = (
        DocumentEmbedding.objects
        .filter(user_id=user_id)
        .annotate(distance=CosineDistance("embedding", query_vector))
        .order_by("distance")[:5]
    )

    print(f"\n📚 Chunks recuperados: {len(chunks)}")

    for c in chunks:
        print(
            f"- file_id={c.file_id} chunk={c.chunk_index} distance={c.distance:.4f}"
        )

    context = build_context(chunks=chunks)

    print("\n" + "=" * 70)
    print("📄 CONTEXTO GERADO")
    print("=" * 70)

    print(context)


if __name__ == "__main__":

    test_context_builder(
        user_id=1,
        question="Quem é a secretária de educação de Remígio?",
    )
```

**OUTPUT:**
```bash
🔎 Pergunta:
Quem é a secretária de educação de Remígio?

🧠 Embedding da pergunta gerou

📚 Chunks recuperados: 5
- file_id=18 chunk=3 distance=0.3542
- file_id=15 chunk=2 distance=0.3542
- file_id=24 chunk=0 distance=0.3636
- file_id=23 chunk=10 distance=0.4023
- file_id=22 chunk=10 distance=0.4023

======================================================================
📄 CONTEXTO GERADO
======================================================================
[workspace/Modelos/Gabinete//home/drigols/ragproject/media/workspace/user_1/folder_17/Cópia_de_ROBOTICA.docx]
"Roseluce dos Santos Souza

Secretária Municipal de Educação"

[workspace/Modelos/Transporte//home/drigols/ragproject/media/workspace/user_1/folder_19/Adriano_transporte.docx]
"Roseluce dos Santos Souza

Secretária Municipal de Educação"

[workspace/Planejamentos//home/drigols/ragproject/media/workspace/user_1/folder_20/Planejamento_dos_4_anos_-_v2.docx]
"ESTADO DA PARAÍBA

                PREFEITURA MUNICIPAL DE REMÍGIO

                SECRETARIA MUNICIPAL DE SAÚDE

                CNPJ: 11.376.311/0001-76

                Rua Patrício Valentim Monteiro, SN – Bela Vista

                Remígio-PB

                Telefone: (83) 3364-1700

                e-mail: secsauderemigio@gmail.com





                        CNPJ: 09.048.976/0001-09

                Avenida Joaquim Cavalcante de Morais, N° 150, Centro Remígio-PB

                e-mail: secmunremigio@gmail.com



Revisão do PCCR da educação;

Valorização dos salários dos professores e demais profissionais da Educação;"

[workspace/Modelos/Administrativo e Finanças//home/drigols/ragproject/media/workspace/user_1/folder_14/Ubiratan_Marques_-_selo_unicef.docx]
"Luis Cláudio Régis Marinho

Prefeito(a) Municipal de Remígio"

[workspace/Modelos/Administrativo e Finanças//home/drigols/ragproject/media/workspace/user_1/folder_14/Conselho.docx]
"Luis Cláudio Régis Marinho

Prefeito(a) Municipal de Remígio"
```

Vejam, que a pergunta que nós fizemos gerou:

 - Quantos chunks foram encontrados
 - O id do arquivo: `file_id=???`
 - Quantos chunks ele (esse arquivo) tem: `chunk=???`
 - A distância dele: `distance=???`


















































---

<div id="generate-answer"></div>

## `Gerando Respostas com LLM utilizando Contexto Recuperado: generate_answer()`

> Aqui, vamos implementar a função `generate_answer()` que será responsável por gerar a resposta final de um sistema *RAG (Retrieval-Augmented Generation)* utilizando um modelo de linguagem local.

Ela receberá dois elementos principais:

 - `question` → a pergunta feita pelo usuário
 - `context` → o conjunto de trechos de documentos recuperados do banco vetorial

### `Código Completo`

A nossa função `generate_answer()` (completa) vai ficar da seguinte maneira:

[rag/services/generation/answer_generator.py](../../../rag/services/generation/answer_generator.py)
```python
from typing import Any

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


def _get_llm() -> ChatOpenAI:
    """
    Retorna o LLM da OpenAI configurado.
    """

    return ChatOpenAI(
        model="gpt-4o-mini",  # rápido e barato (recomendado para RAG)
        temperature=0.0,
    )


def generate_answer(
    *,
    question: str,
    context: str,
) -> str:

    template: str = """
Use apenas o contexto abaixo para responder.

Se a resposta não estiver no contexto,
diga que não encontrou informação suficiente.

Cite explicitamente os arquivos e pastas usados.

Contexto:
{context}

Pergunta:
{question}

Resposta:
    """

    prompt: PromptTemplate = PromptTemplate(
        template=template.strip(),
        input_variables=["context", "question"],
    )

    formatted_prompt: str = prompt.format(
        context=context,
        question=question,
    )

    llm: ChatOpenAI = _get_llm()

    response: Any = llm.invoke(formatted_prompt)

    return response.content.strip()
```

### `Testando manualmente`

Agora, vamos criar alguns códigos que serão responsáveis por testar (manualmente) se a função `generate_answer()` consegue gerar respostas:

```python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from pgvector.django import CosineDistance

from rag.models import DocumentEmbedding
from rag.services.ingestion.embeddings import get_embedding_model
from rag.services.generation.context_builder import build_context
from rag.services.generation.answer_generator import generate_answer


def test_rag_question(user_id: int, question: str):

    print("\n🔎 Pergunta:")
    print(question)

    # -----------------------------------------
    # 1️⃣ gerar embedding da pergunta
    # -----------------------------------------

    embedding_model = get_embedding_model()

    query_vector = embedding_model.embed_query(question)

    print("\n🧠 Embedding da pergunta gerado")

    # -----------------------------------------
    # 2️⃣ buscar chunks similares no pgvector
    # -----------------------------------------

    chunks = (
        DocumentEmbedding.objects
        .filter(user_id=user_id)
        .annotate(distance=CosineDistance("embedding", query_vector))
        .order_by("distance")[:5]
    )

    print(f"\n📚 Chunks recuperados: {len(chunks)}")

    for c in chunks:
        print(
            f"- file_id={c.file_id} chunk={c.chunk_index} distance={c.distance:.4f}"
        )

    # -----------------------------------------
    # 3️⃣ construir contexto
    # -----------------------------------------

    context = build_context(chunks=chunks)

    print("\n" + "=" * 70)
    print("📄 CONTEXTO")
    print("=" * 70)

    print(context[:1000])  # mostra só parte do contexto

    # -----------------------------------------
    # 4️⃣ gerar resposta com LLM
    # -----------------------------------------

    answer = generate_answer(
        question=question,
        context=context,
    )

    print("\n" + "=" * 70)
    print("🤖 RESPOSTA DO LLM")
    print("=" * 70)

    print(answer)


if __name__ == "__main__":

    test_rag_question(
        user_id=1,
        question="Quem é a secretária de educação de Remígio?",
    )
```

**OUTPUT:**
```bash
🔎 Pergunta:
Quem é a secretária de educação de Remígio?

🧠 Embedding da pergunta gerado

📚 Chunks recuperados: 5
- file_id=18 chunk=3 distance=0.3542
- file_id=15 chunk=2 distance=0.3542
- file_id=24 chunk=0 distance=0.3636
- file_id=23 chunk=10 distance=0.4023
- file_id=22 chunk=10 distance=0.4023

======================================================================
📄 CONTEXTO
======================================================================
[workspace/Modelos/Gabinete//home/drigols/ragproject/media/workspace/user_1/folder_17/Cópia_de_ROBOTICA.docx]
"Roseluce dos Santos Souza

Secretária Municipal de Educação"

[workspace/Modelos/Transporte//home/drigols/ragproject/media/workspace/user_1/folder_19/Adriano_transporte.docx]
"Roseluce dos Santos Souza

Secretária Municipal de Educação"

[workspace/Planejamentos//home/drigols/ragproject/media/workspace/user_1/folder_20/Planejamento_dos_4_anos_-_v2.docx]
"ESTADO DA PARAÍBA

                PREFEITURA MUNICIPAL DE REMÍGIO

                SECRETARIA MUNICIPAL DE SAÚDE

                CNPJ: 11.376.311/0001-76

                Rua Patrício Valentim Monteiro, SN – Bela Vista

                Remígio-PB

                Telefone: (83) 3364-1700

                e-mail: secsauderemigio@gmail.com





                        CNPJ: 09.048.976/0001-09

                Avenida Joaquim Cavalcante de Morais, N° 150, Centro Remígio-PB

                e-mail: secmunremigio@gmail.com



Revisão do PCCR da educação;

Valorização dos salários dos professores e demais profissionais da Educação;"

[workspace/Modelos/Administrativo e F

======================================================================
🤖 RESPOSTA DO LLM
======================================================================
A secretária de educação de Remígio é Roseluce dos Santos Souza. A informação pode ser encontrada nos seguintes arquivos:

1. [workspace/Modelos/Gabinete//home/drigols/ragproject/media/workspace/user_1/folder_17/Cópia_de_ROBOTICA.docx]
2. [workspace/Modelos/Transporte//home/drigols/ragproject/media/workspace/user_1/folder_19/Adriano_transporte.docx]
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
