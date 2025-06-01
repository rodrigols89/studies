import tensorflow as tf
from transformers import AutoTokenizer

from utils import read_txt

# Load the BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Read the input text
file_path = "../datasets/the-verdict.txt"
text = read_txt(file_path)

# Tokenize and convert text to input IDs
encoding = tokenizer.encode_plus(
    text,
    add_special_tokens=True,   # Add [CLS] and [SEP] tokens
    return_tensors="tf",       # Use TensorFlow tensors
    truncation=True,           # Truncate if the text is too long
    padding=False              # Do not apply padding
)

# Get input IDs
input_ids = encoding["input_ids"]  # shape: (1, seq_len)

# Define vocabulary size and embedding dimension
vocab_size = tokenizer.vocab_size
embedding_dim = 768  # BERT-base uses 768-dimensional embeddings

# Create the embedding layer
embedding_layer = tf.keras.layers.Embedding(
    input_dim=vocab_size,
    output_dim=embedding_dim
)

# Apply embedding lookup on input IDs
embedded_tokens = embedding_layer(input_ids)  # shape: (1, seq_len, 768)

# Print information about the embedding layer
print("Layer dimensions (shape):", embedding_layer.weights[0].shape)
print("\nFirst token embedding dimension (shape):", embedding_layer.weights[0][0].shape)
print("\nFirst token embedding value (tensor):", embedding_layer.weights[0][0][:20])
