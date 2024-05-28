from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Constants(BaseConstants):
    name_in_url = 'introduction'
    players_per_group = None  # Adjust as needed for each game
    num_rounds = 1
    game_sequence = ['PrisonersDilemma', 'PublicGoods', 'MarketEntry']
    endowment = c(10)
    multiplier = 2
    payoff_matrix_pd = {
        'C': {'C': (1, 1), 'D': (0, 5)},
        'D': {'C': (5, 0), 'D': (3, 3)},
    }

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            players = self.get_players()
            treatments = ['control', 'choice_blindness', 'choice_overload', 'both']
            num_treatments = len(treatments)
            for i, player in enumerate(players):
                player.participant.vars['group'] = treatments[i % num_treatments]

class Group(BaseGroup):
    def set_payoffs_pd(self):
        for p in self.get_players():
            opponent = p.get_others_in_group()[0]
            payoff_matrix = Constants.payoff_matrix_pd
            p.payoff = payoff_matrix[p.decision][opponent.decision][0]
            opponent.payoff = payoff_matrix[p.decision][opponent.decision][1]

    def set_payoffs_pg(self):
        total_contribution = sum([p.contribution for p in self.get_players()])
        individual_share = total_contribution * Constants.multiplier / Constants.players_per_group
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + individual_share

class Player(BasePlayer):
    consent = models.BooleanField(
        choices=[
            [True, 'Yes'],
            [False, 'No']
        ],
        widget=widgets.RadioSelect
    )
    decision = models.StringField(
        choices=['C', 'D'],
        widget=widgets.RadioSelect,
        label='Your decision:'
    )
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment,
        label="How much will you contribute to the public pool?"
    )
    is_student = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect,
        label='Are you a student in the Experimental Economics class of Prof. Rosemarie Nagel?'
    )
    participant_type = models.StringField(choices=['student', 'random', 'prolific'])
    fictitious_name = models.StringField(blank=True)