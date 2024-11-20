from src.constant import *
from graphics.gamelib import draw_begin, draw_end, draw_text, draw_rectangle, draw_oval
from src.snake import Snake
from src.fruit import Fruit
from src.obstacle import Obstacle


class GameRenderer:
    def __init__(
        self, level: int, snake: Snake, fruit: Fruit, obstacle: Obstacle
    ) -> None:
        """
        Inicializa el renderizador del juego con los elementos necesarios.

        :param level: El nivel actual del juego.
        :param snake: El objeto que representa la serpiente.
        :param fruit: El objeto que representa las frutas en el juego.
        :param obstacle: El objeto que representa los obstáculos en el juego.
        """
        self.level = level
        self.snake = snake
        self.fruit = fruit
        self.obstacle = obstacle

    def show_level(self) -> None:
        """
        Muestra el nivel actual en la pantalla.

        Dibuja un texto en la parte superior izquierda de la pantalla indicando el nivel.
        """
        draw_text(f"Level {self.level}", HORIZONTAL_MARGIN + 25, VERTICAL_MARGIN - 15)

    def show_condition(self) -> None:
        """
        Muestra el contador de frutas restantes para ganar y una representación visual de la fruta actual.

        Dibuja el número de frutas restantes y un círculo que representa la fruta actual en la pantalla.
        """
        draw_text(
            f"Fruits: {self.fruit.quantity_fruits}",
            WINDOW_WIDTH - HORIZONTAL_MARGIN * 2.6,
            VERTICAL_MARGIN - 15,
        )
        upper_curve, lower_curve = VERTICAL_MARGIN - 24, VERTICAL_MARGIN - 9
        left_curve, right_curve = (WINDOW_WIDTH - 62), (WINDOW_WIDTH - 47)
        draw_oval(
            left_curve, upper_curve, right_curve, lower_curve, fill=self.fruit.colour
        )

    def show_keys(self) -> None:
        """
        Muestra las teclas disponibles para el jugador.

        Dibuja las teclas de dirección (↑, ↓, ←, →) y la tecla de pausa (P) en la parte inferior de la pantalla.
        """
        draw_text(
            f"⇧", WINDOW_WIDTH / 2 + HORIZONTAL_MARGIN * 2, WINDOW_HEIGHT - 38, size=15
        )
        draw_text(
            f"⇨",
            WINDOW_WIDTH / 2 + HORIZONTAL_MARGIN * 2 + 10,
            WINDOW_HEIGHT - 30,
            size=15,
        )
        draw_text(
            f"⇩", WINDOW_WIDTH / 2 + HORIZONTAL_MARGIN * 2, WINDOW_HEIGHT - 20, size=15
        )
        draw_text(
            f"⇦",
            WINDOW_WIDTH / 2 + HORIZONTAL_MARGIN * 2 - 10,
            WINDOW_HEIGHT - 30,
            size=15,
        )
        draw_text(
            f"P: Pause",
            WINDOW_WIDTH / 2 - HORIZONTAL_MARGIN * 2,
            WINDOW_HEIGHT - 30,
            size=15,
        )

    def draw_board(self) -> None:
        """
        Dibuja el tablero del juego en la pantalla.

        Dibuja un rectángulo que representa el borde del tablero en la pantalla.
        """
        draw_rectangle(
            BOARD_SIDES["left"],
            BOARD_SIDES["up"],
            BOARD_SIDES["right"],
            BOARD_SIDES["down"],
            fill="#4CCD2C",
            outline="#22AB00",
            width=2,
        )

    def draw_element(
        self, element_coordinates: list[tuple[int, int]], colour: str
    ) -> None:
        """
        Dibuja un elemento del juego (serpiente, fruta, obstáculo) en la pantalla.

        :param element_coordinates: Lista de coordenadas de los elementos a dibujar.
        :param colour: El color en el que se debe dibujar el elemento.
        """
        for pixel_x_position, pixel_y_position in self.convert_coordinates_to_pixels(
            element_coordinates
        ):
            upper_curve, lower_curve = pixel_y_position, (
                pixel_y_position + LOCKERS_DIMENSIONS["height"]
            )
            left_curve, right_curve = pixel_x_position, (
                pixel_x_position + LOCKERS_DIMENSIONS["width"]
            )
            draw_oval(
                left_curve,
                upper_curve,
                right_curve,
                lower_curve,
                fill=colour,
                outline="#202020",
            )

    def show_game(self) -> None:
        """
        Muestra el estado completo del juego en la pantalla.

        Dibuja todos los elementos visuales del juego: nivel, estado de frutas, teclas, tablero, serpiente, frutas y obstáculos.
        """
        draw_begin()
        self.show_level()
        self.show_condition()
        self.show_keys()
        self.draw_board()
        self.draw_element(self.snake.coordinates, self.snake.colour)
        self.draw_element(self.fruit.coordinates, self.fruit.colour)
        self.draw_element(self.obstacle.coordinates, self.obstacle.colour)
        draw_end()

    def show_game_over(self) -> None:
        """
        Muestra el mensaje de "GAME OVER" en la pantalla.

        Dibuja un texto en el centro de la pantalla indicando que el juego ha terminado.
        """
        draw_text(
            "GAME",
            WINDOW_WIDTH / 2 - 5,
            WINDOW_HEIGHT / 2 - 80,
            size=70,
            fill="#E3E4E5",
        )
        draw_text("OVER", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, size=70, fill="#E3E4E5")

    def show_restart_button(self) -> None:
        """
        Muestra el botón de reinicio en la pantalla.

        Dibuja un rectángulo con el texto "RESTART" en el área definida como el botón de reinicio.
        """
        button_width, button_height = (BUTTON_SIDES["left"] + BUTTON_SIDES["right"]), (
            BUTTON_SIDES["up"] + BUTTON_SIDES["down"]
        )
        draw_rectangle(
            BUTTON_SIDES["left"],
            BUTTON_SIDES["up"],
            BUTTON_SIDES["right"],
            BUTTON_SIDES["down"],
            fill="#000",
            outline="#FFF",
        )
        draw_text("RESTART", button_width / 2, button_height / 2, size=15)

    def show_end(self) -> None:
        """
        Muestra la pantalla final del juego con el mensaje "GAME OVER" y el botón de reinicio.

        Dibuja la pantalla final con el mensaje de "GAME OVER" y el botón de reinicio en la parte inferior.
        """
        draw_begin()
        self.show_game_over()
        self.show_restart_button()
        draw_end()

    def convert_coordinates_to_pixels(
        self, element_coordinates: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        """
        Convierte las coordenadas de los elementos del tablero a posiciones en píxeles en la pantalla.

        :param element_coordinates: Lista de coordenadas (x, y) en el tablero.
        :return: Lista de coordenadas convertidas a píxeles (x_pixel, y_pixel).
        """
        return [
            (
                HORIZONTAL_MARGIN + LOCKERS_DIMENSIONS["width"] * x_coordinate,
                VERTICAL_MARGIN + LOCKERS_DIMENSIONS["height"] * y_coordinate,
            )
            for x_coordinate, y_coordinate in element_coordinates
        ]
