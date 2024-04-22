import tensorflow as tf
import regex as re
from pyvi import ViTokenizer


class Datasets:
    def __init__(self, file_path, max_sequence_length=25):
        self.file_path = file_path
        self.max_sequence_length = max_sequence_length
        self.tokenizer = None
        self.vocab_size = None

    def load_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        split_data = text.split('\n')
        pattern = r'[1234567890#%&\'\-/:;<=>@_`~!^$,.*+?[\]{}|\\]|\([^)]+\)'
        cleaned_data = self.delete_special_char(split_data, pattern)
        tokenized_sentences = self.tokenize_pyvi_Vinh(cleaned_data)
        self.tokenizer = tf.keras.preprocessing.text.Tokenizer()
        self.tokenizer.fit_on_texts(tokenized_sentences)
        seq = self.tokenizer.texts_to_sequences(tokenized_sentences)
        X, y = self.generate_sequences(seq)
        return X, y

    def delete_special_char(self, data, pattern):
        clean_data = [re.sub(pattern,  '', line) for line in data]
        return clean_data

    def tokenize_pyvi_Vinh(self, data):
        tokenized_sentences = [ViTokenizer.tokenize(sentence.lower()).split() for sentence in data]
        return tokenized_sentences

    def generate_sequences(self, sequences):
        X = []
        y = []
        total_words_dropped = 0
        for i in sequences:
            if len(i) > 1:
                for index in range(1, len(i)):
                    X.append(i[:index])
                    y.append(i[index])
            else:
                total_words_dropped += 1
        print("Total Single Words Dropped are:", total_words_dropped)
        X = tf.keras.preprocessing.sequence.pad_sequences(X, maxlen=self.max_sequence_length)
        y = tf.keras.utils.to_categorical(y, num_classes=self.vocab_size)
        return X, y

    def get_vocab_size(self):
        self.vocab_size = len(self.tokenizer.word_index) + 1
        return self.vocab_size

# # Example usage:
# file_path = "C:\\Users\\Admin\\Desktop\\word_recomment\\word_recommend\\data\\data_19_9_2023.txt"
file_path = "../data/data_19_9_2023.txt"
custom_dataset = Datasets(file_path)
X, y = custom_dataset.load_data()
vocab_size = custom_dataset.get_vocab_size()
print("Vocabulary size:", vocab_size)
