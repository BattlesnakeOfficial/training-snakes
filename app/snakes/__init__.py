import random
from snake_10 import Snake10
from snake_5 import Snake5
from snake_4 import Snake4
from snake_3 import Snake3
from snake_2 import Snake2
from snake_1 import Snake1
from snake_0 import Snake0

_snakes = {
    "snake_0": Snake0(),
    "snake_1": Snake1(),
    "snake_2": Snake2(),
    "snake_3": Snake3(),
    "snake_4": Snake4(),
    "snake_5": Snake5(),
    "bambora": Snake10(),
}


def get_snake(snake_name):
    return _snakes.get(snake_name, Snake1())


def get_random_color(name):
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())