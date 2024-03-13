import tokenize
import random
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
# from underthesea import word_tokenize
import h5py
from config import MODEL_PATH, TOKENIZER_PATH
def loading_model():
  global model
  model = tf.keras.models.load_model(MODEL_PATH)
  global model_ffnn
  # Đọc file model
  # with h5py.File('./src/best_model_ffnn.hdf5', 'r') as f:
  #     model_ffnn = load_model(f)
  global tokenizer
  with open(TOKENIZER_PATH,'rb') as handle:
    tokenizer = pickle.load(handle)
  global max_seq_len
  max_seq_len = 26

def predict(seed_text, next_words):
  for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences(
      [token_list], maxlen=max_seq_len - 1, padding='pre')
    predicted_probs = model.predict(token_list)
    predicted_word = tokenizer.index_word[np.argmax(predicted_probs)]
    seed_text += " " + predicted_word

  encoding_result = output_encoding(seed_text)
  return encoding_result

def generate_text(seed_text, next_words, num_samples):
    generated_texts = []
    for _ in range(num_samples):
        generated_text = seed_text
        for _ in range(next_words):
            token_list = tokenizer.texts_to_sequences([generated_text])[0]
            token_list = pad_sequences([token_list], maxlen=max_seq_len - 1, padding='pre')
            predicted_probs = model.predict(token_list)
            chosen_word = getPredict(predicted_probs)
            generated_text += " " + chosen_word
            generated_text = generated_text.replace("_", " ")
        generated_texts.append(generated_text)
        encoding_result = output_encoding(generated_texts)

    return encoding_result

def getPredict(predicted_probs):
    top_3_indices = np.argsort(predicted_probs[0])[::-1][:3]
    predicted_words = [tokenizer.index_word[i] for i in top_3_indices]
    chosen_word = random.choice(predicted_words)
    return chosen_word
def output_encoding(predict_words):
    data = {"status": True,
            "recommendations": predict_words,
            "error": None
            }
    return(data)

def pre_processing(seed_text, num_predictions, word_dict, max_sequence_length, stop_words):
    # Loại bỏ các ký tự đặc biệt
    seed_text_cleaned = re.sub(
        r'[^a-zA-Z0-9\sđĐáÁàÀảẢãÃạẠăĂắẮằẰẳẲẵẴạẠâÂấẤầẦẩẨẫẪậẬêÊếẾềỀểỂễỄệỆôÔốỐồỒổỔỗỖộỘơƠớỚờỜởỞỡỠợỢưƯứỨừỪửỬữỮựỰơƠáÁàÀảẢãÃạẠéÉèÈẻẺẽẼếẾềỀểỂễỄếẾêÊấẤầẦẩẨẫẪậẬíÍìÌỉỈĩĨịỊóÓòÒỏỎõÕọỌốỐồỒổỔỗỖộỘơƠớỚờỜởỞỡỠợỢúÚùÙủỦũŨụỤưỪỨừỪửỬữỮựỰýÝỳỲỷỶỹỸỵỴ\s]+',
        '', seed_text).lower()
    # Tách từ
    tokens_pyvi = ViTokenizer.tokenize(seed_text_cleaned).split()
    tokens_underthesea = word_tokenize(" ".join(tokens_pyvi))
    words = [token.replace('_', ' ') for token in tokens_underthesea]
    # Loại bỏ stop word
    words = [word for word in words if word not in stop_words]
    # Thêm padding phía trước mỗi câu nếu câu ngắn
    token_list = [word_dict[word] for word in words]
    token_list = pad_sequences([token_list], maxlen=max_sequence_length - 1, padding='pre')
def predict_next_words(seed_text, num_predictions, word_dict, max_sequence_length, stop_words):
    predicted_words = []
    for _ in range(num_predictions):
        # Dự đoán từ tiếp theo
        predicted_probs = model.predict(token_list, verbose=0)[0]
        top_n_indices = np.argsort(predicted_probs)[-num_predictions:][::-1]
        predicted_word = ""
        for word, index in word_dict.items():
            if index == top_n_indices[0]:
                predicted_word = word
                break
        seed_text += " " + predicted_word
        # Lưu từ tiếp theo vào danh sách
        predicted_words.append(predicted_word)
    return predicted_words
def main():
    loading_model()
    while True:
        seed_text = input("Nhập đoạn văn bản cần dự đoán (để thoát nhập 'exit'): ")
        if seed_text.lower() == 'exit':
            break
        next_words = int(input("Nhập số từ tiếp theo muốn dự đoán: "))
        num_samples = int(input("Nhập số lần dự đoán: "))
        print("Kết quả dự đoán:")
        print(generate_text(seed_text, next_words, num_samples))

if __name__ == '__main__':
    main()



