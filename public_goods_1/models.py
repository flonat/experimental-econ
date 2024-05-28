from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Constants(BaseConstants):
    name_in_url = 'public_goods_1'
    players_per_group = None  # Single-player game
    num_rounds = 1
    instructions_template = 'public_goods/Instructions.html'
    endowment = c(10)
    multiplier = 2
    computer_contribution = c(5)  # Fixed contribution by the computer

class Subsession(BaseSubsession):
    def creating_session(self):
        treatments = ['control', 'choice_blindness', 'choice_overload', 'both']
        for player in self.get_players():
            if 'treatment' not in player.participant.vars:
                player.participant.vars['treatment'] = random.choice(treatments)
            player.treatment = player.participant.vars['treatment']

class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        players = self.get_players()
        self.total_contribution = sum([p.contribution for p in players]) + Constants.computer_contribution
        self.individual_share = self.total_contribution * Constants.multiplier / (len(players) + 1)  # Include the computer
        for p in players:
            p.payoff = Constants.endowment - p.contribution + self.individual_share

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
    treatment = models.StringField()

    def set_contribution(self, contribution):
        if self.treatment in ['choice_blindness', 'both']:
            self.contribution = Constants.endowment - contribution
        else:
            self.contribution = contribution
