from base_snake import BaseSnake
from utils.vector import up, down, left, right
from logic import BadMoves, ChaiseTail, Eat, Kill, PathDistances


class TailChaser2(BaseSnake, BadMoves, ChaiseTail, Eat, Kill, PathDistances):
    DIFFICULTY = 9

    def is_hungry(self, gs):
        paths = gs.best_paths_to(gs.me.head, gs.food)
        if len(paths) == 0:
            return
        if len(paths) == 1:
            distance_to_closest_food = paths[0][1]
            return gs.me.health < distance_to_closest_food*2

        distance_to_second_closest_food = paths[1][1]
        return gs.me.health < distance_to_second_closest_food*2


    def move(self, gamestate):
        options = [
            (self.eat, "simple eat"),
            (self.possible_kill, "possible kill"),
            (self.chase_tail, "tail"),
            (lambda gs: up, "up"),
            (lambda gs: down, "down"),
            (lambda gs: left, "left"),
            (lambda gs: right, "right"),
        ]

        for f, taunt in options:
            desired_move = f(gamestate)
            if not self.bad_move(desired_move, gamestate):
                return desired_move, taunt

        return down
