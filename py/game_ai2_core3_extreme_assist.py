import numpy as np

from ai.TreeStepAI import TreeStepAI
from game.Game import Game
from logic.StandardLogic import CustomInitializer, StandardInitializer
from nerve.EvaluateCore import EvaluateCore
from ui.ConsoleUI import ConsoleReactor, ConsolePlayer, ConsoleIndicator

board = np.array([
	[2, 2, 3, 1],
	[4, 4, 6, 8],
	[1, 5, 2, 1],
	[2, 3, 1, 3],
], np.int)

core = EvaluateCore("../graph/core3", "core")
Game(
	StandardInitializer(),
	ConsoleReactor(),
	CustomInitializer(board),
	ConsoleIndicator(),
	ConsolePlayer(),
	TreeStepAI(core, 256)
).process()
