from otree.api import Currency as c, currency_range
from otree.api import Page, WaitPage
from . import models
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def get_template_name(self):
        return 'introduction/Introduction.html'

class InformationSheet(Page):
    def get_template_name(self):
        return 'introduction/InformationSheet.html'

class ProlificSheet(Page):
    def get_template_name(self):
        return 'introduction/ProlificSheet.html'

class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['consent']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        if self.player.consent == 'no':
            self.participant.vars['consent'] = False

    def get_template_name(self):
        return 'introduction/ConsentForm.html'

class FollowUpQuestion(Page):
    form_model = 'player'
    form_fields = ['participant_type', 'fictitious_name']

    def before_next_page(self):
        redirect_url = 'GamesIntro'
        self.participant.vars['redirect_url'] = redirect_url

    def get_template_name(self):
        return 'introduction/FollowUpQuestion.html'

class GamesIntro(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars.get('consent', True)

    def get_template_name(self):
        return 'introduction/GamesIntro.html'

page_sequence = [
    Introduction,
    InformationSheet,
    ProlificSheet,
    ConsentForm,
    FollowUpQuestion,
    GamesIntro,
]
