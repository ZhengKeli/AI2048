import os
from abc import ABCMeta, abstractmethod

import tensorflow as tf


class NerveCore:
    __metaclass__ = ABCMeta

    def __init__(self, path: str = None, name: str = None):
        self.path = path
        self.name = name
        self.graph = tf.Graph()
        self.sess = tf.Session(graph=self.graph)

        tf.Graph()

        # try to load
        if not self.load_graph(path, name):
            self.create_graph()
            print("graph", name, "created")
            self.save_graph(path, name)

    def load_graph(self, path, name):
        if (path is None) or (name is None):
            return False
        try:
            with self.graph.as_default():
                tf.train.import_meta_graph(path + "/" + name + ".meta") \
                    .restore(self.sess, tf.train.latest_checkpoint(path))
            print("graph loaded:", name)
            return True
        except OSError as e:
            print(e)
            return False

    def save_graph(self, path: str = None, name: str = None):
        if (path is None) or (name is None):
            path = self.path
            name = self.name

        if (path is None) or (name is None):
            return False
        try:
            if not os.path.exists(path):
                os.makedirs(path,exist_ok=True)
            with self.graph.as_default():
                saver = tf.train.Saver()
                saver.save(self.sess, path + "/" + name)
            print("graph saved:", name)
            return True
        except OSError as e:
            print(e)
            return False

    @abstractmethod
    def create_graph(self):
        pass
