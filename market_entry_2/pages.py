from . import models
from otree.api import Page, WaitPage
from .models import Constants

class Intro(Page):
    def get_template_name(self):
        return 'Intro.html'

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def get_timeout_seconds(self):
        if self.player.treatment in ['choice_overload', 'both']:
            return 10
        return None

    def before_next_page(self):
        if self.player.treatment in ['choice_blindness', 'both']:
            # Alter the decision to simulate choice blindness
            if self.player.decision == 'Enter':
                self.player.decision = 'Stay Out'
            else:
                self.player.decision = 'Enter'
        self.player.set_payoff()
    
    def get_template_name(self):
        return 'Decision.html'

class Results(Page):
    def vars_for_template(self):
        return {
            'my_decision': self.player.decision,
            'player_role': self.player.player_role,
            'payoff': self.player.payoff,
        }
    
    def get_template_name(self):
        return 'Results.html'

page_sequence = [Intro, Decision, Results]