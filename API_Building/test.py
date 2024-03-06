import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam
import numpy as np
import regex as re
import pickle
from pyvi import ViTokenizer
import pandas as pd

file_path = "./data_19_9_2023.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
split_data = text.split('\n')
split_data

# xoá kí tự đặc biệt
pattern = r'[1234567890#%&\'\-/:;<=>@_`~!^$,.*+?[\]{}|\\]|\([^)]+\)'
def delete_special_char(data, pattern):
  clean_data = [re.sub(pattern,  '', line) for line in data]
  return clean_data

cleaned_data = delete_special_char(split_data, pattern)
# print(cleaned_data)

def tokenize_pyvi_Vinh(data):
  tokenized_sentences = [ViTokenizer.tokenize(sentence.lower()).split() for sentence in data]
  return tokenized_sentences

tokenized_sentences = tokenize_pyvi_Vinh(cleaned_data)
print(tokenized_sentences)

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(tokenized_sentences)
seq = tokenizer.texts_to_sequences(tokenized_sentences)

input_sequences = []
for line in tokenized_sentences:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)
with open('tokenizer.picker', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)