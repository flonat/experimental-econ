import os
from os import environ

SESSION_CONFIGS = [
    dict(
        name='otree_experimental_econ',
        display_name="Experimental Economics Survey",
        num_demo_participants=4,
        app_sequence=[
            'introduction',
            'prisoners_dilemma',  # Add the Prisoner's Dilemma game here
            'public_goods',
            'market_entry',  # Add the Market Entry game here
            'post_game_questions',
            'end'
        ],
    ),
    # Add other session configs here
]


# Default session configurations
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

# Other Django settings
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Required apps for your project
INSTALLED_APPS = [
    'otree',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'romarin']
SECRET_KEY = os.environ.get('SECRET_KEY', 'aPL!fPfTQm8FT-hGi786XF27RNsrqPGz3XYzZCV*')
ADMIN_PASSWORD = os.environ.get('GarciaFaria73!')

LANGUAGE_CODE = 'en'

USE_TZ = True
