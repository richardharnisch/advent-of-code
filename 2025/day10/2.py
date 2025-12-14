import sys
import os
from copy import deepcopy
from tqdm import tqdm

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 1


class Machine:
    def __init__(self, definition: str):
        inputs = definition.split(" ")
        lights = len(inputs[0]) - 2
        self.lights = [0 for light in range(lights)]
        self.target = [int(target) for target in inputs[-1][1:-1].split(",")]
        self.buttons = [tuple(map(int, pair[1:-1].split(","))) for pair in inputs[1:-1]]

    def __repr__(self):
        str = f"""{{   target  = {self.target},
    state   = {self.lights},
    buttons = {self.buttons}}}
"""
        return str

    def press(self, button_index: int, lights: list[int]) -> list[int]:
        lights = deepcopy(lights)
        button = self.buttons[button_index]
        for i in button:
            lights[i] += 1
        return lights

    def bfs(self, lights) -> int:
        from collections import deque

        initial = tuple(lights)
        target = tuple(self.target)
        visited = set()
        queue = deque([(initial, 0)])

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            if state in visited:
                continue
            visited.add(state)
            for button in range(len(self.buttons)):
                next_state = tuple(self.press(button, list(state)))
                if next_state not in visited:
                    queue.append((next_state, steps + 1))
        return -1  # No solution found


input = sys.stdin.read().strip().split("\n")
machines = [Machine(line) for line in input]
dprint_list(machines)

output = 0

for machine in tqdm(machines):
    output += machine.bfs(machine.lights)
print(output)
