from game.GameComponent import GameAI
from logic.Action import Action
from logic.Board import Board
from logic.utils import get_action_map
from nerve.EvaluateCore import EvaluateCore


class OneStepAI(GameAI):
	
	def __init__(self, core: EvaluateCore):
		super().__init__()
		self.core = core
	
	def on_suggest_action(self, board: Board) -> Action:
		action_map = get_action_map(board.matrix)
		options = list(action_map.keys())
		
		best_action = options[0]
		best_score = 0
		for action in options:
			this_board = action_map[action]
			this_score = self.core.run_evaluate([this_board])
			if this_score[0] > best_score:
				best_action = action
				best_score = this_score
		return best_action
