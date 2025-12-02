import sys
import re
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sys.stdin.read().strip()
output = 0
ranges = input.split(",")


for id_range in ranges:
    start, end = map(int, id_range.split("-"))
    for n in range(start, end + 1):
        s = str(n)
        for div in divisors(len(s)):
            print(f"Comparing {split_str(s, div)}...") if DEBUG > 1 else None
            if all_equal(split_str(s, div)):
                output += n
                if DEBUG:
                    print(f"Found matching ID: {s}")
                break

print(output)
