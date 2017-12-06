
# AI 2048 #

[2048](https://gabrielecirulli.github.io/2048/) should be a well-known game. If you've never played it, I suggest you to play several times and learn about its rules.

This is a project making an AI to play the 2048 game. To be honest, this is my first try in making AI for a game. (And it is the first practical project about deep learning that succeeds) 

In fact, it is not hard at all to make the AI for this game. (Maybe that's why I can succeed 🙂 ) So I think this project may be suitable for beginners and that's why I share this project here.


# Project structure #
All the runnable python scripts in directory `./py`. And the other scripts are placed in the subdirectory of `./py`. Such as:
* `./py/game` the game logic and game process
* `./py/nerve` the tools for neural network
* `./py/ai` the tools for game AI

The directory `./graph` stores well-trained neural network graphs of the cores.

The directory `./.idea` and file `./AI2048.iml` are "project files" of IDE **Intellij IDEA**. If you are using this IDE, you can import this project.


# Running #
Here I will tell you how to run the scripts in this project and that way you can have a first look of what the AIs can do.

## Environment ##
To run the scripts, firstly you need to build the environment. This project mainly needs **Python3** with **TensorFlow** (including **Numpy**). The exact versions I used are placed here for reference:
* Python 3.5.2
* TensorFlow 1.4.0
* Numpy 1.13.3

Here I will not explain how to install **Python3** or **TensorFlow**. If you need such guides, please refer to some other sites.

## Runnable scripts ##
All the runnable scripts are placed in directory `./py`.  All these scripts are supposed to run under directory `./py` (i.e. working directory is `./py`). 

Here are the introduction of these runnable scripts:
* `./py/game_console.py` - launch a console-based 2048 game
* `./py/game_random.py` - the game played by the "random AI". It takes actions completely randomly. (Well, maybe it is not really "intelligence")
* `./py/game_aix-corex.py` - the game played by a an AI
* `./py/game_ai2-core3_extreme.py` - this is the best AI in this project. It can play until appears "2048" almost every time. But it also takes a lot of time to "think".
* `./py/game_assist2_core3_extreme.py` - scripts that can let the best AI assist you in playing 2048.
* `./py/train_corex.py` - a set of scripts, which can train the neural network "core".
* `./py/match.py` - a script that tests all the AIs and compares how powerful they are. 

## Expected result of `match.py` ##
Here I place the expected average max rounds of the AIs in tests. This may help you to judge if the AIs are working normally.
* `random` - about 100 rounds
* `ai1_core1` - about 170 rounds
* `ai1_core2` - about 300 rounds
* `ai2_core2` - about 700 rounds
* `ai2_core3` - about 1000 rounds


# Working principle #
Things about the working principles are written in an other .md file: [`PRINCIPLE.md`](https://github.com/ZhengKeli/AI2048/blob/master/PRINCIPLE.md). You can refer to it, if you want to learn about the working principle of the AIs.

