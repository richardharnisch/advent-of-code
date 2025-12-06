import sys
import os
from copy import deepcopy

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 1

fresh, _ = sys.stdin.read().strip().split("\n\n")
output = 0

fresh = fresh.split("\n")
fresh_lists = []

for fresh_list in fresh:
    start, end = map(int, fresh_list.split("-"))
    added = False
    for i in fresh_lists:
        if i[0] <= start <= i[1] or i[0] <= end <= i[1]:
            i[0] = min(i[0], start)
            i[1] = max(i[1], end)
            added = True
            break
    if not added:
        fresh_lists.append([start, end])


fresh_lists.sort(key=lambda x: x[0])

merged_lists = [fresh_lists[0]]
for start, end in fresh_lists[1:]:
    last_end = merged_lists[-1][1]
    if start <= last_end:
        merged_lists[-1][1] = max(last_end, end)
    else:
        merged_lists.append([start, end])

for fresh_list in merged_lists:
    start, end = fresh_list
    output += end - start
    output += 1  # for inclusive ranges

print(output)
