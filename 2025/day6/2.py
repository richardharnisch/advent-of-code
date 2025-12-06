import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *
import pandas as pd

DEBUG = 0

# get each character in the input as a 2d DataFrame
input = pd.DataFrame([list(row) for row in sys.stdin.read().split("\n")[:-1]])
# rotate the DataFrame 90 degrees so that columns become rows
input = input.transpose()[::-1]
dprint("problems list:\n", input, level=2)
# convert back to list of lists
input = [list(row) for row in input.values.tolist()]

output = 0
numbers = []
for row in input:
    if all(c == " " for c in row):
        continue

    if row[-1] == "+":
        numbers.append(int("".join(row[:-1]).strip()))
        dprint(*numbers, sep=" + ")
        answer = sum(numbers)
        output += answer
        numbers = []
    elif row[-1] == "*":
        numbers.append(int("".join(row[:-1]).strip()))
        dprint(*numbers, sep=" * ")
        answer = 1
        for num in numbers:
            answer *= num
        output += answer
        numbers = []
    else:
        numbers.append(int("".join(row).strip()))

print(output)
