from typing import Optional

import numpy as np

from logic.Action import Action
from logic.Pop import Pop


def apply_action(board, action: Action):
	new_board_matrix = np.zeros([4, 4], np.int)
	
	if action == Action.LEFT:
		def get_old_value(row, column):
			return board[row][column]
		
		def set_new_value(row, column, value):
			new_board_matrix[row][column] = value
		
		def get_new_value(row, column):
			return new_board_matrix[row][column]
	elif action == Action.RIGHT:
		def get_old_value(row, column):
			return board[row][3 - column]
		
		def set_new_value(row, column, value):
			new_board_matrix[row][3 - column] = value
		
		def get_new_value(row, column):
			return new_board_matrix[row][3 - column]
	elif action == Action.UP:
		def get_old_value(row, column):
			return board[column][row]
		
		def set_new_value(row, column, value):
			new_board_matrix[column][row] = value
		
		def get_new_value(row, column):
			return new_board_matrix[column][row]
	else:
		def get_old_value(row, column):
			return board[3 - column][row]
		
		def set_new_value(row, column, value):
			new_board_matrix[3 - column][row] = value
		
		def get_new_value(row, column):
			return new_board_matrix[3 - column][row]
	
	changed = False
	for r in range(4):
		c_old = 0
		c_new = 0
		while c_old < 4 and c_new < 4:
			value_old = get_old_value(r, c_old)
			value_new = get_new_value(r, c_new)
			
			if value_old == 0:
				c_old += 1
			elif value_new == 0:
				set_new_value(r, c_new, value_old)
				if c_new != c_old:
					changed = True
				c_old += 1
			elif value_old == value_new:
				set_new_value(r, c_new, value_old + 1)
				changed = True
				c_old += 1
				c_new += 1
			else:
				c_new += 1
	
	return new_board_matrix, changed


def apply_pop(board, pop: Pop):
	new_board_matrix = np.array(board, np.int)
	new_board_matrix[pop.position[0]][pop.position[1]] = pop.value
	return new_board_matrix


def get_action_map(board):
	action_map = {}
	for action in Action:
		new_board_matrix, changed = apply_action(board, action)
		if changed:
			action_map[action] = new_board_matrix
	return action_map


def get_random_pop(board) -> Optional[Pop]:
	empty_places = []
	for row in range(4):
		for column in range(4):
			if board[row][column] == 0:
				empty_places.append((row, column))
	if not len(empty_places) > 0:
		return None
	
	index = int(np.random.uniform() * len(empty_places))
	position = empty_places[index]
	
	if np.random.uniform() < 0.125:
		value = 2
	else:
		value = 1
	
	return Pop(position, value)
