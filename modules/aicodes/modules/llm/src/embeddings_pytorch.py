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

input_ids = encoding["input_ids"]
token_type_ids = encoding["token_type_ids"]
attention_mask = encoding["attention_mask"]

print("Tensor input_ids shape:", input_ids.shape)
print("Tensor token_type_ids shape:", token_type_ids.shape)
print("Tensor attention_mask shape:", attention_mask.shape)
