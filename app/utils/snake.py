from vector import Vector


class Snake(object):

    def __init__(self, data):
        self.data = data
        self._coords = None

    @property
    def coords(self):
        if self._coords is None:
            points = self.data["body"]["data"]
            self._coords = [Vector(p["x"], p["y"]) for p in points]
        return self._coords

    @property
    def head(self):
        return self.coords[0]

    @property
    def neck(self):
        return self.coords[1]

    @property
    def tail(self):
        return self.coords[self.length-1]

    @property
    def current_direction(self):
        return self.head - self.neck

    @property
    def length(self):
        return self.data["length"]

    @property
    def health(self):
        return self.data["health"]

    @property
    def id(self):
        return self.data["id"]

    @property
    def name(self):
        return self.data["name"]

    @property
    def taunt(self):
        taunt = self.data["taunt"]
        return taunt if taunt is not None else ""
