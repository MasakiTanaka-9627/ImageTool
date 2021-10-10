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

