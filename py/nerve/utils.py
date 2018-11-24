import numpy as np

from nerve.GameRecorder import GameRecorder


def train_core(core, game, train_count, group_size=None, learning_rate=0.005):
	if group_size is None:
		group_size = train_count
	
	train_id = 0
	group_id = 0
	while train_id < train_count:
		item_id = 0
		sum_distance = 0
		sum_round = 0
		while train_id < train_count and item_id < group_size:
			recorder = GameRecorder()
			game.add_components(recorder)
			game.process()
			
			val_board = recorder.history
			val_real_score = np.arange(0, len(val_board), 1.0)[::-1]
			val_train, val_loss, val_score = core.run_train(val_board, val_real_score, learning_rate)
			
			sum_distance += np.average(np.sqrt(val_loss))
			sum_round += len(val_board)
			train_id += 1
			item_id += 1
		
		print(
			"train[", train_id - group_size, ":", train_id, "]", "\t",
			"ave_distance=", sum_distance / group_size, "\t",
			"ave_max_round", sum_round / group_size)
		core.save_graph()
		group_id += 1
