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
    form_fields = ['decision']

    def before_next_page(self):
        # Set the computer's decision here
        self.player.computer_decision = 'Defect'  # or some logic to determine the computer's decision
        self.player.set_payoff()

    def get_template_name(self):
        return 'Decision.html'

class Results(Page):
    def vars_for_template(self):
        return {
            'my_decision': self.player.decision,
            'computer_decision': self.player.computer_decision,
            'my_payoff': self.player.payoff,
        }

    def get_template_name(self):
        return 'Results.html'

page_sequence = [Intro, Decision, Results]
