import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sys.stdin.read().strip()
output = 0

banks = input.split("\n")

for bank in banks:
    batteries = list(map(int, bank))
    joltage = 0
    for i in range(11, -1, -1):
        digit = max(batteries[: -i or None])
        digit_index = batteries.index(digit) + 1
        batteries = batteries[digit_index:]
        joltage += digit * (10**i)

    if DEBUG:
        print(f"Bank: {bank} => Joltage: {joltage}")
    output += joltage

print(output)
