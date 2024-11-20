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
    """
    Clase que gestiona el flujo completo del juego SNAKE.

    Esta clase es responsable de inicializar el juego, gestionar los eventos, mover la serpiente,
    verificar las colisiones y renderizar el estado del juego en cada ciclo. Además, maneja la lógica
    para verificar si el jugador ha ganado o desea reiniciar el juego.

    Atributos:
        level (int): Nivel del juego que determina la dificultad y el tipo de obstáculos.
        game (Game): Instancia del objeto `Game`, que maneja las reglas y el estado general del juego.
        snake (Snake): Instancia del objeto `Snake`, que representa a la serpiente del jugador.
        fruit (Fruit): Instancia del objeto `Fruit`, que gestiona la colocación y la cantidad de frutas.
        obstacle_loader (ObstacleLoader): Instancia que carga los obstáculos del nivel.
        obstacle (Obstacle): Instancia del objeto `Obstacle`, que representa los obstáculos del nivel.
        event_controller (EventController): Controlador que maneja los eventos del teclado y los botones.
        renderer (GameRenderer): Instancia del objeto `GameRenderer`, responsable de renderizar la interfaz gráfica.
    """

    def __init__(self, level: int) -> None:
        """
        Inicializa los componentes del juego, como la serpiente, la fruta, los obstáculos,
        y el controlador de eventos. Establece el nivel de dificultad y prepara el renderizado.

        :param level: Nivel de dificultad para el juego (ej. 1 para fácil, 2 para medio, 3 para difícil).
        """
        self.level = level
        self.game = Game()
        self.snake = Snake()
        self.fruit = Fruit()
        self.obstacle_loader = ObstacleLoader(OBSTACLE_FILE)
        self.obstacle = Obstacle(self.obstacle_loader)
        self.event_controller = EventController()
        self.renderer = GameRenderer(level, self.snake, self.fruit, self.obstacle)

    def start_game(self) -> None:
        """
        Inicia el juego mostrando el título, ajustando la ventana y luego ejecutando el bucle de juego.

        Este método es el punto de entrada principal, que configura el entorno del juego
        y comienza el ciclo de juego hasta que el jugador decida finalizar.
        """
        title("SNAKE")
        resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self._initialize_game()
        self._game_loop()

    def _initialize_game(self) -> None:
        """
        Inicializa el estado del juego antes de comenzar el bucle principal.

        Establece los obstáculos, la fruta y cualquier otra configuración inicial
        necesaria para el inicio del juego.
        """
        self.obstacle.set_obstacle(self.level)
        self.fruit.set_fruit(
            self.game.get_board_dimensions(),
            self.snake.coordinates,
            self.obstacle.coordinates,
        )

    def _game_loop(self) -> None:
        """
        Ejecuta el bucle principal del juego.

        Este método se ejecuta en un ciclo continuo hasta que se cumpla la condición de finalización
        del juego, verificando constantemente los eventos, el movimiento de la serpiente y las
        colisiones con la fruta. También maneja el renderizado del juego en cada iteración.
        """
        while loop(fps=8) and not self.game.finish_game(
            self.snake, self.fruit.quantity_fruits, self.obstacle.coordinates
        ):
            self._handle_events()
            self._move_snake()
            self._check_fruit_collision()
            self.renderer.show_game()  # Usamos el renderizado aquí

    def _handle_events(self) -> None:
        """
        Maneja los eventos de entrada, como la presión de teclas para el movimiento de la serpiente
        o la interacción con el botón de pausa.

        Recibe los eventos generados durante el ciclo del juego y los pasa al controlador de eventos
        para su procesamiento.
        """
        events = get_events()
        self.event_controller.handle_key_events(events, self.game)

    def _move_snake(self) -> None:
        """
        Mueve la serpiente en función del último movimiento registrado.

        Este método utiliza el movimiento almacenado por el juego para mover la serpiente en la
        dirección correcta según las teclas presionadas por el jugador.
        """
        self.snake.move(self.game.get_last_move())

    def _check_fruit_collision(self) -> None:
        """
        Verifica si la cabeza de la serpiente ha colisionado con una fruta.

        Si la serpiente come una fruta, se incrementa la cantidad de frutas y se genera
        una nueva fruta en una posición válida dentro del tablero.
        """
        if self.snake.head in self.fruit.coordinates:
            self.snake.eat_fruit()
            self.fruit.set_quantity_fruits()
            self.fruit.set_fruit(
                self.game.get_board_dimensions(),
                self.snake.coordinates,
                self.obstacle.coordinates,
            )

    def won(self) -> bool:
        """
        Verifica si el jugador ha ganado el juego.

        :return: True si el jugador ha alcanzado el objetivo de cantidad de frutas, False en caso contrario.
        """
        return self.game._you_won(self.fruit.quantity_fruits)

    def restart_game(self) -> bool:
        """
        Maneja la lógica de reinicio del juego utilizando el controlador de eventos.

        Escucha el evento del botón de reinicio y, si es presionado, reinicia el estado del juego.

        :return: True si el botón de reinicio fue presionado, False si no se presionó el botón.
        """
        event = wait(EventType.ButtonPress)
        return self.event_controller.is_restart_button_pressed(event)

    def end_game(self) -> None:
        """
        Muestra la pantalla de fin de juego.

        Este método es llamado cuando el juego ha terminado, ya sea por ganar o perder,
        y se muestra la interfaz de fin de juego.
        """
        self.renderer.show_end()
