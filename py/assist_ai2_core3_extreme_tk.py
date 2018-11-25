from ai.TreeStepAI import TreeStepAI
from game.Game import Game
from logic.StandardLogic import StandardLogic
from nerve.EvaluateCore import EvaluateCore
from ui.TkinterUI import TkinterIndicator, TkinterView, TkinterPlayer

core = EvaluateCore("../graph/core3", "core")
view = TkinterView()
Game(
	StandardLogic(),
	TkinterIndicator(view),
	TkinterPlayer(view),
	TreeStepAI(core, 1e4)
).process()
