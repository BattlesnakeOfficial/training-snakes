from base_distances import BaseDistances
from utils.vector import directions


class OrthogonalDistances(BaseDistances):

    def closest_to(self, goals, start):
        if len(goals) == 0:
            return None

        def _dist(a, b):
            return abs((a-b).magnitude)
        goals.sort(key=lambda x: _dist(x, start), reverse=False)
        return goals[0]

    def directions_to(self, goal, gamestate):
        head = gamestate.me.head
        distances = [((goal-head-d).magnitude, d) for d in directions]
        distances.sort(key=lambda x: x[0], reverse=False)
        return [d[1] for d in distances]
