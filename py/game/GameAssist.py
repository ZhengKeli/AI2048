from abc import ABCMeta

from ai.EvaluateCore import EvaluateCore
from game.Action import Action
from game.Game import Game
from game.GameAI1 import GameAI1
from game.GameAI2 import GameAI2
from game.Pop import Pop


class GameAssist(Game):
    __metaclass__ = ABCMeta

    keyboard = {
        "w": Action.UP,
        "s": Action.DOWN,
        "a": Action.LEFT,
        "d": Action.RIGHT,
        "": None
    }

    def on_init_board(self):
        if self.board is None:
            super().on_init_board()

    def on_get_pop(self) -> Pop:
        print(self.board)
        input_list = input("next pop up:").split()
        if len(input_list) == 0:
            return super().on_get_pop()
        (row, column, value) = (int(item) for item in input_list)
        return Pop((row, column), value)

    def on_get_action(self) -> Action:
        print(self.board)
        ai_action = super().on_get_action()
        print("AI suggested action:", ai_action.value)
        user_action = GameAssist.keyboard[input("Your action:")]
        if user_action is None:
            return ai_action
        else:
            return user_action

    def on_dead(self):
        print(self.board)
        print("You are dead!")


class GameAssist1(GameAssist, GameAI1):
    def __init__(self, core: EvaluateCore, board=None):
        super().__init__(core, False)
        self.board = board


class GameAssist2(GameAssist, GameAI2):
    def __init__(self, core: EvaluateCore, variant: float, board=None):
        super().__init__(core, variant, False)
        self.board = board
