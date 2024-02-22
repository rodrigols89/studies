# Extracting features from Text

## Contents

 - [**Noise Removal**](#noise-removal)
   - [**Noise Removal with sub() method (Regular Expression)**](#noise-removal-sub-method)
     - [Removing whitespace with the sub() method](#sub-remove-whitespace)
     - [Remove punctuation with the sub() method](#sub-remove-punctuation)
 - [**Stopword Removal**](#stopword-removal)
   - [**Stopword Removal with NLTK library**](#stopword-removal-nltk)
 - [**Stemming**](#stemming)
   - [**Stemming with NLTK library**](#stemming-nltk)
 - [**Lemmatization:**](#lemmatization)
   - [**Lemmatization with NLTK library**](#lemmatization-nltk)
 - [**Part-of-Speech Tagging:**](#part-of-speech-tagging)
 - [**Tokenization**](#intro-to-tokenization)
   - **Tokenization with the NLTK library:**
     - [Tokenization text by words](#tokenization-by-words-nltk)
     - [Tokezination text by sentences](#tokenization-by-sentences-nltk)
 - Bag of words
 - n-grams
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





























































































<!--- ( Stopword Removal ) ---->

---

<div id="stopword-removal"></div>

## Stopword Removal

> In **Natural Language Processing (NLP)**, *"removing irrelevant words (Stopwords Removal)"* is the process of removing words from a string that do not provide any information about the tone of a statement.

**Irrelevant words (Stopwords)** are words that we remove during preprocessing when we don't care about the structure of the sentences. They are usually the most common words in a language and do not provide any information about the tone of a statement.

They include words like:

- **“a”;**
- **“an”;**
- **“the”...**

---

<div id="stopword-removal-nltk"></div>

## Stopword Removal with NLTK library

> The **NLTK** library provides a *built-in library* of **"stopwords"**.

See the code below:

[nltk_stopwords.py](src/stopword-removal/nltk_stopwords.py)
```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download and load stopwords.
import nltk
nltk.download("punkt")
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Sentence to apply Stopword removal.
nbc_statement = (
    "NBC was founded in 1926 making it the oldest major broadcast network in the USA"
)
word_tokens = word_tokenize(nbc_statement)  # Tokenize nbc_statement

statement_no_stop = [
    word for word in word_tokens if word.lower() not in stop_words
]  # Apply list comprehension

print(statement_no_stop)
```

**OUTPUT:**
```bash
['NBC', 'founded', '1926', 'making', 'oldest', 'major', 'broadcast', 'network', 'USA']
```

Note that to remove the **irrelevant words (Stopwords)**, several processes were done before that, which were:

- **Downloading the Stopwords**
- **Converting the Stopwords into a set**
  - Note that we are using Stopwords from the English language.
- **Tokenizing the text by words:**
  - Note that we are not considering semicolons (which are also not in the text).
  - And we are not tokenizing by sentences but by words.
- **Applying a list comprehension that returns only the words that are not in the Stopword set.**



















































































































<!---- ( Stemming ) --->

---

<div id="stemming"></div>

## Stemming

> In **Natural Language Processing (NLP)**, **Stemming** is the preprocessing normalization task concerned with the direct removal of word *affixes* (prefixes and suffixes).

For example, **Stemming** would change the word **“going”** to **“go”**. This is a common method used by search engines to improve the match between user input and website accesses.

---

<div id="stemming-nltk"></div>

## Stemming with NLTK library

> The **NLTK** library has a *built-in Stemming* called **PorterStemmer**.

In practice, we can apply the concept of **Stemming** more or less like this, with the NLTK library and **PorterStemmer**:

[nltk_stemming.py](src/stemming/nltk_stemming.py)
```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

tokenized = [
    "NBC",
    "was",
    "founded",
    "in",
    "1926",
    ".",
    "This",
    "makes",
    "NBC",
    "the",
    "oldest",
    "major",
    "broadcast",
    "network",
    ".",
]

stemmed = [stemmer.stem(token) for token in tokenized]
print(stemmed)
```

**OUTPUT:**
```bash
'nbc', 'wa', 'found', 'in', '1926', '.', 'thi', 'make', 'nbc', 'the', 'oldest', 'major', 'broadcast', 'network', '.']
```

**NOTE:**  
Oops, but which words were applied **Stemming**?

- First, I don't know if you noticed, but all letters were converted to lowercase.
- was > wa
- founded > found
- this > thi
- makes > make

**NOTE:**  
The fact that these words have been reduced is useful for many language processing applications. However, you need to be careful when defining the stemming of strings because words can often be converted into something unrecognizable.







































































<!---- ( Lemmatization ) --->

---

<div id="lemmatization"></div>

## Lemmatization

> In **Natural Language Processing (NLP)**, **"lemmatization"** is the preprocessing normalization task concerned with bringing words to their root forms.

**NOTE:**  
This is a more complicated process than stemming because it requires the method to know the grammatical class of each word. Since lemmatization requires the grammatical class, it is a less efficient approach than stemming.

---

<div id="lemmatization-nltk"></div>

## Lemmatization with NLTK library

With the **NLTK** library, it's very easy to apply the concept of **Lemmatization**. See the code below:

[nltk_lemmatization.py](src/lemmatization/nltk_lemmatization.py)
```python
import nltk
nltk.download("wordnet")

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
tokenized = ["NBC", "was", "founded", "in", "1926"]

# Apply Lemmatization.
lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]
print(lemmatized)
```

**OUTPUT:**
```bash
['NBC', 'wa', 'founded', 'in', '1926']
```

The result of **Lemmatization**, saved in the variable *lemmatized*, contains **'wa'**, while the rest of the words remain the same. It's not very useful.

**NOTE:**  
This happened because the **lemmatize** instance of the **WordNetLemmatizer** class treats each word as a noun.

> To take advantage of the power of lemmatization, we need to tag each word in our text with the most likely grammatical class.

Let's see another example:

[nltk_lemmatization-02.py](src/lemmatization/nltk_lemmatization-02.py)
```python
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

populated_island = "Indonesia was founded in 1945. It contains the most populated island in the world, Java, with over 140 million people."

tokenized_string = word_tokenize(populated_island)
lemmatized_words = [lemmatizer.lemmatize(token) for token in tokenized_string]

try:
    print(f"A lemmatizer exists: {lemmatizer}")
except:
    print("Expected a variable called `lemmatizer`")
try:
    print(f"Words Tokenized: {tokenized_string}")
except:
    print("Expected a variable called `tokenized_string`")
try:
    print(f"Lemmatized Words: {lemmatized_words}")
except:
    print("Expected a variable called `lemmatized_words`")
```

**OUTPUT:**
```bash
Words Tokenized: ['Indonesia', 'was', 'founded', 'in', '1945', '.', 'It', 'contains', 'the', 'most', 'populated', 'island', 'in', 'the', 'world', ',', 'Java', ',', 'with', 'over', '140', 'million', 'people', '.']
Lemmatized Words: ['Indonesia', 'wa', 'founded', 'in', '1945', '.', 'It', 'contains', 'the', 'most', 'populated', 'island', 'in', 'the', 'world', ',', 'Java', ',', 'with', 'over', '140', 'million', 'people', '.']
```

**NOTE:**  
Notice that out of all these words, only **"was"** was lemmatized to **"wa"**. As we already know, this is happening because we need to tag each word in our text with the most likely grammatical class.





















<!--- ( Part-of-Speech Tagging ) --->

---

<div id="part-of-speech-tagging"></div>

## Part-of-Speech Tagging

> In **Natural Language Processing (NLP)**, **"Part-of-Speech Tagging"** is the process of assigning a grammatical class to each word in a string. Using the grammatical class can improve the results of **Lemmatization**.

To improve the performance of lemmatization, we need to find the grammatical class for each word in our string. This can be a somewhat complex task (but not so much).

See the code snippets below that apply this concept in practice:

[nltk_part-of-speech-tagging.py](src/part-of-speech-tagging/nltk_part-of-speech-tagging.py)
```python
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import Counter


def get_part_of_speech(word):

    probable_part_of_speech = wordnet.synsets(word)
    pos_counts = Counter()

    pos_counts["n"] = len(
        [item for item in probable_part_of_speech if item.pos() == "n"]
    )
    pos_counts["v"] = len(
        [item for item in probable_part_of_speech if item.pos() == "v"]
    )
    pos_counts["a"] = len(
        [item for item in probable_part_of_speech if item.pos() == "a"]
    )
    pos_counts["r"] = len(
        [item for item in probable_part_of_speech if item.pos() == "r"]
    )

    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
    return most_likely_part_of_speech


if __name__ == "__main__":

    lemmatizer = WordNetLemmatizer()  # Instance.

    tokenized = ["How", "old", "is", "the", "country", "Indonesia"]
    lemmatized = [
        lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized
    ]
    print(lemmatized)
```

***OUTPUT:**
```bash
['How', 'old', 'be', 'the', 'country', 'Indonesia']
```






























































































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
