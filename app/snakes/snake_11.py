from base_snake import BaseSnake
from utils.vector import up, down, left, right, Vector
from logic import BadMoves, ChaiseTail, Eat, Kill, PathDistances, IncreaseBoardControl, Surround


class SurroundSnake(BaseSnake, BadMoves, ChaiseTail, Eat, Kill, PathDistances, IncreaseBoardControl, Surround):
    DIFFICULTY = 11

    def is_hungry(self, gs):
        paths = gs.best_paths_to(gs.me.head, gs.food)
        if len(paths) == 0:
            return
        if len(paths) == 1:
            distance_to_closest_food = paths[0][1]
            return gs.me.health < distance_to_closest_food*2

        distance_to_second_closest_food = paths[1][1]
        return gs.me.health < distance_to_second_closest_food*2 + 5

    def move(self, gamestate):
        options = [
            (self.eat, "eat"),
            (self.surround, "surround"),
            (self.possible_kill, "possible kill"),
            (self.increase_board_control, "control"),
            (self.chase_tail, "tail"),
            (lambda gs: up, "up"),
            (lambda gs: down, "down"),
            (lambda gs: left, "left"),
            (lambda gs: right, "right"),
        ]
        return self.get_best_move(gamestate, options)
