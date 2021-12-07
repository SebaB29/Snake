from src.constant import BOARD_ROWS, BOARD_COLUMNS, KEYS

class Game:

    def __init__(self) -> None:
        """
        Inicializa la clase Game
        """
        self.__last_move = "RIGHT"

    def get_board_dimensions(self) -> tuple:
        """
        Devuelve: las dimensiones del tablero (tuple)
        """
        return (BOARD_ROWS, BOARD_COLUMNS)

    def get_last_move(self) -> str:
        """
        Devuelve: la última jugada realizada (str)
        """
        return self.__last_move

    def set_move(self, key: str) -> None:
        """
        Recibe: una tecla (str)

        Establece el movimiento si la tecla esta en KEYS
        """
        if key in KEYS:
            self.__last_move = key

    def __you_lost(self, snake_head: tuple, you_crashed: bool) -> bool:
        """
        Recibe: las coordenadas de la cabeza del snake (tuple) y una variable que determina si el snake choco (bool)

        Devuelve: 
            True: si perdio, es decir, si el snake choco o esta fuera de rango

            False: en caso contrario
        """
        return not (0 <= snake_head[0] < BOARD_ROWS and 0 <= snake_head[1] < BOARD_COLUMNS) or you_crashed

    def _you_won(self, quantity_fruits: int) -> bool:
        """
        Recibe: la cantidad de frutas que hay que comer para ganar (int)
        
        Devuelve:
                True: si ganó, es decir, si la cantidad de frutas es cero
                
                False: en caso contrario
        """
        return not quantity_fruits

    def _finish_game(self, snake: object, quantity_fruits: int, obstacle_coordinates: list) -> bool:
        """
        Recibe: el snake (object), la cantidad de frutas que hay que comer para ganar (int) 
                y las coordenadas del obstaculo (tuple(tuple))
        
        Ejecuta los métodos _you_won y you_lost
        
        Devuelve:
                True: en caso de que se haya ganado o perdido
                
                False: en caso contrario
        """
        return self._you_won(quantity_fruits) or self.__you_lost(snake.get_head(), snake._you_crashed(obstacle_coordinates))