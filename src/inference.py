import random
import numpy as np
# import regex as re
# from pyvi import ViTokenizer
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from config import MODEL_PATH, TOKENIZER_PATH, MAX_SEQ_LEN, NUM_NEXT_WORDS, NUM_SAMPLES


class WordRecommender:
    def __init__(self, model_path, tokenizer_path, max_seq_len):
        self.model_path = model_path
        self.tokenizer_path = tokenizer_path
        self.max_seq_len = max_seq_len
        self.model = None
        self.tokenizer = None

    def load_model_and_tokenizer(self):
        self.model = self.load_model(self.model_path)
        with open(self.tokenizer_path, 'rb') as handle:
            self.tokenizer = pickle.load(handle)

    def load_model(self, model_path):
        return tf.keras.models.load_model(model_path)

    def get_predicted_word(self, predicted_probs):
        top_3_indices = np.argsort(predicted_probs[0])[::-1][:3]
        predicted_words = [self.tokenizer.index_word[i] for i in top_3_indices]
        chosen_word = random.choice(predicted_words)
        return chosen_word

    def generate_text(self, seed_text, next_words, num_samples):
        generated_texts = []
        for _ in range(num_samples):
            generated_text = seed_text
            for _ in range(next_words):
                token_list = self.tokenizer.texts_to_sequences([generated_text])[0]
                token_list = pad_sequences([token_list], maxlen=self.max_seq_len - 1, padding='pre')
                predicted_probs = self.model.predict(token_list)
                chosen_word = self.get_predicted_word(predicted_probs)
                generated_text += " " + chosen_word
                generated_text = generated_text.replace("_", " ")
            generated_texts.append(generated_text)
        return generated_texts

def main():
    model_path = MODEL_PATH  
    tokenizer_path = TOKENIZER_PATH  
    max_seq_len = MAX_SEQ_LEN
    next_words = NUM_NEXT_WORDS
    num_samples = NUM_SAMPLES
    word_recommender = WordRecommender(model_path, tokenizer_path, max_seq_len)
    word_recommender.load_model_and_tokenizer()

    while True:
        seed_text = str(input("Enter seed text (type 'exit' to quit): ")).lower()
        if seed_text == 'exit':
            break
        
        generated_text = word_recommender.generate_text(seed_text, next_words, num_samples)
        print("Generated Texts:")
        for text in generated_text:
            print(text)

if __name__ == '__main__':
    main()
