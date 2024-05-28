from . import models
from otree.api import Page, WaitPage
from .models import Constants

class Introduction(Page):
    pass

class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def get_timeout_seconds(self):
        if self.player.treatment in ['choice_overload', 'both']:
            return 10
        return None

    def before_next_page(self):
        self.player.set_contribution(self.player.contribution)
        self.group.set_payoffs()

class Results(Page):
    def vars_for_template(self):
        return {
            'total_contribution': self.group.total_contribution,
            'individual_share': self.group.individual_share,
            'payoff': self.player.payoff,
            'computer_contribution': Constants.computer_contribution
        }.payoff,
        
page_sequence = [Intro, Decision, Results]
