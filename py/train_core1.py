from ai.OneStepAI import OneStepAI
from game.Game import Game
from logic.StandardLogic import StandardLogic
from nerve.EvaluateCore import EvaluateCore
from nerve.utils import train_core

core = EvaluateCore("../graph/core1", "core")
game = Game(
	StandardLogic(),
	OneStepAI(core)
)
train_core(
	core, game,
	train_count=3e3,
	group_size=100,
	learning_rate=0.003
)
