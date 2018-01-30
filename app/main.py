import flask
import json
from utils.game_state import GameState
from snakes import get_snake

app = flask.Flask(__name__)


@app.route('/')
def index():
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@app.route('/start', methods=['GET', 'POST'])
def start():
    snake = get_snake()

    return json.dumps({
        'name': snake.name(),
        'color': snake.color(),
        'head_url': snake.head_url(),
        'taunt': snake.taunt()
    })


@app.route('/move', methods=['GET', 'POST'])
def move():
    snake = get_snake()
    data = flask.request.json
    gamestate = GameState(data)
    move = snake.move(gamestate)

    return json.dumps({
        "move": move.direction()
    })


@app.route('/end', methods=['GET', 'POST'])
def end():
    snake = get_snake()
    snake.end()

    return json.dumps({})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
