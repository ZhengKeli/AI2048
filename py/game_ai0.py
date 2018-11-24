from ai.RandomAI import RandomAI
from game.Game import Game
from logic.StandardLogic import StandardLogic
from ui.ConsoleUI import ConsoleIndicator

Game(
	StandardLogic(),
	ConsoleIndicator(),
	RandomAI()
).process()
