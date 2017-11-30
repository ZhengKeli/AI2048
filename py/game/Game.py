from abc import ABCMeta, abstractmethod

import numpy as np

from game.Action import Action
from game.Pop import Pop
from game.utils import get_action_map, apply_pop


class Game:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.board = None
        self.action_map = None
        self.round = 0

        self.last_action = 0
        self.last_pop = 0

    def begin_loop(self):
        self.init_game()
        while True:
            if not self.next_round():
                break

    def begin_loop_recorded(self):
        self.init_game()
        history = []
        while True:
            history.append(self.board)
            if not self.next_round():
                history.append(self.board)
                break
        return history

    def on_init_board(self):
        self.board = np.zeros([4, 4], np.int)
        self.apply_pop()
        self.apply_pop()

    def init_game(self):
        self.round = 0
        self.on_init_board()
        self.action_map = get_action_map(self.board)

    def next_round(self):
        self.apply_action()
        self.apply_pop()

        self.action_map = get_action_map(self.board)
        if len(self.action_map) == 0:
            self.on_dead()
            return False

        self.round += 1
        return True

    @abstractmethod
    def on_dead(self):
        pass

    def apply_action(self):
        action = self.on_get_action()
        self.board = self.action_map[action]
        self.last_action = action

    @abstractmethod
    def on_get_action(self) -> Action:
        pass

    def apply_pop(self):
        pop = self.on_get_pop()
        self.board = apply_pop(self.board, pop)
        self.last_pop = pop

    def on_get_pop(self) -> Pop:
        empty_places = []
        for row in range(4):
            for column in range(4):
                if self.board[row][column] == 0:
                    empty_places.append((row, column))
        index = int(np.random.uniform() * len(empty_places))
        position = empty_places[index]

        if np.random.uniform() < 0.125:
            value = 2
        else:
            value = 1

        return Pop(position, value)
