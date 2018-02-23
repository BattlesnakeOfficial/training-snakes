import random
# from snake_10 import Snake10
from snake_8 import TailChaser
from snake_7 import Snake7
from snake_6 import SimpleSometimesHungrySnake
from snake_5 import SimpleHungrySnake
from snake_4 import ScaredSnake
from snake_3 import Snake3
from snake_2 import Snake2
from snake_1 import Snake1
from snake_0 import Snake0

_snakes = {
    "snake_0": Snake0(),
    "snake_1": Snake1(),
    "snake_2": Snake2(),
    "snake_3": Snake3(),
    "snake_4": ScaredSnake(),
    "snake_5": SimpleHungrySnake(),
    "snake_6": SimpleSometimesHungrySnake(),
    "snake_7": Snake7(),
    "snake_8": TailChaser(),
    # "bambora": Snake10(),
}


def get_snake(snake_name):
    return _snakes.get(snake_name, Snake1())


def get_random_color(name):
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())