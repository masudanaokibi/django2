from .base import * # base.pyを読み込む 

# 開発、本番で分けたい設定を記載
# ssh ec2-user@18.181.168.249 -i C:\Users\masud\Downloads\test-key-1.pem -L 15432:database-1.crr3xmeryalf.ap-northeast-1.rds.amazonaws.com:5432

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
