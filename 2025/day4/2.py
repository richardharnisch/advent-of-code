import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 1

input = sys.stdin.read().strip().split("\n")
input = [list(row) for row in input]
output = 0


def remove_rolls(input):
    removed_rolls = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if (
                input[i][j] == "@"
                and count_nested(
                    get_neighborhood(input, (i, j), use_diagonal=True), "@"
                )
                < 5
            ):
                removed_rolls += 1
                input[i][j] = "."
                if DEBUG:
                    print("x", end="")
            elif DEBUG:
                print(input[i][j], end="")
        if DEBUG:
            print("\n", end="")
    return removed_rolls


working = 1
while working:
    if DEBUG:
        print(f"=== Iteration {working} ===")
        working += 1
    previous_output = output
    output += remove_rolls(input)
    if previous_output == output:
        working = 0

print(output)
