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
    return_tensors=None,      # "pt" for Pytorch, "tf" for TensorFlow or None
    truncation=True,          # Truncates if too long
    padding=False             # Do not add padding
)

# decode process = here we convert IDs back to text
token_ids = encoding["input_ids"]
decoded_text = tokenizer.decode(token_ids)

print("\nDecoded text (first 353 chars):\n", decoded_text[:353])
