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
    tens = max(batteries[:-1])
    tens_index = batteries.index(tens) + 1
    ones = max(batteries[tens_index:])
    joltage = (tens * 10) + ones
    if DEBUG:
        print(f"Bank: {bank} => Tens: {tens}, Ones: {ones}, Joltage: {joltage}")
    output += joltage

print(output)
