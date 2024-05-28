from otree.api import (
        models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
    )

    class Constants(BaseConstants):
        name_in_url = 'post_game_questions'
        players_per_group = None
        num_rounds = 1

    class Subsession(BaseSubsession):
        pass

    class Group(BaseGroup):
        pass

    class Player(BasePlayer):
        age = models.IntegerField(label="What is your age?")
        gender = models.StringField(
            choices=['Male', 'Female', 'Other'],
            widget=widgets.RadioSelect,
            label="What is your gender?"
        )
        education = models.StringField(
            choices=['High School', 'Bachelor', 'Master', 'PhD'],
            widget=widgets.RadioSelect,
            label="What is your highest level of education?"
        )
        employment = models.StringField(
            choices=['Employed', 'Unemployed', 'Student', 'Retired'],
            widget=widgets.RadioSelect,
            label="What is your employment status?"
        )
        feelings_towards_algorithms = models.IntegerField(
            label="Feelings towards algorithms (fair decisions, unbiased decisions, comfortable to rely on algorithms)",
            widget=widgets.RadioSelectHorizontal,
            choices=[1, 2, 3, 4, 5]
        )
        time_pressure = models.IntegerField(
            label="Time pressure (perform well under time pressure, efficient decision-making under time pressure, stress for quick decision making)",
            widget=widgets.RadioSelectHorizontal,
            choices=[1, 2, 3, 4, 5]
        )
        fairness_of_algorithms = models.IntegerField(
            label="Fairness of algorithms (belief that they are fair, transparent, and whether or not they are biased)",
            widget=widgets.RadioSelectHorizontal,
            choices=[1, 2, 3, 4, 5]
        )