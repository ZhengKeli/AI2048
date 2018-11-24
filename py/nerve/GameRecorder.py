import numpy as np

from game.GameComponent import GameListener
from logic.Board import Board
from logic.Pop import Pop


class GameRecorder(GameListener):
	
	def __init__(self):
		self.history = []
	
	def on_inited(self, board: Board):
		self.history.append(np.array(board.matrix))
	
	def on_applied_reaction(self, pop: Pop, board: Board):
		self.history.append(np.array(board.matrix))
