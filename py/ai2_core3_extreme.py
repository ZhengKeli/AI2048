from ai.TreeStepAI import TreeStepAI
from game.Game import Game
from logic.StandardLogic import StandardLogic
from nerve.EvaluateCore import EvaluateCore
from ui.ConsoleUI import ConsoleIndicator

core = EvaluateCore("../graph/core3", "core")
Game(
	StandardLogic(),
	ConsoleIndicator(),
	TreeStepAI(core, 1e4)
).process()
