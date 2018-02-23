from utils.vector import up, down, left, right, noop
from base_snake import BaseSnake


class Snake2(BaseSnake):

    def move(self, gamestate):

        current_vector = gamestate.me.current_direction
        if current_vector == noop:
            return up

        return gamestate.first_empty_direction(
            gamestate.me.head,
            [current_vector, up, down, left, right],
            up
        )

    def name(self):
        return "Training Snake 2"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
