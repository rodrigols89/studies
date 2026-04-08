# `Convertendo textos em chunks`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Criando uma função (chunk_text) para gerar chunking de textos`](#chunk-text)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

> ✂️ **Chunking é o coração de um RAG bem feito.**

Você **nunca** envia um arquivo inteiro para embeddings porque:

* modelos têm limite de tokens
* textos grandes perdem foco semântico
* a busca vetorial fica imprecisa
* respostas começam a misturar assuntos diferentes

> **NOTE:**  
> 👉 O que o RAG realmente entende são **pedaços bem definidos de texto**, com tamanho controlado e **continuidade semântica**.

Neste passo, vamos:

* dividir textos em chunks de tamanho ideal
* manter contexto entre chunks usando overlap
* preparar dados prontos para embeddings
* **sem misturar dados entre usuários**

### `Exemplo Visual (entendimento intuitivo)`

Imagine este texto grande:

```text
[ Documento inteiro ]
---------------------------------------------------------
| Introdução | Conceitos | Exemplos | Regras | Conclusão |
---------------------------------------------------------
```

> **NOTE:**  
> Se você gerar **um único embedding**, o vetor vira um “mix” de tudo.

Agora com chunking:

```text
Chunk 0: Introdução + Conceitos iniciais
Chunk 1: Conceitos avançados + Exemplos
Chunk 2: Exemplos + Regras
Chunk 3: Regras + Conclusão
```

🔁 O **overlap** garante que:

* nenhuma ideia seja cortada no meio
* perguntas encontrem contexto suficiente
* respostas fiquem mais precisas

### `Boas práticas adotadas`

* 📏 **300–800 tokens por chunk**
* 🔁 **Overlap de 10–20%**
* 🧠 **Manter contexto semântico**
* 🔐 **Nunca misturar usuários**


















































---

<div id="chunk-text"></div>

## `Criando uma função (chunk_text) para gerar chunking de textos`

> Nesta etapa, vamos criar uma função que será responsável por **quebrar um texto grande em pedaços menores (chunks)** de forma inteligente.

Isso é **fundamental em sistemas de RAG**, porque:

 - **Nunca devemos gerar embedding de um texto inteiro**
 - Modelos de embedding têm limite de tokens
 - Chunks menores:
   - melhoram a recuperação semântica
   - evitam perda de contexto
   - aumentam a qualidade das respostas

> **⚠️ NOTE:**  
> Aqui, vamos usar o **LangChain** e, mais especificamente, o `RecursiveCharacterTextSplitter`, que faz essa divisão respeitando a estrutura do texto.

### `Código completo`

A nossa função `chunk_text()` vai ficar da seguinte maneira:

[rag/services/ingestion/chunking.py](../../../rag/services/ingestion/chunking.py)
```python
from typing import List

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)


def chunk_text(
    *,
    text: str,
    chunk_size: int,
    chunk_overlap: int,
) -> List[str]:
    """
    Divide um texto em chunks semanticamente consistentes.

    Regras adotadas:
    - chunk_size: tamanho máximo do chunk
    - chunk_overlap: sobreposição entre chunks
    """

    splitter: RecursiveCharacterTextSplitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )
    )

    chunks: List[str] = splitter.split_text(text)

    return chunks
```

### `Explicação passo a passo (Step-by-Step)`

Vamos começar importando a tipagem `List`:

[rag/services/ingestion/chunking.py](../../../rag/services/ingestion/chunking.py)
```python
from typing import List
```

 - **O que essa importação faz?**
   - Importa o tipo `List` do módulo `typing`.
 - **Para que vamos usar?**
   - Para **tipagem estática**
   - Para deixar claro que a função retorna:
     - uma lista de strings → `List[str]`

Agora, nós vamos importar a classe `RecursiveCharacterTextSplitter` da biblioteca LangChain:

[rag/services/ingestion/chunking.py](../../../rag/services/ingestion/chunking.py)
```python
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)
```

 - **O que essa importação faz?**
   - Importa a classe `RecursiveCharacterTextSplitter` da biblioteca LangChain.
 - **O que essa classe faz?**
   - Ela divide um texto grande em vários pedaços menores (**chunks**) usando uma estratégia **recursiva**, tentando:
     - Separar primeiro por estruturas maiores (parágrafos)
     - Depois por estruturas menores (linhas, frases, palavras)
     - Só quebrar “na força” se não houver alternativa

