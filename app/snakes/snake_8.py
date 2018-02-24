import random
from base_snake import BaseSnake
from snake_7 import AttemptKillsSnake


class TailChaser(BaseSnake):

    THRESHOLD = 30

    def move(self, gamestate):

        if len(gamestate.possible_kill_coords) > 0:
            goal = random.choice(gamestate.possible_kill_coords)
            return goal - gamestate.me.head, "kill?"

        if gamestate.me.health < self.THRESHOLD:
            return AttemptKillsSnake().move(gamestate), "hungry"

        visitable_tails = gamestate.best_paths_to(gamestate.me.head, gamestate.all_tails)
        if len(visitable_tails) > 0:
            closest_goal = visitable_tails[0]
            (goal, distance_from_start, path) = closest_goal
            m = path[1] - gamestate.me.head
            print m
            return m, "tail"

    def name(self):
        return "Training Snake 8"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
