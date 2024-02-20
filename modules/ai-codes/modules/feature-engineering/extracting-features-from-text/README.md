# Extracting features from Text

## Contents

 - [**Noise Removal**](#noise-removal)
   - [**Noise Removal with sub() method (Regular Expression)**](#noise-removal-sub-method)
     - [Removing whitespace with the sub() method](#sub-remove-whitespace)
     - [Remove punctuation with the sub() method](#sub-remove-punctuation)
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
