FROM python:3.11
# ENV PYTHON_VERSION 3.11
WORKDIR /app

COPY requirement.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirement.txt

COPY . .

CMD [ "python", "./src/word_recommend_api.py" ]