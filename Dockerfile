FROM python:3.11
WORKDIR /app_word_recommend

COPY ./src/bi_lstm/config.py /app_word_recommend/src/bil_stm/
COPY ./src/bi_lstm/inference.py /app_word_recommend/src/bi_lstm/
COPY ./src/bi_lstm/word_recommend_api.py /app_word_recommend/src/bi_lstm/
COPY ./model/word_recommendation.h5 /app_word_recommend/model/
COPY ./model/tokenizer.picker /app_word_recommend/model/
COPY requirement.txt .

CMD [ "python", "pip install --upgrade pip", "pip install -r requirement.txt", "./src/bi_lstm/word_recommend_api.py" ]
