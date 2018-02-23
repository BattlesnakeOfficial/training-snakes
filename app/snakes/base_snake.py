from utils.game_state import GameState


class BaseSnake(object):

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
