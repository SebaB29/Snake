from src.constant import AMOUNT_FRUITS_TO_WIN
from random import randint


class Fruit:
    def __init__(self) -> None:
        """
        Inicializa una instancia de la clase Fruit.

        La fruta tiene una lista vacía de coordenadas, un color predeterminado (#F00)
        y una cantidad de frutas necesarias para ganar, definida por la constante AMOUNT_FRUITS_TO_WIN.
        """
        self._coordinates = []
        self._colour = "#F00"
        self._quantity_fruits = AMOUNT_FRUITS_TO_WIN

    @property
    def coordinates(self) -> list[tuple[int, int]]:
        """
        Obtiene las coordenadas de la fruta en el tablero.

        :return: Lista de coordenadas de la fruta en formato (x, y).
        """
        return self._coordinates

    @property
    def colour(self) -> str:
        """
        Obtiene el color de la fruta.

        :return: Color de la fruta en formato hexadecimal, por defecto "#F00" (rojo).
        """
        return self._colour

    @property
    def quantity_fruits(self) -> int:
        """
        Obtiene la cantidad de frutas restantes para ganar el juego.

        :return: Número de frutas necesarias para ganar el juego.
        """
        return self._quantity_fruits

    def set_fruit(
        self,
        board_dimensions: tuple[int],
        snake_coordinates: list[tuple[int, int]],
        obstacle_coordinates: list[tuple[int, int]],
    ) -> None:
        """
        Establece las nuevas coordenadas de la fruta, asegurándose de que no se superponga
        con la serpiente o con los obstáculos en el tablero.

        :param board_dimensions: Dimensiones del tablero, representadas como una tupla (alto, ancho).
        :param snake_coordinates: Coordenadas de la serpiente, representadas como una lista de tuplas (x, y).
        :param obstacle_coordinates: Coordenadas de los obstáculos, representadas como una lista de tuplas (x, y).

        :return: None. La fruta es colocada en una posición válida.
        """
        self._coordinates = [
            self._generate_fruit(
                board_dimensions, snake_coordinates, obstacle_coordinates
            )
        ]

    def set_quantity_fruits(self) -> None:
        """
        Disminuye en uno la cantidad de frutas necesarias para ganar el juego.

        Este método es utilizado cuando la serpiente come una fruta.
        La cantidad de frutas necesarias para ganar se reduce.
        """
        self._quantity_fruits -= 1

    def _generate_fruit(
        self,
        board_dimensions: tuple[int],
        snake_coordinates: list[tuple[int, int]],
        obstacle_coordinates: list[tuple[int, int]],
    ) -> tuple[int]:
        """
        Genera y devuelve nuevas coordenadas para la fruta dentro de los límites del tablero,
        asegurándose de que no se coloque sobre la serpiente ni sobre los obstáculos.

        :param board_dimensions: Dimensiones del tablero, representadas como una tupla (alto, ancho).
        :param snake_coordinates: Coordenadas de la serpiente, representadas como una lista de tuplas (x, y).
        :param obstacle_coordinates: Coordenadas de los obstáculos, representadas como una lista de tuplas (x, y).

        :return: Una tupla con las nuevas coordenadas de la fruta (x, y).
        """
        new_coordinates = None
        while (
            new_coordinates is None
            or new_coordinates in snake_coordinates
            or new_coordinates in obstacle_coordinates
        ):
            new_coordinates = (
                randint(0, board_dimensions[1] - 1),
                randint(0, board_dimensions[0] - 1),
            )

        return new_coordinates
