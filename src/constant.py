OBSTACLE_FILE = "resources/obstacles.txt"

BOARD_ROWS, BOARD_COLUMNS = (21, 21)

AMOUNT_FRUITS_TO_WIN = 20

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

KEYS = {
	"UP": (0,-1),
	"DOWN": (0,1),
	"LEFT": (-1,0),
	"RIGHT": (1,0),
}