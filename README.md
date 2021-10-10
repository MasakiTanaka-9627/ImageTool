# tool

## 環境構築

settings.py

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

## heroku

https://qiita.com/yusuke_mrmt/items/1a3ee727d119617b2d85
runtime.txt
Procfile
settings.py


https://qiita.com/Kohey222/items/82f3a76e0247b2d387db
> heroku config:set DISABLE_COLLECTSTATIC=1