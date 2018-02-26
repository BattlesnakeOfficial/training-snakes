from app.utils.game_state import GameState
from app.utils.vector import Vector as V


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
    assert gs.is_empty(V(0, 0)) == False
    assert gs.is_empty(V(0, 1)) == False


def test_distance_to():
    gs1 = build_test_gamestate(1, 3)
    dists1 = gs1.best_paths_to(V(0, 0), [V(0, 2)])
    expected1 = [
        (V(0, 2),
         3,
         [V(0, 0), V(0, 1), V(0, 2)]
         )
    ]
    print dists1
    assert dists1 == expected1


def test_distance_to_multiple():
    gs = build_test_gamestate(1, 3)
    dists = gs.best_paths_to(V(0, 0), [V(0, 2), V(0, 1)], True)
    assert dists == [
        (V(0, 1), 2, [V(0, 0), V(0, 1)]),
        (V(0, 2), 3, [V(0, 0), V(0, 1), V(0, 2)]),
    ]

def test_safe_tails():
    gs = build_test_gamestate(1, 2, me=[(0, 1), (0, 0), (0, 0)], opponents=[[(2, 1), (2, 0)], [(3, 1), (3, 0), (3, 0)]])
    assert gs.safe_tails == [V(2, 0)]


def test_distance_to_turn_around():
    head = (2, 1)
    headV = V(2, 1)
    tail = (2, 0)
    tailV = V(2, 0)
    gs1 = build_test_gamestate(3, 3, [head, tail])
    dists1 = gs1.best_paths_to(headV, [tailV])
    expected1 = [
        (tailV, 4, [headV, V(1, 1), V(1, 0), tailV])
    ]
    assert dists1 == expected1