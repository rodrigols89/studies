# Stopword Removal (Remoção de palavras irrelevantes)

## Conteúdo

 - [01 - Introdução a Stopword (Palavras irrelevantes)](#intro)
 - [02 - Removendo Stopword com a biblioteca NLTK](#nltk-stopword)



x







---

<div id="intro"></div>

## 01 - Introdução a Stopword (Palavras irrelevantes)

> No processamento de linguagem natural, a remoção de palavras irrelevantes é o processo de remover palavras de uma string que não fornecem nenhuma informação sobre o tom de uma declaração.

**Palavras irrelevantes (Stopword)** são palavras que removemos durante o pré-processamento, quando não nos importamos com a estrutura das frases. Geralmente são as palavras mais comuns em um idioma e não fornecem nenhuma informação sobre o tom de uma declaração.

Eles incluem palavras como:

 - **“a”**
 - **“an”**
 - **“the”**

---

<div id="nltk-stopword"></div>

## 02 - Removendo Stopword com a biblioteca NLTK

> A biblioteca **NLTK** fornece uma biblioteca integrada com essas palavras.

Veja o código abaixo:

[stopword.py](src/stopword.py)
```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Sentence to apply Stopword removal.
nbc_statement = "NBC was founded in 1926 making it the oldest major broadcast network in the USA"

word_tokens = word_tokenize(nbc_statement) # Tokenize nbc_statement
statement_no_stop = [word for word in word_tokens if word not in stop_words] # Apply list comprehension
 
print(statement_no_stop)
```

**OUTPUT:**  
```
['NBC', 'founded', '1926', 'making', 'oldest', 'major', 'broadcast', 'network', 'USA']
```

Veja que para remover as **palavras irrelevantes (Stopword)** foi feito vários processos antes disso, que foram:

 - **Baixar as Stopword**
 - **Transformar as Stopword em um conjunto (set)**
   - Veja que nós estamos utilizando as Stopword da língua Inglesa (English).
 - **Separar/Tokenzinar o texto por palavras:**
   - Veja que nós não estamos considerando ponto e vírgula *(que também não tem no texto)*.
   - E também não estamos separando por sentenças e sim por palavras.
 - **Aplicar uma *list comprehension* que retorna apenas as palavras que não estão no conjunto de Stopword.**

---

**REFERÊNCIAS:**  
[CodeAcademy - Text Preprocessing](https://www.codecademy.com/learn/text-preprocessing)

---

**Rodrigo Leite -** *drigols*
