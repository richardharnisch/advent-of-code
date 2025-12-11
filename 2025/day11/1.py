import sys
import os
from collections import defaultdict
from typing import Literal

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sys.stdin.read().strip().split("\n")
output = 0

graph = defaultdict(list)

for device in input:
    name, connections = device.split(": ")
    for connection in connections.split(" "):
        graph[name].append(connection)

dprint_list([f"{key}: {graph[key]}" for key in graph])

memoize = {}


def count_paths(node: tuple[int, int] | Literal["you"], graph: dict) -> int:
    if node == "out":
        return 1
    elif node in memoize:
        return memoize[node]
    else:
        count = 0
        for parent in graph[node]:
            count += count_paths(parent, graph)
        memoize[node] = count
        return count


print(count_paths("you", graph))
