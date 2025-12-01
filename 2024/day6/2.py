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


class State:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        return f"{self.x}, {self.y} looking {self.direction}"

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
            and self.direction == other.direction
        )

    def __hash__(self):
        return hash((self.x, self.y, self.direction))


def walk_path(maze, guard):
    guard_direction = "up"
    states = set()

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
            # print(f"rotated to {direction}") if DEBUG else None
        else:
            maze[guard[0]][guard[1]] = 1
            states.add(State(guard[0], guard[1], direction))
            guard = guard_next(guard, direction)
            # print(f"moved to {guard}") if DEBUG else None
        return guard, direction

    while guard_in_scope(maze, guard):
        guard, guard_direction = move_guard(guard, guard_direction)

    return states


def test_loop(maze, guard):
    states = set()
    guard_direction = "up"

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
        else:
            guard = guard_next(guard, direction)
        return guard, direction

    while guard_in_scope(maze, guard):
        current_state = State(guard[0], guard[1], guard_direction)
        if current_state in states:
            return True
        states.add(current_state)

        guard, guard_direction = move_guard(guard, guard_direction)

    return False


states = walk_path(maze, guard)
print(states) if DEBUG else None

possible_loops = 0


def can_cause_loop(x, y, states):
    for state in states:
        if state.x == x and state.y == y:
            return True
    return False


for x, line in enumerate(maze):
    for y, char in enumerate(line):
        print(f"testing obstruction at {x}, {y}...") if DEBUG else None
        if maze[x][y] != -1 and guard != [x, y] and can_cause_loop(x, y, states):
            original_value = maze[x][y]
            maze[x][y] = -1
            if test_loop(maze, guard):
                possible_loops += 1
                print(f"obstruction at {x}, {y} causes a loop") if DEBUG else None
            maze[x][y] = original_value
    print(f"finished row {x}") if DEBUG else None


print(possible_loops)
