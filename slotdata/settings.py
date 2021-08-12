import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


SECRET_KEY = env('SECRET_KEY')

DEBUG = env.get_value('DEBUG', cast=bool)

ALLOWED_HOSTS = [
    '118.27.117.87',
    'localhost',
    '127.0.0.1',
    'bishi.xyz',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'list',
    'bootstrap4',
    'bootstrapform',
    'django_crontab',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'slotdata.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'slotdata.wsgi.application'


#
DATABASES = {

    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'slotdata',
        'USER': 'bishi',
        'PASSWORD': '7234',
        'HOST': 'localhost',
        'PORT': '',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
# collectstaticなどを行った際にファイルを設置するstaticフォルダの場所を記述（開発の際は必要ないのでコメントアウトしておく）

# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# htmlファイルなどから読み込むstaticフォルダの場所を記述
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRONJOBS = [
    # 時間指定、アプリ名.ファイル名.メソッド名
    # ('*/3 * * * *', 'list.cron.cron_shori')

]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


# Upload Settings

DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000
FILE_UPLOAD_MAX_MEMORY_SIZE = 15728640
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640
