########################################################
# Rodrigo Leite - drigols                              #
# Last update: 29/12/2021                              #
########################################################

from nltk.tokenize import sent_tokenize

text = "So, during test time, any word that is not present in the vocabulary will be mapped to a UNK token. This is how we can tackle the problem of OOV in word tokenizers."
tokenized_by_sentence = sent_tokenize(text)

print(tokenized_by_sentence)
