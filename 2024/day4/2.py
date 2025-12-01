import sys

grid = []


def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_valid_position(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def is_x(x, y):
        if not (
            is_valid_position(x + 1, y + 1)
            and is_valid_position(x - 1, y - 1)
            and is_valid_position(x + 1, y - 1)
            and is_valid_position(x - 1, y + 1)
        ):
            return False

        def diagonal(direction):
            dx, dy = 1, 1 - (direction * 2)
            if grid[x + dx][y + dy] == "M" and grid[x - dx][y - dy] == "S":
                return True
            if grid[x + dx][y + dy] == "S" and grid[x - dx][y - dy] == "M":
                return True
            return False

        if grid[x][y] == "A" and diagonal(0) and diagonal(1):
            return True

        return False

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if is_x(i, j):
                count += 1

    return count


for line in sys.stdin:
    grid.append(line.strip())

print(count_x_mas(grid))
