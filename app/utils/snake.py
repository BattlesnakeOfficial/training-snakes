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
        except Exception as e:
            print e
            pprint.pprint(self.data)

    @property
    def head(self):
        try:
            return self.coords[0]
        except Exception as e:
            print e
            pprint.pprint(self.data)

    @property
    def neck(self):
        try:
            return self.coords[1]
        except Exception as e:
            print e
            pprint.pprint(self.data)

    @property
    def tail(self):
        try:
            return self.coords[len(self.coords)-1]
        except Exception as e:
            print e
            pprint.pprint(self.data)

    @property
    def current_direction(self):
        try:
            return self.head - self.neck
        except Exception as e:
            print e
            pprint.pprint(self.data)

    @property
    def length(self):
        try:
            return self.data["length"]
        except Exception as e:
            print e
            pprint.pprint(self.data)

    @property
    def health(self):
        try:
            return self.data["health"]
        except Exception as e:
            print e
            pprint.pprint(self.data)

    @property
    def id(self):
        try:
            return self.data["id"]
        except Exception as e:
            print e
            pprint.pprint(self.data)

    @property
    def name(self):
        try:
            return self.data["name"]
        except Exception as e:
            print e
            pprint.pprint(self.data)

    @property
    def taunt(self):
        try:
            taunt = self.data["taunt"]
            return taunt if taunt is not None else ""
        except Exception as e:
            print e
            pprint.pprint(self.data)