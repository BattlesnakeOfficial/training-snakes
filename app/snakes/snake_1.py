from utils.vector import up, down, left, right
from snake_0 import Snake0


class Snake1(Snake0):

    def move(self, gamestate):
        default_move = Snake0().move(gamestate)
        v = gamestate.first_empty_direction(
            gamestate.me.head,
            [default_move, up, down, left, right],
            default_move,
        )
        return v

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
