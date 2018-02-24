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
                empty_squares[Vector(x, y).key] = True

        for p in self.me.coords:
            if p.key in empty_squares:
                del empty_squares[p.key]

        for snake in self.opponents:
            for p in snake.coords:
                if p.key in empty_squares:
                    del empty_squares[p.key]

        self._empty_squares = empty_squares
        return empty_squares

    def first_empty_direction(self, start, options, default=up):
        for v in options:
            if self.is_empty(start + v):
                return v
        return default

    def is_empty(self, v):
        return v.key in self.empty_squares()

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
                for my_neighbour in self.me.head.neighbours():
                    for their_neighbour in snake.head.neighbours():
                        if my_neighbour == their_neighbour:
                            death_coords.append(my_neighbour)
        return death_coords

    @property
    def all_tails(self):
        all_tails = [self.me.tail]
        for s in self.opponents:
            all_tails.append(s.tail)
        return all_tails

    def travel_times(self, start):
        shortest_travel_times = {start.key: 0}

        to_visit = [(start, 0)]
        while len(to_visit) > 0:
            (curr, turns) = to_visit.pop(0)
            for next in curr.neighbours():
                if self.is_empty(next) and next.key not in shortest_travel_times:
                    shortest_travel_times[next.key] = turns+1
                    to_visit.append((next, turns+1))
        return shortest_travel_times

    def best_paths_to(self, start, goals, allow_length_1=False):
        travel_times = self.travel_times(start)

        best_paths = []
        for goal in goals:
            path = self._path(start, goal, travel_times, allow_length_1)
            if path:
                best_paths.append((goal, len(path), path))

        best_paths = sorted(best_paths, key=lambda tup: tup[1])
        return best_paths

    def _path(self, start, finish, travel_times, allow_length_1):
        if start == finish:
            return []

        starting_distances = []
        for n in finish.neighbours():
            if not allow_length_1 and n == start:
                continue
            if n.key in travel_times:
                starting_distances.append((n, travel_times[n.key]))

        if len(starting_distances) == 0:
            return
        starting_distances = sorted(starting_distances, key=lambda tup: tup[1])
        closest_start, closest_dist = starting_distances[0]

        path = [finish, closest_start]
        curr = closest_start
        dist = closest_dist
        i = 0
        while curr != start:
            i += 1
            if dist == 1:
                break
            for n in curr.neighbours():
                next_dist = travel_times.get(n.key, dist)
                if next_dist < dist:
                    path.append(n)
                    curr = n
                    dist = next_dist
                    break
        path.reverse()
        return path


    def worst_path_to(self, start, goal):
        # pick furthest choice from goal
        # that can still visit the goal
        pass

    def on_board(self, v):
        if v.x < 0:
            return False
        if v.x >= self.board_width:
            return False
        if v.y < 0:
            return False
        if v.y >= self.board_height:
            return False
        return True

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
    def turn(self):
        return self.data["turn"]

    @property
    def food(self):
        if self._food is None:
            self._food = [Vector(f["x"], f["y"]) for f in self.data["food"]["data"]]
        return self._food
