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
