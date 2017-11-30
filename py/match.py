from ai.EvaluateCore import EvaluateCore
from ai.utils import match_core
from game.GameAI1 import GameAI1
from game.GameAI2 import GameAI2
from game.GameRandom import GameRandom

core1 = EvaluateCore("../graph/core1", "core")
# core2 = EvaluateCore("../graph/core2", "core")
# core3 = EvaluateCore("../graph/core3", "core")
matches = [
    ("random", GameRandom(), 300),
    ("ai1_core1", GameAI1(core1), 200),
    # ("ai1_core2", GameAI1(core2), 200),
    # ("ai2_core2", GameAI2(core2, 256), 100),
    # ("ai2_core3", GameAI2(core3, 256), 100),
    # ("ai2_core3_extreme", GameAI2(core3, 1e4), 50),
]

match_core(matches)
