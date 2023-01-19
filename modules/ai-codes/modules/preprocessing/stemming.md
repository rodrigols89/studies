# Stemming

## Conteúdo

 - [01 - Introdução ao Stemming](#intro)
 - [02 - Stemming com a biblioteca NLTK](#nltk-stemming)

---

<div id="intro"></div>

## 01 - Introdução ao Stemming

> No processamento de linguagem natural, **Stemming** é a tarefa de normalização de pré-processamento de texto preocupada com a remoção direta dos *afixos* de palavras *(prefixos e sufixos)*.

Por exemplo, o **Stemming** trocaria a palavra **“going”** por **“go”**. Este é um método comum usado por mecanismos de pesquisa para melhorar a correspondência entre a entrada do usuário e os acessos ao site.

---

<div id="nltk-stemming"></div>

## 02 - Stemming com a biblioteca NLTK

> A biblioteca NLTK tem um Stemming integrado chamado **PorterStemmer**.

Na prática nós podemos aplicar o conceito de **Stemming** mais ou menos assim, com a biblioteca **NLTK** e **PorterStemmer**:

[porterstemmer.py](src/porterstemmer.py)
```python
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

tokenized = [
  'NBC',
  'was',
  'founded',
  'in',
  '1926',
  '.',
  'This',
  'makes',
  'NBC',
  'the',
  'oldest',
  'major',
  'broadcast',
  'network',
  '.'
]

stemmed = [stemmer.stem(token) for token in tokenized]
print(stemmed)
```

**OUTPUT:**  
```python
['nbc', 'wa', 'found', 'in', '1926', '.', 'thi', 'make', 'nbc', 'the', 'oldest', 'major', 'broadcast', 'network', '.']
```

**NOTE:**  
Opa, mas quais palavras foram aplicadas **Stemming**?

 - Primeiro, não sei se você reparou, mas todas as letras foram colocadas em minúsculo.
 - was > wa
 - founded > found
 - this > thi
 - makes > make

**NOTE:**  
O fato de essas palavras terem sido reduzidas é útil para muitos aplicativos de processamento de linguagem. No entanto, você precisa ter cuidado ao definir o **stemming** das strings, porque as palavras geralmente podem ser convertidas em algo irreconhecível.

---

**REFERÊNCIAS:**  
[CodeAcademy - Text Preprocessing](https://www.codecademy.com/learn/text-preprocessing)

---

**Rodrigo Leite -** *drigols*
