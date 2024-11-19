from src.obstacle_loader import ObstacleLoader

class Obstacle:
    def __init__(self, loader: ObstacleLoader) -> None:
        """
        Inicializa la clase Obstacle con un cargador de datos y establece las propiedades.

        :param loader: Objeto de tipo ObstacleLoader encargado de cargar los datos de obstáculos.
        """
        self._coordinates = []
        self._colour = "#CEB200"
        self._loader = loader
        self._obstacles = self._load_obstacles()

    @property
    def coordinates(self) -> list:
        return self._coordinates

    @property
    def colour(self) -> str:
        return self._colour

    def set_obstacle(self, level: int) -> None:
        """
        Establece las coordenadas del obstáculo basado en el nivel proporcionado.
        
        :param level: Nivel del juego.
        """
        if not self._obstacles:
            print("Error: No hay obstáculos disponibles.")
            return

        obstacle_index = (level - 1) % len(self._obstacles)
        self._coordinates = self._obstacles[obstacle_index]

    def _load_obstacles(self) -> dict:
        """
        Carga los obstáculos usando el loader proporcionado.

        :return: Diccionario con los datos de obstáculos.
        """
        return self._loader.load_obstacles()
