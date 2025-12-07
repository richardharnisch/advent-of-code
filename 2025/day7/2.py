import sys
import os
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sys.stdin.read().strip().split("\n")
beams = [0] * len(input[0])
output = 0

"""
Conceptual approach:
1. Build a directed graph where each splitter is a node and edges represent possible beam paths.
2. Traverse the graph upwards to count unique paths.
3. Starting from bottom node, the amount of possible paths is the sum of paths to all its parents.
4. Need to recursively call a function that counts paths to parents until reaching the top.
"""

# 1. Read input and build graph
graph = defaultdict(list)

for i, line in enumerate(input[:-1]):
    new_beams = [0] * len(line)
    for j, c in enumerate(line):
        if c == "S":
            new_beams[j] = 1
            graph["start"].append((i, j))
            graph[(i, j)].append((i + 1, j))
        if c == "." and beams[j] == 1:
            new_beams[j] = 1
            graph[(i, j)].append((i + 1, j))
        if c == "^" and beams[j] == 1:
            new_beams[j] = 0
            new_beams[j - 1] = 1
            graph[(i, j)].append((i + 1, j - 1))
            new_beams[j + 1] = 1
            graph[(i, j)].append((i + 1, j + 1))
            output += 1
    dprint(f"Row {i}: \n{''.join(map(str, beams))} -> \n{''.join(map(str, new_beams))}")
    beams = new_beams

for j, c in enumerate(input[-1]):
    if beams[j] == 1:
        output += 1
        graph[(len(input) - 1, j)].append("end")

dprint("\nGraph:")
for key in graph:
    dprint(f"{key}: {graph[key]}")


# 2. Function to count paths to given node
memoize = {}


def count_paths(node: tuple[int, int] | Literal["start"], graph: dict) -> int:
    if node == "end":
        return 1
    elif node in memoize:
        return memoize[node]
    else:
        count = 0
        for parent in graph[node]:
            count += count_paths(parent, graph)
        memoize[node] = count
        return count


print(count_paths("start", graph))