> **NOTE:**  
> 👉 Isso garante **chunks semanticamente mais coerentes**.

Agora, nós vamos cria a definição da nossa função `chunk_text`:

[rag/services/ingestion/chunking.py](../../../rag/services/ingestion/chunking.py)
```python
def chunk_text(
    *,
    text: str,
    chunk_size: int,
    chunk_overlap: int,
) -> List[str]:
```

 - **O que essa função faz?**
   - Divide um texto em vários **chunks de tamanho controlado**, com **sobreposição**, retornando uma lista de strings prontas para:
     - embeddings
     - indexação em banco vetorial
     - RAG
 - **O que significa o `*` nos parâmetros?**
   - O `*` força que **todos os argumentos sejam nomeados**.

**Exemplo válido:**
```python
chunk_text(
    text=texto,
    chunk_size=500,
    chunk_overlap=100,
)
```

**Exemplo inválido:**
```python
chunk_text(texto, 500, 100)
```

> **NOTE:**  
> 👉 Isso evita erros e deixa o código mais explícito.

 - **Parâmetros da função**
   - `text: str`
     - Texto completo que será dividido
   - `chunk_size: int`
     - Tamanho máximo de cada chunk
     - Geralmente entre **300 e 800 tokens/caracteres**
   - `chunk_overlap: int`
     - Quantidade de caracteres repetidos entre chunks
     - Ajuda a **preservar contexto**
     - Normalmente entre **10% e 20%** do chunk_size
 - **O que essa função retorna?**
   - `-> List[str]`
   - Uma lista onde:
     - cada item é um chunk de texto
     - cada chunk é uma `str`

Continuando, agora vamos criar uma instância da classe `RecursiveCharacterTextSplitter`:

[rag/services/ingestion/chunking.py](../../../rag/services/ingestion/chunking.py)
```python
def chunk_text(...) -> List[str]:

    ...

    splitter: RecursiveCharacterTextSplitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )
    )
```

A primeira observação que nós temos que ter na instância acima é que nós estamos adicionando uma **tipagem**:

```python
    splitter: RecursiveCharacterTextSplitter = (
        RecursiveCharacterTextSplitter(
            ...
        )
    )
```

 - **Aqui nós estamos dizendo explicitamente:**
   - *“splitter deve ser um `RecursiveCharacterTextSplitter”`*
 - **Isso é usado por:**
   - Linters (mypy, pyright)
   - IDEs (VS Code, PyCharm)
   - Leitura de código / documentação
   - Em runtime, não muda absolutamente nada

> **NOTE:**  
> ⚠️ O Python não valida esse tipo em execução (a não ser que você use ferramentas externas)

Continuando, agora nós vamos explicar os parâmetros dessa instância:

 - **Parâmetros usados:**
   - `chunk_size=chunk_size`
     - **O que faz?**
       - Define o **tamanho máximo** de cada chunk.
   - `chunk_overlap=chunk_overlap`
     - **O que faz?**
       - Define quantos caracteres do chunk anterior serão repetidos no próximo.
   - `separators=[...]`
     - Ela tenta separar o texto nesta ordem:
       - `"\n\n"` → parágrafos
       - `"\n"` → quebras de linha
       - `". "` → fim de frases
       - `" "` → espaços (palavras)
       - `""` → último recurso: caractere por caractere

Agora, nós vamos dividir os textos em `chunks`:

[rag/services/ingestion/chunking.py](../../../rag/services/ingestion/chunking.py)
```python
def chunk_text(...) -> List[str]:

    ...

    chunks: List[str] = splitter.split_text(text)
```

No código acima:

 - **Primeiro nós criamos uma variável `chunks`:**
   - Que vai ser uma lista
   - de strings
 - **O que a função `split_text()` faz?**
   - *A primeira coisa a se observar aqui é que nós estamos utilizando um método da instância `splitter`.*
   - Esse método divide o texto informado em vários chunks, seguindo as regras definidas no *splitter*.
   - `text: str`
     - Texto original completo
 - **O que ela retorna?**
   - `List[str]`
     - Uma lista de strings
     - Cada string é um chunk

> **O que acontece internamente?**

O LangChain:

  1. Analisa o texto
  2. Tenta dividir pelos separadores
  3. Garante `chunk_size`
  4. Aplica `chunk_overlap`
  5. Retorna os chunks prontos

Agora para finalizar nossa função vamos retornar essa lista de `chunks`:

