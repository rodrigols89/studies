# Large Language Models

## Conteúdo

 - **Fundamentos Teóricos:**
   - [O que são LLMs?](#intro-to-llm)
   - [Como o modelo "entende" linguagem?](#how-understand)
   - [Como LLMs são treinados)](#how-are-trained)
   - [Diferença entre LLMs e modelos tradicionais de NLP](#llm-vs-nlp)
   - [Por que os Transformers revolucionaram o NLP?](#transformers-inovation)
   - [Como funciona o Mecanismo de Attention (Atenção)?](#attention-mechanism)
   - [Exemplos de tarefas resolvidas por LLMs](#llm-examples)
   - [Entendendo "Word Embeddings"](#understanding-word-embeddings)
   - [Word2Vec](#word2vec-idea)
   - [Sliding Window (input-target)](#sliding-window)
 - **Preparação e amostragem de dados (Data preparation & sampling):**
     - [Tokenização de texto (Tokenizing text)](#tokenization)
     - [Convertendo tokens em IDs de token (Converting tokens into token IDs)](#token-id)
     - [Convertendo IDs de tokens em tensores de incorporação (Embeddings)](#token-id-to-tensor)
     - [Criando token embeddings](#creating-token-embeddings)
 - **Mecanismo de atenção (Attention mechanism):**
 - **Arquiteturas de LLMs (LLMs architecture):**
 - **Pré-treinamento (Pretraining):**
 - **Loop de treinamento (Training loop):**
 - **Avaliação do modelo (Model evaluation):**
 - **Carregamento pesos pré-treinados (Load pretrained weights):**
 - **Afinação (Fine-tuning):**
   - **Modelos de classificação (Classification models):**
   - **Assistentes pessoais ou modelos de chat (Personal assistants or chat models):**
 - **Utils:**
   - [read_txt()](#read_txt)
 - [**🚀 Instalação / Execução local**](#settings)
 - [**REFERÊNCIAS**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
- Different topic = "200" Whitespace character.
--->






































































































<!--- ( Fundamentos Teóricos ) --->

---

<div id="intro-to-llm"></div>

## O que são LLMs?

**📘 Definição:**  
LLMs (Large Language Models) são modelos de aprendizado de máquina treinados para **"entender"**, **"gerar"** e **"manipular linguagem natural"**.

> **OBSERVAÇÃO:**  
> Eles são chamados de "grandes" por causa da quantidade massiva de parâmetros (milhões ou bilhões) e por serem treinados em grandes volumes de texto da internet, livros, artigos, fóruns, código-fonte etc.




















---

<div id="how-understand"></div>

### Como o modelo "entende" linguagem?

Na verdade, LLMs não entendem no sentido humano. Eles aprendem probabilidades estatísticas:

> Se eu vejo a frase: "O céu está ___", a palavra mais provável é "azul".  
> Esse "palpite" é feito com base no que ele viu durante o treinamento.





















---

<div id="how-are-trained"></div>

### Como LLMs são treinados

 - **Pré-treinamento (Pretraining):**
   - O modelo é exposto a grandes quantidades de texto e aprende padrões de linguagem por meio de tarefas como **"prever a próxima palavra"** (auto-regressivo) ou **"preencher palavras faltantes"** (máscara).
 - **Ajuste fino (Fine-tuning):**
   - O modelo pode ser adaptado para tarefas específicas, como:
     - Classificação de texto;
     - Tradução;
     - Geração de código;
     - Resumo de documentos.





















---

<div id="llm-vs-nlp"></div>

## Diferença entre LLMs e modelos tradicionais de NLP

 - Antes dos LLMs, os modelos de **NLP** eram **específicos para cada tarefa**, como *análise de sentimentos*, *tradução*, ou *resumo*.
 - Com os **LLMs**, **um único modelo pode ser usado para várias tarefas** com pouco ou nenhum ajuste.

### Comparação Direta

| Característica                  | Modelos Tradicionais de NLP                 | LLMs (Large Language Models)                        |
| ------------------------------- | ------------------------------------------- | --------------------------------------------------- |
| **Arquitetura**                 | Simples (SVM, Regressão, Naive Bayes, RNNs) | Transformer (profundo e em larga escala)            |
| **Treinamento**                 | Um modelo por tarefa                        | Um único modelo para tarefas múltiplas              |
| **Requer feature engineering?** | Sim! Manual e demorado                      | Não. O modelo aprende tudo automaticamente          |
| **Escalabilidade**              | Limitado                                    | Altamente escalável e flexível                      |
| **Precisão/Desempenho**         | OK, mas limitado com grandes volumes        | Alta, especialmente com dados em larga escala       |
| **Entrada/Saída**               | Tipicamente vetores numéricos               | Texto puro (prompts e respostas)                    |
| **Contexto considerado**        | Curto (às vezes só 1 frase)                 | Longo (vários parágrafos ou até milhares de tokens) |
| **Exemplos**                    | TF-IDF + SVM, Word2Vec + LSTM               | GPT, BERT, T5, LLaMA, Claude, Gemini                |

### Explicando com um exemplo

 - **Modelo tradicional (pré-LLM):**
   - Transformar o texto em vetores (TF-IDF, Bag of Words).
   - Treinar um SVM ou uma Regressão Logística para prever o sentimento.
   - Modelo só serve pra essa tarefa.
 - **LLM:**
   - Você escreve:
     - `Classifique o sentimento desta frase: Estou muito feliz hoje!`
   - O modelo responde:
     - `Sentimento: Positivo`
   - **OBSERVAÇÃO:** O mesmo modelo pode também traduzir, resumir, gerar código...

### Vantagens dos LLMs sobre modelos tradicionais

 - ✅ **Generalização:** Um modelo para muitas tarefas;
 - ✅ **Zero-shot & few-shot:** Resolve tarefas com poucas instruções;
 - ✅ Menos dependência de dados rotulados;
 - ✅ Contexto mais longo e melhor compreensão;
 - ✅ Geração de linguagem natural mais fluida.

### Mas os modelos tradicionais morreram?

 - **❌ Não! Eles ainda são úteis quando:**
   - Você tem poucos dados e poucos recursos computacionais;
   - A tarefa é muito específica e não exige interpretação profunda;
   - Você precisa de explicabilidade clara e rápida.





















---

<div id="transformers-inovation"></div>

## Por que os Transformers revolucionaram o NLP?

> Transformers são uma arquitetura introduzida no artigo [**"Attention is All You Need" (2017)**](https://arxiv.org/abs/1706.03762).

**OBSERVAÇÃO:**  
Eles eliminaram a necessidade de processar palavras em sequência como faziam **RNNs** e **LSTMs** — e com isso, permitiram muito mais *"paralelismo"*, *"contexto global"* e *"velocidade"*.

### 🚫 Problema dos modelos anteriores (RNN, LSTM)

 - Processavam tokens um por um (sequencialmente).
 - Sofriam com longas dependências ("o que foi dito 30 palavras atrás?").
 - Eram lentos para treinar.
 - Tinha dificuldade com frases longas e contexto amplo.

### ✅ Como o Transformer resolveu tudo isso?

**A resposta:** Attention Mechanism.

> O modelo aprende a **"prestar atenção"** nas palavras mais importantes do texto — independentemente da posição!

### 🧩 Componentes principais do Transformer

| Componente                    | Função Básica                                                    |
| ----------------------------- | ---------------------------------------------------------------- |
| **Embedding**                 | Converte palavras em vetores numéricos.                          |
| **Self-Attention**            | Calcula a importância de cada palavra em relação às outras.      |
| **Positional Encoding**       | Adiciona informação da posição das palavras (já que é paralelo). |
| **Feedforward Layers**        | Faz transformações profundas nos vetores.                        |
| **Normalization & Residuals** | Ajudam a estabilizar e melhorar o aprendizado.                   |





















---

<div id="attention-mechanism"></div>

## Como funciona o Mecanismo de Attention (Atenção)?

> O mecanismo de atenção permite que o modelo **"foque" em partes importantes da entrada** — como humanos fazem ao ler.

Por exemplo, imagine que nós temos a frase:

Imagine a frase:

> “A maçã estava azeda, então ela foi jogada fora.”

 - A palavra **"ela"** poderia se referir à **maçã** ou à **azeda**.
 - O modelo precisa **“prestar atenção”** nas palavras relevantes para entender corretamente.

### 🧮 Fórmula matemática (simples)

A fórmula matemática (simples) é a seguinte:

$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$

 - `QKᵀ`
   - Compara (multiplica) os queries com os keys → gera pontuações de atenção.
 - `/ √d_k`
   - Normaliza para evitar explosões numéricas.
 - `softmax`
   - Transforma em probabilidades.
 - `× V`
   - Gera a atenção ponderada, ou seja, a saída final.

### 🔢 Exemplo numérico ilustrativo

```bash
Frase: ["O", "gato", "correu"]

→ Para "correu", o modelo calcula:

Q(correu) • K(O)     →  baixa atenção
Q(correu) • K(gato)  →  alta atenção
Q(correu) • K(correu)→  média atenção
```

> **Resultado:**  
> O modelo vai ponderar mais o **"gato"**, porque **"gato correu"** tem uma relação forte.





















---

<div id="llm-examples"></div>

### Exemplos de tarefas resolvidas por LLMs

Vamos começar com uma introdução de algumas tarefas que podem ser resolvidas utilizando **"LLMs"**:

| Tarefa                      | Exemplo prático                             |
| --------------------------- | ------------------------------------------- |
| **Geração de texto**        | Chatbots, redação automática                |
| **Classificação**           | Análise de sentimentos, spam vs. não spam   |
| **Tradução**                | Inglês → Português, etc.                    |
| **Perguntas e Respostas**   | Assistente de dúvidas                       |
| **Resumo automático**       | Resumir longos artigos                      |
| **Extração de informações** | Pegar nomes, datas, eventos de um texto     |
| **Geração de código**       | Auto-complete em IDEs, explicação de código |

### 🚀 Aplicações Reais das LLMs

| **Área**                   | **Aplicação**                                                                                       |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| **Assistentes virtuais**   | Chatbots inteligentes (ex: ChatGPT, Google Bard, Alexa)                                             |
| **Educação**               | Tutores personalizados, correção automática de redações, explicações sob demanda                    |
| **Saúde**                  | Análise de prontuários, resposta a perguntas médicas, apoio à decisão clínica                       |
| **Atendimento ao cliente** | Respostas automáticas, suporte 24/7, resumo de interações com usuários                              |
| **Pesquisa e ciência**     | Síntese de artigos, geração de hipóteses, revisão automática de literatura                          |
| **Programação**            | Autocompletar código, explicar funções, gerar trechos em diferentes linguagens (ex: GitHub Copilot) |
| **Tradução de idiomas**    | Traduções contextuais e multilíngues, com adaptação ao domínio específico                           |
| **Criação de conteúdo**    | Geração de artigos, roteiros, marketing, posts para redes sociais                                   |
| **Direito**                | Análise de contratos, extração de cláusulas, sumarização de decisões legais                         |
| **Análise de sentimentos** | Classificação de avaliações e sentimentos em redes sociais e e-commerce                             |
| **Segurança cibernética**  | Explicação de exploits, análise de logs e geração de alertas                                        |
| **Games e NPCs**           | Diálogos gerados dinamicamente, comportamentos inteligentes, roteiros                               |

### 📈 Exemplos Reais de Impacto com LLMs

| **Organização / Produto** | **Uso de LLMs**                                                                          |
| --------------------------|------------------------------------------------------------------------------------------|
| `Duolingo`                | Feedback em tempo real sobre frases escritas por alunos com explicações contextualizadas |
| `Notion AI`               | Geração e reformulação de textos, resumos automáticos, criação de tarefas                |
| `Khan Academy (GPT-4)`    | Tutor personalizado que responde dúvidas dos alunos com explicações passo a passo        |
| `GitHub Copilot`          | Sugestões de código em tempo real, explicações de funções, geração de testes             |
| `GrammarlyGO`             | Reescrita e aprimoramento de textos com base no contexto do usuário                      |
| `Legal Robot`             | Análise de contratos com explicação em linguagem natural das cláusulas jurídicas         |
| `You.com (YouChat)`       | Motor de busca com respostas geradas por LLM, integrando fontes e interatividade         |





















---

<div id="understanding-word-embeddings"></div>

## Entendendo "Word Embeddings"

 - Modelos de Deep Learning, incluindo LLMs, não podem processar texto bruto diretamente;
 - Como o texto é categórico, ele não é compatível com as operações matemáticas utilizadas para implementar e treinar redes neurais;
 - Portanto, precisamos de uma forma de representar palavras como vetores com valores contínuos.

> **OBSERVAÇÃO:**  
> O conceito de converter dados (áudio, vídeo, texto) para o formato de vetor (numérico) é frequentemente chamado de **"embedding"**.

Por exemplo:

![img](images/word-embeddings-01.png)  

> **OBSERVAÇÃO:**  
> No entanto, é importante observar que diferentes formatos de dados exigem *modelos de embbedding* distintos.  
> Por exemplo, um modelo de embedding projetado para texto não seria adequado para embbedding de dados de áudio ou vídeo.





















---

<div id="word2vec-idea"></div>

## Word2Vec

> A principal *ideia* por trás do **Word2Vec** é que *"palavras que aparecem em contextos semelhantes tendem a ter significados semelhantes"*.

Consequentemente, quando projetadas em embeddings de palavras bidimensionais para fins de visualização, palavras semelhantes ficam agrupadas.

![img](images/word2vec-idea-01.png)  





















---

<div id="sliding-window"></div>

## Sliding Window (input-target)

Como já aprendemos, alguns LLMs são pré-treinados para **prever da próxima palavra em um texto**, por exemplo:

![img](images/sliding-window-01.png)  

Vamos ver um exemplo mais fácil:

```python
"O rato roeu a roupa do rei de Roma"
```

**Tokenizado:**
```python
tokens = ["O", "rato", "roeu", "a", "roupa", "do", "rei", "de", "Roma"]
```

Agora, criamos pares `input → target` com *Sliding Window*:

| Input                                                    | Target    |
| -------------------------------------------------------- | --------- |
| `["O"]`                                                  | `"rato"`  |
| `["O", "rato"]`                                          | `"roeu"`  |
| `["O", "rato", "roeu"]`                                  | `"a"`     |
| `["O", "rato", "roeu", "a"]`                             | `"roupa"` |
| `["O", "rato", "roeu", "a", "roupa"]`                    | `"do"`    |
| `["O", "rato", "roeu", "a", "roupa", "do"]`              | `"rei"`   |
| `["O", "rato", "roeu", "a", "roupa", "do", "rei"]`       | `"de"`    |
| `["O", "rato", "roeu", "a", "roupa", "do", "rei", "de"]` | `"Roma"`  |

### 🧠 Como o modelo aprende?

O modelo recebe o **input (lista de tokens)** e é treinado para prever o **target (próximo token)**. Isso é a base do aprendizado de linguagem.

### ✅ Resumo

| Conceito            | Explicação                                                   |
| ------------------- | ------------------------------------------------------------ |
| **O que é?**        | Técnica que divide texto longo em blocos sobrepostos         |
| **Para que serve?** | Permitir input contínuo para LLMs com limitação de tokens    |
| **Quando usar?**    | Em textos longos, geração de texto, fine-tuning              |
| **Quando evitar?**  | Quando o modelo aceita entradas longas ou a tarefa é pequena |







































































































<!--- ( Preparação e amostragem de dados (Data preparation & sampling) ) --->

---

<div id="tokenization"></div>

## Tokenização de texto (Tokenizing text)

> Aqui, vamos discutir como podemos dividir uma entrada texto em *tokens* individuais, uma etapa de pré-processamento necessária para criar *embeddings* para um *LLM*.

Esses tokens são palavras individuais ou caracteres especiais, incluindo sinais de pontuação, conforme mostrado abaixo:

![img](images/tokenizing-01.png)  

Vamos ver como implementar isso na prática:

<!--- ( Transformers (Hugging Face) ) --->
<details>

<summary>Transformers (Hugging Face)</summary>

</br>

Para criar tokens com a biblioteca biblioteca [🤗 Transformers (Hugging Face)](https://github.com/huggingface/transformers) vamos utilizar o tokenizador `AutoTokenizer` com o modelo `bert-base-uncased`:

[transformers_tokenizers.py](src/transformers_tokenizers.py)
```python
from transformers import AutoTokenizer

from utils import read_txt


# load the BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load the and read the text
file_path = "../datasets/the-verdict.txt"
text = read_txt(file_path)

# Tokenization
tokens = tokenizer.tokenize(text)

print("Total number of tokens (without whitespaces):", len(tokens))
print("Tokens (first 10):", tokens[:10])
```

**OUTPUT:**  
```bash
Total number of tokens (without whitespaces): 5212
Tokens (first 10): ['i', 'had', 'always', 'thought', 'jack', 'gi', '##sb', '##urn', 'rather', 'a']
```

> **Por que nós temos mais tokens utilizando o tokenizador da Hugging Face?**

### 🧠 Diferença fundamental: Subword Tokenization

O **BERT** não usa tokenização por palavras ou pontuações simples. Ele usa um método chamado:

> **👉 WordPiece Tokenization:**  
> Palavras desconhecidas ou raras são quebradas em subpartes, chamadas *"subwords"*.

Por exemplo:

```bash
'Gisburn' → ['gi', '##sb', '##urn']
```

A ideia é balancear entre:

 - Cobertura de vocabulário (poucos tokens desconhecidos);
 - Tamanho do vocabulário (tornar o modelo mais eficiente).

### `🧠 O que são esses ##?`

 - No **BERT**, os tokens que começam com `##` são subpalavras que continuam uma palavra anterior.
 - Por exemplo:
   - `gi` é o começo da palavra `Gisburn`;
   - ``##sb`` e ``##urn`` são subpalavras que continuam `gi` até formar `gi + sb + urn = Gisburn`.

Esse tipo de tokenização:

 - Reduz o número de palavras *OOV (out-of-vocabulary)*;
 - Garante que até palavras não vistas no treinamento ainda sejam entendidas em partes.

### 📌 Outros detalhes que aumentam a contagem no BERT:

| Fator                                 | Explicação                                                                        |
| ------------------------------------- | --------------------------------------------------------------------------------- |
| **Subwords**                          | Palavras como `Gisburn`, `unbelievable` viram várias partes                       |
| **Lowercasing**                       | O `bert-base-uncased` transforma tudo em minúsculo antes de tokenizar             |
| **Tokens especiais (em outros usos)** | `[CLS]`, `[SEP]` etc. (no seu caso não estão aparecendo porque você só tokenizou) |
| **Sem filtragem de pontuação**        | O tokenizer BERT inclui pontuações como tokens próprios (`.`, `,`, etc.)          |

### ✅ Conclusão

| Tokenizador          | Tipo de tokenização            | Total de tokens | Exemplo                 |
| -------------------- | ------------------------------ | --------------- | ----------------------- |
| `Seu (com re.split)` | Baseado em pontuação e espaços | 4690            | `'Gisburn'`             |
| `BERT ("WordPiece")` | Subword Tokenization           | 5212            | `'gi', '##sb', '##urn'` |

> **OBSERVAÇÃO:**  
> O BERT gera mais tokens porque ele quebra palavras em partes menores que estão no vocabulário aprendido durante o pré-treinamento. Isso permite lidar melhor com palavras raras ou compostas.

</details>





















---

<div id="token-id"></div>

## Convertendo tokens em IDs de token (Converting tokens into token IDs)

Aqui nós vamos ver o processo de atribuir um ID numérico único para cada token (palavra, subpalavra ou símbolo) com base em um vocabulário fixo do modelo.

### 📘 O que é "Vocabulário" em LLMs?

No contexto de Modelos de Linguagem (LLMs), o vocabulário é a lista de todos os tokens que o modelo conhece.

**✅ Cada token tem:**

 - Uma forma textual (ex: "hello", "##ing", "!")
 - Um ID único (ex: 101, 1254, 999)

> **OBSERVAÇÃO:**  
> Esse vocabulário é definido antes do treinamento do modelo, geralmente criado com base em um grande corpus de texto.

### 🧠 Por que esse vocabulário é importante?

Porque o modelo só consegue processar textos usando os *tokens* do seu *vocabulário*. Se uma palavra não estiver nele, será dividida em subpalavras ou marcada como token desconhecido ([UNK]).

Por exemplo, imagine que temos o seguinte texto como entrada:

**Entrada (Input):**
```python
I love learning because I love new things
```

| Token      | Token ID |
| ---------- | -------- |
| `[PAD]`    | 0        |
| `[UNK]`    | 1        |
| `i`        | 2        |
| `love`     | 3        |
| `learning` | 4        |
| `because`  | 5        |
| `new`      | 6        |
| `things`   | 7        |

**🧮 Tokenização (simples):**
```python
tokens = ['i', 'love', 'learning', 'because', 'i', 'love', 'new', 'things']
```

> **OBSERVAÇÃO:**  
> Mesmo que as palavras **"i"** e **"love"** apareçam mais de uma vez, elas serão tokenizadas da mesma forma, pois o vocabulário é estático.

**🔢 Conversão para Token IDs:**
```python
token_ids = [2, 3, 4, 5, 2, 3, 6, 7]
```

| Palavra      | Token      | Token ID |
| ------------ | ---------- | -------- |
| **I**        | `i`        | 2        |
| **love**     | `love`     | 3        |
| **learning** | `learning` | 4        |
| **because**  | `because`  | 5        |
| **I**        | `i`        | 2        |
| **love**     | `love`     | 3        |
| **new**      | `new`      | 6        |
| **things**   | `things`   | 7        |

**✅ Observações:**

 - Tokens repetidos (como "i" e "love") continuam recebendo o mesmo ID.
 - O modelo trata repetições de **forma contextual**:
   - Ou seja, mesmo com o mesmo token ID, o significado pode *"mudar dependendo do contexto anterior"*.

Agora vamos ver como implementar isso na prática:

<!--- ( Transformers (Hugging Face) ) --->
<details>

<summary>Transformers (Hugging Face)</summary>

</br>

Com a biblioteca **transformers (Hugging Face)** podemos utilizar a função `tokenizer.get_vocab()` para pegar o vocaculário dos tokens:

[transformers_tokenizers.py](src/transformers_tokenizers.py)
```python
from transformers import AutoTokenizer

from utils import read_txt


# load the BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load the and read the text
file_path = "../datasets/the-verdict.txt"
text = read_txt(file_path)

tokens = tokenizer.tokenize(text)   # Tokenize the text
vocabulary = tokenizer.get_vocab()  # Get the vocabulary

print("Vocabulary type:", type(vocabulary))
for voc in list(vocabulary.items())[:10]:
    print(voc)
```

**OUTPUT:**
```bash
Vocabulary type: <class 'dict'>
('women', 2308)
('[unused452]', 457)
('sponsorship', 12026)
('devout', 26092)
('william', 2520)
('glide', 21096)
('referees', 25118)
('handball', 12378)
('1950s', 4856)
('treated', 5845)
```

</details>





















---

<div id="token-id-to-tensor"></div>

## Convertendo IDs de tokens em tensores de incorporação (Embeddings)

Converter os IDs de tokens em *tensores de incorporação ("Embeddings")* é a última etapa da preparação antes do modelo propriamente dito (LLM) processar os dados.

Vamos ver como fazer isso na prática:

<!--- ( PyTorch ) --->
<details>

<summary>Transformers (PyTorch)</summary>

<br/>

Para transformar os IDs de tokens em tensores, você só precisa ajustar o parâmetro `return_tensors="pt" (para utilizar PyTorch)`: 

[embeddings_pytorch.py](src/embeddings_pytorch.py)
```python
# encode process = here we tokenize + convert to IDs
encoding = tokenizer.encode_plus(
    text,
    add_special_tokens=True,
    return_tensors="pt",      # pt = Pytorch
    truncation=True,
    padding=False
)

input_ids = encoding["input_ids"]
token_type_ids = encoding["token_type_ids"]
attention_mask = encoding["attention_mask"]

print("Tensor input_ids shape:", input_ids.shape)
print("Tensor token_type_ids shape:", token_type_ids.shape)
print("Tensor attention_mask shape:", attention_mask.shape)
```

**OUTPUT:**
```bash
Tensor input_ids shape: torch.Size([1, 512])
Tensor token_type_ids shape: torch.Size([1, 512])
Tensor attention_mask shape: torch.Size([1, 512])
```

> **NOTE:**  
> Vejam que agora nós temos **PyTorch tensores**.

</details>

<!--- ( TensorFlow ) --->
<details>

<summary>Transformers (TensorFlow)</summary>

<br/>

Para transformar os IDs de tokens em tensores, você só precisa ajustar o parâmetro `return_tensors="tf" (para utilizar TensorFlow)`: 

[embeddings_tensorflow.py](src/embeddings_tensorflow.py)
```python
encoding = tokenizer.encode_plus(
    text,
    add_special_tokens=True,
    return_tensors="tf",      # tf = Tensorflow
    truncation=True,
    padding=False
)

input_ids = encoding["input_ids"]
token_type_ids = encoding["token_type_ids"]
attention_mask = encoding["attention_mask"]

print("Tensor input_ids shape:", input_ids[0, :10])
print("Tensor token_type_ids shape:", token_type_ids[0, :10])
print("Tensor attention_mask shape:", attention_mask[0, :10])
```

**OUTPUT:**
```bash
Tensor input_ids shape: tf.Tensor([  101  1045  2018  2467  2245  2990 21025 19022 14287  2738], shape=(10,), dtype=int32)
Tensor token_type_ids shape: tf.Tensor([0 0 0 0 0 0 0 0 0 0], shape=(10,), dtype=int32)
Tensor attention_mask shape: tf.Tensor([1 1 1 1 1 1 1 1 1 1], shape=(10,), dtype=int32)
```

> **NOTE:**  
> Vejam que agora nós temos **TensorFlow tensores**.

</details>





















---

<div id="creating-token-embeddings"></div>

## Criando token embeddings

Token Embedding é o processo de transformar:

 - Tokens *inteiros* (IDs):
   - Que são números inteiros representando palavras ou subpalavras.
 - Em vetores densos de *números reais*.

Esse processo é essencial para que os modelos de linguagem (LLMs) possam trabalhar com texto de forma numérica.

Por exemplo:

**Exemplo-01:**  
```bash
token_id  = 1037     # "a" no BERT tokenizer.
embedding = [0.1, 0.5, ..., -0.2]  # vetor de 768 dimensões.
```

<br/>

**Exemplo-02:**  
![img](images/token-embedding-01.png)  

<br/>

**Exemplo-03:**  
![img](images/token-embedding-02.png)  

### 🧠 Por que isso é importante?

Redes neurais não entendem palavras ou números inteiros diretamente — elas precisam de *vetores contínuos* que capturam semântica, contexto e relação entre palavras. Embeddings fazem essa ponte.

### 🚫 Quando não utilizar?

 - ❌ Se estiver usando um modelo pré-treinado completo (ex: AutoModel do Hugging Face) — os embeddings já estão lá.
 - ❌ Se estiver apenas tokenizando e não treinando nenhum modelo.

Vamos ver como fazer isso na prática:

<details>

<summary>Transformer + PyTorch</summary>

<br/>

[token_embedding_pytorch.py](src/token_embedding_pytorch.py)
```python
import torch
from transformers import AutoTokenizer

from utils import read_txt


# load the BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load the and read the text
file_path = "../datasets/the-verdict.txt"
text = read_txt(file_path)

# encode process = here we tokenize + convert to IDs
encoding = tokenizer.encode_plus(
    text,
    add_special_tokens=True,  # Add [CLS], [SEP]
    return_tensors="pt",      # pt = Pytorch
    truncation=True,          # Truncates if too long
    padding=False             # Do not add padding
)

# Get the input IDs
input_ids = encoding["input_ids"]

vocab_size = tokenizer.vocab_size     # vocab size
embedding_dim = 768                   # embedding dim

# Create embedding layer
embedding_layer = torch.nn.Embedding(vocab_size, embedding_dim)

print("Layer dimensions (shape):", embedding_layer.weight.shape)
print("\nFirst token embedding dimension (shape):", embedding_layer.weight[0].shape)
print("\nFirst token embedding value (tensor):", embedding_layer.weight[0][:20])
```

#### Explicação do Código

 - `vocab_size = tokenizer.vocab_size`
   - Obtém o número total de tokens únicos no vocabulário do tokenizador `BERT (bert-base-uncased)`.
   - **Exemplo:** Se o `vocab_size` for 30.522 (que é o nosso caso), significa que existem 30.522 tokens distintos (palavras, subpalavras, pontuações, etc.) que o modelo entende.
 - `embedding_dim = 768`
   - Define a dimensão dos vetores de embedding.
   - **Por que 768?** Essa é a dimensão usada pelo modelo BERT-base (cada token é representado como um vetor de 768 números).
 - `embedding_layer = torch.nn.Embedding(vocab_size, embedding_dim)`
   - **O que faz:** Cria uma camada de embedding do PyTorch.
   - **Como funciona internamente:** É como uma *"tabela de lookup"* que, dado um *token_id (um número entre 0 e vocab_size-1)*, retorna um vetor de tamanho *embedding_dim (nesse caso, 768)*.
   - **Inicialização:** Os vetores são inicializados aleatoriamente (a menos que você carregue pesos pré-treinados).
 - `O que tem dentro de embedding_layer?`
   - A principal coisa que ele contém é a tabela de embeddings – uma matriz de pesos onde cada linha representa o vetor associado a um token:
     - `Linha[0]:` 768 pesos (weight) para o token 0.
     - `Linha[1]:` 768 pesos (weight) para o token 1.
     - ...
     - `Linha[vocab_size-1]:` 768 pesos (weight) para o token `vocab_size-1`.

**OUTPUT:**
```bash
Layer dimensions (shape): torch.Size([30522, 768])

First token embedding dimension (shape): torch.Size([768])

First token embedding value (tensor): tensor([-0.2344, -0.0046, -2.6109, -1.0261,  0.7495, -0.0959,  2.9716, -1.6094,
        -0.1729,  0.0674, -0.6070, -1.8236,  1.1297,  0.4856, -1.7770, -0.8983,
        -1.3048, -1.2164, -0.1922, -0.0672], grad_fn=<SliceBackward0>)
```

Vejam que:

 - `print("Layer dimensions (shape):", embedding_layer.weight.shape)`
   - Aqui nós temos uma camada embedding com 30.522 tokens, cada um com 768 valores (pesos/weights):
     - Como nós sabemos esse valores (pesos/weights) foram inicializados aleatoriamente.
 - `print("\nFirst token embedding dimension (shape):", embedding_layer.weight[0].shape)`
   - Aqui nós estamos exibindo as dimensões do primeiro token (palavra única) na tabela de embeddings:
     - Nada mas do que uma lista com 768 valores (pesos/weights), *reais*.
 - `print("First token embedding value (tensor):", embedding_layer.weight[0][:20])`
   - Aqui nós estamos exibindo os 20 pesos (weights) do primeiro token (palavra única) da camada de embedding.

Você pode explorar mais detalhes da nossa camada embedding utilizando:

```python
print(embedding_layer.__dict__)
```

**OUTPUT:**
```bash
{'training': True, '_parameters': {'weight': Parameter containing:
tensor([[ 1.2361,  1.0225, -1.2596,  ...,  0.4168,  1.4311,  0.3879],
        [-0.7385,  0.5236, -1.4423,  ...,  1.0549, -2.3647,  1.2509],
        [ 0.8065,  0.5177, -0.0426,  ..., -0.4130,  0.5765, -0.4022],
        ...,
        [-1.2222, -0.8426,  0.2170,  ..., -0.6425,  0.9004, -1.2794],
        [-0.8202,  0.8905, -0.0465,  ..., -0.2120,  0.7153,  0.7043],
        [ 0.8098,  0.1132,  1.3992,  ...,  0.1763, -0.0457, -0.0235]],
       requires_grad=True)}, '_buffers': {}, '_non_persistent_buffers_set': set(), '_backward_pre_hooks': OrderedDict(), '_backward_hooks': OrderedDict(), '_is_full_backward_hook': None, '_forward_hooks': Order
edDict(), '_forward_hooks_with_kwargs': OrderedDict(), '_forward_hooks_always_called': OrderedDict(), '_forward_pre_hooks': OrderedDict(), '_forward_pre_hooks_with_kwargs': OrderedDict(), '_state_dict_hooks': O
rderedDict(), '_state_dict_pre_hooks': OrderedDict(), '_load_state_dict_pre_hooks': OrderedDict(), '_load_state_dict_post_hooks': OrderedDict(), '_modules': {}, 'num_embeddings': 30522, 'embedding_dim': 768, 'p
adding_idx': None, 'max_norm': None, 'norm_type': 2.0, 'scale_grad_by_freq': False, 'sparse': False}
```

> **OBSERVAÇÃO:**  
> Vejam que aqui nós podemos ver todos os parâmetros e atributos da camada embedding.

</details>



<!--- ( TensorFlow ) --->
<details>

<summary>Transformers + TensorFlow</summary>

<br/>

[token_embedding_tensorflow.py](src/token_embedding_tensorflow.py)
```python
import tensorflow as tf
from transformers import AutoTokenizer

from utils import read_txt

# Load the BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Read the input text
file_path = "../datasets/the-verdict.txt"
text = read_txt(file_path)

# Tokenize and convert text to input IDs
encoding = tokenizer.encode_plus(
    text,
    add_special_tokens=True,   # Add [CLS] and [SEP] tokens
    return_tensors="tf",       # Use TensorFlow tensors
    truncation=True,           # Truncate if the text is too long
    padding=False              # Do not apply padding
)

# Get input IDs
input_ids = encoding["input_ids"]  # shape: (1, seq_len)

# Define vocabulary size and embedding dimension
vocab_size = tokenizer.vocab_size
embedding_dim = 768  # BERT-base uses 768-dimensional embeddings

# Create the embedding layer
embedding_layer = tf.keras.layers.Embedding(
    input_dim=vocab_size,
    output_dim=embedding_dim
)

# Apply embedding lookup on input IDs
embedded_tokens = embedding_layer(input_ids)  # shape: (1, seq_len, 768)

# Print information about the embedding layer
print("Layer dimensions (shape):", embedding_layer.weights[0].shape)
print("\nFirst token embedding dimension (shape):", embedding_layer.weights[0][0].shape)
print("\nFirst token embedding value (tensor):", embedding_layer.weights[0][0][:20])
```

**OUTPUT:**
```bash
Layer dimensions (shape): (30522, 768)

First token embedding dimension (shape): (768,)

First token embedding value (tensor): tf.Tensor(
[-0.04233279 -0.0479785  -0.00253046 -0.02014258  0.01921842 -0.02670938
  0.01929888  0.0185066   0.01841432 -0.04865185  0.01238776 -0.0382238
 -0.00538279  0.0330565  -0.01576235 -0.03277471  0.02024061 -0.03092581
 -0.02762043  0.00779605], shape=(20,), dtype=float32)
```

</details>







































































































<!--- ( Utils ) --->

---

<div id="read-txt"></div>

## read_txt()

Aqui nós vamos aprender como ler um arquivo de texto no formato `.txt`:

<!--- ( Python (From Scratch) ) --->
<details>

<summary>Python (From Scratch)</summary>

</br>

[utils.py](src/utils.py)
```python
import re


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


if __name__ == "__main__":

    file_path = "../datasets/the-verdict.txt"
    text = read_txt(file_path)

    print("Total number of characters:", len(text))
    print("Text type:", type(text), "\n")
```

**OUTPUT:**
```bash
Total number of characters: 20479
Text type: <class 'str'> 
```

> **OBSERVAÇÃO:**  
> Podemos usar o conceito **fatiamento (slicing)** para selecionar uma parte específica do texto.

```python
print(text[:353])
```

**OUTPUT:**
```bash
I HAD always thought Jack Gisburn rather a cheap genius--though a good fellow enough--so it was no great surprise to me to hear that, in the height of his glory, he had dropped his painting, married a rich widow, and established himself in a villa on the Riviera. (Though I rather thought it would have been Rome or Florence.)

"The height of his glory"
```

</details>







































































































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










<!--- ( REFERÊNCIAS ) --->

---

<div id="ref"></div>

## REFERÊNCIAS

 - **AI Agents:**
   - [ChatGPT](https://chat.openai.com/)
 - **Books:**
   - [Build a Large Language Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**





<details>

<summary></summary>

<br/>

[](src/)
```python

```

**OUTPUT:**
```bash

```

</details>
