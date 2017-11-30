from game.Action import Action
from game.Game import Game


class GameConsole(Game):
    keyboard = {
        "w": Action.UP,
        "s": Action.DOWN,
        "a": Action.LEFT,
        "d": Action.RIGHT
    }

    def on_get_action(self) -> Action:
        while True:
            print("round", self.round)
            print(self.board)

            key = input("Input your action:")
            if key not in GameConsole.keyboard:
                print("Please type 'w' 'a' 's' or 'd' but not '", key, "'", sep="")
                continue

            action = GameConsole.keyboard[key]
            if action not in self.action_map:
                print("Your action is illegal!")
                continue

            return action

    def on_dead(self):
        print("round", self.round)
        print(self.board)
        print("You are dead!")
