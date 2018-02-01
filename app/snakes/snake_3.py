from utils.vector import Vector, up, down, left, right
from base_snake import BaseSnake


class Snake2(BaseSnake):

    def move(self, gamestate):

        current_vector = gamestate.current_direction()
        if current_vector == Vector(0, 0):
            return up

        head = gamestate.my_head()
        for v in [current_vector, up, down, left, right]:
            if gamestate.is_empty(head + v):
                return v

        return Vector(0, 1)

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
