import random
from utils.game_state import GameState


class BaseSnake(object):

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

