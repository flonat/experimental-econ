from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

class Constants(BaseConstants):
    name_in_url = 'games'
    players_per_group = 2
    num_rounds = 2
    game_sequence = ['PrisonersDilemma', 'PublicGoods', 'MarketEntry']
    payoff_matrix_pd = {
        'C': {'C': (1, 1), 'D': (0, 5)},
        'D': {'C': (5, 0), 'D': (3, 3)},
    }
    # Add payoffs for PublicGoods and MarketEntry games if needed

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['group'] = random.choice(
                    ['control', 'choice_blindness', 'choice_overload', 'both']
                )

class Group(BaseGroup):
    def set_payoffs_pd(self):
        for p in self.get_players():
            opponent = p.get_others_in_group()[0]
            payoff_matrix = Constants.payoff_matrix_pd
            p.payoff = payoff_matrix[p.decision][opponent.decision][0]
            opponent.payoff = payoff_matrix[p.decision][opponent.decision][1]

class Player(BasePlayer):
    decision = models.StringField(
        choices=['C', 'D'],
        widget=widgets.RadioSelect,
        label='Your decision:'
    )
