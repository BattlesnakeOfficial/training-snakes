import random
from base_snake import BaseSnake
from snake_3 import Snake3
from snake_5 import Snake5


class Snake7(BaseSnake):

    THRESHOLD = 30

    def move(self, gamestate):

        if len(gamestate.possible_kill_coords) > 0:
            goal = random.choice(gamestate.possible_kill_coords)
            return goal - gamestate.me.head

        if gamestate.me.health > self.THRESHOLD:
            return Snake3().move(gamestate)
        return Snake5().move(gamestate)


    def name(self):
        return "Training Snake 7"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
