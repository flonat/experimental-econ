from . import models
from otree.api import Page, WaitPage
from .models import Constants

class Introduction(Page):
    pass

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def get_timeout_seconds(self):
        if self.player.treatment in ['choice_overload', 'both']:
            return 10
        return None

    def before_next_page(self):
        self.player.set_payoff()

class Results(Page):
    def vars_for_template(self):
        return {
            'my_decision': self.player.decision,
            'computer_decision': self.player.computer_decision,
            'my_payoff': self.player.payoff,
        }

page_sequence = [Introduction, Decision, Results]
