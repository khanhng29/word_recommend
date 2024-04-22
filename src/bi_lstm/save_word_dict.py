from pymongo import MongoClient

# Kết nối tới MongoDB
client = MongoClient('localhost', 27017)
db = client['testdb_5_3']  # Tên của database
collection = db['word_dict_data']  # Tên của collection

# Đọc từ file txt và lưu vào MongoDB
with open('C:/Users/Admin/Desktop/word_recomment/word_recommend/data/word_dict.txt', 'r', encoding='utf-8') as file:
    for line in file:
        word, key = line.strip().split(': ')
        try:
            key = int(key)
        except ValueError:
            print(f"Không thể chuyển đổi '{key}' thành số nguyên. Bỏ qua dòng này.")
            continue
        data = {"key": key, "word": word}
        collection.insert_one(data)

# Đóng kết nối tới MongoDB
client.close()
