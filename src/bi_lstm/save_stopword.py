import pymongo
import json

# Kết nối tới MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["testdb_5_3"]
collection = db["stopword_data"]

# Đọc dữ liệu từ tệp .txt và lưu vào MongoDB
def save_to_mongodb(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for idx, line in enumerate(file, 1):  # Sử dụng enumerate để đếm từ 1
            # Tạo một document mới với trường text và trường key
            document = {
                "text": line.strip(),
                "key": idx  # Thêm trường key với giá trị là số thứ tự
            }
            collection.insert_one(document)


# Đường dẫn đến tệp .txt
file_path = 'C:/Users/Admin/Desktop/word_recomment/word_recommend/data/vietnamese-stopwords.txt'

# Lưu dữ liệu từ tệp .txt vào MongoDB
save_to_mongodb(file_path)

