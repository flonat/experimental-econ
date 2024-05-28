import os
from pathlib import Path

# Define the BASE_DIR to be the directory where settings.py is located
BASE_DIR = Path(__file__).resolve().parent

# Set the secret key from the environment or provide a default value
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

# Set the admin password from the environment
ADMIN_PASSWORD = os.environ.get('OTREE_ADMIN_PASSWORD')

# Other Django settings
DEBUG = False

ALLOWED_HOSTS = ['*']

# Language code
LANGUAGE_CODE = 'en-us'  # Add this line`

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Application definition
INSTALLED_APPS = [
    'otree',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add your oTree apps here
    'introduction',
    'prisoners_dilemma',
    'public_goods',
    'market_entry',
    'post_game_questions',
    'end',
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

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# oTree settings
INSTALLED_OTREE_APPS = [
    'introduction',
    'prisoners_dilemma',
    'public_goods',
    'market_entry',
    'post_game_questions',
    'end',
]

SESSION_CONFIGS = [
    dict(
        name='otree_experimental_econ',
        display_name="Experimental Economics Survey",
        num_demo_participants=4,
        app_sequence=[
            'introduction',
            'prisoners_dilemma',
            'public_goods',
            'market_entry',
            'post_game_questions',
            'end'
        ],
    ),
]
