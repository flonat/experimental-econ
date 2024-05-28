from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class InformationSheet(Page):
    def is_displayed(self):
        return self.round_number == 1

class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['consent']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        if self.player.consent == 'no':
            self.participant.vars['consent'] = False

class FollowUpQuestion(Page):
    form_model = 'player'
    form_fields = ['is_student', 'fictitious_name']

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars.get('consent', True)

    def vars_for_template(self):
        return {
            'is_student': self.player.is_student,
            'fictitious_name': self.player.fictitious_name,
        }

    def before_next_page(self):
        if self.player.is_student == 'yes' and not self.player.fictitious_name:
            self._is_frozen = True  # prevent proceeding without fictitious name

class GamesIntro(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars.get('consent', True)

page_sequence = [Introduction, InformationSheet, ConsentForm, FollowUpQuestion, GamesIntro]
