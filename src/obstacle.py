from src.obstacle_loader import ObstacleLoader


class Obstacle:
    """
    Representa un obstáculo en el juego, con coordenadas y color configurables.

    La clase `Obstacle` gestiona los obstáculos que aparecen en el tablero de juego. Utiliza un cargador externo (`ObstacleLoader`) para cargar los datos de obstáculos y puede establecer las coordenadas de los mismos en función del nivel del juego.

    Atributos:
        _coordinates (list): Lista de coordenadas de los obstáculos en el tablero.
        _colour (str): Color del obstáculo en formato hexadecimal (por defecto, "#CEB200").
        _loader (ObstacleLoader): Objeto responsable de cargar los datos de obstáculos.
        _obstacles (list): Lista de listas de coordenadas que representan los obstáculos, cargados desde el `ObstacleLoader`.

    Métodos:
        __init__(loader: ObstacleLoader) -> None: Inicializa la clase con un cargador de datos de obstáculos.
        coordinates() -> list: Obtiene las coordenadas actuales de los obstáculos.
        colour() -> str: Obtiene el color de los obstáculos.
        set_obstacle(level: int) -> None: Establece las coordenadas del obstáculo según el nivel del juego.
        _load_obstacles() -> dict: Carga los obstáculos desde el cargador.
    """

    def __init__(self, loader: ObstacleLoader) -> None:
        """
        Inicializa un objeto de la clase Obstacle, configurando el cargador de datos y las propiedades de los obstáculos.

        Este constructor recibe un objeto de tipo `ObstacleLoader` para cargar los datos de obstáculos y establece los valores iniciales para las coordenadas y el color del obstáculo.

        :param loader: Objeto de tipo `ObstacleLoader` encargado de cargar los datos de obstáculos desde una fuente externa.
        """
        self._coordinates = []
        self._colour = "#CEB200"
        self._loader = loader
        self._obstacles = self._load_obstacles()

    @property
    def coordinates(self) -> list:
        """
        Obtiene las coordenadas actuales de los obstáculos.

        Este método es una propiedad que devuelve la lista de coordenadas de los obstáculos que han sido configurados en el juego.

        :return: Lista de coordenadas de los obstáculos.
        """
        return self._coordinates

    @property
    def colour(self) -> str:
        """
        Obtiene el color actual del obstáculo.

        Este método es una propiedad que devuelve el color del obstáculo.

        :return: Color del obstáculo en formato hexadecimal (str).
        """
        return self._colour

    def set_obstacle(self, level: int) -> None:
        """
        Establece las coordenadas del obstáculo para el nivel especificado.

        Este método configura las coordenadas del obstáculo en función del nivel del juego. Los obstáculos se cargan previamente y se selecciona uno según el índice del nivel, con un ciclo entre ellos basado en el nivel proporcionado.

        :param level: Nivel del juego (un entero positivo) que determina qué conjunto de coordenadas de obstáculos se debe utilizar.
        :raises ValueError: Si no se puede encontrar un obstáculo disponible o si los datos no son válidos.
        """
        if not self._obstacles:
            print("Error: No hay obstáculos disponibles.")
            return

        obstacle_index = (level - 1) % len(self._obstacles)
        self._coordinates = self._obstacles[obstacle_index]

    def _load_obstacles(self) -> dict:
        """
        Carga los datos de obstáculos utilizando el cargador proporcionado.

        Este método interactúa con el cargador de obstáculos para obtener los datos de los obstáculos configurados. Los datos se organizan en un diccionario para facilitar el acceso.

        :return: Diccionario con los datos de obstáculos, donde cada nivel está asociado a un conjunto de coordenadas.
        """
        return self._loader.load_obstacles()
