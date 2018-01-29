import pprint
import bottle
import json


@bottle.get('/')
def index():
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@bottle.post('/start')
def start():
    data = bottle.request.json
    pprint.pprint(data)

    return json.dumps({
        'name': 'battlesnake-python',
        'color': '#00ff00',
        'head_url': 'http://battlesnake-python.herokuapp.com',
        'taunt': 'battlesnake-python!'
    })


def _list_empty_squares(data):
    width = data["width"]
    height = data["height"]
    empty_squares = {}
    for x in range(0, width):
        for y in range(0, height):
            empty_squares[(x, y)] = True

    for snake in data["snakes"]["data"]:
        segments = snake["body"]["data"]
        for segment in segments:
            x = segment["x"]
            y = segment["y"]
            del empty_squares[(x, y)]

    pprint.pprint(empty_squares)

    return empty_squares


def _vector_to_direction(v):
    return {
        (0, -1): "up",
        (0, 1): "down",
        (1, 0): "right",
        (-1, 0): "left",
    }[v]


def _sub_vector(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1])


def _add_vector(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])


def _my_head(data):
    segments = data["you"]["body"]["data"]
    p = segments[0]
    head = (p["x"], p["y"])
    return head


def _my_neck(data):
    segments = data["you"]["body"]["data"]
    p = segments[1]
    head = (p["x"], p["y"])
    return head


def current_direction(data):
    return _sub_vector(_my_head(data), _my_neck(data))


@bottle.post('/move')
def move():
    data = bottle.request.json
    current_vector = current_direction(data)
    if current_vector == (0,0):
        return "up"

    head = _my_head(data)
    empty_squares = _list_empty_squares(data)
    pprint.pprint(
        [current_vector, (0, 1), (0, -1), (1, 0), (-1, 0)]
    )
    for v in [current_vector, (0,1), (0,-1), (1,0), (-1,0)]:
        next_pos = _add_vector(head, v)
        print next_pos
        if next_pos in empty_squares:
            if next_pos in empty_squares:
                response = {"move": _vector_to_direction(v)}
                pprint.pprint(response)
                return json.dumps(response)


@bottle.post('/end')
def end():
    data = bottle.request.json
    pprint.pprint(data)
    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()

if __name__ == "__main__":
    bottle.run(host='0.0.0.0', port=8080, debug=True)
