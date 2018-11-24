from typing import Optional, List

from game.GameComponent import GameAI, GamePlayer, GameComponent, GameInitializer, GameReactor, GameListener
from logic.Action import Action
from logic.Board import Board
from logic.Pop import Pop


class Game:
	def __init__(self, *components: GameComponent):
		self.listeners: List[GameListener] = []
		self.initializer = None
		self.reactor = None
		self.player = None
		self.ai = None
		self.add_components(*components)
	
	def add_components(self, *components: GameComponent):
		for component in components:
			if isinstance(component, GameListener):
				component: GameListener
				self.listeners.append(component)
			if isinstance(component, GameInitializer):
				component: GameInitializer
				self.initializer = component
			if isinstance(component, GameReactor):
				component: GameReactor
				self.reactor: GameReactor = component
			if isinstance(component, GamePlayer):
				component: GamePlayer
				self.player: GamePlayer = component
			if isinstance(component, GameAI):
				component: GameAI
				self.ai: GameAI = component
	
	# process
	
	def process(self):
		
		if self.initializer is None:
			raise RuntimeError("There's no GameInitializer")
		if self.reactor is None:
			raise RuntimeError("There's no GameReactor")
		if (self.player is None) and (self.ai is None):
			raise RuntimeError("There's neither GamePlayer nor GameAI")
		
		# init
		board = self.init()
		self.inited(board)
		
		rounds = 0
		while not board.is_dead():
			self.new_round(rounds)
			
			# action
			action = self.get_action(board)
			board.apply_action(action)
			self.applied_action(action, board)
			
			# pop
			pop = self.get_reaction(board)
			if pop is not None:
				board.apply_pop(pop)
			self.applied_reaction(pop, board)
			
			rounds += 1
		
		self.dead(rounds, board)
	
	# events
	
	def init(self) -> Board:
		return self.initializer.on_init()
	
	def inited(self, board: Board):
		for listener in self.listeners:
			listener.on_inited(board)
	
	def new_round(self, rounds: int):
		for listener in self.listeners:
			listener.on_new_round(rounds)
	
	def get_action(self, board: Board) -> Action:
		if self.ai is None:
			if self.player is None:
				raise RuntimeError("No action provided!")
			else:
				return self.player.on_get_action(board)
		else:
			if self.player is None:
				return self.ai.on_suggest_action(board)
			else:
				suggestion = self.ai.on_suggest_action(board)
				self.ai_suggested(suggestion)
				return self.player.on_get_action(board)
	
	def ai_suggested(self, suggestion: Action):
		for listener in self.listeners:
			listener.on_ai_suggested(suggestion)
	
	def applied_action(self, action: Action, board: Board):
		for listener in self.listeners:
			listener.on_applied_action(action, board)
	
	def get_reaction(self, board: Board) -> Optional[Pop]:
		return self.reactor.on_get_reaction(board)
	
	def applied_reaction(self, pop: Pop, board: Board):
		for listener in self.listeners:
			listener.on_applied_reaction(pop, board)
	
	def dead(self, rounds: int, board: Board):
		for listener in self.listeners:
			listener.on_dead(rounds, board)
