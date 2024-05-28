from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Constants(BaseConstants):
    name_in_url = 'market_entry'
    players_per_group = None  # Single-player game for simplicity
    num_rounds = 1
    instructions_template = 'market_entry/Instructions.html'
    entry_cost = c(5)
    incumbent_benefit = c(10)
    challenger_benefit = c(15)

class Subsession(BaseSubsession):
    def creating_session(self):
        treatments = ['control', 'choice_blindness', 'choice_overload', 'both']
        for player in self.get_players():
            if 'treatment' not in player.participant.vars:
                player.participant.vars['treatment'] = random.choice(treatments)
            player.treatment = player.participant.vars['treatment']
            player.role = random.choice(['incumbent', 'challenger'])

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    decision = models.StringField(
        choices=[('Enter', 'Enter'), ('Stay Out', 'Stay Out')],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )
    treatment = models.StringField()
    role = models.StringField()

    def set_payoff(self):
        num_competitors = random.randint(0, 5)  # Random number of competitors

        if self.role == 'incumbent':
            if self.decision == 'Enter':
                if num_competitors < 3:
                    self.payoff = Constants.incumbent_benefit - Constants.entry_cost
                else:
                    self.payoff = c(2)  # Low payoff if many competitors
            else:
                self.payoff = Constants.incumbent_benefit
        else:  # challenger
            if self.decision == 'Enter':
                if num_competitors < 3:
                    self.payoff = Constants.challenger_benefit - Constants.entry_cost
                else:
                    self.payoff = c(2)  # Low payoff if many competitors
            else:
                self.payoff = Constants.incumbent_benefit - Constants.entry_cost
