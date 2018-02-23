from utils.vector import up, down, left, right
from base_snake import BaseSnake


class Snake5(BaseSnake):

    def move(self, gamestate):
        closest_food = self._closest_to(gamestate.food, gamestate.me.head)
        if closest_food is None:
            return up
        return gamestate.first_empty_direction(
            gamestate.me.head,
            self._directions_to(closest_food, gamestate),
            up)

    def _closest_to(self, goals, start):
        if len(goals) == 0:
            return None

        def _dist(a, b):
            return abs((a-b).magnitude)
        goals.sort(key=lambda x: _dist(x, start), reverse=False)
        return goals[0]

    def _directions_to(self, goal, gamestate):
        distances = [
            ((goal-gamestate.me.head-left).magnitude, left),
            ((goal-gamestate.me.head-right).magnitude, right),
            ((goal-gamestate.me.head-up).magnitude, up),
            ((goal-gamestate.me.head-down).magnitude, down),
        ]
        distances.sort(key=lambda x: x[0], reverse=False)
        return [d[1] for d in distances]

    def name(self):
        return "Training Snake 5"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
