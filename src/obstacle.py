from src.constant import OBSTACLE_FILE
from csv import reader

class Obstacle:

    def __init__(self) -> None:
        """
        Inicializa la clase Obstacle
        """
        self.__coordinates = None
        self.__colour = "#CEB200"
        self.__obstacles = self.__read_obstacle_file()

    def get_coordinates(self) -> list:
        """
        Devuelve: las coordenadas del obstáculo (list)
        """
        return self.__coordinates
    
    def get_colour(self) -> str:
        """
        Devuelve: el color del obstáculo (str)
        """
        return self.__colour

    def set_obstacle(self, level: int) -> None:
        """
        Recibe: el nivel (int)

        Establece las coordenadas del obstáculo que corresponde
        """
        obstacle_index = (level - 1) % len(self.__obstacles)
        self.__coordinates = self.__obstacles[obstacle_index]

    def __read_obstacle_file(self) -> dict:
        """
        Lee el archivo con las coordenadas de los obstáculos

        Devuelve: un diccionario (dict) con las coordenadas de todos los obstáculos
        """
        obstacles = {}
        with open(OBSTACLE_FILE) as file:
            csv_reader = reader(file, delimiter=" ")
            for i, coordinate_group in enumerate(csv_reader):
                for coordinates in coordinate_group[:-2]:
                    obstacles[i] = list(map(eval, coordinates.split(";")))

        return obstacles