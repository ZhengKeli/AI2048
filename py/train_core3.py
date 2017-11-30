from ai.EvaluateCore import EvaluateCore
from ai.utils import train_core
from game.GameAI1 import GameAI1
from game.GameAI2 import GameAI2

core = EvaluateCore("../graph/core3", "core")
game1 = GameAI1(core)
game2 = GameAI2(core, 128)

train_core(
    core, game1,
    train_count=2e3,
    group_size=100,
    learning_rate=0.005
)

train_core(
    core, game1,
    train_count=2e3,
    group_size=100,
    learning_rate=0.003
)

train_core(
    core, game2,
    train_count=200,
    group_size=10,
    learning_rate=0.001
)

train_core(
    core, game2,
    train_count=200,
    group_size=10,
    learning_rate=3e-4
)
