import re


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        print("The text read successfully.")
        print("Total number of characters:", len(text))
        print("Text type:", type(text), "\n")
    return text


def tokenizer_txt(text):
    text_tokenized = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    text_tokenized = [item.strip() for item in text_tokenized if item.strip()]
    print("Text tokenized successfully.")
    print("Total number of tokens (without whitespaces):", len(text_tokenized), "\n")
    return text_tokenized


if __name__ == "__main__":

    file_path = "../datasets/the-verdict.txt"
    text = read_txt(file_path)

    tokens = tokenizer_txt(text)
    sorted_tokens = sorted(tokens, key=len, reverse=True)

    print(tokens[0:10])
