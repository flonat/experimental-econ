from otree.api import Currency as c, currency_range
from otree.api import Page, WaitPage

class EndPage(Page):
    def is_displayed(self):
        return self.round_number == 1

    def get_template_name(self):
        return 'EndPage.html'

page_sequence = [EndPage]