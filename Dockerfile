# Python3のイメージを基にする
FROM python:3
ENV PYTHONUNBUFFERED 1

# ビルド時に/codeというディレクトリを作成する
RUN mkdir /code

# ワークディレクトリの設定
WORKDIR /code

# requirements.txtを/code/にコピーする
ADD requirements.txt /code/

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-jpn\
    libtesseract-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtを基にpip installする
RUN pip install -r requirements.txt
ADD . /code/
