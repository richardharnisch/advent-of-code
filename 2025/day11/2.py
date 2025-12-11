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

dprint_list([f"{key}: {graph[key]}" for key in graph], level=2)


def count_paths(start: str, end: str, graph: dict) -> int:
    memoize = {}

    def _count_paths(start: str, end: str, graph: dict) -> int:
        if start == end:
            return 1
        elif start in memoize:
            return memoize[start]
        else:
            count = 0
            for parent in graph[start]:
                count += _count_paths(parent, end, graph)
            memoize[start] = count
            return count

    return _count_paths(start, end, graph)


dprint("Paths from 'svr' to 'dac':", count_paths("svr", "dac", graph))
dprint("Paths from 'svr' to 'fft':", count_paths("svr", "fft", graph))
dprint("Paths from 'dac' to 'fft':", count_paths("dac", "fft", graph))
dprint("Paths from 'fft' to 'dac':", count_paths("fft", "dac", graph))
dprint("Paths from 'dac' to 'out':", count_paths("dac", "out", graph))
dprint("Paths from 'fft' to 'out':", count_paths("fft", "out", graph))

output = (
    count_paths("svr", "fft", graph),
    count_paths("fft", "dac", graph),
    count_paths("dac", "out", graph),
)
dprint("Output components:", output)
print(output[0] * output[1] * output[2])
