from tkinter.constants import HORIZONTAL


OBSTACLE_FILE = "resources/obstacles.txt"

BOARD_ROWS = 21
BOARD_COLUMNS = 21

AMOUNT_FRUITS_TO_WIN = 20

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
HORIZONTAL_MARGIN = 40
VERTICAL_MARGIN = 60

BOARD_DIMENSIONS = {
                      "width": WINDOW_WIDTH - HORIZONTAL_MARGIN * 2,
                      "height": WINDOW_HEIGHT - VERTICAL_MARGIN * 2
}

LOCKERS_DIMENSIONS = {
                      "width": BOARD_DIMENSIONS["width"] / BOARD_COLUMNS,
                      "height": BOARD_DIMENSIONS["height"] / BOARD_ROWS
}

BOARD_SIDES = {
                "left": HORIZONTAL_MARGIN,
                "right": WINDOW_WIDTH - HORIZONTAL_MARGIN,
                "up": VERTICAL_MARGIN,
                "down": WINDOW_HEIGHT - VERTICAL_MARGIN
}

BUTTON_SIDES = {
                "left": WINDOW_WIDTH * 1/4,
                "right": WINDOW_WIDTH * 3/4,
                "up": 400,
                "down": 450
}

PAUSE = "P"

KEYS = {
	"UP": (0,-1),
	"DOWN": (0,1),
	"LEFT": (-1,0),
	"RIGHT": (1,0),
}