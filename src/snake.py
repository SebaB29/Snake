from src.constant import KEYS

class Snake:

    def __init__(self) -> None:
        """
        Inicializa la clase Snake
        """
        self.__coordinates = [(0,0),(1,0),(2,0)]
        self.__colour = "#1A8500"
        self.__head = self.__coordinates[-1]
        self.__tail = self.__coordinates[0]

    def get_coordinates(self) -> list:
        """
        Devuelve: las coordenadas del snake (list)
        """
        return self.__coordinates
    
    def get_colour(self) -> str:
        """
        Devuelve: el color del snake (str)
        """
        return self.__colour

    def get_head(self) -> tuple:
        """
        Devuelve: las coordenadas de la cabeza del snake (tuple)
        """
        return self.__head

    def __set_head(self) -> None:
        """
        Establece las nuevas coordenadas de la cabeza
        """
        self.__head = self.__coordinates[-1]

    def __set_tail(self) -> None:
        """
        Establece las nuevas coordenadas de la cola del snake
        """
        self.__tail = self.__coordinates[0]

    def move(self, last_move: str) -> tuple:
        """
        Recibe: el último movimiento realizado (str)

        Actualiza las coordenadas del snake y ejecuta los métodos __set_head y __set_tail()
        """
        self.__coordinates.append((self.__head[0] + KEYS[last_move][0] , self.__head[1] + KEYS[last_move][1]))
        self.__coordinates.pop(0)
        self.__set_head()
        self.__set_tail()

    def eat_fruit(self, fruit: object) -> None:
        """
        Recibe: fruit (object)

        Agrega las coordenadas de la fruta al snake y ejecuta el método set_quantity_fruits()
        """
        self.__coordinates.insert(0, self.__tail)
        fruit.set_quantity_fruits()

    def _you_crashed(self, obstacle_coordinates: tuple):
        """
        Recibe: las coordenadas del obstacul (tuple)

        Devuelve:
                True: si el snake choco, es decir, si la cabeza choca con el cuerpo o contra un obstáculo

                False: en caso contrario
        """
        return self.__head in self.__coordinates[:-1] or self.__head in obstacle_coordinates