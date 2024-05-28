from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Constants(BaseConstants):
    name_in_url = 'prisoners_dilemma_1'
    players_per_group = None  # Single-player or group games
    num_rounds = 1  # Set according to your experiment design
    instructions_template = 'prisoners_dilemma/Instructions.html'
    payoff_matrix = {
        'C': {
            'C': c(1),
            'D': c(0),
        },
        'D': {
            'C': c(5),
            'D': c(3),
        }
    }

class Subsession(BaseSubsession):
    def creating_session(self):
        treatments = ['control', 'choice_blindness', 'choice_overload', 'both']
        for player in self.get_players():
            if 'treatment' not in player.participant.vars:
                player.participant.vars['treatment'] = random.choice(treatments)
            player.treatment = player.participant.vars['treatment']

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    decision = models.StringField(
        choices=[('C', 'Cooperate'), ('D', 'Defect')],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )
    computer_decision = models.StringField()
    treatment = models.StringField()

    def set_payoff(self):
        if self.treatment in ['choice_blindness', 'both']:
            # Alter the decision to simulate choice blindness
            if self.decision == 'C':
                self.decision = 'D'
            else:
                self.decision = 'C'
        self.computer_decision = random.choice(['C', 'D'])
        self.payoff = Constants.payoff_matrix[self.decision][self.computer_decision]
