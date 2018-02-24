import random
from utils.game_state import GameState
from utils.vector import up, down, left, right


class BaseSnake(object):

    HUNGER_THRESHOLD = 30

    def payload_to_game_state(self, payload):
        return GameState(payload)

    def move(self, gamestate):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def name(self):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def color(self):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def head_url(self):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def taunt(self):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def end(self):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def bad_move(self, move, gs):
        if move is None:
            return True
        coord = gs.me.head + move
        if not gs.is_empty(coord) and coord not in gs.all_tails:
            return True
        if coord in gs.possible_death_coords:
            return True
        return False

    def chase_tail(self, gamestate):
        allow_length_1 = gamestate.turn >= 5
        visitable_tails = gamestate.best_paths_to(gamestate.me.head, gamestate.all_tails, allow_length_1)
        if len(visitable_tails) > 0:
            closest_goal = visitable_tails[0]
            (goal, distance_from_start, path) = closest_goal
            m = path[1] - gamestate.me.head
            return m

    def orthogonal_eat(self, gamestate):
        if gamestate.me.health < self.HUNGER_THRESHOLD:
            closest_food = self._orthogonal_closest_to(gamestate.food, gamestate.me.head)
            if closest_food is None:
                return up
            return gamestate.first_empty_direction(
                gamestate.me.head,
                self._orthogonal_directions_to(closest_food, gamestate),
                up)

    def _orthogonal_closest_to(self, goals, start):
        if len(goals) == 0:
            return None

        def _dist(a, b):
            return abs((a-b).magnitude)
        goals.sort(key=lambda x: _dist(x, start), reverse=False)
        return goals[0]

    def _orthogonal_directions_to(self, goal, gamestate):
        distances = [
            ((goal-gamestate.me.head-left).magnitude, left),
            ((goal-gamestate.me.head-right).magnitude, right),
            ((goal-gamestate.me.head-up).magnitude, up),
            ((goal-gamestate.me.head-down).magnitude, down),
        ]
        distances.sort(key=lambda x: x[0], reverse=False)
        return [d[1] for d in distances]

    def possible_kill(self, gamestate):
        if len(gamestate.possible_kill_coords) > 0:
            goal = random.choice(gamestate.possible_kill_coords)
            return goal - gamestate.me.head

