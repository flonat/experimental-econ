from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class InformationSheet(Page):
    pass

class ProlificSheet(Page):
    pass

class ConsentForm(Page):
    pass

class FollowUpQuestion(Page):
    form_model = 'player'
    form_fields = ['participant_type', 'fictitious_name']

    def before_next_page(self):
        if self.player.participant_type == 'student':
            self.participant.vars['redirect_url'] = 'GamesIntro'
        elif self.player.participant_type == 'random':
            self.participant.vars['redirect_url'] = 'GamesIntro'
        elif self.player.participant_type == 'prolific':
            self.participant.vars['redirect_url'] = 'GamesIntro'

class GamesIntro(Page):
    pass

class GameWaitPage(WaitPage):
    wait_for_all_groups = True

class PrisonersDilemmaIntro(Page):
    pass

class PrisonersDilemma(Page):
    form_model = 'player'
    form_fields = ['decision']

    def get_timeout_seconds(self):
        if self.participant.vars['group'] in ['choice_overload', 'both']:
            return 10
        return None

    def before_next_page(self):
        if self.participant.vars['group'] in ['choice_blindness', 'both']:
            if self.player.decision == 'C':
                self.player.decision = 'D'
            else:
                self.player.decision = 'C'

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs_pd'

class Results(Page):
    def vars_for_template(self):
        return {
            'payoff': self.player.payoff,
            'opponent_decision': self.player.get_others_in_group()[0].decision,
        }

class PublicGoodsIntro(Page):
    pass

class PublicGoods(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def get_timeout_seconds(self):
        if self.participant.vars['group'] in ['choice_overload', 'both']:
            return 10
        return None

    def before_next_page(self):
        if self.participant.vars['group'] in ['choice_blindness', 'both']:
            self.player.contribution = Constants.endowment - self.player.contribution

class PublicGoodsResultsWaitPage(WaitPage):
    body_text = "Waiting for other participants to contribute."
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.group.set_payoffs_pg()

class PublicGoodsResults(Page):
    def vars_for_template(self):
        total_contribution = sum([p.contribution for p in self.group.get_players()])
        individual_share = total_contribution * Constants.multiplier / Constants.players_per_group
        return {
            'total_contribution': total_contribution,
            'individual_share': individual_share,
            'payoff': self.player.payoff,
        }

class MarketEntryIntro(Page):
    pass

class MarketEntry(Page):
    form_model = 'player'
    # Define form fields and logic for Market Entry Game
    pass

class MarketEntryResults(Page):
    # Define results page for Market Entry Game
    pass

class PostGameQuestions(Page):
    pass

class EndPage(Page):
    def is_displayed(self):
        return self.player.participant_type in ['student', 'random']

class ProlificEndPage(Page):
    def is_displayed(self):
        return self.player.participant_type == 'prolific'

page_sequence = [
    Introduction,
    InformationSheet,
    ConsentForm,
    FollowUpQuestion,
    GamesIntro,
    PrisonersDilemmaIntro,
    PrisonersDilemma,
    ResultsWaitPage,
    Results,
    PublicGoodsIntro,
    PublicGoods,
    PublicGoodsResultsWaitPage,
    PublicGoodsResults,
    MarketEntryIntro,
    MarketEntry,
    MarketEntryResults,
    PostGameQuestions,
    EndPage,
    ProlificEndPage
]
