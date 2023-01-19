# Lemmatization & Part-of-Speech Tagging

## Conteúdo

 - [01 - Introdução a Lemmatization (Lemmatização)](#intro)
 - [02 - Lemmatization (Lemmatização) na prática](#practice-lemmatization)
 - [03 - Introdução ao Part-of-Speech Tagging (marcação de classe gramatical)](#post)

---

<div id="intro"></div>

## 01 - Introdução a Lemmatization (Lemmatização)

> No processamento de linguagem natural, a lematização é a tarefa de normalização de pré-processamento de texto preocupada em trazer as palavras às suas formas de raiz.

A **Lemmatização** é um método para lançar palavras às suas formas de raiz. Este é um processo mais complicado do que *stemming*, porque requer que o método conheça a classe gramatical de cada palavra.

**NOTE:**  
Uma vez que a **Lemmatização** requer a classe gramatical, é uma abordagem menos eficiente do que a *stemming*.

---

<div id="practice-lemmatization"></div>

## 02 - Lemmatization (Lemmatização) na prática

Com a biblioteca NLTK é muito fácil aplicar o conceito de **Lemmatização**. Veja o código abaixo:

[lemmatization.py](src/lemmatization.py)
```python
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer() # Instance.
tokenized = ["NBC", "was", "founded", "in", "1926"]

# Apply Lemmatization.
lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]
print(lemmatized)
```

**OUTPUT:**  
```
['NBC', 'wa', 'founded', 'in', '1926']
```

O resultado da **Lemmatização**, salvo na variável *lemmatized* contém **'wa'**, enquanto o resto das palavras permanecem as mesmas. Não é muito útil.

**NOTE:**  
Isso aconteceu porque a instância **lemmatize** da classe **WordNetLemmatizer** trata cada palavra como um substantivo.

> Para tirar proveito do poder da lematização, precisamos marcar cada palavra em nosso texto com a classe gramatical mais provável.

Vamos ver outro exemplo:

[lemmatization-v2.py](src/lemmatization-v2.py)
```python
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer() # Instance.

populated_island = 'Indonesia was founded in 1945. It contains the most populated island in the world, Java, with over 140 million people.'

tokenized_string = word_tokenize(populated_island)
lemmatized_words = [lemmatizer.lemmatize(token) for token in tokenized_string]

try:
  print(f'A lemmatizer exists: {lemmatizer}')
except:
  print('Expected a variable called `lemmatizer`')
try:
  print(f'Words Tokenized: {tokenized_string}')
except:
  print('Expected a variable called `tokenized_string`')
try:
  print(f'Lemmatized Words: {lemmatized_words}')
except:
  print('Expected a variable called `lemmatized_words`')
```

**OUTPUT:**  
```python
A lemmatizer exists: <WordNetLemmatizer>
Words Tokenized: ['Indonesia', 'was', 'founded', 'in', '1945', '.', 'It', 'contains', 'the', 'most', 'populated', 'island', 'in', 'the', 'world', ',', 'Java', ',', 'with', 'over', '140', 'million', 'people', '.']
Lemmatized Words: ['Indonesia', 'wa', 'founded', 'in', '1945', '.', 'It', 'contains', 'the', 'most', 'populated', 'island', 'in', 'the', 'world', ',', 'Java', ',', 'with', 'over', '140', 'million', 'people', '.']
```

**NOTE:**  
Veja que de todas essas palavras apenas **"was"** foi lematizado para **"wa"**. Isso está acontecendo como nós já sabemos porque, precisamos marcar cada palavra em nosso texto com a classe gramatical mais provável.

---

<div id="post"></div>

## 03 - Introdução ao Part-of-Speech Tagging (marcação de classe gramatical)

> No processamento de linguagem natural, a **marcação de classe gramatical (part-of-speech tagging)** é o processo de atribuir uma classe gramatical a cada palavra em uma string. Usar a classe gramatical pode melhorar os resultados da **Lemmatization (Lemmatização)**.

Para melhorar o desempenho da lematização, precisamos encontrar a classe gramatical para cada palavra em nossa string. Essa pode ser uma tarefa um pouco que complexa (mas nem tanto).

Veja o exemplo abaixo de um código que aplica esse conceito na prática:

[part_of_speech.py](src/part_of_speech.py)
```python
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import Counter
import nltk


def get_part_of_speech(word):

  probable_part_of_speech = wordnet.synsets(word)
  pos_counts = Counter()

  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
  
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech

if __name__ =='__main__':

  lemmatizer = WordNetLemmatizer() # Instance.

  tokenized = ["How", "old", "is", "the", "country", "Indonesia"]
  lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]
  print(lemmatized)
```

**OUTPUT:**  
```python
['How', 'old', 'be', 'the', 'country', 'Indonesia']
```

**NOTE:**  
Como passamos na classe gramatical, **"is"** foi lançado em sua raiz, **"be".** Isso significa que palavras como **"was"** e **"were"** serão convertidas para **be**.

**AGORA VAMOS EXPLICAR ALGUMAS PARTES DO CÓDIGO ACIMA:**  

**1° -** Importamos as seguintes  classes:

 - **wordnet:**
   - É um banco de dados que usamos para contextualizar palavras.
 - **Counter:**
   - É um contêiner que armazena elementos como chaves de dicionário.

```python
from nltk.corpus import wordnet
from collections import Counter
```

**2° -** Dentro da nossa função, usamos a função **wordnet.synsets()** para obter um conjunto de sinônimos para a palavra:

```python
probable_part_of_speech = wordnet.synsets(word)
```

**NOTE:**  
Os sinônimos retornados vêm com sua classe gramatical.

**3° -** Use sinônimos para determinar a parte gramatical mais provável

Em seguida, criamos um objeto **Counter()** e definimos cada valor para a contagem do número de sinônimos que se enquadram em cada classe de palavras:

```python
pos_counts = Counter()
pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
```

**NOTE:**  
Esta linha conta o número de substantivos no conjunto de sinônimos: **n = nouns**.

**4° -**  Retorne a classe gramatical mais comum

Agora que temos uma contagem para cada classe gramatical, podemos usar o método **most_common()** do objeto **pos_counts = Counter()** para encontrar e retornar a classe gramatical mais provável:

```python
most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
```

---

**REFERÊNCIAS:**  
[CodeAcademy - Text Preprocessing](https://www.codecademy.com/learn/text-preprocessing)

---

**Rodrigo Leite -** *drigols*
