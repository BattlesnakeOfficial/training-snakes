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
    dists = gs.best_paths_to(Vector(0, 0), [Vector(0, 2)])
    assert dists == [(Vector(0, 2), 2,[Vector(0, 2), Vector(0, 1), Vector(0, 0)])]


def test_distance_to_multiple():
    gs = build_test_gamestate(1, 3)
    dists = gs.best_paths_to(Vector(0, 0), [Vector(0, 2), Vector(0, 1)])
    assert dists == [
        (Vector(0, 1), 1, [Vector(0, 1), Vector(0, 0)]),
        (Vector(0, 2), 2, [Vector(0, 2), Vector(0, 1), Vector(0, 0)]),
    ]

def test_

    {u'food': {u'data': [{u'object': u'point', u'x': 8, u'y': 0}],
               2018 - 02 - 24T01:17:34.132082 + 00:00
    app[web
    .1]:            u'object': u'list'},
    2018 - 02 - 24
    T01:17:34.132144 + 00:00
    app[web
    .1]:  u'height': 20,
                     2018 - 02 - 24
    T01:17:34.132204 + 00:00
    app[web
    .1]:  u'id': 2,
                 2018 - 02 - 24
    T01:17:34.132264 + 00:00
    app[web
    .1]:  u'object': u'world',
                     2018 - 02 - 24
    T01:17:34.134344 + 00:00
    app[web
    .1]:  u'snakes': {u'data': [{u'body': {u'data': [{u'object': u'point',
                                                      2018 - 02 - 24T01:17:34.134425 + 00:00
    app[web
    .1]:                                              u'x': 12,
                                                            2018 - 02 - 24
    T01:17:34.134516 + 00:00
    app[web
    .1]:                                              u'y': 16},
    2018 - 02 - 24
    T01:17:34.134762 + 00:00
    app[web
    .1]:                                             {u'object': u'point',
                                                      2018 - 02 - 24T01:17:34.134843 + 00:00
    app[web
    .1]:                                              u'x': 11,
                                                            2018 - 02 - 24
    T01:17:34.134931 + 00:00
    app[web
    .1]:                                              u'y': 16},
    2018 - 02 - 24
    T01:17:34.135163 + 00:00
    app[web
    .1]:                                             {u'object': u'point',
                                                      2018 - 02 - 24T01:17:34.135270 + 00:00
    app[web
    .1]:                                              u'x': 11,
                                                            2018 - 02 - 24
    T01:17:34.135387 + 00:00
    app[web
    .1]:                                              u'y': 16}],
    2018 - 02 - 24
    T01:17:34.135469 + 00:00
    app[web
    .1]:                                   u'object': u'list'},
    2018 - 02 - 24
    T01:17:34.139428 + 00:00
    app[web
    .1]:                         u'health': 99,
                                            2018 - 02 - 24
    T01:17:34.139510 + 00:00
    app[web
    .1]:                         u'id': u'e529d577-d595-45bd-b2b4-20ae7e85890b',
                                        2018 - 02 - 24
    T01:17:34.139588 + 00:00
    app[web
    .1]:                         u'length': 3,
                                            2018 - 02 - 24
    T01:17:34.139668 + 00:00
    app[web
    .1]:                         u'name': u'dsnek',
                                          2018 - 02 - 24
    T01:17:34.139746 + 00:00
    app[web
    .1]:                         u'object': u'snake',
                                            2018 - 02 - 24
    T01:17:34.139836 + 00:00
    app[web
    .1]:                         u'taunt': None},
    2018 - 02 - 24
    T01:17:34.140907 + 00:00
    app[web
    .1]:                        {u'body': {u'data': [{u'object': u'point',
                                                      2018 - 02 - 24T01:17:34.140986 + 00:00
    app[web
    .1]:                                              u'x': 14,
                                                            2018 - 02 - 24
    T01:17:34.141078 + 00:00
    app[web
    .1]:                                              u'y': 1},
    2018 - 02 - 24
    T01:17:34.141322 + 00:00
    app[web
    .1]:                                             {u'object': u'point',
                                                      2018 - 02 - 24T01:17:34.141406 + 00:00
    app[web
    .1]:                                              u'x': 14,
                                                            2018 - 02 - 24
    T01:17:34.141496 + 00:00
    app[web
    .1]:                                              u'y': 2},
    2018 - 02 - 24
    T01:17:34.141734 + 00:00
    app[web
    .1]:                                             {u'object': u'point',
                                                      2018 - 02 - 24T01:17:34.141815 + 00:00
    app[web
    .1]:                                              u'x': 14,
                                                            2018 - 02 - 24
    T01:17:34.141942 + 00:00
    app[web
    .1]:                                              u'y': 2}],
    2018 - 02 - 24
    T01:17:34.142047 + 00:00
    app[web
    .1]:                                   u'object': u'list'},
    2018 - 02 - 24
    T01:17:34.142126 + 00:00
    app[web
    .1]:                         u'health': 99,
                                            2018 - 02 - 24
    T01:17:34.142210 + 00:00
    app[web
    .1]:                         u'id': u'9b7e6063-6143-4630-99f1-3d97d8c1a9a5',
                                        2018 - 02 - 24
    T01:17:34.142284 + 00:00
    app[web
    .1]:                         u'length': 3,
                                            2018 - 02 - 24
    T01:17:34.142361 + 00:00
    app[web
    .1]:                         u'name': u'8',
                                          2018 - 02 - 24
    T01:17:34.142430 + 00:00
    app[web
    .1]:                         u'object': u'snake',
                                            2018 - 02 - 24
    T01:17:34.142558 + 00:00
    app[web
    .1]:                         u'taunt': None}],
    2018 - 02 - 24
    T01:17:34.142658 + 00:00
    app[web
    .1]:              u'object': u'list'},
    2018 - 02 - 24
    T01:17:34.142732 + 00:00
    app[web
    .1]:  u'turn': 1,
                   2018 - 02 - 24
    T01:17:34.142808 + 00:00
    app[web
    .1]:  u'width': 20,
                    2018 - 02 - 24
    T01:17:34.147577 + 00:00
    app[web
    .1]:  u'you': {u'body': {u'data': [{u'object': u'point', u'x': 14, u'y': 1},
                                       2018 - 02 - 24T01:17:34.147984 + 00:00
    app[web
    .1]:                               {u'object': u'point', u'x': 14, u'y': 2},
                                       2018 - 02 - 24
    T01:17:34.148419 + 00:00
    app[web
    .1]:                               {u'object': u'point', u'x': 14, u'y': 2}],
    2018 - 02 - 24
    T01:17:34.148526 + 00:00
    app[web
    .1]:                     u'object': u'list'},
    2018 - 02 - 24
    T01:17:34.148599 + 00:00
    app[web
    .1]:           u'health': 99,
                              2018 - 02 - 24
    T01:17:34.148677 + 00:00
    app[web
    .1]:           u'id': u'9b7e6063-6143-4630-99f1-3d97d8c1a9a5',
                          2018 - 02 - 24
    T01:17:34.148748 + 00:00
    app[web
    .1]:           u'length': 3,
                              2018 - 02 - 24
    T01:17:34.148824 + 00:00
    app[web
    .1]:           u'name': u'8',
                            2018 - 02 - 24
    T01:17:34.148896 + 00:00
    app[web
    .1]:           u'object': u'snake',
                              2018 - 02 - 24
    T01:17:34.149017 + 00:00
    app[web
    .1]:           u'taunt': None}}