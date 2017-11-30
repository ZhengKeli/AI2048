from ai.EvaluateCore import EvaluateCore
from ai.Tree import PopTree
from game.Action import Action
from game.Game import Game


class GameAI2(Game):
    def __init__(self, core: EvaluateCore, variant: float = 63, print_process: bool = False):
        super().__init__()

        self.core = core
        self.tree = None
        self.variant = variant

        self.print_process = print_process

    def init_game(self):
        super().init_game()
        self.tree = PopTree(self.board, 1, self.last_pop)

    def next_round(self):
        alive = super().next_round()
        if alive:
            action_branch = self.tree.pick_branch(self.last_action)
            self.tree = action_branch.pick_branch(self.last_pop)
        return alive

    def on_get_action(self) -> Action:
        if self.print_process:
            print("round", self.round)
            print(self.board)

        # tree thinking
        self.tree.grow_tree(self.variant)
        val_board = self.tree.evaluate_board_score_gather([])
        if len(val_board) > 0:
            result = self.core.run_evaluate(val_board)
            self.tree.evaluate_board_score_dispatch(result)

        # find best action
        max_score = 0
        max_score_branch = self.tree.branches[0]
        for branch in self.tree.branches:
            score = branch.compute_tree_score()
            if score > max_score:
                max_score = score
                max_score_branch = branch
        best_action = max_score_branch.action

        if self.print_process:
            print(best_action.value)
        return best_action

    def on_dead(self):
        if self.print_process:
            print("round", self.round)
            print(self.board)
            print("Dead!")
