# end/models.py

from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

class Constants(BaseConstants):
    name_in_url = 'end'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass
