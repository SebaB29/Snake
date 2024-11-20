from graphics.gamelib import resize, title, loop, wait, get_events, EventType
from src.constant import WINDOW_HEIGHT, WINDOW_WIDTH, OBSTACLE_FILE
from src.game import Game
from src.snake import Snake
from src.fruit import Fruit
from src.obstacle import Obstacle
from src.obstacle_loader import ObstacleLoader
from src.event_controller import EventController
from graphics.game_render import GameRenderer

class Program:

    def __init__(self, level):
        self.level = level
        self.game = Game()
        self.snake = Snake()
        self.fruit = Fruit()
        self.obstacle_loader = ObstacleLoader(OBSTACLE_FILE)
        self.obstacle = Obstacle(self.obstacle_loader)
        self.event_controller = EventController()
        self.renderer = GameRenderer(level, self.snake, self.fruit, self.obstacle)

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
        while loop(fps=8) and not self.game.finish_game(self.snake, self.fruit.quantity_fruits, self.obstacle.coordinates):
            self._handle_events()
            self._move_snake()
            self._check_fruit_collision()
            self.renderer.show_game()  # Usamos el renderizado aquí

    def _handle_events(self):
        """
        Maneja los eventos de entrada, como presionar teclas o interactuar con la interfaz.
        """
        events = get_events()
        self.event_controller.handle_key_events(events, self.game)

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
        """
        Maneja la lógica de reinicio del juego usando el controlador de eventos.
        """
        event = wait(EventType.ButtonPress)
        return self.event_controller.is_restart_button_pressed(event)

    def end_game(self):
        self.renderer.show_end()