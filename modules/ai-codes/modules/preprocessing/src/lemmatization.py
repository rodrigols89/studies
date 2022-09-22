########################################################
# Rodrigo Leite - drigols                              #
# Last update: 29/12/2021                              #
########################################################

from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer() # Instance.
tokenized = ["NBC", "was", "founded", "in", "1926"]

# Apply Lemmatization.
lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]
print(lemmatized)
