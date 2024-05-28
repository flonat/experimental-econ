from otree.api import Currency as c, currency_range
from otree.api import Page, WaitPage
from .models import Constants, Player

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def get_template_name(self):
        return 'Introduction.html'

    def before_next_page(self):
        pass  # No need to store consent variable anymore

class InformationSheet(Page):
    def get_template_name(self):
        return 'InformationSheet.html'

class ProlificSheet(Page):
    def get_template_name(self):
        return 'ProlificSheet.html'

class ConsentForm(Page):
    def get_template_name(self):
        return 'ConsentForm.html'

class FollowUpQuestion(Page):
    form_model = 'player'
    form_fields = ['participant_type', 'fictitious_name']

    def before_next_page(self):
        redirect_url = 'GamesIntro'
        self.participant.vars['redirect_url'] = redirect_url

    def get_template_name(self):
        return 'FollowUpQuestion.html'

class GamesIntro(Page):
    def is_displayed(self):
        return self.round_number == 1

    def get_template_name(self):
        return 'GamesIntro.html'

page_sequence = [
    Introduction,
    InformationSheet,
    # ProlificSheet,
    ConsentForm,
    FollowUpQuestion,
    GamesIntro,
]