[rag/services/ingestion/chunking.py](../../../rag/services/ingestion/chunking.py)
```python
def chunk_text(...) -> List[str]:

    ...

    return chunks
```

> **O que isso faz?**  
> Retorna a lista de chunks gerados para quem chamou a função (e passou um texto como argumento).

Uso típico:

* gerar embeddings
* salvar no banco vetorial
* associar a metadados (document_id, user_id, etc.)

### `Testando manualmente`

> Agora, vamos criar alguns códigos que serão responsáveis por testar (manualmente) se a função `split_text()` está funcionando corretamente.

```python
from pathlib import Path

from rag.services.ingestion.text_extraction import extract_txt
from rag.services.ingestion.chunking import chunk_text


def test_txt_pipeline() -> None:
    print("\n🧪 Testando TXT → Extract → Chunk...\n")

    # Caminho do arquivo TXT de exemplo
    path = Path("data/samples/RAG.txt")

    # Extração de texto do arquivo TXT
    # O retorno vai ser um List[Document],
    # onde cada Document tem um atributo page_content
    # com o texto extraído.
    docs = extract_txt(path)

    print(f"📄 Documents retornados: {len(docs)}")

    # Concatenar o texto de todos os Documents em uma única string
    full_text: str = "\n".join(
        doc.page_content
        for doc in docs
    )

    # Exibir o texto completo extraído
    chunks = chunk_text(
        text=full_text,
        chunk_size=500,
        chunk_overlap=100,
    )

    print(f"\n📦 Total de chunks: {len(chunks)}")
    # Exibir os chunks gerados
    for i, chunk in enumerate(chunks):
        print(f"\n🔹 Chunk {i}")
        print("-" * 40)
        print(chunk)


if __name__ == "__main__":
    test_txt_pipeline()
```

