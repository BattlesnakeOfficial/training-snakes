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
            if not self.bad_move(desired_move, gamestate):
                return desired_move, taunt

        return down

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
