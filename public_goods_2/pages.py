from . import models
from otree.api import Page, WaitPage
from .models import Constants

class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1

    def get_template_name(self):
        return 'Intro.html'

class Decision(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def get_timeout_seconds(self):
        if self.player.treatment in ['choice_overload', 'both']:
            return 10
        return None

    def before_next_page(self):
        self.player.set_contribution(self.player.contribution)
        self.group.set_payoffs()
        
    def get_template_name(self):
        return 'Decision.html'

class Results(Page):
    def vars_for_template(self):
        return {
            'total_contribution': self.group.total_contribution,
            'individual_share': self.group.individual_share,
            'payoff': self.player.payoff,
            'computer_contribution': Constants.computer_contribution
        }.payoff,
    
    def get_template_name(self):
        return 'Results.html'
        
page_sequence = [Intro, Decision, Results]
