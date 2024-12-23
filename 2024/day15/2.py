import sys

DEBUG = True

input = sys.stdin.read().strip().split("\n\n")


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Warehouse:
    def __init__(self, data):
        data = [list(_) for _ in data.split("\n")]
        self.warehouse = []
        for row in data:
            row_double = []
            for char in row:
                if char == "@":
                    row_double.append("@")
                    row_double.append(".")
                elif char == "#":
                    row_double.append("#")
                    row_double.append("#")
                elif char == ".":
                    row_double.append(".")
                    row_double.append(".")
                elif char == "O":
                    row_double.append("[")
                    row_double.append("]")
                else:
                    raise ValueError("Invalid character")
            self.warehouse.append(row_double)
        self.width = len(self.warehouse[0])
        self.height = len(self.warehouse)
        self.robot = None
        for y, row in enumerate(self.warehouse):
            for x, cell in enumerate(row):
                if cell == "@":
                    self.robot = Robot(x, y)
                    break
        if not self.robot:
            raise ValueError("Robot not found")

    def __repr__(self):
        output = f"Warehouse with robot at {self.robot}:\n"
        for row in self.warehouse:
            output += "".join(row) + "\n"
        return output

    def gps_sum(self):
        sum = 0

        for y, row in enumerate(self.warehouse):
            for x, cell in enumerate(row):
                if cell == "[":
                    sum += (100 * y) + x
        return sum

    def move(self, direction, x, y):
        dx = direction[0]
        dy = direction[1]

        if self.warehouse[y + dy][x + dx] == "#":
            return False
        elif self.warehouse[y + dy][x + dx] == ".":
            self.warehouse[y + dy][x + dx] = self.warehouse[y][x]
            self.warehouse[y][x] = "."
            return True
        elif self.warehouse[y + dy][x + dx] == "[":
            if self.move(direction, x + dx, y + dy) and self.move(
                direction, x + dx + 1, y + dy
            ):
                return True
        elif self.warehouse[y + dy][x + dx] == "]":
            if self.move(direction, x + dx, y + dy) and self.move(
                direction, x + dx - 1, y + dy
            ):
                return False


warehouse = Warehouse(input[0])1
moves = [_ for _ in input[1] if _ != "\n"]

if DEBUG:
    print(warehouse)

    print("Moves:")
    for move in moves:
        print(move, end="")
    print()

for i, move in enumerate(moves):
    if move not in "^v<>":
        raise ValueError("Invalid move")
    match move:
        case "^":
            direction = (0, -1)
            print("Moving up") if DEBUG else None
        case "v":
            direction = (0, 1)
            print("Moving down") if DEBUG else None
        case "<":
            direction = (-1, 0)
            print("Moving left") if DEBUG else None
        case ">":
            direction = (1, 0)
            print("Moving right") if DEBUG else None

    x = warehouse.robot.x
    y = warehouse.robot.y

    warehouse.move(direction, x, y)
    if DEBUG:
        print(f"Move {i + 1}:")
        print(warehouse)

print("Final GPS Sum:") if DEBUG else None
print(warehouse.gps_sum())
