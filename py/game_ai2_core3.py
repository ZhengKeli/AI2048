from ai.EvaluateCore import EvaluateCore
from game.GameAI2 import GameAI2

core = EvaluateCore("../graph/core3", "core")
GameAI2(core, 256, True).begin_loop()
