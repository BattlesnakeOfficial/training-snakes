
class ChaiseTail(object):

    def chase_tail(self, gs):
        allow_length_1 = gs.turn >= 5

        visitable_tails = gs.best_paths_to(gs.me.head, gs.safe_tails, allow_length_1)
        if len(visitable_tails) > 0:
            closest_goal = visitable_tails[0]
            (goal, distance_from_start, path) = closest_goal
            m = path[1] - gs.me.head
            return m

