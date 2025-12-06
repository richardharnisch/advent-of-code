import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

fresh, ingredients = sys.stdin.read().strip().split("\n\n")
output = 0

fresh = fresh.split("\n")
ingredients = list(map(int, ingredients.split("\n")))
fresh_marker = []

for fresh_list in fresh:
    start, end = map(int, fresh_list.split("-"))
    added = False
    for i in fresh_marker:
        if i[0] <= start <= i[1] or i[0] <= end <= i[1]:
            i[0] = min(i[0], start)
            i[1] = max(i[1], end)
            added = True
            break
    if not added:
        fresh_marker.append([start, end])

for ingredient in ingredients:
    for marker in fresh_marker:
        if marker[0] <= ingredient <= marker[1]:
            output += 1
            break

print(output)
