from src.constant import AMOUNT_FRUITS_TO_WIN
from random import randint

class Fruit:

    def __init__(self) -> None:
        """
        Inicializa la clase Fruit
        """
        self.__coordinates = []
        self.__colour = "#F00"
        self.__quantity_fruits = AMOUNT_FRUITS_TO_WIN

    def get_coordinates(self) -> list:
        """
        Devuelve: las coordenadas de la fruta (list)
        """
        return self.__coordinates
    
    def get_colour(self) -> str:
        """
        Devuelve: el color del objeto (str)
        """
        return self.__colour

    def get_quantity_fruits(self) -> int:
        """
        Devuelve: la cantidad de frutas (int)
        """
        return self.__quantity_fruits

    def set_fruit(self, board_dimensions: tuple, snake_coordinates: list, obstacle_coordinates: list) -> None:
        """
        Recibe: las dimensiones del tablero (tuple), las coordenadas del snake (list[tuple]) y las coordenadas
        del obstáculo (tuple(tuple))

        Si la fruta ya tiene coordenadas las elimina, establece las nuevas coordenadas de la fruta
        """
        if self.__coordinates:
            self.__coordinates.pop()
        self.__coordinates.append(self.__generate_fruit(board_dimensions, snake_coordinates, obstacle_coordinates))

    def set_quantity_fruits(self) -> None:
        """
        Establece la nueva cantidad de frutas necesarias para ganar
        """
        self.__quantity_fruits -= 1

    def __generate_fruit(self, board_dimensions: tuple, snake_coordinates: list, obstacle_coordinates: list) -> tuple:
        """
        Recibe: las dimensiones del tablero (tuple), las coordenadas del snake (list[tuple]) y las coordenadas del
        obstáculo (tuple(tuple))

        Crea las nuevas coordenadas de la fruta, que estén dentro del rango del tablero y que no aparezca
        sobre el snake o el obstáculo

        Devuelve: las nuevas coordenadas de la fruta (tuple)
        """
        new_coordinates = None
        while not new_coordinates or new_coordinates in snake_coordinates or new_coordinates in obstacle_coordinates:
            new_coordinates = (randint(0, board_dimensions[1] - 1), randint(0, board_dimensions[0] - 1))

        return new_coordinates