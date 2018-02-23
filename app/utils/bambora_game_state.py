from utils.game_state import GameState as BaseGameState
from utils.vector import up, down, left, right


class GameState(BaseGameState):

    def _remove_solid_squares(self, empty_squares):
        for snake in self.snakes:
            if snake.length >= self.me.length and snake.id != self.me.id:
                for d in [up, down, left, right]:
                    p = snake.head+d
                    if p in self.food:
                        del empty_squares[p]
        return empty_squares
