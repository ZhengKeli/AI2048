from abc import ABCMeta, abstractmethod
from typing import Optional

from logic.Action import Action
from logic.Board import Board
from logic.Pop import Pop


class GameComponent:
	__metaclass__ = ABCMeta
	
	pass


class GameListener(GameComponent):
	__metaclass__ = ABCMeta
	
	def on_inited(self, board: Board):
		pass
	
	def on_new_round(self, rounds: int):
		pass
	
	def on_ai_suggested(self, suggestion: Action):
		pass
	
	def on_applied_action(self, action: Action, board: Board):
		pass
	
	def on_applied_reaction(self, pop: Pop, board: Board):
		pass
	
	def on_dead(self, rounds: int, board: Board):
		pass


class GameInitializer(GameComponent):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def on_init(self) -> Board:
		pass


class GameReactor(GameComponent):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def on_get_reaction(self, board: Board) -> Optional[Pop]:
		pass


class GamePlayer(GameComponent):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def on_get_action(self, board: Board) -> Action:
		pass


class GameAI(GameComponent):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def on_suggest_action(self, board: Board) -> Action:
		pass
