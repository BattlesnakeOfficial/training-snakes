from base_snake import BaseSnake
from utils.bambora_game_state import GameState
from snakes.bambora.pathfinding import GridWithWeights, calculate_worst_path_direction, wall_breadth_first_search, calculate_path_cost, InvalidPathException, calculate_direction, breadth_first_search


class Snake10(BaseSnake):

    def payload_to_game_state(self, payload):
        return GameState(payload)

    def move(self, gs):
        grid = build_grid(gs.snakes, gs.me, gs.width, gs.height)

        direction = find_best_path(grid, gs.food, gs.snakes, gs.me)
        if direction:
            return direction

        direction = find_best_path(grid, gs.food, gs.snakes, gs.me)
        if direction:
            return direction

        return "left"

    def name(self):
        return "Training Snake 10"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass


def build_grid(snakes, my_snake, width, height):
    grid = GridWithWeights(width, height)
    for i in range(width):
        grid.add_weight((i, height-1), 2)
        grid.add_weight((i, 0), 2)
    for i in range(height):
        grid.add_weight((width-1, i), 2)
        grid.add_weight((0, i), 2)
    for snake in snakes:
        for wall in snake.coords:
            grid.add_wall(tuple(wall))
            if snake == my_snake:
                continue
            grid.add_weight((wall[0]+1, wall[1]), 2)
            grid.add_weight((wall[0]-1, wall[1]), 2)
            grid.add_weight((wall[0], wall[1]+1), 2)
            grid.add_weight((wall[0], wall[1]-1), 2)
            grid.add_weight((wall[0]+2, wall[1]), 2)
            grid.add_weight((wall[0]+1, wall[1]+1), 2)
            grid.add_weight((wall[0], wall[1]+2), 2)
            grid.add_weight((wall[0]+1, wall[1]-1), 2)
            grid.add_weight((wall[0], wall[1]-2), 2)
            grid.add_weight((wall[0]-1, wall[1]-1), 2)
            grid.add_weight((wall[0]-2, wall[1]), 2)
            grid.add_weight((wall[0]-1, wall[1]+1), 2)
        if snake.id != my_snake.id and snake.length >= my_snake.length:
            for p in snake.head.neighbours:
                grid.add_weight((p.x, p.y), 1000)
    return grid


def find_best_path(grid, foods, snakes, my_snake):
    possible_paths = []
    head = tuple(my_snake.get('coords')[0])
    print("snake head: {0}".format(my_snake.get('coords')[0]))
    for food in foods:
        try:
            cost = calculate_path_cost(grid, head, tuple(food))
        except InvalidPathException:
            continue
        possible_paths.append((cost, food))
    if not possible_paths:
        direction = conserve_space(grid, head, snakes)
        print("goal: conserve space")
    else:
        possible_paths.sort(key=lambda path: path[0])

        safe_paths = []
        safe_dirs = {}
        for path in possible_paths:
            goal = tuple(path[1])
            direction = calculate_direction(grid, head, goal)
            if direction == "left":
                new_head = (head[0] - 1, head[1])
            elif direction == "right":
                new_head = (head[0] + 1, head[1])
            elif direction == "up":
                new_head = (head[0], head[1] - 1)
            else:
                new_head = (head[0], head[1] + 1)
            if direction in safe_dirs.values() or breadth_first_search(grid, new_head,
                                                                       len(my_snake.get('coords'))) >= len(
                    my_snake.get('coords')):
                safe_paths.append(path)
                safe_dirs[tuple(path[1])] = direction
        if not safe_paths:
            direction = conserve_space(grid, head, snakes)
            print("goal: conserve space")
        else:
            print("goal: {0}".format(goal))
            if len(safe_dirs.values()) == 1:
                print("dir: {0}".format(direction))
                return list(safe_dirs.values())[0]
            else:
                for safe_path in safe_paths:
                    goal = tuple(safe_path[1])
                    closest_to_food = True
                    for snake in snakes:
                        if snake == my_snake:
                            continue
                        try:
                            cost = calculate_path_cost(grid, tuple(snake.get('coords')[0]), goal)
                            if cost < safe_path[0]:
                                closest_to_food = False
                                break
                            if cost == safe_path[0] and len(snake.get('coords')) >= len(my_snake.get('coords')):
                                closest_to_food = False
                                break

                        except InvalidPathException:
                            continue
                    if closest_to_food:
                        print("dir: {0}".format(direction))
                        return safe_dirs.get(tuple(safe_path[1]))
                print("dir: {0}".format(direction))
                return safe_dirs.get(tuple(safe_paths[0][1]))

    print("dir: {0}".format(direction))
    return direction


def find_best_wall(grid, head, snakes):
    walls = wall_breadth_first_search(grid, head)
    if len(walls) == 0:
        print("no walls seen? probably no possible moves")
        return None
    best_wall = None
    best_cost = 100000
    for wall in walls.keys():
        for snake in snakes:
            pos = position_in_snake(wall, snake)
            if pos > -1:
                cost = len(snake.get('coords', [])) - pos
                if cost < best_cost:
                    best_cost = cost
                    best_wall = wall
                break
    if not best_wall:
        return None #TODO handle this case
    return walls.get(best_wall)


def position_in_snake(point, snake):
    pos = 0
    for coord in snake.get('coords', []):
        if coord[0] == point[0] and coord[1] == point[1]:
            return pos
        pos += 1
    return -1


def conserve_space(grid, head, snakes):
    goal = find_best_wall(grid, head, snakes)
    if not goal:
        return None
    return calculate_worst_path_direction(grid, head, goal)
