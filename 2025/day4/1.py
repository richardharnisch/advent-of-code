import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sys.stdin.read().strip()
input = input.split("\n")
output = 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if (
            input[i][j] == "@"
            and count_nested(get_neighborhood(input, (i, j), use_diagonal=True), "@")
            < 5
        ):
            output += 1
            if DEBUG:
                print("x", end="")
        elif DEBUG:
            print(input[i][j], end="")
    if DEBUG:
        print("\n", end="")


print(output)
