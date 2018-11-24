from typing import Optional

from game.GameComponent import GamePlayer, GameListener, GameReactor
from logic.Action import Action
from logic.Board import Board
from logic.Pop import Pop


class ConsoleIndicator(GameListener):
	
	def on_inited(self, board: Board):
		print(board.matrix)
		print("Game Start!")
	
	def on_new_round(self, rounds: int):
		print()
		print("Round", rounds)
	
	def on_ai_suggested(self, suggestion: Action):
		print()
		print("AI suggested action:", suggestion)
	
	def on_applied_action(self, action: Action, board: Board):
		print()
		print(board.matrix)
		print("Applied action:", action)
	
	def on_applied_reaction(self, pop: Pop, board: Board):
		print()
		print(board.matrix)
		print("Applied pop:", pop.position, pop.value)
	
	def on_dead(self, rounds: int, board: Board):
		print()
		print(board.matrix)
		print("Game Over!")
		print("rounds =", rounds)


class ConsolePlayer(GamePlayer):
	def on_get_action(self, board: Board) -> Action:
		while True:
			print(board.matrix)
			key = input("Input your action:")
			action = {
				"w": Action.UP,
				"s": Action.DOWN,
				"a": Action.LEFT,
				"d": Action.RIGHT
			}.get(key)
			if action is None:
				print("Please type 'w' 'a' 's' or 'd' but not '", key, "'", sep="")
				continue
			if action not in board.get_options():
				print("Your action is illegal!")
				continue
			return action


class ConsoleReactor(GameReactor):
	def on_get_reaction(self, board: Board) -> Optional[Pop]:
		while True:
			print(board.matrix)
			input_list = input("Next pop up (r c v):").split()
			if len(input_list) == 3:
				(row, column, value) = (int(item) for item in input_list)
				return Pop((row, column), value)
			print("Illegal input!")
