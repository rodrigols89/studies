**NOTE:**  
The examples used here will use the [**"Job Salary Prediction (Train_rev1.zip)"**](https://www.kaggle.com/competitions/job-salary-prediction/data?select=Train_rev1.zip) dataset. So you need to first download the dataset and place it in the [/src](src/) folder.

# Extracting features from Text

## Contents

 - [**Lower Casing**](#lower-casing)
 - [**Numbers Removal**](#number-removal)
 - [**Noise Removal**](#noise-removal)
   - [**Noise Removal with sub() method (Regular Expression)**](#noise-removal-sub-method)
     - [Removing whitespace with the sub() method](#sub-remove-whitespace)
     - [Remove punctuation with the sub() method](#sub-remove-punctuation)
 - [**Stopword Removal**](#stopword-removal)
   - [**Stopword Removal with NLTK library**](#stopword-removal-nltk)
 - [**Most frequent word removal**](#most-frequent-word-removal)
 - [**Rare words removal**](#rare-words-removal)
 - [**Stemming**](#stemming)
   - [**Stemming with NLTK library**](#stemming-nltk)
 - [**Lemmatization:**](#lemmatization)
   - [**Lemmatization with NLTK library**](#lemmatization-nltk)
 - [**Part-of-Speech Tagging:**](#part-of-speech-tagging)
 - [**Tokenization**](#intro-to-tokenization)
   - **Tokenization with the NLTK library:**
     - [Tokenization text by words](#tokenization-by-words-nltk)
     - [Tokezination text by sentences](#tokenization-by-sentences-nltk)
 - [**CountVectorizer**](#countvectorizer)
   - [**CountVectorizer with Scikit-learn library**](#countvectorizer-sklearn)
 - Bag of words
 - n-grams
 - word2vec
 - topic extraction
 - [**Settings**](#settings)
 - [**REFERENCES**](#ref)




































































































<!--- ( Lower Casing ) --->

---

<div id="lower-casing"></div>

## Lower Casing

> **Lower casing**, *"also known as converting text to lowercase"*, is a common preprocessing step in *Natural Language Processing (NLP)* and *Text Analysis*.

This process involves transforming all letters in a piece of text to their lowercase form. While seemingly straightforward, lower casing has both advantages and disadvantages that need to be carefully considered in various NLP tasks.

 - **Advantages:**
   - **Normalization:** Lower casing helps in achieving text normalization by ensuring uniformity in text data. It eliminates variations due to capitalization, making it easier to compare and analyze text.
   - **Simplifies Comparison:** Lower casing makes text comparison case-insensitive, which can be crucial for tasks like string matching, searching, and clustering.
   - **Improved Tokenization:** Lower casing can simplify the tokenization process by reducing the number of unique tokens, which can lead to more efficient and accurate NLP models.
   - **Enhanced Generalization:** Lower casing allows models to generalize better across different text sources by treating words with the same spelling but different capitalizations as identical.
 - **Disadvantages:**
   - **Loss of Information:** Lower casing can lead to loss of information, especially in cases where capitalization carries semantic meaning, such as proper nouns or emphasis.
   - **Ambiguity:** Lower casing may introduce ambiguity in cases where words with different meanings are spelled the same but differ in capitalization (e.g., "polish" vs. "Polish").
   - **Preservation of Acronyms:** Lower casing may alter the representation of acronyms and abbreviations, potentially affecting the interpretation of the text.

For example, let's see and example of the **"lower casing"** process:

[lower-casing.py](src/lower-casing/lower-casing.py)
```python
import pandas as pd

# Settings.
pd.set_option("display.max_colwidth", None)
full_df = pd.read_csv("../Train_rev1.csv")

# Get only "df_FullDescription" column/feature.
df_FullDescription = full_df[["FullDescription"]]
df_FullDescription = df_FullDescription.astype({'FullDescription': 'string'}).head(3)  # Get only 3 rows.

# Add new column "processed_FullDescription" to the DataFrame.
df_FullDescription["processed_FullDescription"] = df_FullDescription["FullDescription"].str.lower()
print(df_FullDescription.head())
```

**OUTPUT:**
![img](images/lower-casing-01.png)  




































































































<!--- ( Numbers Removal ) --->

---

<div id="numbers-removal"></div>

## Numbers Removal

> **Numbers removal** is a preprocessing technique commonly used in *Natural Language Processing (NLP*) and *Text Analysis* to eliminate numerical digits from text data.

This process involves stripping all numeric characters from a piece of text, leaving only alphabetic and punctuation symbols. While numbers removal can be beneficial in certain contexts, it also comes with its own set of advantages and disadvantages that need to be carefully considered in various NLP tasks.

 - **Advantages:**
   - **Improved Text Clarity:** By removing numbers from text, readability and interpretability can be enhanced, particularly in cases where numbers are extraneous or irrelevant to the analysis.
   - **Reduced Dimensionality:** Eliminating numerical digits reduces the dimensionality of the text data, which can lead to more efficient and streamlined text processing, especially in tasks like tokenization and feature extraction.
   - **Focus on Textual Context:** Removing numbers allows NLP models to focus more on the textual context and linguistic patterns present in the data, rather than being influenced by numerical values.
   - **Enhanced Generalization:** Text without numerical digits may generalize better across different text sources and domains, making NLP models more robust and adaptable.
 - **Disadvantages:**
   - **Loss of Numerical Information:** Removing numbers may result in the loss of valuable numerical information embedded in the text, such as quantitative data, measurements, or codes.
   - **Altered Semantic Meaning:** In some cases, numbers contribute to the semantic meaning of the text, such as in references to dates, times, quantities, or rankings. Removing numbers can distort or obscure this meaning.
   - **Impact on Certain Tasks:** Tasks that specifically involve numerical analysis or require the retention of numerical information (e.g., sentiment analysis of numerical ratings) may be adversely affected by numbers removal.

**Contextual Considerations:**  
The decision to remove numbers should be context-dependent, considering the specific requirements and goals of the NLP task. In certain domains or text genres, numerical information may be integral to the analysis and should be preserved.




































































































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




































































































<!--- ( Most frequent word removal ) ---->

---

<div id="most-frequent-word-removal"></div>

## Most frequent word removal

> **"Most frequent word removal"** is a preprocessing technique commonly employed in **Natural Language Processing (NLP)** and **Text Analysis** to eliminate high-frequency words from text data.

This process involves identifying and excluding words that occur with the highest frequency in a corpus or document collection. While removing frequent words can be beneficial in certain contexts, it also presents its own set of advantages and disadvantages that require careful consideration in various NLP tasks.

 - **Advantages:**
   - **Noise Reduction:** By eliminating the most frequent words, which often include common stop words and other non-informative terms, the overall noise level in the text data can be reduced. This can lead to a cleaner and more focused representation of the underlying content.
   - **Enhanced Discriminative Power:** Removing highly frequent words can highlight the importance of less common terms that may carry more discriminative power for certain NLP tasks, such as sentiment analysis, topic modeling, or document classification.
   - **Improved Generalization:** By excluding frequently occurring words that may be specific to the training data but not necessarily relevant to the broader context, models can generalize better across different text sources and domains.
   - **Reduced Dimensionality:** The removal of high-frequency words can decrease the dimensionality of the feature space, making subsequent text processing tasks, such as vectorization or classification, more computationally efficient and less prone to overfitting.
 - **Disadvantages:**
   - **Loss of Contextual Information:** Removing frequent words may result in the loss of important contextual information and nuances present in the text. Some common words, such as pronouns or prepositions, contribute significantly to the syntactic and semantic structure of language.
   - **Potential Bias:** The removal of high-frequency words may introduce bias into the analysis, particularly if the selected stop word list or criteria for identifying frequent words are not carefully chosen or tailored to the specific task or domain.
   - **Impact on Interpretability:** Excluding frequent words can make the interpretation of results more challenging, as certain common terms that provide context or domain-specific information may be omitted from the analysis.
   - **Dependence on Corpus Characteristics:** The effectiveness of most frequent word removal depends on the characteristics of the corpus being analyzed. In some cases, the most frequent words may indeed carry significant meaning or serve as key identifiers of the text's topic or genre.




































































































<!--- ( Rare words removal ) ---->

---

<div id="rare-words-removal"></div>

## Rare words removal

> **"Rare words removal"** is a preprocessing technique commonly utilized in *Natural Language Processing (NLP)* and *Text Analysis* to exclude infrequent words from textual data.

This process involves identifying and filtering out words that occur with low frequency in a corpus or collection of documents. While removing rare words can be advantageous in certain scenarios, it also presents its own set of benefits and drawbacks that necessitate careful consideration in various NLP tasks.

 - **Advantages:**
   - **Noise Reduction:** By eliminating rare words, which often include misspellings, typographical errors, or obscure terms, the overall noise level in the text data can be reduced. This leads to a cleaner and more focused representation of the underlying content.
   - **Improved Model Performance:** Excluding rare words can prevent overfitting in NLP models, particularly those based on statistical or machine learning approaches. Focusing on more frequent and meaningful terms can enhance the model's ability to generalize and make accurate predictions.
   - **Enhanced Interpretability:** Removing rare words simplifies the vocabulary used in analysis, making the results more interpretable and comprehensible to users. It helps in focusing attention on the most salient aspects of the text data.
   - **Computational Efficiency:** Reducing the number of rare words in the dataset can lead to computational efficiency gains during text processing tasks such as tokenization, vectorization, and model training. This is particularly beneficial when dealing with large-scale text datasets.
 - **Disadvantages:**
   - **Loss of Information:** Removing rare words may result in the loss of valuable information, particularly in specialized domains or when analyzing niche topics. Rare words can sometimes carry crucial insights or domain-specific knowledge that is pertinent to the analysis.
   - **Underrepresentation of Minority Classes:** In tasks such as sentiment analysis, document classification, or entity recognition, rare words may be associated with minority classes or specific categories of interest. Removing these words can lead to underrepresentation or bias against these classes.
   - **Decreased Generalization:** Over-filtering rare words can limit the generalization capability of NLP models, especially when dealing with diverse or evolving text data. Rare words may contain emerging trends, new terminology, or domain-specific jargon that are relevant for analysis.
   - **Dependence on Corpus Size:** The effectiveness of rare words removal depends on the size and composition of the corpus being analyzed. In smaller datasets, the removal of rare words may significantly reduce the available vocabulary, potentially impacting the quality of analysis.




































































































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




































































































<!--- ( CountVectorizer ) --->

---

<div id="countvectorizer"></div>

## CountVectorizer

> The **"CountVectorizer"** is used to transform words into numerical vectors. **What?**

I don't know if you know, but Machine Learning models mostly learn from numerical data. For example, to learn patterns in an image, Machine Learning models use the pixels of the image, which can be represented by a numerical vector.

**NOTE:**  
But how to transform texts into numbers? One approach (which is the one CountVectorizer uses) is to count how many times each word appears in a text.

For example, imagine that we have the following text:

```python
doc = ["One Cent, Two Cents, Old Cent, New Cent: All About Money"]
```

The **"CountVectorizer"** method would convert it as follows:

![img](images/cv-01.png)  

**NOTE:**  
Notice that initially we had words; Then these words were numerized (you can see in the columns); And finally, we counted how many times each word appeared.

> This format used to store this representation is the same as a **"Sparse Matrix"**.

---

<div id="countvectorizer-sklearn"></div>

## CountVectorizer with Scikit-learn library

For our initial problem, let's imagine that we have the following texts:

[text_countvectorizer-01.py](src/countvectorizer/text_countvectorizer-01.py)
```python
import pandas as pd

pd.options.display.max_colwidth = 200

cat_in_the_hat_docs = [
    "One Cent, Two Cents, Old Cent, New Cent: All About Money (Cat in the Hat's Learning Library)",
    "Inside Your Outside: All About the Human Body (Cat in the Hat's Learning Library)",
    "Oh, The Things You Can Do That Are Good for You: All About Staying Healthy (Cat in the Hat's Learning Library)",
    "On Beyond Bugs: All About Insects (Cat in the Hat's Learning Library)",
    "There's No Place Like Space: All About Our Solar System (Cat in the Hat's Learning Library)",
]

df = pd.DataFrame(cat_in_the_hat_docs, columns=["Text"])
print(df.head())
```

**OUTPUT:**
```bash
                                                                                                             Text
0                    One Cent, Two Cents, Old Cent, New Cent: All About Money (Cat in the Hat's Learning Library)
1                               Inside Your Outside: All About the Human Body (Cat in the Hat's Learning Library)
2  Oh, The Things You Can Do That Are Good for You: All About Staying Healthy (Cat in the Hat's Learning Library)
3                                           On Beyond Bugs: All About Insects (Cat in the Hat's Learning Library)
4                     There's No Place Like Space: All About Our Solar System (Cat in the Hat's Learning Library)
```

As we know, the result of text preprocessing done with **"CountVectorizer"** is a **"Sparse Matrix"**. Now we will learn the basic concepts of how to interpret this Matrix.

Let's start by applying **CountVectorizer** to our text samples:

[text_countvectorizer-01.py](src/countvectorizer/text_countvectorizer-01.py)
```python
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

pd.options.display.max_colwidth = 200

cat_in_the_hat_docs = [
  "One Cent, Two Cents, Old Cent, New Cent: All About Money (Cat in the Hat's Learning Library)",
  "Inside Your Outside: All About the Human Body (Cat in the Hat's Learning Library)",
  "Oh, The Things You Can Do That Are Good for You: All About Staying Healthy (Cat in the Hat's Learning Library)",
  "On Beyond Bugs: All About Insects (Cat in the Hat's Learning Library)",
  "There's No Place Like Space: All About Our Solar System (Cat in the Hat's Learning Library)" 
]

df = pd.DataFrame(cat_in_the_hat_docs, columns=["Text"])

vectorizer = CountVectorizer() # Instance.
df_vectorized = vectorizer.fit_transform(df['Text'])

print("Sparse Matrix type:", type(df_vectorized))
print("Shape:", df_vectorized.shape)
```

**OUTPUT:**
```bash
Sparse Matrix type: <class 'scipy.sparse._csr.csr_matrix'>
Shape: (5, 43)
```

> **NOTE:**  
> The first thing you need to keep in mind now is that we no longer have a Pandas DataFrame. We now have a **Sparse Matrix** *(created with SciPy/Process done internally by Scikit-Learn)*.

Interpreting the output above, we have:

 - **5x43:**
   - 5 samples;
   - 43 unique words (each will be a column in our sparse matrix).
 - **75 stored elements:**
   -We have 43 unique words, where each will be a column of the **Sparse Matrix**, but in total we have 75 words (elements) among all samples (5).

**NOTE:**  
Is there a way to see this matrix in a **Sparse Matrix** format? Of course!

```python
print("Sparse Matrix:", df_vectorized)
```

**OUTPUT:**
```bash
Sparse Matrix:   (0, 28)        1
  (0, 8)        3
  (0, 40)       1
  (0, 9)        1
  (0, 26)       1
  (0, 23)       1
  (0, 1)        1
  (0, 0)        1
  (0, 22)       1
  (0, 7)        1
  (0, 16)       1
  (0, 37)       1
  (0, 13)       1
  (0, 19)       1
  (0, 20)       1
  (1, 1)        1
  (1, 0)        1
  (1, 7)        1
  (1, 16)       1
  (1, 37)       2
  (1, 13)       1
  (1, 19)       1
  (1, 20)       1
  (1, 18)       1
  (1, 42)       1
  :     :
  (3, 16)       1
  (3, 37)       1
  (3, 13)       1
  (3, 19)       1
  (3, 20)       1
  (3, 27)       1
  (3, 3)        1
  (3, 5)        1
  (3, 17)       1
  (4, 1)        1
  (4, 0)        1
  (4, 7)        1
  (4, 16)       1
  (4, 37)       1
  (4, 13)       1
  (4, 19)       1
  (4, 20)       1
  (4, 38)       1
  (4, 24)       1
  (4, 31)       1
  (4, 21)       1
  (4, 33)       1
  (4, 29)       1
  (4, 32)       1
  (4, 35)       1
```

Interpreting the output above, we have:

- **We have a tuple (Row, Column):**
  - This tuple basically represents a mapping to our **Sparse Matrix**.
- **We have the value corresponding to this mapping.**

**NOTE:**  
Okay, but what about the 43 unique words (each in a column in our sparse matrix)? For this, we will use the **get_feature_names_out()** method of the **CountVectorizer** object instance:

```python
print("Unique words: ", vectorizer.get_feature_names_out())
```

**OUTPUT:**
```bash
Unique words: ['about' 'all' 'are' 'beyond' 'body' 'bugs' 'can' 'cat' 'cent' 'cents'
 'do' 'for' 'good' 'hat' 'healthy' 'human' 'in' 'insects' 'inside'
 'learning' 'library' 'like' 'money' 'new' 'no' 'oh' 'old' 'on' 'one'
 'our' 'outside' 'place' 'solar' 'space' 'staying' 'system' 'that' 'the'
 'there' 'things' 'two' 'you' 'your']
```

> **NOTE:**  
> The first observation here is that by default, the **CountVectorizer** object applies preprocessing transforming all words to *"lowercase"*.

Notice that we have as output a list with all features (which were previously words in a text and now unique features) that were mapped to our **"Sparse Matrix"**.

**Interpreting one of the mappings of the Sparse Matrix:**

 - If you look at the example **(0, 8) 3** we have that:
   - In row zero (first sample);
   - Column 8 (it will be 9 since we start from zero);
   - We have an element appearing 3 times.

> **But what element (feature) is this?**

**NOTE:**  
Remember that we have the **get_feature_names_out()** method that returns a list with each word as a feature? So, if you look for the eighth (8) element (starting from zero, of course), you will find the element **"cent"**. That is, in the first sample, the element (word) **"cent"** appears 3 times.

> Okay, but how do I view this **"Sparse Matrix"** as a **"Dense Matrix"**?

It's simple, for that we can use 2 methods:

 - toarray()
 - todense()

```python
print("Dense Matrix:\n", df_vectorized.toarray())
```

**OUTPUT:**
```bash
Dense Matrix:
array([[1, 1, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0,
        1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
       [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
       [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0,
        0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 1, 0, 2, 0],
       [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0,
        0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1,
        0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0]])
```

```python
print("Dense Matrix:\n", df_vectorized.todense())
```

**OUTPUT:**
```bash
Dense Matrix:
matrix([[1, 1, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1,
         0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
         0],
        [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,
         1],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1,
         0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 1, 0, 2,
         0],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1,
         0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
         0],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1,
         1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0,
         0]])
```

**NOTE:**  
If you pay close attention, you'll see that our *Matrix* is in the format of a list of lists. What does that mean? I'll refactor it to make it clearer for you...

**OUTPUT:**
```bash
[
  [1, 1, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1,
   0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,0],
    
  [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1,
   0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,1],
    
  [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1,
   0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 1, 0, 2,0],
    
  [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1,
   0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,0],
    
  [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1,
   1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0,0]
]
```

Notice that we have:

 - A list (matrix);
 - With 5 lists inside (our 5 vectorized samples).




































































































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

 - **General:**
   - [CodeAcademy - Text Preprocessing](https://www.codecademy.com/learn/text-preprocessing)
   - [ChatGPT](https://chat.openai.com/)
   - [Gemini](https://gemini.google.com/app)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
