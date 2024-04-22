import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
from model import PositionalEmbedding, TransformerDecoder
from datasets import prepare_dataset
from config import SEQUENCE_LENGTH, VOCAB_SIZE, EMBED_DIM, LATENT_DIM, NUM_HEADS, BATCH_SIZE

# Chuẩn bị dữ liệu
train_dataset, val_dataset, train_steps, val_steps = prepare_dataset("C:\\Users\\Admin\\Desktop\\word_recomment\\word_recommend\\data\\data_19_9_2023.txt","C:\\Users\\Admin\\Desktop\\word_recomment\\word_recommend\\model\\wd_transformers.txt", vocab_size=VOCAB_SIZE, sequence_length=SEQUENCE_LENGTH, batch_size=BATCH_SIZE)
# Xây dựng mô hình
inputs = tf.keras.Input(shape=(None,), dtype="int64")
x = PositionalEmbedding(SEQUENCE_LENGTH, VOCAB_SIZE, EMBED_DIM)(inputs)
x = TransformerDecoder(EMBED_DIM, LATENT_DIM, NUM_HEADS)(x, x)
outputs = tf.keras.layers.Dense(VOCAB_SIZE, activation="softmax")(x)
model = tf.keras.Model(inputs, outputs)

# Khởi tạo callback để lưu lại trọng số tốt nhất
checkpoint = ModelCheckpoint("C:\\Users\\Admin\\Desktop\\word_recomment\\word_recommend\\model\\new_model___.hdf5", monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')

# Huấn luyện mô hình
model.compile(optimizer=Adam(), loss="sparse_categorical_crossentropy", metrics=["accuracy"])
history = model.fit(train_dataset, 
                    epochs=1, 
                    steps_per_epoch=train_steps,
                    validation_data=val_dataset, 
                    validation_steps=val_steps,
                    callbacks=[checkpoint])
