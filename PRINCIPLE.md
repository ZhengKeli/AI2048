# Working principle #
Here I will introduce the working principle of the AIs.


# The main idea #

## EvaluateCore ##
The EvaluateCore is called "core" in short in this project. What exactly it is? In fact it can be regarded as an evaluator of the situation. The core evaluates the situations,telling you it is bad or good, how bad or how good it is.

Typically, in my project, when you input the board of the game, the core will return a score, telling you, in its opinion, how many rounds can someone still plays.

But how to calculate such a score? In this project, I the calculation is done by a neural network. The structure of neural network and the training tricks are explained later.

relevant code: [`./py/ai/EvaluateCore.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/ai/EvaluateCore.py).


## AI1 ##
The first AI directly uses the core. It predicts the available next actions, and compare the results of the actions using the score from the core. And it just chooses the best action. 

Notice that it only predicts the next one action, so this AI is kind of weak. However, it's a stair of the better AI.

relevant code: [`./py/game/GameAI1.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/game/GameAI1.py).


## Prediction tree ##
Like chess games, we can use prediction tree to make the AI
more powerful. The prediction tree will predict the next action, the pop up after it, and even the father action after that and so on. This way the AI can predict and consider various situations.

relevant code: [`./py/ai/Tree.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/ai/Tree.py).


## AI2 ##
The second AI combines the prediction tree and evaluate core, it first "grows" the prediction tree. Once the tree has grown to a needed scale, it computes the score of the "leaves" and then makes a summary branch by branch. Finally it gets the summarized scores of each available next action and then just chooses the best action.

This AI can be powerful if the tree is big enough. 

relevant code: [`./py/game/GameAI2.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/game/GameAI2.py).



# About the core #

## Structure ##
The structure of the neural network is important in deep learning. In such a case, simply making a fully connected neural network is not very appropriate.

The main idea in designing the structure is that every row and column changes in parallel during every single action. So we can catch the signature in a single row or column as a depending factor in evaluation.

So I first cut the board into 8 lines (4 rows and 4 columns), and throw them into a fully connected network. Here I believe the processes in analyzing the lines are the same. So here I use shared weights and bias for each line.

After the analyze of the lines, the results of 8 analyzes are thrown together into a bigger fully connected network. And this network outputs the result of the evaluation as a score.

(Sorry, here should be a picture, but I don't have time to draw one)


## Trainings ##
Now the neural network has been created. But how to train it? Just think about it, the count of remaining rounds before death in fact badly depends on the player's level. Such score, in fact, can not be precisely predicted. So how can we offer a "right score" for training? The way is to train the core with **records of an AI player**.

In this project, I've trained 3 neural networks in different ways. And because of that, their power is very different from each other.

### core1 ###
This core is trained with the game records of the "random AI". That is, let the "random AI" play once. Record the board before every action. Then tag the boards with the real count of the remaining rounds before death. Finally train the neural network with these tagged boards.

Notices that because the AI is not smart at all. So the training records are not very ideal. As a result, the core1 is not very powerful.

relevant code: [`./py/train_core1.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/train_core1.py).

### core2 ###
This core is trained by the AI1. But don't forget that, in order to work, AI1 needs a core! So which core dose AI1 use? core1? Nope, It uses directly core2. So core2 is trained by AI1 with core2 itself.

That means the core2 is someway trained by **itself**! In this way, when the core is better, the trainings records become better, and then in return the core is trained to be better than better. Such training works well!

relevant code: [`./py/train_core2.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/train_core2.py).

### core3 ###
AI2 with its predict tree, should works better than AI1. So the training records offered by AI2 should be better. But with the tree AI2 works too slowly to offer enough records for the training. (Unless you have enough time 🙃 ) So I do not directly apply the self-training on AI2.

I do it such way: 
* Firstly I train the core in the same way as core2. This should need about 3,000 records. I call this "pre-training". (Instead of training a new core, you can also directly start from a trained core2)
* After that, I train the core with AI2. Starting from herer, it only need about 200 records. After only hundreds of trains the core can be powerful enough. That saves a lot of time, although the process is still very very s-l--w---o.

relevant code: [`./py/train_core3.py`](https://github.com/ZhengKeli/AI2048/blob/master/py/train_core3.py).
