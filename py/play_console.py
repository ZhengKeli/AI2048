from game.Game import Game
from logic.StandardLogic import StandardLogic
from ui.ConsoleUI import ConsoleIndicator, ConsolePlayer

Game(
	StandardLogic(),
	ConsoleIndicator(),
	ConsolePlayer(),
).process()
