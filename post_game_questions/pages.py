from otree.api import Currency as c, currency_range
from . import models
from otree.api import Page, WaitPage
from .models import Constants

class GeneralQuestions(Page):
    def is_displayed(self):
        return self.round_number == 1
 
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'employment']
    
    def get_template_name(self):
        return 'GeneralQuestions.html'

class SpecificQuestions(Page):
    template_name = 'template/SpecificQuestions.html'
    form_model = 'player'
    form_fields = [
        'feelings_towards_algorithms',
        'time_pressure',
        'fairness_of_algorithms'
    ]
    
    def get_template_name(self):
        return 'SpecificQuestions.html'

page_sequence = [GeneralQuestions, SpecificQuestions]