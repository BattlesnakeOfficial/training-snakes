from app.utils.game_state import GameState
from app.utils.vector import Vector


def build_test_gamestate(width=3, height=3, me=[(0,0)], opponents=[], food=[(2,2)]):

    def _tuples_to_snake(tuples):
        return {
        "body": {
          "data": [
            {
              "object": "point",
              "x": 13,
              "y": 19
            },
            {
              "object": "point",
              "x": 13,
              "y": 19
            },
            {
              "object": "point",
              "x": 13,
              "y": 19
            }
          ],
          "object": "list"
        },
        "health": 100,
        "id": "58a0142f-4cd7-4d35-9b17-815ec8ff8e70",
        "length": 3,
        "name": "Sonic Snake",
        "object": "snake",
        "taunt": "Gotta go fast"
      }

    def _tuples_to_coords(tuples):
        return [{
            "object": "point",
            "x": t[0],
            "y": t[1]
        } for t in tuples]

    data = {
      "food": {
        "data": _tuples_to_coords(food),
        "object": "list"
      },
      "height": height,
      "id": 1,
      "object": "world",
      "snakes": {
        "data": [_tuples_to_snake(coords) for coords in opponents],
        "object": "list"
      },
      "turn": 0,
      "width": width,
      "you": _tuples_to_snake(me)
    }
    gs = GameState(data)
    return gs


def test_distance_to():
    gs = build_test_gamestate(1, 3)
    dists = gs.distance_to(Vector(0, 0), [Vector(0, 2)])
    assert dists == [(Vector(0, 2), 2)]


def test_distance_to_multiple():
    gs = build_test_gamestate(1, 3)
    dists = gs.distance_to(Vector(0, 0), [Vector(0, 2), Vector(0, 1)])
    assert dists == [(Vector(0, 1), 1), (Vector(0, 2), 2)]