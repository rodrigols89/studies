# Extracting features from Text

## Contents

 - [**Noise Removal**](#noise-removal)
   - [**Noise Removal with sub() method (Regular Expression)**](#noise-removal-sub-method)
     - [Removing whitespace with the sub() method](#sub-remove-whitespace)
     - [Remove punctuation with the sub() method](#sub-remove-punctuation)
 - [**Tokenization**](#intro-to-tokenization)
   - **Tokenization with the NLTK library:**
     - [Tokenization text by words](#tokenization-by-words-nltk)
     - [Tokezination text by sentences](#tokenization-by-sentences-nltk)
 - Bag of words
 - n-grams
 - CountVectorizer
 - TF-IDF
 - word2vec
 - topic extraction
 - [**Settings**](#settings)
 - [**REFERENCES**](#ref)




































































































<!--- ( Noise Removal ) --->

---

<div id="noise-removal"></div>

## Noise Removal

In *Natural Language Processing (NLP)*, **Noise Removal** is a text preprocessing task dedicated to removing text formatting.

Text cleaning is a technique that developers use in various domains. Depending on the goal of your project and where you get your data from, you can remove *unwanted (indesejada)* information such as:

- Punctuation and accents;
- Special characters;
- Numeric digits;
- Initial, final, and vertical white space;
- HTML formatting.

---

<div id=noise-removal-sub-method></div>

## Noise Removal with sub() method (Regular Expression)

Fortunately (Felizmente), you can use the **.sub()** method from the **re (regular expression)** library in Python for most of your **Noise Removal** needs.

The **sub()** method has three mandatory arguments:

- **pattern:**
  - A regular expression that is searched for in the input string. There must be an **"r"** preceding the string to indicate that it is a raw string, which treats backslashes as literal characters.
- **replacement_text:**
  - Text that replaces all matches in the input string.
- **input:**
  - The input string that will be edited by the **sub()** method.

The method returns a string with all instances of **pattern** replaced by **replacement_text**. Let's look at some examples of how to use this method to remove and replace text from a string.

---

<div id="sub-remove-whitespace"></div>

## Removing whitespace with the sub() method

Let's remove white spaces at the beginning, middle, and end of a text:

[sub_remove_whitespaces.py](src/noise-removal/sub_remove_whitespaces.py)
```python
import re

text = "Beginning...      Middle...      End...      "
result = re.sub(r"\s{5}", "", text)

print(result)
```

**OUTPUT**
```bash
Beginning... Middle... End...
```

> **NOTE:**  
> Notice that with the **sub()** method and a simple *Regular Expression*, we managed to remove 5 white space characters.

---

<div id="sub-remove-punctuation"></div>

## Remove punctuation with the sub() method

> Okay, but how can I remove *unwanted (indesejada)* punctuations?

See the code below:

[sub_remove_punctuation.py](src/noise-removal/sub_remove_punctuation.py)
```python
import re

text = "Hello! How are you? I'm fine. Thanks for asking:)"
print("Original text:", text)

# Remove punctuation.
result = re.sub(r"[\)\.\?\!\,\:\;\'\"]", "", text)
print("Noise Removal:", result)
```

**OUTPUT:**
```bash
Original text: Hello! How are you? I'm fine. Thanks for asking:)
Noise Removal: Hello How are you Im fine Thanks for asking
```

> **NOTE:**  
> Notice that in this simple **Noise Removal** process, we removed predefined punctuations from the text.




































































































<!--- ( Tokenization ) --->

---

<div id="intro-to-tokenization"></div>

## Tokenization

> In natural language processing, **"Tokenization"** is the text preprocessing task that divides the text into smaller components of text (*known as tokens*).

For many **Natural Language Processing (NLP)** tasks, we need to access each word in a string. However to access each word, we first have to divide the text into smaller components. The method for breaking the text into smaller components is called **Tokenization**, and the individual components are called **tokens**.

Some common operations that require **tokenization** include:

- Discovering how many words or phrases appear in the text;
- Determining how many times a specific word or phrase exists;
- Counting which terms are likely to co-occur...

> **NOTE:**  
> While **tokens** are typically individual words or terms, they can also be phrases or pieces of text of other sizes.

---

<div id="tokenization-by-words-nltk"></div>

## Tokenization text by words

To **tokenize** individual words, we can use the **word_tokenize()** function from the **NLTK (Natural Language Toolkit)** library.

The function takes a string and returns a list of words. See a simple example below:

[nltk_word_tokenize.py](src/tokenization/nltk_word_tokenize.py)
```python
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "Life is short, so live it! This text has 29 characters, including spaces and punctuation. It consists of one sentence with proper punctuation and a comma."

tokenized_by_word = word_tokenize(text)
print(tokenized_by_word)
```

**OUTPUT:**
```bash
['Life', 'is', 'short', ',', 'so', 'live', 'it', '!', 'This', 'text', 'has', '29', 'characters', ',', 'including', 'spaces', 'and', 'punctuation', '.', 'It', 'consists', 'of', 'one', 'sentence', 'with', 'proper', 'punctuation', 'and', 'a', 'comma', '.']
```

> **NOTE:**  
> See that we **tokenized** the text **by words**.

---

<div id="tokenization-by-sentences-nltk"></div>

## Tokezination text by sentences

> If I want to apply sentence **Tokenization**, for example, separating by **"commas"** or **"punctuations"**?

Simple, for that you just need to use the **sent_tokenize()** method from the **nltk.tokenize** class:

[nltk_sent_tokenize.py](src/tokenization/nltk_sent_tokenize.py)
```python
from nltk.tokenize import sent_tokenize

text = "So, during test time, any word that is not present in the vocabulary will be mapped to a UNK token. This is how we can tackle the problem of OOV in word tokenizers."

tokenized_by_sentence = sent_tokenize(text)
print(tokenized_by_sentence)
```

**OUTPUT:**
```bash
['So, during test time, any word that is not present in the vocabulary will be mapped to a UNK token.', 'This is how we can tackle the problem of OOV in word tokenizers.']
```



















































<!--- ( Settings ) --->

---

<div id="settings"></div>

## Settings

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv ai-environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source ai-environment/bin/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source ai-environment/Scripts/activate
```

**UPDATE PIP:**
```bash
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**Now, Be Happy!!!** 😬





<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - **Noise Removal:**
   - [CodeAcademy - Text Preprocessing](https://www.codecademy.com/learn/text-preprocessing)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
