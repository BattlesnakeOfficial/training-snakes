import random
from utils.game_state import GameState
from logic import BadMoves


class BaseSnake(BadMoves):

    HUNGER_THRESHOLD = 30
    DIFFICULTY = 8

    def payload_to_game_state(self, payload):
        return GameState(payload)

    def color(self):
        r = lambda: random.randint(0, 255)
        return '#%02X%02X%02X' % (r(), r(), r())

    def name(self):
        return "snake_%d" % self.DIFFICULTY

    def move(self, gamestate):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def end(self, details):
        pass

    def get_best_move(self, gamestate, options):
        move_response = {}

        def get_move(f, name):
            if f not in move_response:
                move_response[name] = f(gamestate)
            return move_response[name]

        for (f, name) in options:
            move = get_move(f, name)
            if move is None:
                continue
            if self.death_move(move, gamestate):
                continue
            if self.risky_move(move, gamestate):
                continue
            return move, name

        for (f, name) in options:
            move = get_move(f, name)
            if self.risky_move(move, gamestate):
                continue
            return move, name

        f, name = options[0]
        return get_move(f, name)
