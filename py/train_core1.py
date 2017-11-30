from ai.EvaluateCore import EvaluateCore
from ai.utils import train_core
from game.GameRandom import GameRandom

core = EvaluateCore("../graph/core1", "core")
game = GameRandom()

train_core(
    core, game,
    train_count=3e3,
    group_size=100,
    learning_rate=0.003
)
