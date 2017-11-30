from abc import ABCMeta, abstractmethod

from game.Action import Action
from game.Pop import Pop
from game.utils import apply_action, apply_pop


class Tree:
    __metaclass__ = ABCMeta

    def __init__(self, board):
        self.board = board
        self.board_id = None
        self.board_score = None

        self.weight = None

        self.branches = None

    def evaluate_board_score_gather(self, pending: list):
        if self.branches is not None:
            for branch in self.branches:
                branch.evaluate_board_score_gather(pending)
        elif self.board_score is None:
            self.board_id = len(pending)
            pending.append(self.board)
        return pending

    def evaluate_board_score_dispatch(self, result):
        if self.branches is not None:
            for branch in self.branches:
                branch.evaluate_board_score_dispatch(result)
        elif self.board_id is not None:
            self.board_score = result[self.board_id]
            self.board_id = None

    def grow_tree(self, variant):
        if self.grow_next_branches(variant):
            for branch in self.branches:
                branch.grow_tree(variant * branch.weight)

    @abstractmethod
    def grow_next_branches(self, variant: float = None) -> bool:
        pass

    @abstractmethod
    def compute_tree_score(self):
        pass


class ActionTree(Tree):
    __metaclass__ = ABCMeta

    def __init__(self, board, action: Action):
        super().__init__(board)
        self.action = action

    def grow_next_branches(self, variant: float = None) -> bool:
        if self.branches is not None:
            return True

        positions = []
        for row in range(4):
            for column in range(4):
                if self.board[row][column] == 0:
                    positions.append((row, column))

        branch_count = 2 * len(positions)
        if variant is not None and variant < branch_count:
            return False

        branches = []
        for position in positions:
            for (value, rate) in [(1, 0.875), (2, 0.125)]:
                pop = Pop(position, value)
                new_board = apply_pop(self.board, pop)
                branches.append(PopTree(new_board, rate / branch_count, pop))
        self.branches = branches
        return True

    def compute_tree_score(self):
        if self.branches is None:
            return self.board_score
        else:
            weighted_branch_scores = [branch.compute_tree_score() * branch.possibility for branch in self.branches]
            return sum(weighted_branch_scores)

    def pick_branch(self, pop: Pop):
        if self.branches is None:
            new_board = apply_pop(self.board, pop)
            return PopTree(new_board, 1, pop)
        for branch in self.branches:
            if branch.pop == pop:
                return branch


class PopTree(Tree):
    def __init__(self, board, possibility: float, pop: Pop):
        super().__init__(board)
        self.weight = possibility
        self.pop = pop
        self.possibility = possibility

    def grow_next_branches(self, variant: float = None) -> bool:
        if self.branches is not None:
            return True

        branches = []
        for action in Action:
            new_board, changed = apply_action(self.board, action)
            if changed:
                branches.append(ActionTree(new_board, action))
        branch_count = len(branches)

        if variant is not None and variant < branch_count:
            return False

        for branch in branches:
            branch.weight = 1.0 / branch_count
        self.branches = branches
        return True

    def compute_tree_score(self):
        if self.branches is None:
            return self.board_score
        else:
            branch_scores = [branch.compute_tree_score() for branch in self.branches]
            return max(branch_scores, default=0)

    def pick_branch(self, action: Action):
        if self.branches is None:
            new_board, changed = apply_action(self.board, action)
            return ActionTree(new_board, action)
        for branch in self.branches:
            if branch.action == action:
                return branch
