from typing import Optional

from game.GameComponent import GameInitializer, GameReactor
from logic.Board import Board
from logic.Pop import Pop
from logic.utils import get_random_pop


class StandardInitializer(GameInitializer):
	def on_init(self) -> Board:
		board = Board()
		board.apply_pop(get_random_pop(board.matrix))
		board.apply_pop(get_random_pop(board.matrix))
		return board


class StandardReactor(GameReactor):
	def on_get_reaction(self, board: Board) -> Optional[Pop]:
		return get_random_pop(board.matrix)


class StandardLogic(StandardInitializer, StandardReactor):
	pass


class CustomInitializer(GameInitializer):
	
	def __init__(self, board):
		if isinstance(board, Board):
			self.board = board
		else:
			self.board = Board(board)
	
	def on_init(self) -> Board:
		return self.board
