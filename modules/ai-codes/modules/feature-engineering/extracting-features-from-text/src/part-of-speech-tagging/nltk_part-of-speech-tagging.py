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
