from utils.vector import Vector, up, down, left, right, noop
from base_snake import BaseSnake

from bambora.snakes.food_helper import move_to_food


class Snake5(BaseSnake):

    def move(self, gamestate):
        move_to_food(gamestate)

    def name(self):
        return "Training Snake 10"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
