import random
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

from config import MODEL_SAVE_PATH, TOKENIZER_PATH
def loading_model():
  global model
  model = tf.keras.models.load_model(MODEL_SAVE_PATH)

  global model_ffnn
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

def predict_next_words(seed_text, num_predictions, word_dict, max_sequence_length, stop_words):
    predicted_words = []
    for _ in range(num_predictions):
        predicted_probs = model.predict(token_list, verbose=0)[0]
        top_n_indices = np.argsort(predicted_probs)[-num_predictions:][::-1]
        predicted_word = ""
        for word, index in word_dict.items():
            if index == top_n_indices[0]:
                predicted_word = word
                break
        seed_text += " " + predicted_word
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



