from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage

class EndPage(Page):
    pass

page_sequence = [EndPage]