import heapq


class InvalidPathException(Exception):
    pass


# A* algorithm taken from http://www.redblobgames.com/pathfinding/a-star/implementation.html
class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def add_wall(self, wall):
        self.walls.append(wall)

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def neighbor_walls(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(lambda id: not self.passable(id), results)
        return results


class GridWithWeights(SquareGrid):

    def __init__(self, width, height):
        SquareGrid.__init__(self, width, height)
        self.weights = {}

    def add_weight(self, node, weight):
        self.weights[node] = weight

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def breadth_first_search(graph, start, max_search=100):
    frontier = PriorityQueue()
    frontier.put(start, 1)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next, 1)
                visited[next] = True
        if len(visited) > max_search:
            return len(visited)
    return len(visited)


def wall_breadth_first_search(graph, start):
    frontier = PriorityQueue()
    visited = {}
    neighbors = graph.neighbors(start)
    for next in neighbors:
        frontier.put(next, 1)
        visited[next] = True
    visited[start] = True
    walls = {}

    while not frontier.empty():
        current = frontier.get()
        neighbors = graph.neighbors(current)
        for wall in graph.neighbor_walls(current):
            walls[wall] = current
        for next in neighbors:
            if next not in visited:
                frontier.put(next, 1)
                visited[next] = True
    return walls


def calculate_path_cost(graph, start, goal):
    paths, costs = a_star_search(graph, start, goal)
    if goal not in costs:
        raise InvalidPathException("Could not find a path from {start} to {goal}".format(start=start, goal=goal))
    return costs.get(goal)


def calculate_direction(graph, start, goal):
    paths, costs = a_star_search(graph, start, goal)
    if goal not in paths:
        raise InvalidPathException("Could not find a path from {start} to {goal}".format(start=start, goal=goal))
    node = goal
    previous_node = None
    while node != start:
        previous_node = node
        node = paths.get(node)
    if not previous_node:
        raise InvalidPathException("Could not find a path from {start} to {goal}".format(start=start, goal=goal))
    x_diff = previous_node[0] - start[0]
    y_diff = previous_node[1] - start[1]
    print("next node: {0}".format(previous_node))
    if x_diff > 0:
        return "right"
    elif x_diff < 0:
        return "left"
    elif y_diff < 0:
        return "up"
    elif y_diff > 0:
        return "down"
    else:
        raise InvalidPathException("Could not find a path from {start} to {goal}".format(start=start, goal=goal))


def calculate_worst_path_direction(graph, start, goal):
    x_delta = start[0] - goal[0]
    y_delta = start[1] - goal[1]
    neighbors = list(graph.neighbors(start))
    dir_map = {
        (start[0]+1, start[1]): "right",
        (start[0], start[1]+1): "down",
        (start[0]-1, start[1]): "left",
        (start[0], start[1]-1): "up"
    }
    if len(neighbors) < 2:
        return dir_map.get(neighbors[0])

    safe_dirs = []
    for neighbor in neighbors:
        try:
            cost = calculate_path_cost(graph, neighbor, goal)
        except InvalidPathException:
            continue
        safe_dirs.append(dir_map.get(neighbor))

    if len(safe_dirs) < 2:
        return safe_dirs[0]

    if abs(y_delta) > abs(x_delta):
        if y_delta < 0:
            if x_delta < 0:
                dir_order = ["up", "left", "right", "down"]
            else:
                dir_order = ["up", "right", "left", "down"]
        else:
            if x_delta < 0:
                dir_order = ["down", "left", "right", "up"]
            else:
                dir_order = ["down","right", "left", "up"]
    else:
        if x_delta < 0:
            if y_delta < 0:
                dir_order = ["left", "up", "down", "right"]
            else:
                dir_order = ["left", "down", "up", "right"]
        else:
            if y_delta < 0:
                dir_order = ["right", "up", "down", "left"]
            else:
                dir_order = ["right", "down", "up", "left"]
    for dir in dir_order:
        if dir in safe_dirs:
            return dir
    print("shouldn't be possible to get to the final return statement in calculate worst path")
    return safe_dirs[0]