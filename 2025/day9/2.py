import sys
import os
from tqdm import tqdm
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = [
    tuple(map(int, tile.split(","))) for tile in sys.stdin.read().strip().split("\n")
]
if DEBUG:
    plt.figure(figsize=(8, 8))
    plt.scatter(*zip(*input), s=5)
    plt.savefig("points.png")

vertices = []
for i, tile in list(enumerate(input))[:-1]:
    vertices.append([input[i], input[i + 1]])
vertices.append([input[-1], input[0]])

dprint(vertices)
if DEBUG:
    for v in vertices:
        x_vals = [v[0][0], v[1][0]]
        y_vals = [v[0][1], v[1][1]]
        plt.plot(x_vals, y_vals, color="red", linewidth=1)
    plt.savefig("points_with_lines.png")
areas = []

for i, tile in list(enumerate(input))[:-1]:
    for j, tile in list(enumerate(input))[i + 1 :]:
        x1, y1 = input[i]
        x2, y2 = input[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        areas.append((i, j, area))
areas = sorted(areas, key=lambda x: x[2], reverse=True)
for area in areas:
    dprint(f"{input[area[0]]} to {input[area[1]]} area: {area[2]}")

for area in tqdm(areas):
    inside_shape = True
    x1, y1 = input[area[0]]
    x2, y2 = input[area[1]]
    edges = [
        ((x1, y1), (x2, y1)),
        ((x1, y1), (x1, y2)),
        ((x2, y1), (x1, y2)),
        ((x2, y2), (x2, y1)),
        # ((x2, y2), (x1, y2)),
        # ((x2, y2), (x1, y1)),
    ]
    for vertex in vertices:
        for edge in edges:
            if lines_cross(vertex, edge):
                inside_shape = False
                break
    if inside_shape:
        print(f"rectangle at: {input[area[0]]}, {input[area[1]]}, area:")
        print(area[2])
        if DEBUG:
            plt.figure(figsize=(64, 64))
            plt.scatter(*zip(*input), s=5)
            for v in vertices:
                x_vals = [v[0][0], v[1][0]]
                y_vals = [v[0][1], v[1][1]]
                plt.plot(x_vals, y_vals, color="red", linewidth=1)
            rect_x = [x1, x2, x2, x1, x1]
            rect_y = [y1, y1, y2, y2, y1]
            plt.plot(rect_x, rect_y, color="green", linewidth=2)
            plt.savefig(f"points_with_rectangle_{area}.png")
            plt.close()
        else:
            break
