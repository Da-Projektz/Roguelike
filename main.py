# Prohibit Pygame from polluting `/dev/stdout`.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from game import RogueLike



# Protect other scripts from running main functions.
if __name__ == "__main__":
    rl = RogueLike(False)
    rl.run_game()
