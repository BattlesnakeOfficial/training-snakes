from vector import Vector, up, down, left, right
from snake import Snake

class GameState(object):

    def __init__(self, data):
        self.data = data
        self._empty_squares = None
        self._food = None
        self._snakes = None
        self._me = None

    def other_heads(self):
        heads = []
        for snake in self.data["snakes"]["data"]:
            head = snake["body"]["data"][0]
            heads.append(Vector(head["x"], head["y"]))
        return heads

    def neighbouring_heads(self):
        neighbours = []
        for snake in self.snakes:
            if snake.head in self.me.head.neighbours():
                neighbours.append(snake.head)
        return neighbours

    def neighbouring_heads_next(self):
        next_heads = []
        for h in self.neighbouring_heads():
            for v in [up, down, left, right]:
                next_heads.append(h+v)
        return next_heads

    def empty_squares(self):

        if self._empty_squares is not None:
            return self._empty_squares

        width = self.data["width"]
        height = self.data["height"]
        empty_squares = {}
        for x in range(0, width):
            for y in range(0, height):
                empty_squares[(x, y)] = True

        empty_squares = self._remove_solid_squares(empty_squares)
        self._empty_squares = empty_squares
        return empty_squares

    def _remove_solid_squares(self, empty_squares):
        for snake in self.data["snakes"]["data"]:
            segments = snake["body"]["data"]
            for segment in segments:
                x = segment["x"]
                y = segment["y"]
                v = (x, y)
                if v in empty_squares:
                    del empty_squares[v]
        return empty_squares

    def first_empty_direction(self, start, options, default=up):
        for v in options:
            if self.is_empty(start + v):
                return v
        return default

    def is_empty(self, v):
        return (v.x, v.y) in self.empty_squares()

    @property
    def me(self):
        if self._me is None:
            self._me = Snake(self.data["you"])
        return self._me

    @property
    def snakes(self):
        if self._snakes is None:
            self._snakes = [Snake(d) for d in self.data["snakes"]]
        return self._snakes

    @property
    def board_width(self):
        return self.data["width"]

    @property
    def board_height(self):
        return self.data["height"]

    @property
    def food(self):
        if self._food is None:
            self._food = [Vector(f["x"], f["y"]) for f in self.data["food"]["data"]]
        return self._food
