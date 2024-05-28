SESSION_CONFIGS = [
    dict(
        name='otree_experimental_econ',
        display_name="Experimental Economics Survey",
        num_demo_participants=4,
        app_sequence=[
            'introduction',
            'games',
            'post_game_questions',
            'end'
        ],
    ),
]

# Default session configurations
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

# Required apps for your project
INSTALLED_APPS = ['otree']

LANGUAGE_CODE = 'en'

USE_TZ = True
