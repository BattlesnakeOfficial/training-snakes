
class BaseDistances(object):

    def closest_to(self, goals, start):
        raise NotImplementedError()

    def directions_to(self, goal, gamestate):
        raise NotImplementedError()
