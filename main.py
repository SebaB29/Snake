from graphics import WINDOW_DIMENSIONS, BUTTON_SIDES, BOARD_ROWS, BOARD_COLUMNS, show_game, show_end
from gamelib import resize, title, init, loop, wait, get_events, EventType
from snake import Game, Snake, Fruit, Obstacle

def main(level=0):

    resize(WINDOW_DIMENSIONS["width"], WINDOW_DIMENSIONS["height"])
    title("SNAKE")

    game, snake, fruit, obstacle = Game(BOARD_ROWS, BOARD_COLUMNS), Snake(), Fruit(), Obstacle()
    obstacle.set_obstacle(level)
    fruit.set_fruit(game.get_board(), snake.get_snake(), obstacle.get_obstacle())

    while loop(fps = 8) and not game._finish_game(snake, fruit.get_quantity_fruits(), obstacle.get_obstacle()):
        for event in get_events():
            if event.type == EventType.KeyPress:
                event.key = event.key.upper()
                game.set_move(event.key)
                if event.key == "P":
                    wait(EventType.KeyPress)

        snake.move(game.get_last_move())
        if snake.get_head() in fruit.get_fruit():
            snake.eat_fruit(fruit)
            fruit.set_fruit(game.get_board(), snake.get_snake(), obstacle.get_obstacle())

        show_game(level, snake, fruit, obstacle)

    if game._you_won(fruit.get_quantity_fruits()):
        main(level = level + 1)

    show_end()

    event = wait(EventType.ButtonPress)
    if not event:
        exit()
    elif BUTTON_SIDES["left"] <= event.x <= BUTTON_SIDES["right"] and BUTTON_SIDES["up"] <= event.y <= BUTTON_SIDES["down"]:
        main()

init(main)
