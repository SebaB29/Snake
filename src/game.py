from src.constant import BOARD_ROWS, BOARD_COLUMNS, KEYS
from src.snake import Snake


class Game:

    def __init__(self) -> None:
        """
        Inicializa la clase Game con el movimiento inicial de la serpiente.

        El movimiento predeterminado es 'RIGHT'. Esta clase gestiona las acciones relacionadas
        con el tablero de juego, los movimientos de la serpiente y las condiciones de victoria o derrota.
        """
        self._last_move = "RIGHT"

    def get_board_dimensions(self) -> tuple[int]:
        """
        Devuelve las dimensiones del tablero de juego como una tupla.

        El tablero se define por la cantidad de filas y columnas especificadas
        en las constantes BOARD_ROWS y BOARD_COLUMNS.

        Returns:
            tuple: Una tupla con dos enteros, el número de filas y columnas del tablero.
        """
        return (BOARD_ROWS, BOARD_COLUMNS)

    def get_last_move(self) -> str:
        """
        Obtiene la última dirección de movimiento realizada por la serpiente.

        Returns:
            str: La última dirección de movimiento de la serpiente, que puede ser 'UP', 'DOWN', 'LEFT' o 'RIGHT'.
        """
        return self._last_move

    def set_move(self, key: str) -> None:
        """
        Establece la nueva dirección de movimiento de la serpiente.

        Si la tecla proporcionada está dentro de las teclas permitidas en KEYS,
        el movimiento de la serpiente se actualizará.

        Args:
            key (str): La tecla presionada por el jugador, que debe estar en el conjunto de teclas válidas (KEYS).

        Returns:
            None
        """
        if key in KEYS:
            self._last_move = key

    def _you_lost(self, snake_head: tuple[int], you_crashed: bool) -> bool:
        """
        Verifica si el jugador ha perdido el juego, ya sea por chocar contra los límites del tablero o contra un obstáculo.

        Args:
            snake_head (tuple): Las coordenadas de la cabeza de la serpiente, representadas como una tupla (x, y).
            you_crashed (bool): Un valor booleano que indica si la serpiente ha chocado contra un obstáculo.

        Returns:
            bool:
                - True si el jugador ha perdido (ya sea porque la cabeza de la serpiente está fuera de los límites
                  del tablero o porque la serpiente chocó contra un obstáculo).
                - False si el jugador no ha perdido.
        """
        return (
            not (0 <= snake_head[0] < BOARD_ROWS and 0 <= snake_head[1] < BOARD_COLUMNS)
            or you_crashed
        )

    def _you_won(self, quantity_fruits: int) -> bool:
        """
        Verifica si el jugador ha ganado el juego, es decir, ha comido todas las frutas necesarias.

        Args:
            quantity_fruits (int): La cantidad de frutas que el jugador necesita comer para ganar el juego.

        Returns:
            bool:
                - True si el jugador ha ganado (es decir, si la cantidad de frutas es 0).
                - False si el jugador no ha ganado aún.
        """
        return not quantity_fruits

    def finish_game(
        self,
        snake: Snake,
        quantity_fruits: int,
        obstacle_coordinates: list[tuple[int, int]],
    ) -> bool:
        """
        Evalúa si el juego ha terminado, ya sea por victoria o derrota.

        Este método invoca las funciones _you_won y _you_lost para determinar el estado final del juego.

        Args:
            snake (object): El objeto de la serpiente, que contiene las coordenadas de la cabeza y la lógica de colisión.
            quantity_fruits (int): La cantidad de frutas que faltan por comer para ganar el juego.
            obstacle_coordinates (list): Una lista de tuplas que representan las coordenadas de los obstáculos en el tablero.

        Returns:
            bool:
                - True si el jugador ha ganado o perdido (si se cumplen las condiciones de victoria o derrota).
                - False si el juego continúa.
        """
        return self._you_won(quantity_fruits) or self._you_lost(
            snake.head, snake.you_crashed(obstacle_coordinates)
        )
