import sys
import re

DEBUG = False

input = sys.stdin.read().strip()
ranges = input.split(",")
output = 0

for id_range in ranges:
    start, end = map(int, id_range.split("-"))
    for n in range(start, end + 1):
        s = str(n)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            left, right = s[:mid], s[mid:]
            if left == right:
                output += n
                if DEBUG:
                    print(f"Found matching ID: {s}")

print(output)
