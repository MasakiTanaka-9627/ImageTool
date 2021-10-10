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