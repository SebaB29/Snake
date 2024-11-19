from src.program import Program
from graphics.gamelib import init

def main(level=1):
    """
    Inicia el ciclo del juego para un nivel específico, maneja la transición entre niveles y reinicios del juego.
    """
    while True:
        game = Program(level)
        game.start_game()
        
        if game.won():
            level += 1
        else:
            game.end_game()
            level = 1
            if not game.restart_game():
                break

    print("Juego finalizado.")

if __name__ == "__main__":
    init(main)
