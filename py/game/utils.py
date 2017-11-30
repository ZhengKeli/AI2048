import numpy as np

from game.Pop import Pop
from game.Action import Action


def apply_action(board, action: Action):
    new_board = np.zeros([4, 4], np.int)

    if action == Action.LEFT:
        def get_old_value(row, column):
            return board[row][column]

        def set_new_value(row, column, value):
            new_board[row][column] = value

        def get_new_value(row, column):
            return new_board[row][column]
    elif action == Action.RIGHT:
        def get_old_value(row, column):
            return board[row][3 - column]

        def set_new_value(row, column, value):
            new_board[row][3 - column] = value

        def get_new_value(row, column):
            return new_board[row][3 - column]
    elif action == Action.UP:
        def get_old_value(row, column):
            return board[column][row]

        def set_new_value(row, column, value):
            new_board[column][row] = value

        def get_new_value(row, column):
            return new_board[column][row]
    else:
        def get_old_value(row, column):
            return board[3 - column][row]

        def set_new_value(row, column, value):
            new_board[3 - column][row] = value

        def get_new_value(row, column):
            return new_board[3 - column][row]

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

    return new_board, changed


def apply_pop(board, pop: Pop):
    new_board = np.array(board)
    new_board[pop.position[0]][pop.position[1]] = pop.value
    return new_board


def get_action_map(board):
    allowed_actions = {}
    for action in Action:
        new_board, changed = apply_action(board, action)
        if changed:
            allowed_actions[action] = new_board
    return allowed_actions
