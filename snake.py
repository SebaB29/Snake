from random import randint
from csv import reader

BOARD_ROWS, BOARD_COLUMNS = (21, 21)
AMOUNT_TO_WIN = 20
KEYS = {
	"UP": (0,-1),
	"DOWN": (0,1),
	"LEFT": (-1,0),
	"RIGHT": (1,0),
	}

class Game:

    def __init__(self) -> None:
        """
        Inicializa la clase Game
        """
        self.__rows = BOARD_ROWS
        self.__columns = BOARD_COLUMNS
        self.__last_move = "RIGHT"

    def get_board_dimensions(self) -> list:
        """
        Devuelve: las dimensiones del tablero (tuple)
        """
        return (self.__rows, self.__columns)

    def get_last_move(self) -> str:
        """
        Devuelve: la última jugada realizada (str)
        """
        return self.__last_move

    def set_move(self, key: str) -> None:
        """
        Recibe: una tecla (str)

        Establece el movimiento si la tecla esta en KEYS
        """
        if key in KEYS:
            self.__last_move = key

    def __you_lost(self, snake_head: tuple, you_crashed: bool) -> bool:
        """
        Recibe: las coordenadas de la cabeza del snake (tuple) y una variable que determina si el snake choco (bool)

        Devuelve: 
            True: si perdio, es decir, si el snake choco o esta fuera de rango

            False: en caso contrario
        """
        return not (0 <= snake_head[0] < self.__rows and 0 <= snake_head[1] < self.__columns) or you_crashed

    def _you_won(self, quantity_fruits: int) -> bool:
        """
        Recibe: la cantidad de frutas que hay que comer para ganar (int)
        
        Devuelve:
                True: si ganó, es decir, si la cantidad de frutas es cero
                
                False: en caso contrario
        """
        return not quantity_fruits

    def _finish_game(self, snake: object, quantity_fruits: int, obstacle_coordinates: list) -> bool:
        """
        Recibe: el snake (object), la cantidad de frutas que hay que comer para ganar (int) 
                y las coordenadas del obstaculo (tuple(tuple))
        
        Ejecuta los métodos _you_won y you_lost
        
        Devuelve:
                True: en caso de que se haya ganado o perdido
                
                False: en caso contrario
        """
        return self._you_won(quantity_fruits) or self.__you_lost(snake.get_head(), snake._you_crashed(obstacle_coordinates))


class Object:

    def __init__(self, coordinates: list, colour: str) -> None:
        self.coordinates = coordinates
        self.colour = colour
    
    def get_coordinates(self) -> list:
        """
        Devuelve: las coordenadas del objeto (list)
        """
        return self.coordinates
    
    def get_colour(self) -> str:
        """
        Devuelve: el color del objeto (str)
        """
        return self.colour


class Snake(Object):

    def __init__(self) -> None:
        """
        Inicializa la clase Snake
        """
        Object.__init__(self, [(0,0),(1,0),(2,0)], "#1A8500")
        self.__head = self.coordinates[-1]
        self.__tail = self.coordinates[0]

    def get_head(self) -> tuple:
        """
        Devuelve: las coordenadas de la cabeza del snake (tuple)
        """
        return self.__head

    def __set_head(self) -> None:
        """
        Establece las nuevas coordenadas de la cabeza
        """
        self.__head = self.coordinates[-1]

    def __set_tail(self) -> None:
        """
        Establece las nuevas coordenadas de la cola del snake
        """
        self.__tail = self.coordinates[0]

    def move(self, last_move: str) -> tuple:
        """
        Recibe: el último movimiento realizado (str)

        Actualiza las coordenadas del snake y ejecuta los métodos __set_head y __set_tail()
        """
        self.coordinates.append((self.__head[0] + KEYS[last_move][0] , self.__head[1] + KEYS[last_move][1]))
        self.coordinates.pop(0)
        self.__set_head()
        self.__set_tail()

    def eat_fruit(self, fruit: object) -> None:
        """
        Recibe: fruit (object)

        Agrega las coordenadas de la fruta al snake y ejecuta el método set_quantity_fruits()
        """
        self.coordinates.insert(0, self.__tail)
        fruit.set_quantity_fruits()

    def _you_crashed(self, obstacle_coordinates: tuple):
        """
        Recibe: las coordenadas del obstacul (tuple)

        Devuelve:
                True: si el snake choco, es decir, si la cabeza choca con el cuerpo o contra un obstáculo

                False: en caso contrario
        """
        return self.__head in self.coordinates[:-1] or self.__head in obstacle_coordinates


class Fruit(Object):

    def __init__(self) -> None:
        """
        Inicializa la clase Fruit
        """
        Object.__init__(self, [], "#F00")
        self.__quantity_fruits = AMOUNT_TO_WIN

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
        if self.coordinates:
            self.coordinates.pop()
        self.coordinates.append(self.__generate_fruit(board_dimensions, snake_coordinates, obstacle_coordinates))

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


class Obstacle(Object):

    def __init__(self) -> None:
        """
        Inicializa la clase Obstacle
        """
        Object.__init__(self, None, "#CEB200")
        self.__obstacles = self.__read_obstacle_file()

    def set_obstacle(self, level: int) -> None:
        """
        Recibe: el nivel (int)

        Establece las coordenadas del obstáculo que corresponde
        """
        obstacle_index = (level - 1) % len(self.__obstacles)
        self.coordinates = self.__obstacles[obstacle_index]

    def __read_obstacle_file(self) -> dict:
        """
        Lee el archivo con las coordenadas de los obstáculos

        Devuelve: un diccionario (dict) con las coordenadas de todos los obstáculos
        """
        obstacles = {}
        with open("obstacles.txt") as file:
            csv_reader = reader(file, delimiter=" ")
            for i, coordinate_group in enumerate(csv_reader):
                for coordinates in coordinate_group[:-2]:
                    obstacles[i] = list(map(eval, coordinates.split(";")))

        return obstacles
