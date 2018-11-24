from ai.OneStepAI import OneStepAI
from game.Game import Game
from logic.StandardLogic import StandardLogic
from nerve.EvaluateCore import EvaluateCore
from ui.ConsoleUI import ConsoleIndicator

core = EvaluateCore("../graph/core2", "core")
Game(
	StandardLogic(),
	ConsoleIndicator(),
	OneStepAI(core)
).process()
