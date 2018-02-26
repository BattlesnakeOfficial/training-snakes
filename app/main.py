import flask
import json
from snakes import get_snake

app = flask.Flask(__name__)


@app.route('/<snake_name>/')
def index(snake_name):
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@app.route('/<snake_name>/start', methods=['GET', 'POST'])
def start(snake_name):
    snake = get_snake(snake_name)

    return json.dumps({
        'name': snake.name(),
        'color': snake.color(),
        'head_url': "https://www.placecage.com/50/50",
        'taunt': "hello"
    })


@app.route('/<snake_name>/move', methods=['GET', 'POST'])
def move(snake_name):
    snake = get_snake(snake_name)
    data = flask.request.json
    gamestate = snake.payload_to_game_state(data)
    move = snake.move(gamestate)
    if move is None:
        return json.dumps({"move": "up", 'taunt': "hello"})

    if type(move) is tuple:
        move, taunt = move
        return json.dumps({
            "move": move.direction(),
            "taunt": taunt
        })

    return json.dumps({
        'taunt': "hello",
        "move": move.direction()
    })


@app.route('/<snake_name>/end', methods=['GET', 'POST'])
def end(snake_name):
    snake = get_snake(snake_name)
    snake.end()
    return json.dumps({})


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    except Exception as e:
        raise e
