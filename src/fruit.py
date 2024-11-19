from src.constant import AMOUNT_FRUITS_TO_WIN
from random import randint
class Fruit:
    def __init__(self) -> None:
        """
        Inicializa la clase Fruit con una lista de coordenadas vacía y la cantidad de frutas necesarias para ganar.
        """
        self._coordinates = []
        self._colour = "#F00"
        self._quantity_fruits = AMOUNT_FRUITS_TO_WIN

    @property
    def coordinates(self) -> list:
        """
        Devuelve las coordenadas de la fruta.
        """
        return self._coordinates

    @property
    def colour(self) -> str:
        """
        Devuelve el color de la fruta.
        """
        return self._colour

    @property
    def quantity_fruits(self) -> int:
        """
        Devuelve la cantidad de frutas restantes para ganar.
        """
        return self._quantity_fruits

    def set_fruit(self, board_dimensions: tuple, snake_coordinates: list, obstacle_coordinates: list) -> None:
        """
        Recibe: las dimensiones del tablero (tuple), las coordenadas del snake (list[tuple]) y las coordenadas
        del obstáculo (tuple(tuple))

        Establece las nuevas coordenadas de la fruta, garantizando que no se superponga con el snake ni con el obstáculo.
        """
        self._coordinates = [self._generate_fruit(board_dimensions, snake_coordinates, obstacle_coordinates)]

    def set_quantity_fruits(self) -> None:
        """
        Disminuye en uno la cantidad de frutas necesarias para ganar.
        """
        self._quantity_fruits -= 1

    def _generate_fruit(self, board_dimensions: tuple, snake_coordinates: list, obstacle_coordinates: list) -> tuple:
        """
        Genera nuevas coordenadas para la fruta dentro del rango del tablero, evitando que aparezca sobre el snake
        o el obstáculo.

        Devuelve: las nuevas coordenadas de la fruta (tuple).
        """
        new_coordinates = None
        while new_coordinates is None or new_coordinates in snake_coordinates or new_coordinates in obstacle_coordinates:
            new_coordinates = (randint(0, board_dimensions[1] - 1), randint(0, board_dimensions[0] - 1))

        return new_coordinates
