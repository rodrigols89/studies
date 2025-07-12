# Pythonando (Arcane 06 - 2025)

 - **Teoria:**
   - [RAG (Retrieval-Augmented Generation)](#intro-to-rag)
   - [Chunks](#intro-to-chunks)
   - [Overlap](#intro-to-overlap)
   - [RAG + Retriever (Implementação)](#rag-retriever)
 - **Implementação:**
   - [Criando o projeto "core" do djando](#django-core)
   - [Criando e configurando o app "users"](#app-users)
   - [Mapeando a rota "users" com a view "register"](#mapping-users-to-register-view)
<!---
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
--->






































































































<!--- ( Teoria ) --->

---

<div id="intro-to-rag"></div>

## RAG (Retrieval-Augmented Generation)

Retrieval‑Augmented Generation (RAG) é uma técnica que combina:

 - Recuperação de documentos (retrieval);
 - Com modelos geradores de linguagem (generation).

Em vez de confiar apenas no conhecimento “embutido” nos parâmetros do modelo, o RAG permite que o sistema vá buscar trechos de texto relevantes em uma base externa (por exemplo, Wikipedia, banco de documentos corporativos) e use essas informações para gerar respostas mais precisas e contextualizadas.

![img](images/rag-01.png)  

### Quando utilizar RAG

 - **Base de conhecimento grande e em constante atualização:**
   - Documentações, FAQs, bases científicas.
 - **Domínios técnicos/especializados:**
   - Jurídico, médico, pesquisadores que exigem precisão e citações.
 - **Sistemas de suporte ao cliente:**
   - Chatbots que precisam referenciar manuais, políticas, termos de serviço.

### Quando não utilizar RAG

 - **Tarefas de conversação livre:**
   - Bate‑papo informal, criação de conteúdo criativo onde não há necessidade de buscar fatos externos.
 - **Restrições de latência:**
   - Se seu sistema exige respostas em tempo real (<100 ms) e não comporta o tempo extra de recuperação.
 - **Ambientes com poucos dados:**
   - Se a base de documentos for pequena e autossuficiente, pode ser mais simples usar um LLM puro ou até finetuning.




















---

<div id="intro-to-chunks"></div>

## Chunks

> Imagina que você precisa criar um *RAG* que utiliza a **Constituição Federal** para auxiliar advogados.

Se, para uma pergunta sobre **direito do consumidor**, enviarmos *toda a constituição*, isso fará com que o modelo de IA não consiga processar todas as informações, já que, quanto maior o prompt, **menos precisa tende a ser a resposta**.

Para isso, utilizamos a técnica de **"chunks"**, onde, pegamos um arquivo geral e o quebramos em vários pequenos trechos:

![img](images/chunks-01.png)  

> **NOTE:**  
> Podemos usar um `chunk_size` para especificar quantos caracteres teremos por **chunk**.

A *Constituição Federal* possui **64.488 palavras**. Se definirmos um `chunk_size` como **100**, teremos **645 mini arquivos (64.488÷100)** da Constituição.

### 🧾 Exemplos:

 - **Art. 1º** A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos...
 - **Parágrafo único.** Todo o poder emana do povo, que o exerce por meio de representantes eleitos ou diretamente, nos termos desta Constituição...
 - **Art. 2º** São Poderes da União, independentes e harmônicos entre si, o Legislativo, o Executivo e o Judiciário...




















---

<div id="intro-to-overlap"></div>

## Overlap

**Mas agora enfrentamos outro problema:**  
Ao separar o texto por chunks, pode ser que eles **fiquem sem sentido**, já que partes importantes da informação podem ser **cortadas (separadas)**.

> **NOTE:**  
> Para isso, usamos o parâmetro `chunk_overlap`.

 - Ele define quantos caracteres de sobreposição haverá entre um chunk e o próximo.
 - 👉 Isso é útil para manter o contexto entre pedaços consecutivos.

Por exemplo, Exemplo com `chunk_size = 500` e `chunk_overlap = 100`

```bash
[000 ... 499]
[400 ... 899]
[800 ... 1299]
```

Vejam que:

 - **Nosso primeiro chunk comeca em 000 e termina em 499:**
   - Ou seja, as primeiras 500 palavras da Constituição.
 - **Nosso segundo chunk começa em 400 (por causa do "chunk_overlap = 100") e termina em 899:**
   - Ou seja, ele está pegando as 100 últimas palavras do chunk anterior.
   - **NOTE:** Isso é importante para evitar perda de contexto entre os chunks.

Por exemplo, imagine que temos o seguinte texto:

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
> Vejam que nós pegamos as **3 últimas palavras do chunk (overlap = 3)** para não perde contexto.




















---

<div id="rag-retriever"></div>

## RAG + Retriever (Implementação)

> Aqui vamos aprender o básico de como implementar um `RAG (Retrieval-Augmented Generation)` baseado em `Retriever`.

De início vamos ler um documento (PDF) e para isso a biblioteca LangChain já tem uma função pronta para isso:

[rag_retriever.py](rag_retriever.py)
```python
pdf_pah = "perceptron.pdf"     # PDF path
loader = PyPDFLoader(pdf_pah)  # PDF loader
pdf = loader.load()            # PDF documents

print("Document type:", type(pdf))
print("Document content:", pdf)
```

> **NOTE:**  
> O código acima vai printar várias informações sobre o documento (PDF) que foi lido, como, conteúdo, número de páginas e etc.

Continuando, agora nós vamos quebrar o conteúdo do documento em várias `chunks` e `overlap`:

[rag_retriever.py](rag_retriever.py)
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Cria um splitter de 500 (documentos) e overlap de 100 (100 palavras casa)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

# Divide (splita) o PDF em chunks
chunks = splitter.split_documents(pdf)

for index, chunk in enumerate(chunks):
    if index == 5:
        break
    print(chunk.page_content, "\n\n")
```

**OUTPUT:**
```bash
Perceptron
tags: #python_full_ai  #perceptron
Perceptron: Fundamentos Teóricos e
matemáticos
O Perceptron constitui a base fundamental para o desenvolvimento
de redes neurais mais complexas. Este material explora sua teoria,
formulação matemática e aplicações práticas.
Fundamentos Históricos e Conceituais
Em 1943, Warren McCulloch e Walter Pitts publicaram o artigo que
revolucionou todo o nosso entendimento moderno sobre inteligências 


revolucionou todo o nosso entendimento moderno sobre inteligências
artificiais como as conhecemos hoje, desde o ChatGPT, MidJourney,
ClaudeAI, entre outros.
"A Logical Calculus of the Ideas Immanent in Nervous Activity"
nos deu a ideia do primeiro neurônio artificial, baseado nos neurônios
biológicos do nosso próprio cérebro, chamado de Perceptron.
O Perceptron é um classificador binário de problemas linearmente
separáveis. Ele é a forma mais elementar de uma rede neural e, por 


separáveis. Ele é a forma mais elementar de uma rede neural e, por
isso, individualmente, não é capaz de resolver muitos problemas, já
que seria equiparado a um único neurônio do nosso cérebro.
Contudo, ele nos permite a criação do Multilayer Perceptron, um
conjunto de Perceptrons ligados em camadas, que dá origem às
redes neurais.
Funcionamento do Perceptron 


Onde:
A imagem acima serve apenas como uma representação humanizada
do Perceptron para fins didáticos. No entanto, para o computador, o
Perceptron nada mais é do que uma função matemática.
O problema de representar o Perceptron dessa maneira é que a
função resultante só funciona com dois valores de entrada. Para que
ele seja mais útil e escalável, precisamos expressá-lo de forma
dinâmica, capaz de lidar com múltiplas entradas.
Z=
N
∑
i=1
xiwi
x₁, x₂, ..., x ₙ  são as entradas 


dinâmica, capaz de lidar com múltiplas entradas.
Z=
N
∑
i=1
xiwi
x₁, x₂, ..., x ₙ  são as entradas
w₁, w₂, ..., w ₙ  são os pesos que representam o aprendizado do
modelo
Σ representa a soma ponderada das entradas pelos pesos
Z é o resultado da somatória
z=f(x1,x2)
f(x1,x2)=(x1 ⋅w1)+(x2 ⋅w2)
```

> **NOTE:**  
> Vejam que nós dividimos nosso PDF em vários `chunks (documentos)` e `overlap (100 palavras cada)`.

Agora nós vamos utilizar uma Rede Neural que foi treinada para pegar textos (palavras) e transformar em Embeddings (vetores):

```bash
pip install -U sentence-transformers
```

```bash
pip install -U langchain-huggingface
```

[rag_retriever.py](rag_retriever.py)
```python
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
```

> Continuando, vocês concordam que nós temos que salvar nossos `chunks` em algum banco de dados?

Uma abordagem comum no mundo de IA hoje em dia é utilizar a biblioteca **[FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss)** que é um tipo de arquivo específico para armazenar dados vetoriais:

[rag_retriever.py](rag_retriever.py)
```python
from langchain_community.vectorstores import FAISS

db_path = "faiss_database"  # Database path

if os.path.exists(db_path):
    vectordb = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
    vectordb.add_documents(chunks)
else:
    vectordb = FAISS.from_documents(chunks, embeddings)

vectordb.save_local(db_path)
```

Se você prestar atenção vai ver que foi criado um diretório chamado `faiss_database` onde os `chunks` estarão armazenados. Porém, esses dados estão em binário.

> **Como eu vejo eles agora?**

Bem, eu tenho script simples, só para isso:

<details>

<summary>FAISS to JSON</summary>

<br/>

[faiss.view.py](faiss_database/faiss.view.py)
```python
import os
import json
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Caminho para o banco de dados FAISS
db_path = "faiss_database"

# Instancia os embeddings Hugging Face (gratuito)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Carrega o índice FAISS
db = FAISS.load_local(
    db_path,
    embeddings,
    allow_dangerous_deserialization=True
)

# Acessa o índice e os documentos
faiss_index = db.index
documentos = list(db.docstore._dict.values())

# Constrói os dados
dados = []
for i, doc in enumerate(documentos):
    vetor = faiss_index.reconstruct(i)
    item = {
        "id": i,
        "conteudo": doc.page_content.replace("\n", " ").strip(),
        "vetor_parcial": vetor[:10].tolist()
    }
    dados.append(item)

# Define o caminho completo para salvar o JSON no mesmo diretório do índice
json_path = os.path.join(db_path, "faiss_exportado.json")

# Salva o arquivo JSON
with open(json_path, "w", encoding="utf-8") as jsonfile:
    json.dump(dados, jsonfile, ensure_ascii=False, indent=2)

print(f"Arquivo criado com sucesso.")
```

</details>

Agora se você olhar em [faiss_exportado.json](faiss_database/faiss_exportado.json) vai ver um JSON com os `chunks` armazenados no formato JSON com os seus respectivos vetores.







































































































<!--- ( Implementação ) --->

---

<div id="django-core"></div>

## Criando o projeto "core" do djando

De início vamos começar criando nosso projeto django `core` na `raiz (.)` do nosso projeto:

```bash
django-admin startproject core .
```

> **NOTE:**  
> Para rodar o nosso servidor basta digitar `python manage.py runserver` na raiz do projeto. 




















---

<div id="app-users"></div>

## Criando e configurando o app "users"

> É comum em problemas da *Ciências da Computação* nós dividimos um problema grande em pequenas partes, esse conceito é conhecido como `Dividir para Conquistar`. Por exemplo, para criar um sistema grande como o *Instagram* é interessante nós dividirmmos esse problemas em pequenas partes - No django nós utilizamos o conceito de *"apps"* para dividir nosso problema em partes menores.

Com isso, aqui nós vamos trabalhar na autenticação dos usuários e para isso vamos criar o app `users`:

```bash
python manage.py startapp users
```

Porém, para o django reconhecer esse app, precisamos adicionar ele ao `settings.py` do nosso projeto `core`:

[settings.py](core/settings.py)
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]
```

Agora nós precisamos criar uma `rota/url` para o nosso app `users`. Para isso nós linkamos o arquivo `users/urls.py` do nosso app `users` ao `core/urls.py` do nosso projeto `core`:

[core/urls.py](core/urls.py)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]
```

> **NOTE:**  
> De início o nosso app não vai ter o arquivo `urls.py` pois ele ainda vai ser criado.




















---

<div id="mapping-users-to-register-view"></div>

## Mapeando a rota "users" com a view "register"

Agora nós vamos mapear para quando o usuário clicar na rota/url `users/` ele vai ser redirecionado para a view `register` do nosso app `users`:

[users/urls.py](users/urls.py)
```python
from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]
```

Agora nós precisamos criar o método `register` na view `users/views.py`:

[users/views.py](users/views.py)
```python
from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse("Hello World!")
```

Agora se você for em [http://127.0.0.1:8000/users/register/](http://127.0.0.1:8000/users/register/) você verá a seguinte mensagem **"Hello World!"**.

















































































<!--- ( 🚀 Instalação / Execução local ) --->

---

<div id="settings"></div>

## 🚀 Instalação / Execução local

### Crie e ative o ambiente virtual (recomendado)

```bash
python -m venv environment
```

*LINUX:*  
```bash
source environment/bin/activate
```

*WINDOWS:*  
```bash
source environment/Scripts/activate
```

### Atualize o pip

```bash
python -m pip install --upgrade pip
```

### Instale as dependências

```bash
pip install -U -v --require-virtualenv -r requirements.txt
```





---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
