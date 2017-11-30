import numpy as np

from game.Action import Action
from game.Game import Game


class GameRandom(Game):
    def __init__(self, print_process=False):
        super().__init__()
        self.print_process = print_process

    def on_get_action(self) -> Action:
        if self.print_process:
            print("round", self.round)
            print(self.board)

        actions = list(self.action_map)
        index = np.random.randint(0, len(actions))
        action = actions[index]

        if self.print_process:
            print(action.value)
            print()
        return action

    def on_dead(self):
        if self.print_process:
            print("round", self.round)
            print(self.board)
            print("Dead!")
