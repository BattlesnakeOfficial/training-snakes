# Training Snakes

This is to run several snakes of varying difficulty at 
https://battlesnake-training-snakes.herokuapp.com/snake_1
https://battlesnake-training-snakes.herokuapp.com/snake_2
https://battlesnake-training-snakes.herokuapp.com/snake_3
...

## Running it
Run the snake server locally:
```
> ./scripts/run_snake
```
this should provide all snakes at different paths, i.e.:
- http://localhost:8080/snake_1
- http://localhost:8080/snake_2
- http://localhost:8080/snake_3
- ...

Run the game server locally:
```
> ./scripts/run_server
```

## Training Snakes
To help battlesnake attendies train and verify their snakes, we'll provide a pool of snakes with a gradient of difficulties.

### Snake 0
- Goes in a straight line (always in the longest direction)

### Snake 1
- Avoids walls

### Snake 2
- Avoids walls
- Avoids snake segments

### Snake 3
- Avoids walls
- Avoids snake segments
- Eats first food in list

### Snake 4
- Avoids walls
- Avoids snake segments
- Eats orthoganally closest food

### Snake 5
- Avoids walls
- Avoids snake segments
- Eats orthoganally closest food

### 6/10 Snake
- Avoids walls
- Avoids snake segments
- When hungry, eats closest food

### 7/10 Snake
- Avoids walls
- Avoids snake segments
- When hungry, eats closest food
- Goes for potential head/head kills of smaller snakes

### 8/10 Snake
- Avoids walls
- Avoids snake segments
- When hungry, eats closest food
- Goes for potential head/head kills of smaller snakes
- Moves in to tail of snakes (when they aren't possibly eating)

### 9/10 Snake
- Avoids walls
- Avoids snake segments
- When hungry, eats closest food
- Goes for potential head/head kills of smaller snakes
- Moves in to tail of snakes (when they aren't possibly eating)
- Does not enter small spaces when larger space is an option.

### Other Ideas
- DOS food
- honeypot food
- empty path, instead of shortest path