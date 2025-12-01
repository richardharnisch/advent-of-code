import sys

grid = []


def count_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1),  # Diagonal up-left
    ]

    def is_valid_position(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, direction):
        dx, dy = direction
        for k in range(word_length):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid_position(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            for direction in directions:
                if find_word(i, j, direction):
                    count += 1

    return count


for line in sys.stdin:
    grid.append(line.strip())

print(count_xmas(grid))
