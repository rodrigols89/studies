import re

from utils import read_txt


def tokenizer_txt(text):
    text_tokenized = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    text_tokenized = [item.strip() for item in text_tokenized if item.strip()]
    return text_tokenized


def create_vocabulary(tokens):
    unique_tokens = sorted(set(tokens))
    vocabulary = {}
    for id, token in enumerate(unique_tokens):
        vocabulary[token] = id
    return vocabulary


if __name__ == "__main__":

    file_path = "../datasets/the-verdict.txt"
    text = read_txt(file_path)

    tokens = tokenizer_txt(text)  # Tokenize the text
    vocabulary = create_vocabulary(tokens)  # Create the vocabulary

    print("Vocabulary size:", len(vocabulary))

    # Print some vocabulary examples
    for i, item in enumerate(vocabulary.items()):
        print(item)
        if i >= 20:
            break
