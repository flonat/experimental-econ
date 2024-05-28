from otree.api import Currency as c, currency_range
from otree.api import Page, WaitPage

class EndPage(Page):
    def get_template_name(self):
        return 'EndPage.html'

page_sequence = [EndPage]