**OUTPUT:**
```bash
🧪 Testando TXT → Extract → Chunk...

📄 Documents retornados: 1

📦 Total de chunks: 19

🔹 Chunk 0
----------------------------------------
Introdução à Computação Moderna, Inteligência Artificial e Sistemas Distribuídos

🔹 Chunk 1
----------------------------------------
A computação moderna passou por diversas transformações significativas ao longo das últimas décadas. Desde os primeiros computadores de grande porte, utilizados apenas por governos e instituições acadêmicas, até os dispositivos móveis altamente conectados que utilizamos diariamente, a evolução tecnológica moldou profundamente a forma como vivemos, trabalhamos e nos comunicamos

🔹 Chunk 2
----------------------------------------
. Atualmente, conceitos como computação em nuvem, inteligência artificial, aprendizado de máquina e sistemas distribuídos fazem parte do cotidiano de empresas e desenvolvedores de software em todo o mundo.

🔹 Chunk 3
----------------------------------------
Um dos pilares fundamentais da computação moderna é a abstração. Abstrair significa esconder a complexidade interna de um sistema e expor apenas o que é necessário para o seu uso. Linguagens de programação de alto nível, frameworks, bibliotecas e APIs são exemplos claros desse conceito. Graças à abstração, desenvolvedores conseguem criar sistemas complexos sem precisar entender todos os detalhes de baixo nível, como gerenciamento manual de memória ou instruções específicas de processador.

🔹 Chunk 4
----------------------------------------
Inteligência Artificial e Aprendizado de Máquina

A Inteligência Artificial (IA) é uma área da ciência da computação que busca criar sistemas capazes de realizar tarefas que normalmente exigiriam inteligência humana. Isso inclui reconhecimento de padrões, tomada de decisões, compreensão de linguagem natural e visão computacional. Dentro da IA, uma subárea muito importante é o aprendizado de máquina, também conhecido como machine learning.

🔹 Chunk 5
----------------------------------------
O aprendizado de máquina baseia-se na ideia de que sistemas podem aprender a partir de dados, identificando padrões e melhorando seu desempenho ao longo do tempo sem serem explicitamente programados para cada situação. Existem diferentes tipos de aprendizado de máquina, como o aprendizado supervisionado, não supervisionado e por reforço. Cada um desses paradigmas é utilizado para resolver diferentes tipos de problemas, como classificação, regressão, agrupamento e otimização.

🔹 Chunk 6
----------------------------------------
Nos últimos anos, o avanço do deep learning — uma abordagem baseada em redes neurais artificiais com múltiplas camadas — impulsionou significativamente a área de IA. Modelos de linguagem, por exemplo, são treinados com grandes volumes de texto e conseguem gerar respostas coerentes, resumir conteúdos, responder perguntas e até mesmo auxiliar no desenvolvimento de software.

Processamento de Linguagem Natural

🔹 Chunk 7
----------------------------------------
Processamento de Linguagem Natural

O Processamento de Linguagem Natural (PLN) é um campo da IA focado na interação entre computadores e linguagem humana. Ele envolve tarefas como análise sintática, análise semântica, extração de informações, tradução automática e geração de texto. Uma das maiores dificuldades do PLN é lidar com ambiguidades naturais da linguagem, como palavras com múltiplos significados e frases que dependem fortemente do contexto.

🔹 Chunk 8
----------------------------------------
Modelos modernos de PLN utilizam representações vetoriais chamadas embeddings, que transformam palavras, frases ou documentos inteiros em vetores numéricos. Esses vetores capturam relações semânticas, permitindo que o sistema compreenda que termos diferentes podem ter significados semelhantes. Essa representação é fundamental para aplicações como busca semântica e sistemas de recomendação.

Sistemas de Recuperação de Informação

🔹 Chunk 9
----------------------------------------
Sistemas de Recuperação de Informação

Sistemas de recuperação de informação têm como objetivo encontrar informações relevantes dentro de grandes conjuntos de dados. Motores de busca são um exemplo clássico desse tipo de sistema. Tradicionalmente, esses sistemas utilizavam técnicas baseadas em palavras-chave, como TF-IDF e índices invertidos. Embora eficazes, essas abordagens apresentam limitações quando o usuário não utiliza exatamente os mesmos termos presentes nos documentos.

🔹 Chunk 10
----------------------------------------
Com o surgimento dos embeddings semânticos, tornou-se possível realizar buscas mais inteligentes, levando em consideração o significado das palavras e não apenas sua correspondência literal. Isso abriu caminho para sistemas mais avançados, capazes de responder perguntas complexas e fornecer resultados mais relevantes.

RAG – Retrieval-Augmented Generation

🔹 Chunk 11
----------------------------------------
RAG – Retrieval-Augmented Generation

O conceito de Retrieval-Augmented Generation (RAG) combina recuperação de informação com geração de texto por modelos de linguagem. Em um sistema RAG, o modelo não depende apenas do conhecimento armazenado em seus parâmetros, mas também consulta uma base externa de documentos para obter informações atualizadas ou específicas. Esses documentos são recuperados com base na similaridade semântica e utilizados como contexto para gerar a resposta final.

🔹 Chunk 12
----------------------------------------
Uma arquitetura típica de RAG envolve várias etapas: ingestão de documentos, divisão do texto em partes menores (chunking), geração de embeddings, armazenamento em um banco vetorial e, por fim, a recuperação e utilização desses dados durante a geração da resposta. Esse tipo de abordagem é especialmente útil em cenários corporativos, onde é necessário consultar documentos internos, manuais técnicos ou bases de conhecimento privadas.

Computação em Nuvem e Containers

🔹 Chunk 13
----------------------------------------
Computação em Nuvem e Containers

A computação em nuvem revolucionou a forma como aplicações são desenvolvidas e distribuídas. Em vez de depender de servidores físicos locais, empresas podem utilizar infraestruturas escaláveis fornecidas por grandes provedores de nuvem. Isso permite maior flexibilidade, redução de custos e facilidade de manutenção.

🔹 Chunk 14
----------------------------------------
Containers, como os criados com Docker, são uma tecnologia fundamental nesse contexto. Eles permitem empacotar uma aplicação junto com todas as suas dependências, garantindo que ela funcione de maneira consistente em diferentes ambientes. Em conjunto com orquestradores como Kubernetes, containers facilitam o gerenciamento de sistemas distribuídos complexos.

Sistemas Distribuídos e Escalabilidade

🔹 Chunk 15
----------------------------------------
Sistemas Distribuídos e Escalabilidade

Sistemas distribuídos são compostos por múltiplos componentes que se comunicam através de uma rede para atingir um objetivo comum. Esses sistemas precisam lidar com desafios como latência, tolerância a falhas e consistência de dados. Para isso, diversas estratégias e padrões arquiteturais foram desenvolvidos, como replicação, balanceamento de carga e filas de mensagens.

🔹 Chunk 16
----------------------------------------
A escalabilidade é uma característica essencial de sistemas modernos. Ela pode ser vertical, quando aumentamos os recursos de uma única máquina, ou horizontal, quando adicionamos mais instâncias ao sistema. Arquiteturas baseadas em microsserviços são um exemplo de abordagem que favorece a escalabilidade horizontal.

Considerações Finais

🔹 Chunk 17
----------------------------------------
Considerações Finais

A combinação de inteligência artificial, recuperação de informação e sistemas distribuídos representa uma das áreas mais promissoras da computação atual. Soluções baseadas em RAG demonstram como é possível unir modelos de linguagem avançados com bases de conhecimento externas, criando sistemas mais precisos, confiáveis e úteis.

🔹 Chunk 18
----------------------------------------
À medida que essas tecnologias continuam evoluindo, torna-se cada vez mais importante compreender seus fundamentos, limitações e boas práticas. O estudo contínuo e a experimentação prática são essenciais para profissionais que desejam se manter atualizados e construir soluções inovadoras no cenário tecnológico contemporâneo.
```

