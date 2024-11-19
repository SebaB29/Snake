from src.constant import OBSTACLE_FILE
from csv import reader

class Obstacle:

    def __init__(self) -> None:
        """
        Inicializa la clase Obstacle, establece las coordenadas de los obstáculos y su color.
        """
        self._coordinates = []
        self._colour = "#CEB200"
        self._obstacles = self._read_obstacle_file()

    @property
    def coordinates(self) -> list:
        """
        Devuelve las coordenadas del obstáculo.
        """
        return self._coordinates

    @property
    def colour(self) -> str:
        """
        Devuelve el color del obstáculo.
        """
        return self._colour

    def set_obstacle(self, level: int) -> None:
        """
        Establece las coordenadas del obstáculo basado en el nivel proporcionado.

        Recibe: 
        - `level`: El nivel para el cual se asignan las coordenadas del obstáculo.
        """
        if not self._obstacles:
            print("Error: No hay obstáculos disponibles. Verifica el archivo de obstáculos.")
            return

        obstacle_index = (level - 1) % len(self._obstacles)
        self._coordinates = self._obstacles[obstacle_index]

    def _read_obstacle_file(self) -> dict:
        """
        Lee el archivo con las coordenadas de los obstáculos. Cada línea del archivo representa un grupo de obstáculos.

        Devuelve: 
        - Un diccionario con las coordenadas de todos los obstáculos (dict).
        """
        obstacles = {}
        try:
            with open(OBSTACLE_FILE) as file:
                csv_reader = reader(file, delimiter=" ")
                for i, coordinate_group in enumerate(csv_reader):
                    obstacles[i] = [
                        tuple(map(int, coords.split(','))) for coords in coordinate_group[0].split(';')
                    ]
        except FileNotFoundError:
            print(f"Error: El archivo {OBSTACLE_FILE} no fue encontrado.")
        except Exception as e:
            print(f"Error al leer el archivo de obstáculos: {e}")
        return obstacles
