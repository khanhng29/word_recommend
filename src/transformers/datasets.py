import tensorflow as tf
import numpy as np
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from underthesea import word_tokenize
import re

def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
    return data

def word_separation(input_data):
    data = input_data.split('\n')
    token_underthesea = []
    sentences = []

    for sentence in data:
        text = re.sub(r'[^a-zA-Z0-9\sđĐáÁàÀảẢãÃạẠăĂắẮằẰẳẲẵẴạẠâÂấẤầẦẩẨẫẪậẬêÊếẾềỀểỂễỄệỆôÔốỐồỒổỔỗỖộỘơƠớỚờỜởỞỡỠợỢưƯứỨừỪửỬữỮựỰơƠáÁàÀảẢãÃạẠéÉèÈẻẺẽẼếẾềỀểỂễỄếẾêÊấẤầẦẩẨẫẪậẬíÍìÌỉỈĩĨịỊóÓòÒỏỎõÕọỌốỐồỒổỔỗỖộỘơƠớỚờỜởỞỡỠợỢúÚùÙủỦũŨụỤưỪỨừỪửỬữỮựỰýÝỳỲỷỶỹỸỵỴ\s]+', '', sentence).lower()
        sentences.append(text)

        tokens_underthesea = word_tokenize(text)
        token_underthesea.append(tokens_underthesea)

    return token_underthesea, sentences

def word_embedding(token_underthesea, vocab):
    digitized_sentences = []
    for sentence in token_underthesea:
        digitized_sentence = [vocab[word] for word in sentence if word in vocab]
        digitized_sentences.append(digitized_sentence)
    return digitized_sentences

def convert(input_sequences):
    data_strings = [" ".join(map(str, sequence)) for sequence in input_sequences]
    data_np_arr = np.array(data_strings, dtype=str)
    return data_np_arr

def prepare_lm_dataset(text_batch, custom_text_vectorization):
    vectorized_sequences = custom_text_vectorization(text_batch)
    x = vectorized_sequences[:, :-1]
    y = vectorized_sequences[:, 1:]
    return x, y

def create_text_vectorization_layer(vocab_size, sequence_length):
    custom_text_vectorization = TextVectorization(
        max_tokens=vocab_size,
        output_mode='int',
        output_sequence_length=sequence_length
    )
    return custom_text_vectorization
def build_vocab(token_underthesea, word_dict_file):
    vocab = {}
    for token in token_underthesea:
        for word in token:
            if word not in vocab:
                vocab[word] = len(vocab) + 1

    # Lưu bộ từ điển vào file word_dict
    with open(word_dict_file, 'w', encoding='utf-8') as f:
        for word, index in vocab.items():
            f.write(f"{word}: {index}\n")

    return vocab

def prepare_dataset(data_file, word_dict_file, vocab_size=50, sequence_length=None, batch_size=16, val_size=0.3):
    input_data = load_file(data_file)
    token_underthesea, _ = word_separation(input_data)
    vocab = build_vocab(token_underthesea, word_dict_file)
    input_sequences = word_embedding(token_underthesea, vocab)
    if sequence_length is None:
        sequence_length = max([len(seq) for seq in input_sequences])

    data_np = convert(input_sequences)

    custom_text_vectorization = create_text_vectorization_layer(vocab_size, sequence_length)
    custom_text_vectorization.adapt(data_np)

    dataset = tf.data.Dataset.from_tensor_slices(data_np)
    batched_dataset = dataset.batch(batch_size)

    lm_dataset = batched_dataset.map(lambda x: prepare_lm_dataset(x, custom_text_vectorization), num_parallel_calls=tf.data.experimental.AUTOTUNE)

    val_steps = int(val_size * lm_dataset.cardinality().numpy())
    train_steps = lm_dataset.cardinality().numpy() - val_steps

    val_dataset = lm_dataset.take(val_steps)
    train_dataset = lm_dataset.skip(val_steps)

    return train_dataset, val_dataset, train_steps, val_steps



# Đường dẫn tới tệp dữ liệu###################################
data_file = "C:\\Users\\Admin\\Desktop\\word_recomment\word_recommend\data\data_19_9_2023.txt"
# Thiết lập các siêu tham số
vocab_size = 50
sequence_length = 100
batch_size = 16
val_size = 0.3

# Chuẩn bị tập dữ liệu
word_dict_file = "C:\\Users\\Admin\\Desktop\\word_recomment\\word_recommend\\model\\wd_transformers.txt"  # Đường dẫn đến file word_dict
train_dataset, val_dataset, train_steps, val_steps = prepare_dataset(data_file, word_dict_file, vocab_size=vocab_size, sequence_length=sequence_length, batch_size=batch_size, val_size=val_size)

# In một số thông tin về tập dữ liệu
print("Train dataset steps:", train_steps)
print("Validation dataset steps:", val_steps)

for batch_x, batch_y in train_dataset.take(1):
    print("Sample input shape (train dataset):", batch_x.shape)
    print("Sample target shape (train dataset):", batch_y.shape)

for batch_x, batch_y in val_dataset.take(1):
    print("Sample input shape (validation dataset):", batch_x.shape)
    print("Sample target shape (validation dataset):", batch_y.shape)