### `Testando manualmente (no Workspace de um usuário específico)`

Para testarmos a função `chunk_text()` usando arquivos reais do nosso **media/workspace**, o `driver.py` precisa fazer três etapas:

 - Descobrir os arquivos do workspace do usuário (usando `discover_workspace_files()`)
 - Ler o conteúdo do arquivo físico (absolute_path)
 - Aplicar `chunk_text()` no texto extraído.

Agora o teste ideal no `driver.py` é rodar o pipeline completo até o chunking, usando os arquivos reais do **media/workspace**:

```bash
Workspace
   ↓
discover_workspace_files()
   ↓
extract_text()
   ↓
chunk_text()
```

```python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model

from rag.services.ingestion.file_discovery import discover_workspace_files
from rag.services.ingestion.text_extraction import extract_text
from rag.services.ingestion.chunking import chunk_text


User = get_user_model()


def test_rag_ingestion(user_id: int):

    print("\n🔎 Buscando usuário...")
    user = User.objects.get(id=user_id)
    print(f"Usuário encontrado: {user}")

    print("\n📂 Descobrindo arquivos do workspace...\n")
    inventory = discover_workspace_files(user)
    print(f"Arquivos encontrados: {len(inventory)}\n")

    for file_info in inventory:
        print("📄 Arquivo:", file_info["name"])
        print("📁 Pasta:", file_info["folder"])
        print("📦 Tipo:", file_info["file_type"])
        try:
            # -----------------------------
            # EXTRAÇÃO DE TEXTO
            # -----------------------------
            documents = extract_text(file_info)
            print(f"📜 Documents extraídos: {len(documents)}")
            for doc_index, doc in enumerate(documents):
                text = doc.page_content
                print(
                    f"   Documento {doc_index+1} tamanho: {len(text)} caracteres"
                )

                # -----------------------------
                # CHUNKING
                # -----------------------------
                chunks = chunk_text(
                    text=text,
                    chunk_size=500,
                    chunk_overlap=50,
                )
                print(f"   🧩 Chunks gerados: {len(chunks)}")

                # mostrar apenas primeiros chunks
                for i, chunk in enumerate(chunks[:2]):
                    print(f"\n   --- CHUNK {i+1} ---")
                    print(chunk[:200])
        except Exception as e:
            print("❌ ERRO:", e)
        print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    test_rag_ingestion(user_id=1)
```

