from .base import * # base.pyを読み込む 

# 開発、本番で分けたい設定を記載

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodb3',
        'USER': 'postgres',
        'PASSWORD': 'Zaq12wsx2!',
        'HOST': 'localhost',
        'PORT': '15432'
    }
}
