from ai.OneStepAI import OneStepAI
from ai.TreeStepAI import TreeStepAI
from game.Game import Game
from logic.StandardLogic import StandardLogic
from nerve.EvaluateCore import EvaluateCore
from nerve.utils import train_core

core = EvaluateCore("../graph/core3", "core")
game1 = Game(
	StandardLogic(),
	OneStepAI(core)
)
game2 = Game(
	StandardLogic(),
	TreeStepAI(core, 128)
)
train_core(
	core, game1,
	train_count=3e3,
	group_size=100,
	learning_rate=0.003
)
train_core(
	core, game2,
	train_count=200,
	group_size=10,
	learning_rate=0.0001
)
