from ai.EvaluateCore import EvaluateCore
from game.Action import Action
from game.Game import Game


class GameAI1(Game):
    def __init__(self, core: EvaluateCore, print_process=False):
        super().__init__()
        self.core = core
        self.print_process = print_process

    def on_get_action(self) -> Action:
        if self.print_process:
            print("round", self.round)
            print(self.board)

        actions = list(self.action_map)

        best_action = actions[0]
        best_score = 0
        for this_action in actions:
            this_board = self.action_map[this_action]
            this_score = self.core.run_evaluate([this_board])
            if this_score[0] > best_score:
                best_action = this_action
                best_score = this_score

        if self.print_process:
            print(best_action.value)
        return best_action

    def on_dead(self):
        if self.print_process:
            print("round", self.round)
            print(self.board)
            print("Dead!")
