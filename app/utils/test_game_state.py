from app.utils.game_state import GameState
from app.utils.vector import Vector
import json


def build_test_gamestate(width=3, height=3, me=[(0,0)], opponents=[], food=[]):

    def _tuples_to_snake(tuples):
        return {
        "body": {
          "data": _tuples_to_coords(tuples),
          "object": "list"
        },
        "health": 100,
        "id": "58a0142f-4cd7-4d35-9b17-815ec8ff8e70",
        "length": len(tuples),
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


def test_empty():
    gs = build_test_gamestate(1, 2, me=[(0, 1), (0, 0)])
    assert gs.is_empty(Vector(0, 0), tails_are_empty=False) == False
    assert gs.is_empty(Vector(0, 1), tails_are_empty=False) == False
    assert gs.is_empty(Vector(0, 0), tails_are_empty=True) == True
    assert gs.is_empty(Vector(0, 1), tails_are_empty=True) == False


def test_distance_to():
    gs1 = build_test_gamestate(1, 3)
    dists1 = gs1.best_paths_to(Vector(0, 0), [Vector(0, 2)])
    expected1 = [
        (Vector(0, 2),
         3,
         [Vector(0, 0), Vector(0, 1), Vector(0, 2)]
         )
    ]
    assert dists1 == expected1


def test_distance_to_multiple():
    gs = build_test_gamestate(1, 3)
    dists = gs.best_paths_to(Vector(0, 0), [Vector(0, 2), Vector(0, 1)])
    assert dists == [
        (Vector(0, 1), 2, [Vector(0, 0), Vector(0, 1)]),
        (Vector(0, 2), 3, [Vector(0, 0), Vector(0, 1), Vector(0, 2)]),
    ]


def test_distance_to_turn_around():
    gs1 = build_test_gamestate(3, 3, [(2, 1), (2, 0)])
    dists1 = gs1.best_paths_to(Vector(2, 1), [Vector(2, 0)])
    expected1 = [
        (Vector(2, 0), 2, [Vector(2, 1), Vector(2, 0)])
    ]
    assert dists1 == expected1