########################################################
# Rodrigo Leite - drigols                              #
# Last update: 29/12/2021                              #
########################################################

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
