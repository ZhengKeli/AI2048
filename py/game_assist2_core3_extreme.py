import numpy as np

from ai.EvaluateCore import EvaluateCore
from game.GameAssist import GameAssist2

board = np.array([
    [2, 10, 5, 2],
    [0, 2, 6, 4],
    [0, 0, 2, 6],
    [0, 1, 2, 2],
], np.int)
core = EvaluateCore("../graph/core2", "core")
GameAssist2(core, 1e4, board).begin_loop()
