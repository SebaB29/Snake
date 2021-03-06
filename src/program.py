from graphics.graphics import WINDOW_HEIGHT, WINDOW_WIDTH, BUTTON_SIDES, PAUSE, show_game, show_end
from graphics.gamelib import resize, title, loop, wait, get_events, EventType
from src.constant import PAUSE
from src.game import Game
from src.snake import Snake
from src.fruit import Fruit
from src.obstacle import Obstacle

class Program:

    def __init__(self, level):
        self.level = level
        self.game = Game()
        self.snake = Snake()
        self.fruit = Fruit()
        self.obstacle = Obstacle()

    def get_level(self):
        return self.level

    def start_game(self):
        title("SNAKE")
        resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.obstacle.set_obstacle(self.level)
        self.fruit.set_fruit(self.game.get_board_dimensions(), self.snake.get_coordinates(), self.obstacle.get_coordinates())

        while loop(fps = 8) and not self.game._finish_game(self.snake, self.fruit.get_quantity_fruits(), self.obstacle.get_coordinates()):
            for event in get_events():
                if event.type == EventType.KeyPress:
                    event.key = event.key.upper()
                    self.game.set_move(event.key)
                    if event.key == PAUSE:
                        wait(EventType.KeyPress)

            self.snake.move(self.game.get_last_move())
            if self.snake.get_head() in self.fruit.get_coordinates():
                self.snake.eat_fruit()
                self.fruit.set_quantity_fruits()
                self.fruit.set_fruit(self.game.get_board_dimensions(), self.snake.get_coordinates(), self.obstacle.get_coordinates())

            show_game(
                    self.level,
                    [self.snake.get_coordinates(), self.snake.get_colour()],
                    [self.fruit.get_coordinates(), self.fruit.get_colour(), self.fruit.get_quantity_fruits()],
                    [self.obstacle.get_coordinates(), self.obstacle.get_colour()]
                    )

    def won(self):
        return self.game._you_won(self.fruit.get_quantity_fruits())

    def restart_game(self):
        event = wait(EventType.ButtonPress)
        return event and BUTTON_SIDES["left"] <= event.x <= BUTTON_SIDES["right"] and BUTTON_SIDES["up"] <= event.y <= BUTTON_SIDES["down"]

    def end_game(self):
        show_end()