from graphics.gamelib import resize, title, loop, wait, get_events, EventType
from src.constant import WINDOW_HEIGHT, WINDOW_WIDTH, BUTTON_SIDES, PAUSE, OBSTACLE_FILE
from src.game import Game
from src.snake import Snake
from src.fruit import Fruit
from src.obstacle import Obstacle
from src.obstacle_loader import ObstacleLoader
from graphics.game_render import GameRenderer

class Program:

    def __init__(self, level):
        self.level = level
        self.game = Game()
        self.snake = Snake()
        self.fruit = Fruit()
        self.obstacle_loader = ObstacleLoader(OBSTACLE_FILE)
        self.obstacle = Obstacle(self.obstacle_loader)
        self.renderer = GameRenderer(level, self.snake, self.fruit, self.obstacle)  # Nueva instancia de GameRenderer

    def start_game(self):
        title("SNAKE")
        resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self._initialize_game()
        self._game_loop()

    def _initialize_game(self):
        """
        Inicializa el estado del juego antes de comenzar el bucle principal.
        Establece los obstáculos, la fruta y cualquier otra configuración inicial.
        """
        self.obstacle.set_obstacle(self.level)
        self.fruit.set_fruit(self.game.get_board_dimensions(), self.snake.coordinates, self.obstacle.coordinates)

    def _game_loop(self):
        """
        Ejecuta el bucle principal del juego. Se repite hasta que el juego termine.
        """
        while loop(fps=8) and not self.game._finish_game(self.snake, self.fruit.quantity_fruits, self.obstacle.coordinates):
            self._handle_events()
            self._move_snake()
            self._check_fruit_collision()
            self.renderer.show_game()  # Usamos el renderizado aquí

    def _handle_events(self):
        """
        Maneja los eventos de entrada, como presionar teclas o interactuar con la interfaz.
        """
        for event in get_events():
            if event.type == EventType.KeyPress:
                event.key = event.key.upper()
                self.game.set_move(event.key)

                if event.key == PAUSE:
                    wait(EventType.KeyPress)

    def _move_snake(self):
        """
        Mueve la serpiente en función del movimiento actual.
        """
        self.snake.move(self.game.get_last_move())

    def _check_fruit_collision(self):
        """
        Verifica si la serpiente ha comido una fruta y la actualiza.
        """
        if self.snake.head in self.fruit.coordinates:
            self.snake.eat_fruit()
            self.fruit.set_quantity_fruits()
            self.fruit.set_fruit(self.game.get_board_dimensions(), self.snake.coordinates, self.obstacle.coordinates)

    def won(self):
        return self.game._you_won(self.fruit.quantity_fruits)

    def restart_game(self):
        event = wait(EventType.ButtonPress)
        return event and BUTTON_SIDES["left"] <= event.x <= BUTTON_SIDES["right"] and BUTTON_SIDES["up"] <= event.y <= BUTTON_SIDES["down"]

    def end_game(self):
        self.renderer.show_end()  # Usamos el renderizado para mostrar el fin del juego