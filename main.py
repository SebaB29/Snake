from src.program import Program
from graphics.gamelib import init

def main(level = 1):
    game = Program(level)
    game.start_game()
    if (game.won()):
        main(level = level + 1)
    game.end_game()
    if (game.restart_game()):
        main()

init(main)