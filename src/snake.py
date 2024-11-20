from src.constant import KEYS


class Snake:
    """
    Representa una serpiente en el juego Snake.

    La serpiente está compuesta por una lista de coordenadas que representan
    las posiciones de su cuerpo en el tablero.
    """

    def __init__(self) -> None:
        """
        Inicializa la serpiente con un cuerpo compuesto por tres segmentos
        horizontales consecutivos y un color predeterminado.

        Atributos:
            _coordinates (list): Lista de tuplas que representan las coordenadas
                de los segmentos del cuerpo de la serpiente en el tablero.
            _colour (str): Código de color hexadecimal que representa el color
                de la serpiente.
        """
        self._coordinates = [(0, 0), (1, 0), (2, 0)]
        self._colour = "#1A8500"

    @property
    def coordinates(self) -> list:
        """
        Obtiene todas las coordenadas del cuerpo de la serpiente.

        :return: Lista de tuplas representando las posiciones del cuerpo.
        """
        return self._coordinates

    @property
    def head(self) -> tuple:
        """
        Obtiene las coordenadas actuales de la cabeza de la serpiente.

        :return: Una tupla representando la posición de la cabeza.
        """
        return self._coordinates[-1]

    @property
    def tail(self) -> tuple:
        """
        Obtiene las coordenadas actuales de la cola de la serpiente.

        :return: Una tupla representando la posición de la cola.
        """
        return self._coordinates[0]

    @property
    def colour(self) -> str:
        """
        Obtiene el color de la serpiente.

        :return: Un string con el código hexadecimal del color.
        """
        return self._colour

    def move(self, last_move: str) -> None:
        """
        Mueve la serpiente en la dirección indicada por el último movimiento.

        La cabeza se mueve a una nueva posición calculada a partir de
        la dirección, y la cola se elimina para mantener la longitud constante.

        :param last_move: Un string que representa la dirección del movimiento
            ('UP', 'DOWN', 'LEFT', 'RIGHT').
        """
        new_head = (
            self.head[0] + KEYS[last_move][0],
            self.head[1] + KEYS[last_move][1],
        )
        self._coordinates.append(new_head)
        self._coordinates.pop(0)

    def eat_fruit(self) -> None:
        """
        Hace que la serpiente crezca al comer una fruta.

        La longitud de la serpiente aumenta añadiendo una nueva sección en
        la posición de la cola actual.
        """
        self._coordinates.insert(0, self.tail)

    def you_crashed(self, obstacle_coordinates: list[tuple[int, int]]) -> bool:
        """
        Determina si la serpiente ha chocado con su propio cuerpo o con un obstáculo.

        :param obstacle_coordinates: Una tupla o lista de coordenadas que
            representan las posiciones de los obstáculos en el tablero.
        :return: True si la cabeza de la serpiente colisiona con su cuerpo o
            con un obstáculo; False en caso contrario.
        """
        return self.head in self._coordinates[:-1] or self.head in obstacle_coordinates
