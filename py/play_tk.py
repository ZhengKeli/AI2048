from game.Game import Game
from logic.StandardLogic import StandardLogic
from ui.TkinterUI import TkinterIndicator, TkinterPlayer, TkinterView

view = TkinterView()
Game(
	StandardLogic(),
	TkinterIndicator(view),
	TkinterPlayer(view),
).process()
