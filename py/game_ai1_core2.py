from ai.EvaluateCore import EvaluateCore
from game.GameAI1 import GameAI1

core = EvaluateCore("../graph/core2", "core")
GameAI1(core, True).begin_loop()
