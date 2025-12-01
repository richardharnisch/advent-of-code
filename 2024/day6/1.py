import sys

DEBUG = False

input = sys.stdin.read().split("\n")

maze = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]

guard = [0, 0]
guard_direction = "up"


for i, line in enumerate(input):
    for j, char in enumerate(line):
        if char == "#":
            maze[i][j] = -1
        elif char == "^":
            guard = [i, j]


print(maze) if DEBUG else None
print(guard) if DEBUG else None


def is_accessible(position):
    if position[0] < 0 or position[0] >= len(maze):
        return True
    elif position[1] < 0 or position[1] >= len(maze[0]):
        return True
    return maze[position[0]][position[1]] != -1


def guard_in_scope(maze, guard):
    if guard[0] < 0 or guard[0] >= len(maze):
        return False
    elif guard[1] < 0 or guard[1] >= len(maze[0]):
        return False
    return True


def guard_next(guard, direction):
    if direction == "up":
        return [guard[0] - 1, guard[1]]
    elif direction == "down":
        return [guard[0] + 1, guard[1]]
    elif direction == "left":
        return [guard[0], guard[1] - 1]
    elif direction == "right":
        return [guard[0], guard[1] + 1]


def rotate(direction):
    if direction == "up":
        return "right"
    elif direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"
    else:
        raise ValueError("Invalid direction")


def move_guard(guard, direction):
    if not is_accessible(guard_next(guard, direction)):
        direction = rotate(direction)
        print(f"rotated to {direction}") if DEBUG else None
    else:
        maze[guard[0]][guard[1]] = 1
        guard = guard_next(guard, direction)
        print(f"moved to {guard}") if DEBUG else None
    return guard, direction


while guard_in_scope(maze, guard):
    maze[guard[0]][guard[1]] = 1
    guard, guard_direction = move_guard(guard, guard_direction)


if DEBUG:
    for line in maze:
        for char in line:
            if char == -1:
                print("#", end="")
            elif char == 1:
                print("X", end="")
            else:
                print(".", end="")
        print()

print(sum([sum([1 for _ in row if _ == 1]) for row in maze]))
