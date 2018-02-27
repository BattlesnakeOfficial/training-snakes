import random
from snake_10 import ControlFreak
from snake_9 import TailChaser2
from snake_8 import TailChaser
from snake_7 import AttemptKillsSnake
from snake_6 import SimpleSometimesHungrySnake
from snake_5 import SimpleHungrySnake
from snake_4 import ScaredSnake
from snake_3 import Snake3
from snake_2 import Snake2
from snake_1 import Snake1
from snake_0 import Snake0

_snakes = None

SNAKE_CLASSES = [
    Snake0,
    Snake1,
    Snake2,
    Snake3,
    ScaredSnake,
    SimpleHungrySnake,
    SimpleSometimesHungrySnake,
    AttemptKillsSnake,
    TailChaser,
    TailChaser2,
    ControlFreak,
]


def get_snake(snake_name):
    global _snakes

    if _snakes is None:
        _snakes = {}
        for snake_class in SNAKE_CLASSES:
            snake = snake_class()
            name = "snake_%d" % snake.DIFFICULTY
            _snakes[name] = snake

    return _snakes.get(snake_name, Snake1())
