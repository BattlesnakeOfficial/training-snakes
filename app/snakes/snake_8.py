from base_snake import BaseSnake
from utils.vector import up, down, left, right


class TailChaser(BaseSnake):

    def move(self, gamestate):
        options = [
            (self.orthogonal_eat, "simple eat"),
            (self.possible_kill, "possible kill"),
            (self.chase_tail, "tail"),
            (lambda gs: up, "up"),
            (lambda gs: down, "down"),
            (lambda gs: left, "left"),
            (lambda gs: right, "right"),
        ]

        for f, taunt in options:
            desired_move = f(gamestate)
            if not self.bad_move(desired_move, taunt, gamestate):
                print "good: %s, %s" % (desired_move, taunt)
                return desired_move, taunt

        print "dead"
        return "dead"

    def bad_move(self, move, desc, gs):
        if move is None:
            print "bad: is None, %s" % desc
            return True
        coord = gs.me.head + move
        if not gs.is_empty(coord):
            print "bad: is solid, %s" % desc
            return True
        if coord in gs.possible_death_coords:
            print "bad: could be eaten, %s" % desc
            return True
        return False

    def name(self):
        return "Training Snake 8"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
