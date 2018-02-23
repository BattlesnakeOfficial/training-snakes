import random
from base_snake import BaseSnake
from snake_6 import SimpleSometimesHungrySnake


class AttemptKillsSnake(BaseSnake):

    THRESHOLD = 30

    def move(self, gamestate):

        if len(gamestate.possible_kill_coords) > 0:
            goal = random.choice(gamestate.possible_kill_coords)
            return goal - gamestate.me.head

        return SimpleSometimesHungrySnake().move(gamestate)


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
