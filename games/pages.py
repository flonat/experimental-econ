from otree.api import Currency as c, currency_range
    from . import models
    from ._builtin import Page, WaitPage
    from .models import Constants

    class GameWaitPage(WaitPage):
        wait_for_all_groups = True

    class PrisonersDilemma(Page):
        form_model = 'player'
        form_fields = ['decision']

        def vars_for_template(self):
            return {'group': self.participant.vars['group']}

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

    page_sequence = [
        GameWaitPage,
        PrisonersDilemma,
        ResultsWaitPage,
        Results
    ]