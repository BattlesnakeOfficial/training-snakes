from vector import Vector, up, down, left, right


class GameState(object):

    def __init__(self, data):
        self.data = data
        self._empty_squares = None
        self._food = None

    def other_heads(self):
        heads = []
        for snake in self.data["snakes"]["data"]:
            head = snake["body"]["data"][0]
            heads.append(Vector(head["x"], head["y"]))
        return heads

    def neighbouring_heads(self):
        neighbouring_squares = [
            self.my_head+up,
            self.my_head +down,
            self.my_head +left,
            self.my_head +right,
        ]

        neighbours = []
        for other_head in self.other_heads():
            if other_head in neighbouring_squares:
                neighbours.append(other_head)
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

        for snake in self.data["snakes"]["data"]:
            segments = snake["body"]["data"]
            for segment in segments:
                x = segment["x"]
                y = segment["y"]
                v = (x, y)
                if v in empty_squares:
                    del empty_squares[v]

        self._empty_squares = empty_squares
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
        return self.data["you"]

    @property
    def snakes(self):
        return self.data["snakes"]

    @property
    def my_head(self):
        segments = self.data["you"]["body"]["data"]
        p = segments[0]
        return Vector(p["x"], p["y"])

    @property
    def my_neck(self):
        segments = self.data["you"]["body"]["data"]
        p = segments[1]
        return Vector(p["x"], p["y"])

    @property
    def current_direction(self):
        return self.my_head - self.my_neck

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
