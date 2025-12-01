import sys

DEBUG = False

input = sys.stdin.read().strip()

map = [[int(h) for h in _] for _ in input.split("\n")]
if DEBUG:
    for row in map:
        for h in row:
            print(h, end="")
        print()


def map_value(x, y):
    if 0 <= x < len(map) and 0 <= y < len(map[0]):
        return map[x][y]
    return -1


def get_trails(map, x, y):
    trails = set()
    height = map[x][y]
    if height == 9:
        print(f"Found trail ending at {x}, {y}") if DEBUG else None
        trails.add((x, y))
        return trails
    if map_value(x + 1, y) == height + 1:
        trails.update(get_trails(map, x + 1, y))
    if map_value(x - 1, y) == height + 1:
        trails.update(get_trails(map, x - 1, y))
    if map_value(x, y + 1) == height + 1:
        trails.update(get_trails(map, x, y + 1))
    if map_value(x, y - 1) == height + 1:
        trails.update(get_trails(map, x, y - 1))
    return trails


sum_scores = 0

for x, row in enumerate(map):
    for y, height in enumerate(row):
        if map[x][y] == 0:
            score = len(get_trails(map, x, y))
            sum_scores += score
            if DEBUG:
                print(f"Found trailhead at {x}, {y} with {score} trails")
print(sum_scores)
