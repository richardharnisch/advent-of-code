import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sys.stdin.read().strip().split("\n\n")
gifts = [[list(line) for line in gift.split("\n")[1:]] for gift in input[:-1]]
gifts_sizes = [count_nested(gift, "#") for gift in gifts]
trees = input[-1].split("\n")
output = 0

for gift, size in zip(gifts, gifts_sizes):
    dprint(f"Gift size: {size}, gift:\n{gift}")


class Tree:
    def __init__(
        self,
        height: int,
        width: int,
        gifts: List[int],
    ):
        self.height = height
        self.width = width
        self.gifts = gifts
        total_size = self.width * self.height

    def possible_packing(self) -> bool:
        # heuristic to check if definitely NOT possible
        return sum(self.gifts) <= (self.width // 3) * (self.height // 3)


for tree in trees:
    size, gifts_str = tree.split(": ")
    height, width = map(int, size.split("x"))
    gifts = list(map(int, gifts_str.split(" ")))
    tree = Tree(height, width, gifts)
    output += int(tree.possible_packing())

print(output)
