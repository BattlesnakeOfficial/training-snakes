

class Eat(object):
    HUNGER_THRESHOLD = 30

    def is_hungry(self, gamestate):
        return gamestate.me.health < self.HUNGER_THRESHOLD

    def eat(self, gs):
        if self.is_hungry(gs):
            closest_food = self.closest_to(gs.me.head, gs.food, gs)
            if closest_food is None:
                return None

            return gs.first_empty_direction(
                gs.me.head,
                self.directions_to(closest_food, gs),
                None
            )
