import re
import os
import sys

# Add the root directory 'aicodes' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings

import tensorflow as tf


def read_txt_line_by_line(file_path):
    txt = tf.data.TextLineDataset(file_path)
    return txt


def print_txt_line_by_line(txt):
    for linha in txt:
        print(linha.numpy().decode('utf-8'))


def tokenizer_txt(text):
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    return preprocessed


if __name__ == "__main__":

    file_path = "datasets/the-verdict.txt"

    text = read_txt_line_by_line(file_path)

    print_txt_line_by_line(text)

