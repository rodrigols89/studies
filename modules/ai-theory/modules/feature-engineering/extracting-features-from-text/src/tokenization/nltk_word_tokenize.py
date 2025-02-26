import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "Life is short, so live it! This text has 29 characters, including spaces and punctuation. It consists of one sentence with proper punctuation and a comma."

tokenized_by_word = word_tokenize(text)
print(tokenized_by_word)
