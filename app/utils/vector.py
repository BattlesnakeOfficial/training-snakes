
class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def direction(self):
        return {
            (0, -1): "up",
            (0, 1): "down",
            (1, 0): "right",
            (-1, 0): "left",
        }[(self.x, self.y)]

    def __str__(self):
        return self.direction()

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __eq__(self, other):
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        return True


up = Vector(0, -1)
down = Vector(0, 1)
right = Vector(1, 0)
left = Vector(-1, 0)
