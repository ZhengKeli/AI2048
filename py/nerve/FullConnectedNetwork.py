import tensorflow as tf


class FullConnectedNetwork:
    def __init__(self, shape, activation, keep=None):
        self.shape = shape
        self.keep = keep
        self.activation = activation
        self.weights = [
            tf.Variable(tf.random_normal(shape=[shape[i], shape[i + 1]], ))
            for i in range(len(shape) - 1)
        ]
        self.bias = [
            tf.Variable(tf.random_normal(
                shape=[shape[i + 1]],
            ))
            for i in range(len(shape) - 1)
        ]

    def apply(self, inputs):
        last_output = inputs
        for i in range(len(self.shape) - 1):
            layer_input = last_output
            layout_output = self.activation(tf.matmul(layer_input, self.weights[i]) + self.bias[i])

            if self.keep is None:
                layer_output = layout_output
            else:
                layer_output = tf.nn.dropout(layout_output, self.keep)

            last_output = layer_output
        return last_output
