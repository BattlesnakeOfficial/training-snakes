import random


class Kill(object):

    def possible_kill(self, gamestate):
        if len(gamestate.possible_kill_coords) > 0:
            goal = random.choice(gamestate.possible_kill_coords)
            return goal - gamestate.me.head

