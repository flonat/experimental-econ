from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

class Constants(BaseConstants):
    name_in_url = 'introduction'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    consent = models.StringField(
        choices=['yes', 'no'],
        widget=widgets.RadioSelectHorizontal,
        label='Do you consent to participate in this study?',
    )
    is_student = models.StringField(
        choices=['yes', 'no'],
        widget=widgets.RadioSelectHorizontal,
        label='Are you a student in the Experimental Economics class of Prof. Rosemarie Nagel?',
    )
    fictitious_name = models.StringField(
        label='Fictitious Name',
        blank=True
    )
