import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.optimizers import Adam

class WordRecommendationModel:
    def __init__(self, vocab_size, output_dim=128, input_length=25, dropout_threshold=0.5):
        self.vocab_size = vocab_size
        self.output_dim = output_dim
        self.input_length = input_length
        self.dropout_threshold = dropout_threshold
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            Embedding(input_dim=self.vocab_size, output_dim=self.output_dim, input_length=self.input_length),
            Bidirectional(LSTM(units=self.output_dim, dropout=self.dropout_threshold, return_sequences=True), merge_mode='concat'),
            Bidirectional(LSTM(units=self.output_dim, return_sequences=True)),
            tf.keras.layers.GlobalAveragePooling1D(),
            Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.1),
            Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.1),
            Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.1),
            Dense(128, activation='relu'),
            Dense(self.vocab_size, activation='sigmoid')
        ])
        return model

    def compile_model(self):
        adam = Adam(learning_rate=0.001)
        self.model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=tf.keras.metrics.CategoricalAccuracy(name='categorical_accuracy', dtype=None))

    def train_model(self, X, y, batch_size=128, epochs=1, shuffle=True):
        self.model.fit(X, y, batch_size=batch_size, epochs=epochs, shuffle=shuffle)

    def save_model(self, filepath):
        self.model.save(filepath)