**OUTPUT:**
```bash
🔎 Buscando usuário...
Usuário encontrado: drigols

📂 Descobrindo arquivos do workspace...

Arquivos encontrados: 40

📄 Arquivo: TERMO DE EMPRÉSTIMO DE BEM MÓVEL.docx
📁 Pasta: workspace/Termos e Declarações/Termos de Emprestimo
📦 Tipo: .docx
📜 Documents extraídos: 1
   Documento 1 tamanho: 3772 caracteres
   🧩 Chunks gerados: 9

   --- CHUNK 1 ---
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

   --- CHUNK 2 ---
I - PARTES:

Empréstimo: SECRETARIA DE EDUCAÇÃO, com sede na Av. Joaquim Cavalcante de Morais, s/n - Centro, Remígio PB, Cep: 58398-000 representada neste ato por Roseluce dos Santos Souza, Secretária

======================================================================

📄 Arquivo: Poliana.docx
📁 Pasta: workspace/Termos e Declarações/Termos de Emprestimo
📦 Tipo: .docx
📜 Documents extraídos: 1
   Documento 1 tamanho: 3810 caracteres
   🧩 Chunks gerados: 9

   --- CHUNK 1 ---
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

   --- CHUNK 2 ---
I - PARTES:

Empréstimo: SECRETARIA DE EDUCAÇÃO, com sede na Av. Joaquim Cavalcante de Morais, s/n - Centro, Remígio PB, Cep: 58398-000 representada neste ato por Roseluce dos Santos Souza, Secretária

======================================================================

📄 Arquivo: Paloma.docx
📁 Pasta: workspace/Termos e Declarações/Termos de Emprestimo
📦 Tipo: .docx
📜 Documents extraídos: 1
   Documento 1 tamanho: 3816 caracteres
   🧩 Chunks gerados: 9

   --- CHUNK 1 ---
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

   --- CHUNK 2 ---
I - PARTES:

Empréstimo: SECRETARIA DE EDUCAÇÃO, com sede na Av. Joaquim Cavalcante de Morais, s/n - Centro, Remígio PB, Cep: 58398-000 representada neste ato por Roseluce dos Santos Souza, Secretária

======================================================================

📄 Arquivo: Nice.docx
📁 Pasta: workspace/Termos e Declarações/Termos de Emprestimo
📦 Tipo: .docx
📜 Documents extraídos: 1
   Documento 1 tamanho: 3813 caracteres
   🧩 Chunks gerados: 9

   --- CHUNK 1 ---
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

   --- CHUNK 2 ---
I - PARTES:

Empréstimo: SECRETARIA DE EDUCAÇÃO, com sede na Av. Joaquim Cavalcante de Morais, s/n - Centro, Remígio PB, Cep: 58398-000 representada neste ato por Roseluce dos Santos Souza, Secretária

======================================================================

📄 Arquivo: Estabilizador.docx
📁 Pasta: workspace/Termos e Declarações/Termos de Emprestimo
📦 Tipo: .docx
📜 Documents extraídos: 1
   Documento 1 tamanho: 3745 caracteres
   🧩 Chunks gerados: 9

   --- CHUNK 1 ---
PREFEITURA MUNICIPAL DE REMÍGIO

SECRETARIA DE EDUCAÇÃO

CNPJ 09.048.976/0001-09

Av. Joaquim Cavalcante de Morais, SN – Centro

 CEP: 58.398-000-Remígio – PB

secmunremigio@hotmail.com

TERMO DE EMP

   --- CHUNK 2 ---
I - PARTES:

Empréstimo: SECRETARIA DE EDUCAÇÃO, com sede na Av. Joaquim Cavalcante de Morais, s/n - Centro, Remígio PB, Cep: 58398-000 representada neste ato por Roseluce dos Santos Souza, Secretária

======================================================================


    ...


======================================================================

📄 Arquivo: RAG.txt
📁 Pasta: workspace/1/2/3/4/5
📦 Tipo: .txt
📜 Documents extraídos: 1
   Documento 1 tamanho: 11 caracteres
   🧩 Chunks gerados: 1

   --- CHUNK 1 ---
Meu txt....

======================================================================

📄 Arquivo: RAG.txt
📁 Pasta: workspace/1/2/3/4
📦 Tipo: .txt
📜 Documents extraídos: 1
   Documento 1 tamanho: 11 caracteres
   🧩 Chunks gerados: 1

   --- CHUNK 1 ---
Meu txt....

======================================================================

📄 Arquivo: RAG.txt
📁 Pasta: workspace/1/2/3
📦 Tipo: .txt
📜 Documents extraídos: 1
   Documento 1 tamanho: 11 caracteres
   🧩 Chunks gerados: 1

   --- CHUNK 1 ---
Meu txt....

======================================================================

📄 Arquivo: RAG.txt
📁 Pasta: workspace/1/2
📦 Tipo: .txt
📜 Documents extraídos: 1
   Documento 1 tamanho: 11 caracteres
   🧩 Chunks gerados: 1

   --- CHUNK 1 ---
Meu txt....

======================================================================

📄 Arquivo: RAG.txt
📁 Pasta: workspace/1
📦 Tipo: .txt
📜 Documents extraídos: 1
   Documento 1 tamanho: 11 caracteres
   🧩 Chunks gerados: 1

   --- CHUNK 1 ---
Meu txt....

======================================================================
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
