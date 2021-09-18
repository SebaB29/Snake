from gamelib import draw_begin, draw_end, draw_text, draw_rectangle, draw_oval
from snake import BOARD_ROWS, BOARD_COLUMNS

WINDOW_DIMENSIONS = {
                      "height": 500,
                      "width": 500
                     }
MARGINS = {
            "horizontal": 40,
            "vertical": 60
           }
BOARD_DIMENSIONS = {
                      "width": WINDOW_DIMENSIONS["width"] - MARGINS["horizontal"] * 2,
                      "height": WINDOW_DIMENSIONS["height"] - MARGINS["vertical"] * 2
                    }
LOCKERS_DIMENSIONS = {
                      "width": BOARD_DIMENSIONS["width"] / BOARD_COLUMNS,
                      "height": BOARD_DIMENSIONS["height"] / BOARD_ROWS
                      }
BOARD_SIDES = {
                "left": MARGINS["horizontal"],
                "right": WINDOW_DIMENSIONS["width"] - MARGINS["horizontal"],
                "up": MARGINS["vertical"],
                "down": WINDOW_DIMENSIONS["height"] - MARGINS["vertical"]
               }
BUTTON_SIDES = {
                "left": WINDOW_DIMENSIONS["width"] * 1/4,
                "right": WINDOW_DIMENSIONS["width"] * 3/4,
                "up": 400,
                "down": 450
                }

def show_level(level: int) -> None:
    """
    Recibe: el nivel actual (int)
    
    Lo muestra en la pantalla
    """
    draw_text(f"Level {level}", MARGINS["horizontal"] + 25, MARGINS["vertical"] - 15)

def show_condition(quantity_fruits: int, fruit_colour: str) -> None:
    """
    Recibe: la cantidad de frutas (int) y su color (str)
    
    Muestra un contador para saber cuantas frutas faltan comer para ganar el nivel
    """
    draw_text(f"Fruits: {quantity_fruits}", WINDOW_DIMENSIONS["width"] - MARGINS["horizontal"] * 2.6, MARGINS["vertical"] - 15)

    upper_curve, lower_curve = MARGINS["vertical"] - 24, MARGINS["vertical"] - 9
    left_curve, right_curve = (WINDOW_DIMENSIONS["width"] - 62), (WINDOW_DIMENSIONS["width"] - 47)
    draw_oval(left_curve, upper_curve, right_curve, lower_curve, fill=fruit_colour)

def show_keys() -> None:
    """
    Muestra en la pantalla las teclas disponibles
    """
    draw_text(f"⇧", WINDOW_DIMENSIONS["width"] / 2 + MARGINS["horizontal"] * 2, WINDOW_DIMENSIONS["height"] - 38, size=15)
    draw_text(f"⇨", WINDOW_DIMENSIONS["width"] / 2 + MARGINS["horizontal"] * 2 + 10, WINDOW_DIMENSIONS["height"] - 30, size=15)
    draw_text(f"⇩", WINDOW_DIMENSIONS["width"] / 2 + MARGINS["horizontal"] * 2, WINDOW_DIMENSIONS["height"] - 20, size=15)
    draw_text(f"⇦", WINDOW_DIMENSIONS["width"] / 2 + MARGINS["horizontal"] * 2 - 10, WINDOW_DIMENSIONS["height"] - 30, size=15)
    draw_text(f"P: Pause", WINDOW_DIMENSIONS["width"] / 2 - MARGINS["horizontal"] * 2, WINDOW_DIMENSIONS["height"] - 30, size=15)

def draw_board() -> None:
    """
    Dibuja en la pantalla el tablero
    """
    draw_rectangle(BOARD_SIDES["left"], BOARD_SIDES["up"], BOARD_SIDES["right"], BOARD_SIDES["down"], fill="#4CCD2C", outline="#22AB00", width=2)

def draw_element(element_coordinates: list, colour: str) -> None:
    """
    Recibe: las coordenadas de un elemento (list[tuples]) y su color (str)
    
    Dibuja en la pantalla el elemento
    """
    for pixel_x_position, pixel_y_position in convert_coordinates_to_pixels(element_coordinates):
        upper_curve, lower_curve = pixel_y_position, (pixel_y_position + LOCKERS_DIMENSIONS["height"])
        left_curve, right_curve = pixel_x_position, (pixel_x_position + LOCKERS_DIMENSIONS["width"])
        draw_oval(left_curve, upper_curve, right_curve, lower_curve, fill=colour, outline="#202020")

def show_game_over() -> None:
    """
    Muestra en la pantalla el mensaje GAME OVER
    """
    draw_text("GAME", WINDOW_DIMENSIONS["width"] / 2 - 5, WINDOW_DIMENSIONS["height"] / 2 - 80, size=70, fill="#E3E4E5")
    draw_text("OVER", WINDOW_DIMENSIONS["width"] / 2, WINDOW_DIMENSIONS["height"] / 2, size=70, fill="#E3E4E5")

def show_restart_button() -> None:
    """
    Muestra en la pantalla el botón RESTART
    """
    button_width, button_height = (BUTTON_SIDES["left"] + BUTTON_SIDES["right"]), (BUTTON_SIDES["up"] + BUTTON_SIDES["down"])
    draw_rectangle(BUTTON_SIDES["left"], BUTTON_SIDES["up"], BUTTON_SIDES["right"], BUTTON_SIDES["down"], fill="#000", outline="#FFF")
    draw_text("RESTART", button_width / 2, button_height / 2, size=15)

def show_game(level: int, snake_data: list, fruit_data: list, obstacle_data: list) -> None:
    """
    Recibe: el nivel actual (int), snake (object), fruit (object) y obstacle (object)
    
    Ejecuta las funciones gráficas que muestran el juego
    """
    draw_begin()
    show_level(level)
    show_condition(fruit_data[2], fruit_data[1])
    show_keys()
    draw_board()
    draw_element(snake_data[0], snake_data[1])
    draw_element(fruit_data[0], fruit_data[1])
    draw_element(obstacle_data[0], obstacle_data[1])
    draw_end()

def show_end() -> None:
    """
    Ejecuta las funciones gráficas que muestran el final del juego
    """
    draw_begin()
    show_game_over()
    show_restart_button()
    draw_end()

def convert_coordinates_to_pixels(element_coordinates: list) -> list:
    """
    Recibe: las coordenadas de un elemento (list[tuples])
    
    Devuelve: su posición en pixels (list[tuples])
    """

    return [
        (MARGINS["horizontal"] + LOCKERS_DIMENSIONS["width"] * x_coordinate, MARGINS["vertical"] + LOCKERS_DIMENSIONS["height"] * y_coordinate)
        for x_coordinate, y_coordinate in element_coordinates
        ]