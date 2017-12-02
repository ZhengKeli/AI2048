import tensorflow as tf

from nerve.FullConnectedNetwork import FullConnectedNetwork
from nerve.NerveCore import NerveCore


class EvaluateCore(NerveCore):
    def __init__(self, path=None, name=None):
        super().__init__(path, name)
        with self.graph.as_default() as graph:
            self.board = graph.get_tensor_by_name("board:0")
            self.score = graph.get_tensor_by_name("score:0")
            self.real_score = graph.get_tensor_by_name("real_score:0")

            self.loss = graph.get_tensor_by_name("loss:0")
            self.ave_loss = graph.get_tensor_by_name("ave_loss:0")
            self.learning_rate = graph.get_tensor_by_name("learning_rate:0")
            self.train = graph.get_operation_by_name("train")

    def create_graph(self):
        with self.graph.as_default():
            # neural network
            board = tf.placeholder(tf.float32, shape=[None, 4, 4], name="board")  # [-1,4,4]

            rows = tf.unstack(board, axis=-1)  # 4*[-1,4]
            cols = tf.unstack(board, axis=-2)  # 4*[-1,4]
            lines = [line for group in [rows, cols] for line in group]  # 8*[-1,4]

            line_analyser = FullConnectedNetwork([4, 16, 16, 16], tf.nn.relu)
            analysed = [line_analyser.apply(line) for line in lines]  # 8*[-1,16]
            analysed = tf.stack(analysed, -2)  # [-1,8,16]
            analysed = tf.reshape(analysed, [-1, 8 * 16])  # [-1,8*16]

            final_analyser = FullConnectedNetwork([8 * 16, 64, 32], tf.nn.relu)
            final = final_analyser.apply(analysed)  # [-1,32]

            score = tf.reduce_mean(final, -1, name="score")  # [-1,32]

            # train
            real_score = tf.placeholder(tf.float32, name="real_score")  # [-1]
            loss = tf.square(score - real_score, name="loss")  # [-1]
            ave_loss = tf.reduce_mean(loss, name="ave_loss")

            learning_rate = tf.Variable(0.005, False, name="learning_rate")
            train = tf.train.AdamOptimizer(learning_rate).minimize(ave_loss, name="train")

            self.sess.run(tf.global_variables_initializer())

    def run_evaluate(self, val_board):
        return self.sess.run(
            fetches=self.score,
            feed_dict={self.board: val_board}
        )

    def run_train(self, val_board, val_real_score, val_learning_rate=None):
        feed_dict = {self.board: val_board, self.real_score: val_real_score, }
        if val_learning_rate is not None:
            feed_dict[self.learning_rate] = val_learning_rate
        return self.sess.run(
            fetches=[self.train, self.loss, self.score],
            feed_dict=feed_dict
        )
