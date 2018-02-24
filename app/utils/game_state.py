from vector import Vector, up, down, left, right
from snake import Snake


class GameState(object):

    def __init__(self, data):
        self.data = data
        self._empty_squares = None
        self._empty_squares_with_tails = None
        self._food = None
        self._snakes = None
        self._all_snakes = None
        self._me = None
        self._other_heads = None
        self._opponents = None

    def other_heads(self):
        if self._other_heads is None:
            heads = []
            for snake in self.data["snakes"]["data"]:
                head = snake["body"]["data"][0]
                heads.append(Vector(head["x"], head["y"]))
            self._other_heads = heads
        return self._other_heads

    def neighbouring_heads(self):
        neighbours = []
        for snake in self.opponents:
            if snake.head in self.me.head.neighbours():
                neighbours.append(snake.head)
        return neighbours

    def neighbouring_heads_next(self):
        next_heads = []
        for h in self.neighbouring_heads():
            for v in [up, down, left, right]:
                next_heads.append(h+v)
        return next_heads

    def empty_squares(self):

        if self._empty_squares is not None:
            return self._empty_squares

        width = self.data["width"]
        height = self.data["height"]
        empty_squares = {}
        for x in range(0, width):
            for y in range(0, height):
                empty_squares[(x, y)] = True

        for p in self.me.coords:
            v = (p.x, p.y)
            if v in empty_squares:
                del empty_squares[v]

        for snake in self.opponents:
            for p in snake.coords:
                v = (p.x, p.y)
                if v in empty_squares:
                    del empty_squares[v]

        self._empty_squares = empty_squares
        return empty_squares

    def empty_squares_with_tails(self):
        if self._empty_squares_with_tails is not None:
            return self._empty_squares_with_tails

        self._empty_squares_with_tails = self.empty_squares()
        for tail in self.all_tails:
            self._empty_squares_with_tails[(tail.x, tail.y)] = True

        return self._empty_squares_with_tails

    def first_empty_direction(self, start, options, default=up):
        for v in options:
            if self.is_empty(start + v):
                return v
        return default

    def is_empty(self, v, tails_are_empty=True):
        p = (v.x, v.y)
        if tails_are_empty:
            return p in self.empty_squares_with_tails()
        return p in self.empty_squares()

    @property
    def possible_kill_coords(self):
        kill_coords = []
        for snake in self.opponents:
            if snake.length < self.me.length:
                for my_neighbour in self.me.head.neighbours():
                    for their_neighbour in snake.head.neighbours():
                        if my_neighbour == their_neighbour:
                            kill_coords.append(my_neighbour)
        return kill_coords

    @property
    def possible_death_coords(self):
        death_coords = []
        for snake in self.opponents:
            if snake.length > self.me.length:
                for my_neighbour in self.me.head.neighbours:
                    for their_neighbour in snake.head.neighbours:
                        if my_neighbour == their_neighbour:
                            death_coords.append(my_neighbour)
        return death_coords

    @property
    def all_tails(self):
        all_tails = [self.me.tail]
        for s in self.opponents:
            all_tails.append(s.tail)
        return all_tails

    def best_paths_to(self, start, goals):
        reached_goals = []
        unreached_goals = goals
        visited = {}
        to_visit = [(start, 0)]
        while len(to_visit) > 0 and len(unreached_goals) > 0:
            p, dist = to_visit.pop()
            if p.key in visited:
                continue

            if not self.is_empty(p, tails_are_empty=False) and start.is_neighbour(p):
                continue
            visited[p.key] = dist

            if p in unreached_goals:
                path = self._path(p, start, visited)
                reached_goals.append((p, len(path), path))
                unreached_goals.remove(p)

            for n in p.neighbours():
                if self.is_empty(n):
                    to_visit.append((n, dist + 1))

        reached_goals = sorted(reached_goals, key=lambda tup: tup[1])
        return reached_goals

    def worst_path_to(self, start, goal):
        # pick furthest choice from goal
        # that can still visit the goal
        pass

    def _path(self, start, finish, visited):
        path = [start]
        current_position = start
        current_distance = visited[start.key]
        while not current_position == finish:
            for n in current_position.neighbours():
                d = visited.get(n.key)
                if d is not None and d < current_distance:
                    path.append(n)
                    current_position = n
                    current_distance = d
                    break
        path.reverse()
        return path

    @property
    def me(self):
        if self._me is None:
            self._me = Snake(self.data["you"])
        return self._me

    @property
    def all_snakes(self):
        if self._all_snakes is None:
            self._all_snakes = [Snake(d) for d in self.data["snakes"]["data"]]
        return self._all_snakes

    @property
    def opponents(self):
        if self._opponents is None:
            self._opponents = [s for s in self.all_snakes if s.id != self.me.id]
        return self._opponents

    @property
    def board_width(self):
        return self.data["width"]

    @property
    def board_height(self):
        return self.data["height"]

    @property
    def food(self):
        if self._food is None:
            self._food = [Vector(f["x"], f["y"]) for f in self.data["food"]["data"]]
        return self._food
