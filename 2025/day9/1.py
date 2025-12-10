import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = [
    tuple(map(int, tile.split(","))) for tile in sys.stdin.read().strip().split("\n")
]
areas = []

for i, tile in list(enumerate(input))[:-1]:
    for j, tile in list(enumerate(input))[i + 1 :]:
        x1, y1 = input[i]
        x2, y2 = input[j]
        area = abs(1 + x1 - x2) * abs(1 + y1 - y2)
        areas.append((i, j, area))
        dprint(f"{input[i]} to {input[j]} area: {area}")
areas = sorted(areas, key=lambda x: x[2], reverse=True)

print(areas[0][2])
