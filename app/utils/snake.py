from vector import Vector
import pprint


class Snake(object):
    EXAMPLE_DATA = {
        u'body': {u'data': [{u'object': u'point',
                          u'x': 13,
                          u'y': 7},
                         {u'object': u'point',
                          u'x': 13,
                          u'y': 8},
                         {u'object': u'point',
                          u'x': 13,
                          u'y': 9}],
               u'object': u'list'},
     u'health': 97,
     u'id': u'8fa5374a-c355-47d3-a6a2-795c65137d75',
     u'length': 3,
     u'name': u'1',
     u'object': u'snake',
     u'taunt': None}

    def __init__(self, data):
        self.data = data
        self._coords = None

    @property
    def coords(self):
        try:
            if self._coords is None:
                points = self.data["body"]["data"]
                self._coords = [Vector(p["x"], p["y"]) for p in points]
            return self._coords
        except:
            pprint.pprint(self.data)

    @property
    def head(self):
        return self.coords[0]

    @property
    def neck(self):
        return self.coords[1]

    @property
    def tail(self):
        return self.coords[len(self.coords)-1]

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
