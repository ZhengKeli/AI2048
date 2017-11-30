from ai.EvaluateCore import EvaluateCore
from ai.utils import train_core
from game.GameAI1 import GameAI1

core = EvaluateCore("../graph/core2", "core")
game = GameAI1(core)

train_core(
    core, game,
    train_count=3e3,
    group_size=100,
    learning_rate=0.003
)
