from utils.vector import Vector, up, down, left, right
from snake_0 import Snake0


class Snake1(Snake0):

    def move(self, gamestate):
        default_move = Snake0().move(gamestate)
        head = gamestate.my_head
        for v in [default_move, up, down, left, right]:
            if gamestate.is_empty(head + v):
                return v
        return default_move

    def name(self):
        return "Training Snake 1"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
