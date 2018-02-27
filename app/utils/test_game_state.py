from app.utils.vector import Vector as V
from test import build_test_gamestate


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