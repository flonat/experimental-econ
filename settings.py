import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
ADMIN_PASSWORD = os.environ.get('OTREE_ADMIN_PASSWORD')

DEBUG = False

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'en-us'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = [
    'otree',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'introduction',
    'prisoners_dilemma_1',
    'public_goods_1',
    'market_entry_1',
    'prisoners_dilemma_2',
    'public_goods_2',
    'market_entry_2',
    'post_game_questions',
    'end',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Keep CSRF middleware enabled
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'yourapp.middlewares.DisableCSRFForSpecificViewsMiddleware',  # Add custom middleware
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'introduction', 'templates')],
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

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, 'static'),
]

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'otree_experimental_econ',
        'display_name': "Experimental Economics",
        'num_demo_participants': 4,
        'app_sequence': [
            'introduction',
            'prisoners_dilemma_1',
            'public_goods_1',
            'market_entry_1',
            'prisoners_dilemma_2',
            'public_goods_2',
            'market_entry_2',
            'post_game_questions',
            'end'
        ],
    },
]

INSTALLED_OTREE_APPS = [
    'introduction',
    'prisoners_dilemma_1',
    'public_goods_1',
    'market_entry_1',
    'prisoners_dilemma_2',
    'public_goods_2',
    'market_entry_2',
    'post_game_questions',
    'end',
]

CSRF_TRUSTED_ORIGINS = ['https://romarin.fly.dev/']
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False