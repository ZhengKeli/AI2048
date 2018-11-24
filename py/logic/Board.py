from typing import Optional

import numpy as np

from logic.Pop import Pop
from logic.utils import apply_pop, get_action_map, get_random_pop
from .Action import Action


class Board:
	
	def __init__(self, matrix=None):
		if matrix is None:
			matrix = np.zeros([4, 4], np.int)
		self.matrix = matrix
	
	def apply_std_init(self):
		self.matrix = np.zeros([4, 4], np.int)
		return self.apply_random_pop(), self.apply_random_pop()
	
	def apply_raw_init(self, matrix):
		self.matrix = matrix
		return matrix
	
	def apply_random_pop(self):
		pop = get_random_pop(self.matrix)
		if pop is None:
			return None
		else:
			return self.apply_pop(pop)
	
	def apply_pop(self, pop: Pop) -> Optional[Pop]:
		self.matrix = apply_pop(self.matrix, pop)
		return pop
	
	def apply_action(self, action: Action) -> Optional[Action]:
		new_board = get_action_map(self.matrix).get(action)
		if new_board is None:
			return None
		self.matrix = new_board
		return action
	
	def get_options(self):
		return list(get_action_map(self.matrix).keys())
	
	def is_dead(self) -> bool:
		return len(get_action_map(self.matrix)) == 0
