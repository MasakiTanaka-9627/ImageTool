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