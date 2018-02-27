from utils.test import build_test_gamestate
from logic import Eat, PathDistances
from snakes.base_snake import BaseSnake


def test_eat_closest():
    class EatingSnake(BaseSnake, Eat, PathDistances):
        pass

    gs = build_test_gamestate(3,3, me=[(1, 1), (2, 1)], food=[(0, 0), (1, 2)])
    move = EatingSnake().move(gs)
    assert move == "up"
