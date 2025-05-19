import re

text = "Hello! How are you? I'm fine. Thanks for asking:)"
print("Original text:", text)

# Remove punctuation.
result = re.sub(r"[\)\.\?\!\,\:\;\'\"]", "", text)
print("Noise Removal:", result)
