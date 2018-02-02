from utils.vector import Vector, up, down, left, right, noop
from base_snake import BaseSnake


class Snake0(BaseSnake):

    def move(self, gamestate):

        current_vector = gamestate.current_direction
        if current_vector != noop:
            return current_vector

        head = gamestate.my_head
        dist_left = head.x
        dist_right = gamestate.board_width - dist_left
        dist_up = head.y
        dist_down = gamestate.board_height - dist_up
        dists = [dist_left, dist_right, dist_up, dist_down]
        max_dist = max(dists)

        return {
            dist_left: left,
            dist_right: right,
            dist_up: up,
            dist_down: down,
        }.get(max_dist, up)

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
