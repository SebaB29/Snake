from src.constant import KEYS

class Snake:
    def __init__(self) -> None:
        """
        Inicializa la clase Snake con una lista de coordenadas que representa su cuerpo.
        """
        self.__coordinates = [(0, 0), (1, 0), (2, 0)]  # Coordenadas del cuerpo
        self.__colour = "#1A8500"  # Color de la serpiente

    @property
    def coordinates(self) -> list:
        """
        Devuelve las coordenadas completas de la serpiente.
        """
        return self.__coordinates

    @property
    def head(self) -> tuple:
        """
        Devuelve las coordenadas de la cabeza de la serpiente.
        """
        return self.__coordinates[-1]

    @property
    def tail(self) -> tuple:
        """
        Devuelve las coordenadas de la cola de la serpiente.
        """
        return self.__coordinates[0]

    @property
    def colour(self) -> str:
        """
        Devuelve el color de la serpiente.
        """
        return self.__colour

    def move(self, last_move: str) -> None:
        """
        Recibe el último movimiento realizado y mueve la serpiente en consecuencia.
        Actualiza la posición de la cabeza y la cola.
        """
        # Calcula la nueva cabeza con base en el movimiento
        new_head = (self.head[0] + KEYS[last_move][0], self.head[1] + KEYS[last_move][1])
        # El movimiento es siempre agregar una nueva cabeza y mover el cuerpo
        self.__coordinates.append(new_head)
        self.__coordinates.pop(0)  # La cola se elimina al final

    def eat_fruit(self) -> None:
        """
        Al comer una fruta, la serpiente crece añadiendo la cola al principio de las coordenadas.
        """
        self.__coordinates.insert(0, self.tail)

    def _you_crashed(self, obstacle_coordinates: tuple) -> bool:
        """
        Verifica si la serpiente ha chocado con su propio cuerpo o con un obstáculo.
        """
        # Choca si la cabeza está en el cuerpo o en las coordenadas de los obstáculos
        return self.head in self.__coordinates[:-1] or self.head in obstacle_coordinates
