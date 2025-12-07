import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sys.stdin.read().strip().split("\n")
beams = [0] * len(input[0])
output = 0


for line in input:
    for i, c in enumerate(line):
        if c == "S":
            beams[i] = 1
        if c == "^" and beams[i] == 1:
            beams[i] = 0
            beams[i - 1] = 1
            beams[i + 1] = 1
            output += 1


print(output)
