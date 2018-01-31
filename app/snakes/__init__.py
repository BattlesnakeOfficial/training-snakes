from snake_1 import Snake1

_snakes = {
    "snake_1": Snake1()
}


def get_snake(snake_name):
    return _snakes.get(snake_name, Snake1())
