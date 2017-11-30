
#AI 2048
[2048](https://gabrielecirulli.github.io/2048/) should be a well-known game. If you've never played it, I suggest you to play several times and learn about its game rules.

This is a project making an AI to play the game 2048. To be honest, this is my first try in making AI for a game. (And it is the first practical project about deep learning that succeeds) 

In fact, it is not hard at all to make the AI for this game. (Maybe that's why I can succeed 🙂 ) So I think this project may be suitable for beginners and that's why I share this project here.


# Project structure

The main enters of this project is the python scripts in directory `./py`. All these scripts are suggested to run under its directory (i.e. working directory is `./py`).
- `./py/game_console.py` - a console-based game 2048
- `./py/game_random.py` - the game played by a AI that actions randomly (well, maybe is not really "intelligence")
- `./py/game_aix-corex.py` - a set of AIs, they are built step by step. And they are stronger and stronger.
- `./py/game_ai2-core3_extreme.py` - this is almost the best AI in this project, but it takes a lot of time to computes.
- `./py/game_assist2_core3_extreme.py` - scripts that can let the best AI assist you when playing 2048.
- `./py/train_corex.py` - a set of scripts, which can train the nerve network "core" using in AIs.
- `./py/match.py` - a script that test all the AIs and compare how strong they are. 

The directory `./graph` is storing the well-trained nerve network graph of the cores. And of course you can move it to some other place and train you own core.

The directory `./.idea` and file `./AI2048.iml` are project files of **Intellij IDEA**. If you are using it, you can import this project.


# Expected result of the AIs
Here I place the expected average max rounds of the AIs in tests. This may help you to judge if your own AI works normally.
- `random` - about 100 rounds
- `ai1_core1` - about 170 rounds
- `ai1_core2` - about 300 rounds
- `ai2_core2` - about 700 rounds
- `ai2_core3` - about 1000 rounds
