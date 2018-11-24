import numpy as np

from game.GameComponent import GameAI
from logic.Action import Action
from logic.Board import Board


class RandomAI(GameAI):
	def on_suggest_action(self, board: Board) -> Action:
		options = board.get_options()
		index = np.random.randint(0, len(options))
		return options[index]
