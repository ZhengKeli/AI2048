# Working principle #
Here I will introduce the working  principle of the AI.


# The main idea #

## Evaluate core ##
The evaluate core is called "core" in short in this project. What exactly it is? In fact it can be regarded as an evaluator of the situation. The core evaluate that a situation is bad or good, and how bad or how good it is.

Typically, in my project, when you input the situation of the board of game, the core will return a score, telling you, in its opinion, starting from this board how many rounds can someone plays.

But how to calculate such answer? There are many ways to do it. But in this project, I implemented the core using a neural network. The structure of neural network and the training tricks are explained later.

The relevant code is in [`./py/ai/EvaluateCore.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/ai/EvaluateCore.py).


## AI1 ##
The first AI directly applies the function of evaluate core. It predicts the available next actions, and compare the results of the actions using the evaluation by the core. And it just choose the best action. 

Notice that it only predict the next one action, so this AI kind of weak. However, it's a stair of the better AI.

The relevant code is in [`./py/game/GameAI1.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/game/GameAI1.py).


## Prediction tree ##
Like chess games, we can use prediction tree to make the AI
more powerful. The prediction tree will predict the next action, the pop up after it, and even the father action after that and so on. This way we can construct a predict tree.

The relevant code is in [`./py/ai/Tree.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/ai/Tree.py).


## AI2 ##
The second AI combine the prediction tree and evaluate core, it first "grows" the prediction tree. Once the tree has grown to a need scale, it evaluates all the "leaves" of the tree and make a summary branch by branch. Finally it get the evaluations of each available next action and then just chooses the best action.

This AI can predict a lot, and generate a series of actions according the predict tree. It can be powerful if the tree is big enough. 

The relevant code is in [`./py/game/GameAI2.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/game/GameAI2.py).



# About the core #

## Structure ##
The structure of the neural network is important in deep learning. So we can't just simply make a full connected neural network to deal with such a complicated problem.

The main idea in designing the structure is that the every row and column changes in parallel in every single action. So we can catch the signature in a single row or column as a depending factor in evaluation.

So the neural network just first cut the board into 8 lines (4 rows and 4 columns), and then throw them into a full connected network. Here I believe the processes in analyzing the lines are the same. So here I use shared weights and bias.

After the analyze of the lines, the results of 8 analyzes are thrown together into a bigger full connected network. And this network outputs the score (result of the evaluation).

(Sorry, there should be a picture or something, but I don't have time to draw one)


## Trainings ##
Now the neural network has been created. But how to train it? Just think about it, the count of remaining rounds before death in fact badly depends on the player's level. Such score, in fact, can not be precise. So how can we offer a "real score" for a board in training? The way is to train the core with **records of an AI player**. And there're some tricks!

In this project, I've trained 3 neural networks in different ways. And because of it, their power is very different from each other.

### core1 ###
This core is trained by the game record of the "random AI". That is, let the "random AI" play once and record the board before every action. Then tag the boards with the count of the remaining rounds before death. Finally train the neural network with these boards and tags.

Notices that because the AI is not smart at all. So the trainings are not very ideal. As a result, the core 1 of cause not very powerful.

The relevant code is in [`./py/train_core1.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/train_core1.py).

### core2 ###
This core is trained by the AI1. But don't forget that, in other to let AI1 work, we need a core! So which core dose AI1 use? core1? Nope, I use directly core2. So core2 is trained by AI1 with core2 itself. 

That means the core2 is someway training by **itself**! In this way, when the core is better, the trainings from AI are better, and then in return the core becomes better than better. Such training works well!

The relevant code is in [`./py/train_core2.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/train_core2.py).

### core3 ###
AI2 with its predict tree, should works better than AI1. And the training records offered by AI2 should be better. But with the tree AI2 works too slowly to offer enough records for the training. (Unless you have enough time 🙃 ) So the self-training can not be applied directly on AI2.

So I do it such way: 

Firstly I train the core in the same way as core2. This should need about 3,000 records. I call this "pre-training". (Instead of train a new core, you can also directly start from a trained core2)

After that, I train the core with AI2 slowly. But it only need about 200 of records. After only hundreds of trains the core can be powerful enough. That saves a lot of time, although the process is really very very s-l--w---o.

The relevant code is in [`./py/train_core3.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/train_core3.py).
