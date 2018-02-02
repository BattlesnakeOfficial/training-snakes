from utils.vector import Vector, up, down, left, right, noop
from base_snake import BaseSnake


class Snake3(BaseSnake):

    def move(self, gamestate):
        first_food = gamestate.food[0]
        ordered_directions = self._directions_to(first_food, gamestate)
        head = gamestate.my_head
        for v in ordered_directions:
            if gamestate.is_empty(head + v):
                return v
        return up

    def _directions_to(self, goal, gamestate):
        to_travel = goal - gamestate.my_head
        horizontal = [left, right] if goal.x < gamestate.my_head.x else [right, left]
        vertical = [up, down] if goal.y < gamestate.my_head.y else [down, up]
        if to_travel.x > to_travel.y:
            return horizontal + vertical
        return vertical + horizontal

    def name(self):
        return "Training Snake 3"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
