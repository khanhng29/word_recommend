
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

# đọc file
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

# chuyển đổi thành sequence(số)/đánh index cho từng token
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(tokenized_sentences)
seq = tokenizer.texts_to_sequences(tokenized_sentences)

X = []
y = []
total_words_dropped = 0

for i in seq:
    if len(i) > 1:
        for index in range(1, len(i)):
            X.append(i[:index])
            y.append(i[index])
    else:
        total_words_dropped += 1
print("Total Single Words Dropped are:", total_words_dropped)
# Dữ liệu đã có thể đem train
print(f'Dữ liệu training sẵn sàng')
print(f'Dữ liệu testing sẵn sàng')

X = tf.keras.preprocessing.sequence.pad_sequences(X, maxlen=25) # vá những chỗ trống với [0] để các input đều có length bằng nhau / độ dài mặc định sẽ là chiều dài của câu dài nhất
y = tf.keras.utils.to_categorical(y) # đổi từ vector(interger) thành binary class matrix
vocab_size = len(tokenizer.word_index) + 1 # vocab size + 1 vì trong đó 1 giá trị OOV(out of vocab)

seq_len = [len(sentence) for sentence in tokenized_sentences]
pd.Series(seq_len).hist(bins=30)

input_dim = vocab_size # độ dài của những từ riêng biệt
output_dim = 128
input_length = X.shape[-1]
dropout_threshold = 0.5

model1 = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=input_dim, output_dim=output_dim, input_length=input_length),
    tf.keras.layers.Bidirectional(LSTM(units=output_dim, dropout= dropout_threshold, return_sequences=True), merge_mode='concat'),
    tf.keras.layers.Bidirectional(LSTM(units=output_dim, return_sequences=True)),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(input_dim, activation='sigmoid')
])

adam = Adam(learning_rate=0.001)
model1.compile(optimizer=adam, loss='categorical_crossentropy', metrics=tf.keras.metrics.CategoricalAccuracy(
    name='categorical_accuracy', dtype=None))

model1.summary()

model1.fit(X,y, batch_size=128, epochs=500, shuffle=True)

model1.save('word_recommendation_Vinh')
