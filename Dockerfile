FROM python:3.11
# ENV PYTHON_VERSION 3.11
WORKDIR /app_word_recommend

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirement.txt


CMD [ "python", "./src/word_recommend_api.py" ]