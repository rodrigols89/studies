import torch
from transformers import AutoTokenizer

from utils import read_txt


# load the BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load the and read the text
file_path = "../datasets/the-verdict.txt"
text = read_txt(file_path)

# encode process = here we tokenize + convert to IDs
encoding = tokenizer.encode_plus(
    text,
    add_special_tokens=True,  # Add [CLS], [SEP]
    return_tensors="pt",      # pt = Pytorch
    truncation=True,          # Truncates if too long
    padding=False             # Do not add padding
)

# Get the input IDs
input_ids = encoding["input_ids"]

vocab_size = tokenizer.vocab_size     # vocab size
embedding_dim = 768                   # embedding dim

# Create embedding layer
embedding_layer = torch.nn.Embedding(vocab_size, embedding_dim)

print("Layer dimensions (shape):", embedding_layer.weight.shape)
print("\nFirst token embedding dimension (shape):", embedding_layer.weight[0].shape)
print("\nFirst token embedding value (tensor):", embedding_layer.weight[0][:20])
