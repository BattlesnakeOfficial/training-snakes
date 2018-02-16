from utils.vector import Vector, up, down, left, right, noop
from base_snake import BaseSnake


class Snake0(BaseSnake):

    def move(self, gamestate):

        current_vector = gamestate.current_direction
        if current_vector != noop:
            return current_vector

        head = gamestate.my_head
        l_wall = Vector(0, head.y)
        r_wall = Vector(gamestate.board_width-1, head.y)
        t_wall = Vector(head.x, 0)
        b_wall = Vector(head.x, gamestate.board_width-1)
        farthest = head.farthest([l_wall, r_wall, t_wall, b_wall])
        return {
            l_wall: left,
            r_wall: right,
            t_wall: up,
            b_wall: down,
        }.get(farthest, up)

    def name(self):
        return "Training Snake 0"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
