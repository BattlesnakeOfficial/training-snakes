
class BaseDistances(object):

    def closest_to(self, start, goals, gamestate):
        raise NotImplementedError()

    def directions_to(self, goal, gamestate):
        raise NotImplementedError()
