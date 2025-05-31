from transformers import AutoTokenizer

from utils import read_txt


# load the BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load the and read the text
file_path = "../datasets/the-verdict.txt"
text = read_txt(file_path)

tokens = tokenizer.tokenize(text)   # Tokenize the text
vocabulary = tokenizer.get_vocab()  # Get the vocabulary

print("Vocabulary type:", type(vocabulary))
for voc in list(vocabulary.items())[:10]:
    print(voc)
