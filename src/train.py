# import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from datasets import Datasets
from model import WordRecommendationModel
from config import DATA_FILE_PATH, MODEL_SAVE_PATH, MAX_SEQ_LEN, OUTPUT_DIM, DROPOUT_THRESHOLD, LEARNING_RATE, EPOCHS, BATCH_SIZE

# Load and preprocess the dataset
dataset = Datasets(DATA_FILE_PATH, MAX_SEQ_LEN)
X, y = dataset.load_data()
vocab_size = dataset.get_vocab_size()

# Define and compile the model
model = WordRecommendationModel(vocab_size, OUTPUT_DIM, MAX_SEQ_LEN, DROPOUT_THRESHOLD)
adam = Adam(learning_rate=LEARNING_RATE)
model.compile_model()

# Train the model
model.train_model(X, y, epochs=EPOCHS, batch_size=BATCH_SIZE)

# Save the trained model
model.save_model(MODEL_SAVE_PATH)
