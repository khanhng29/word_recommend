import h5py
import numpy as np
from keras.models import load_model
from model import PositionalEmbedding, TransformerDecoder
import tensorflow as tf

def load_word_dict(word_dict_file):
    tokens_index = {}
    with open(word_dict_file, 'r', encoding='utf-8') as f:
        for line in f:
            word, index = line.strip().split(': ')
            tokens_index[int(index)] = word
    return tokens_index

# Đường dẫn đến file word_dict
word_dict_file = "C:\\Users\\Admin\\Desktop\\word_recomment\\word_recommend\\model\\wd_transformers.txt"
tokens_index = load_word_dict(word_dict_file)

# Đường dẫn đến file chứa mô hình đã huấn luyện
model_file_path = "C:\\Users\\Admin\\Desktop\\word_recomment\\word_recommend\\model\\best_model_v4.hdf5"

# Định nghĩa custom objects cho việc load model
custom_objects = {'PositionalEmbedding': PositionalEmbedding, 'TransformerDecoder': TransformerDecoder}

# Load mô hình từ tệp HDF5
with h5py.File(model_file_path, "r") as file:
    model_from_memory = load_model(file, custom_objects=custom_objects)

def sample_next(predictions, temperature=1.0):
    predictions = np.asarray(predictions).astype("float64")
    predictions = np.log(predictions) / temperature
    exp_preds = np.exp(predictions)
    predictions = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, predictions, 1)
    return np.argmax(probas)

def predict_next_sentence(keyword, max_length, temp=1.0):
    input_sentence = keyword
    generated_sentence = keyword
    for _ in range(max_length):
        # Tách từ trong câu đầu vào và chuyển thành danh sách các từ
        tokenized_sentence = input_sentence.split()
        
        # Chuyển đổi danh sách các từ thành vector số dựa trên từ điển
        input_indices = [tokens_index.get(token, 0) for token in tokenized_sentence]
        input_indices = tf.expand_dims(input_indices, 0)  # Mở rộng chiều để phù hợp với đầu vào của mô hình
        
        # Dự đoán token tiếp theo từ vector số đầu vào
        predictions = model_from_memory.predict(input_indices, verbose=0)
        
        # Xác định độ dài của câu đầu vào
        prompt_length = len(tokenized_sentence)
        
        # Lấy token tiếp theo dựa trên dự đoán từ mô hình
        next_token = sample_next(predictions[0, prompt_length - 1, :], temp)
        
        # Lấy từ thực tế tương ứng với token
        sampled_token = tokens_index[next_token]
        
        # Kiểm tra xem có phải là token kết thúc hay không
        if sampled_token == "<END>":
            break
        
        # Thêm token vào câu đã tạo
        generated_sentence += " " + sampled_token
        
        # Cập nhật câu đầu vào cho lần lặp tiếp theo
        input_sentence = generated_sentence

    return generated_sentence


# Sử dụng hàm để dự đoán câu văn dựa trên từ khóa và đánh giá BLEU Score
keyword = "được thành"
for _ in range(1):
    predicted_sentence = predict_next_sentence(keyword, max_length=100, temp=1)
    print(predicted_sentence)
