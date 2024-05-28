from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class GeneralQuestions(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'employment']

class SpecificQuestions(Page):
    form_model = 'player'
    form_fields = [
        'feelings_towards_algorithms',
        'time_pressure',
        'fairness_of_algorithms'
    ]

page_sequence = [GeneralQuestions, SpecificQuestions]