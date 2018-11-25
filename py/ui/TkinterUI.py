import threading
import tkinter as tk
from concurrent.futures import Future
from time import sleep
from typing import Optional

from game.GameComponent import GameListener, GamePlayer
from logic.Action import Action
from logic.Board import Board
from logic.Pop import Pop

GRID_SIZE = 4

GLOBAL_BACKGROUND = "#92877d"

HEADER_HEIGHT = 70
HEADER_PADDING = 10
HEADER_COLOR = "#222222"
HEADER_FONT = ("Verdana", 20, "bold")

BOARD_SIZE = 400
CELL_PADDING = 10

CELL_BACKGROUND_EMPTY = "#9e948a"
CELL_BACKGROUND_NUM = {
	2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
	32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
	512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
}
CELL_FOREGROUND_NUM = {
	2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
	32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
	512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"
}
CELL_FONT = ("Verdana", 40, "bold")


class TkinterView:
	
	def __init__(self):
		self.rounds = None
		self.suggestion = None
		self.dead = False
		
		self.board = None
		self.action_request = None
		
		self.window = None
		self.root = None
		self.header_label = None
		self.cells_labels = None
		
		self.start_tk_thread()
	
	def start_tk_thread(self):
		thread_future = Future()
		threading.Thread(target=lambda: self.init_tk_and_loop(thread_future)).start()
		thread_future.result()
		print("started")
	
	def init_tk_and_loop(self, future):
		window = tk.Tk()
		window.title('2048')
		window.bind("<Key>", self.bind_key)
		window.bind("<<UpdateHeader>>", self.bind_update_header)
		window.bind("<<UpdateBoard>>", self.bind_update_board)
		
		root = tk.Frame(window, bg=GLOBAL_BACKGROUND, width=BOARD_SIZE, height=BOARD_SIZE + HEADER_HEIGHT)
		root.grid()
		
		header = tk.Frame(root, bg=GLOBAL_BACKGROUND, width=BOARD_SIZE, height=HEADER_HEIGHT)
		header.grid(row=0, column=0, columnspan=GRID_SIZE, padx=HEADER_PADDING, pady=HEADER_PADDING)
		header_label = tk.Label(header, text="abc", bg=GLOBAL_BACKGROUND, fg=HEADER_COLOR, justify=tk.LEFT, font=HEADER_FONT)
		header_label.grid()
		
		cell_labels = []
		for i in range(GRID_SIZE):
			row = []
			for j in range(GRID_SIZE):
				cell = tk.Frame(root, bg=CELL_BACKGROUND_EMPTY, width=BOARD_SIZE / GRID_SIZE, height=BOARD_SIZE / GRID_SIZE)
				cell.grid(row=i + 1, column=j, padx=CELL_PADDING, pady=CELL_PADDING)
				cell_label = tk.Label(cell, text="", bg=CELL_BACKGROUND_EMPTY, justify=tk.CENTER, font=CELL_FONT, width=4, height=2)
				cell_label.grid()
				row.append(cell_label)
			cell_labels.append(row)
		
		self.window = window
		self.root = root
		self.header_label = header_label
		self.cells_labels = cell_labels
		
		future.set_result(True)
		print("inited")
		self.window.mainloop()
	
	def bind_update_header(self, event):
		header_text = "Rounds=" + str(self.rounds)
		if self.dead:
			header_text += " Game Over!"
		elif self.suggestion is not None:
			header_text += " Suggestion " + str(self.suggestion.value)
		self.header_label.configure(text=header_text)
		self.header_label.update_idletasks()
	
	def bind_update_board(self, event):
		for i in range(GRID_SIZE):
			for j in range(GRID_SIZE):
				num = self.board[i][j]
				cell = self.cells_labels[i][j]
				if num == 0:
					cell.configure(text="", bg=CELL_BACKGROUND_EMPTY)
				else:
					num = pow(2, num)
					cell.configure(text=str(num), bg=CELL_BACKGROUND_NUM[num], fg=CELL_FOREGROUND_NUM[num])
		self.window.update_idletasks()
	
	def show_board(self, board):
		self.board = board
		self.window.event_generate("<<UpdateBoard>>")
	
	def show_rounds(self, rounds):
		self.rounds = rounds
		self.window.event_generate("<<UpdateHeader>>")
	
	def show_suggestion(self, suggestion: Optional[Action]):
		self.suggestion = suggestion
		self.window.event_generate("<<UpdateHeader>>")
	
	def show_dead(self, rounds):
		self.rounds = rounds
		self.dead = True
		self.window.event_generate("<<UpdateHeader>>")
	
	def bind_key(self, event):
		key = event.char
		action = {
			"w": Action.UP,
			"s": Action.DOWN,
			"a": Action.LEFT,
			"d": Action.RIGHT
		}.get(key)
		if action is None:
			return
		if self.action_request is None:
			return
		self.action_request.set_result(action)
	
	def read_action(self) -> Action:
		action_request = Future()
		self.action_request = action_request
		action = action_request.result()
		self.action_request = None
		return action


class TkinterIndicator(GameListener):
	
	def __init__(self, view: TkinterView, interval=0.5) -> None:
		self.view = view
		self.interval = interval
	
	def on_inited(self, board: Board):
		self.view.show_board(board.matrix)
	
	def on_new_round(self, rounds: int):
		self.view.show_suggestion(None)
		self.view.show_rounds(rounds)
	
	def on_applied_action(self, action: Action, board: Board):
		self.view.show_board(board.matrix)
		sleep(self.interval)
	
	def on_applied_reaction(self, pop: Pop, board: Board):
		self.view.show_board(board.matrix)
		sleep(self.interval)
	
	def on_dead(self, rounds: int, board: Board):
		self.view.show_dead(rounds)


class TkinterPlayer(GamePlayer):
	
	def __init__(self, view: TkinterView) -> None:
		self.view = view
	
	def on_ai_suggested(self, suggestion: Action):
		self.view.show_suggestion(suggestion)
	
	def on_get_action(self, board: Board) -> Action:
		return self.view.read_action()
