# Tokenization (tokenização)

## Conteúdo

 - [01 - Introdução ao Tokenization (Tokenização)](#intro)
 - [02 - Tokenization (tokenização) com a biblioteca NLTK (Natural Language Toolkit)](#tokenization-nltk)
 - [03 - Tokenization (tokenização) por sentenças](#sent-tokenize)

---

<div id="intro"></div>

## 01 - Introdução ao Tokenization (Tokenização)

> No processamento de *linguagem natural*, **Tokenization (Tokenização)** é a tarefa de pré-processamento de texto que divide o texto em componentes menores de texto *(conhecidos como tokens)*.

Para muitas tarefas de processamento de linguagem natural, precisamos acessar cada palavra em uma string. Para acessar cada palavra, primeiro temos que dividir o texto em componentes menores. O método para quebrar o texto em componentes menores é chamado de **Tokenization (Tokenização)** e os componentes individuais são chamados de **tokens**.

Algumas operações comuns que exigem tokenização incluem:

 - Descobrir quantas palavras ou frases aparecem no texto;
 - Determinar quantas vezes uma palavra ou frase específica existe;
 - Contabilização de quais termos são susceptíveis de co-ocorrer...

**NOTE:**  
Embora os **tokens** sejam geralmente palavras ou termos individuais, eles também podem ser frases ou pedaços de texto de outro tamanho.

---

<div id="tokenization-nltk"></div>

## 02 - Tokenization (tokenização) com a biblioteca NLTK (Natural Language Toolkit)

Para **tokenizar** palavras individuais, podemos usara função **word_tokenize()** da biblioteca **NLTK (Natural Language Toolkit)**.

A função aceita uma string e retorna uma lista de palavras. Veja um exemplo simples abaixo:

[tokenization.py](src/tokenization.py)
```python
from nltk.tokenize import word_tokenize

text = "Tokenize this text"
tokenized_by_word = word_tokenize(text)

print(tokenized_by_word)
```

**OUTPUT:**
```python
['Tokenize', 'this', 'text']
```

**NOTE:**  
Veja que nós *separamos (tokenizamos)* o texto por palavras.

---

<div id="sent-tokenize"></div>

## 03 - Tokenization (tokenização) por sentenças

Se eu desejar aplicar uma **Tokenization (tokenização)** por sentença. Por exemplo, separando por vírgula ou pontuações?

Simples, para isso basta utilizar o método **sent_tokenize()** da classe **nltk.tokenize**:

[sent_tokenize.py](src/sent_tokenize.py)
```python
from nltk.tokenize import sent_tokenize

text = "So, during test time, any word that is not present in the vocabulary will be mapped to a UNK token. This is how we can tackle the problem of OOV in word tokenizers."
tokenized_by_sentence = sent_tokenize(text)

print(tokenized_by_sentence)
```

**OUTPUT:**  
```python
['So, during test time, any word that is not present in the vocabulary will be mapped to a UNK token.', 'This is how we can tackle the problem of OOV in word tokenizers.']
```

**NOTE:**  
Veja que agora nós aplicamos uma *separção Tokenization (tokenização)*, porém, por sentença.













---

**REFERÊNCIAS:**  
[CodeAcademy - Text Preprocessing](https://www.codecademy.com/learn/text-preprocessing)

---

**Rodrigo Leite -** *drigols*
