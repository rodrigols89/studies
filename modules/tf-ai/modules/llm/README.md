# Large Language Models

## Conteúdo

 - **Introdução a LLMs:**
   - [O que são LLMs?](#intro-to-llm)
   - [Como o modelo "entende" linguagem?](#how-understand)
   - [Como LLMs são treinados)](#how-are-trained)
   - [Diferença entre LLMs e modelos tradicionais de NLP](#llm-vs-nlp)
   - [Por que os Transformers revolucionaram o NLP?](#transformers-inovation)
   - [Como funciona o Mecanismo de Attention (Atenção)?](#attention-mechanism)
   - [Exemplos de tarefas resolvidas por LLMs](#llm-examples)
 - [**🚀 Instalação / Execução local**](#settings)
 - [**REFERÊNCIAS**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
- Different topic = "200" Whitespace character.
--->






































































































<!--- ( Introdução a LLMs ) --->

---

<div id="intro-to-llm"></div>

## O que são LLMs?

**📘 Definição:**  
LLMs (Large Language Models) são modelos de aprendizado de máquina treinados para **"entender"**, **"gerar"** e **"manipular linguagem natural"**.

> **NOTE:**  
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
   - **NOTE:** O mesmo modelo pode também traduzir, resumir, gerar código...

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

**NOTE:**  
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






































































































<!--- ( Arquitetura do Transformer: Encoder e Decode ) --->

---





   - [](#)


































































































<!--- ( 🚀 Instalação / Execução local ) --->

---

<div id="settings"></div>

## 🚀 Instalação / Execução local

*Crie e ative o ambiente virtual (recomendado):**  

```bash
python -m venv environment
```

**LINUX:**  
```bash
source environment/bin/activate
```

**WINDOWS:**  
```bash
source environment/Scripts/activate
```

**ATUALIZE O PIP:**
```bash
python -m pip install --upgrade pip
```

**Instale as dependências:**  

```bash
pip install -U -v --require-virtualenv -r requirements.txt
```










<!--- ( REFERÊNCIAS ) --->

---

<div id="ref"></div>

## REFERÊNCIAS

 - [ChatGPT](https://chat.openai.com/)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

<!--->

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[](src/)
```python

```

</details>

<br/>
