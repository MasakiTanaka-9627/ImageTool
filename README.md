# tool

## 環境構築

1. docker-compose run --rm web django-admin startproject config .

2. settings.pyを書き換える

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': 5432,
    }
}

3. docker-compose up

## herokuへデプロイ

1. 基本設定

https://qiita.com/yusuke_mrmt/items/1a3ee727d119617b2d85
runtime.txt
Procfile
settings.py


https://qiita.com/Kohey222/items/82f3a76e0247b2d387db
> heroku config:set DISABLE_COLLECTSTATIC=1


https://teratail.com/questions/169838
>django_heroku.settings(locals()) 周辺の行をもう少し下の方に移動されるとよいのではないかと思います。

local_settings.pyとsettings.pyで環境を分ける

## app作成・django-bootstrap4の追加

1. rewuirements.txtとsettings.pyにbootstrap4を追加

settings.py
 TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':[
                'bootstrap4.templatetags.bootstrap4',
            ],
        },
    },
    
rewuirements.txt
 django-bootstrap4    

2. OCRアプリの追加

docker-compose run --rm web python manage.py startapp ocr
INSTALLED_APPSに'ocr'を追加

config.urls.pyの修正
orc.urls.pyの修正
orc.views.pyに
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the OCR index.")

を追加。

3. bootstrapを使ったテンプレーを表示させる

inex.htmlを修正

## Imageモデルの追加

https://qiita.com/j54854/items/1f0560142e39d888251c

## OCR機能追加

1. 色々Installする

requirements.txtに
pyocr
tesseract
を追加

2. Dockerfile

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

を追加

## herokuでtesseract-ocr

Aptfileを追加して、herokuでわちゃわちゃする。

https://towardsdatascience.com/deploy-python-tesseract-ocr-on-heroku-bbcc39391a8d

追加する。

TESSDATA_PREFIX ./.apt/usr/share/tesseract-ocr/4.00/tessdata

https://github.com/heroku/heroku-buildpack-apt

heroku-18にダウングレード
エラー文：(127, b'tesseract: error while loading shared libraries: libarchive.so.13: cannot open shared object file: No such file or directory\n')
https://stackoverflow.com/questions/66087588/tesseract-error-while-loading-shared-libraries-libarchive-so-13-python



エラー文：(1, b'Error opening data file ./.apt/usr/share/tesseract-ocr/4.00/tessdata/jpn.traineddata\nPlease make sure the TESSDATA_PREFIX environment variable is set to your "tessdata" directory.\nFailed loading language \'jpn\'\nTesseract couldn\'t load any languages!\nCould not initialize tesseract.\n')


パーミッションがおかしい..

./.apt/usr/share/tesseract-ocr/4.00/tessdata

chmod a+r jpn.traineddata

コマンド
heroku run bash 
chmod -R a+r .apt/

TESSDATA_PREFIX = /app/.apt/usr/share/tesseract-ocr/4.00/tessdata

herokuが起動できた

engならOK、jpnにすると落ちる

localでjpnにしても、起動して正確にOCRできている。

→herokuでも日本語でOCRできた。

## タイムアウト問題

https://qiita.com/geeorgey/items/142146394a704e4ae7a4


rqを使ってみる

https://devcenter.heroku.com/ja/articles/python-rq

orctool.pyを消去してviewで処理して解決

## ファイル名問題

任意のファイル名を付けるようにしたい。
https://freeheroblog.com/filename-hash/