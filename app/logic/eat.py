

class Eat(object):
    HUNGER_THRESHOLD = 30

    def is_hungry(self, gamestate):
        return gamestate.me.health < self.HUNGER_THRESHOLD

    def eat(self, gamestate):
        if self.is_hungry(gamestate):
            closest_food = self.closest_to(gamestate.food, gamestate.me.head)
            if closest_food is None:
                return None

            return gamestate.first_empty_direction(
                gamestate.me.head,
                self.directions_to(closest_food, gamestate),
                None
            )
