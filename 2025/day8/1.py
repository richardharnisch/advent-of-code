import sys
import os
from math import sqrt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0
connectors = 1000

boxes = [
    [tuple([int(coord) for coord in box.split(",")])]
    for box in sys.stdin.read().strip().split("\n")
]

# 2x2 chart showing distance between any two boxes
dists = []
for i, box in list(enumerate(boxes))[:-1]:
    for j, other_box in list(enumerate(boxes))[i + 1 :]:
        dx = box[0][0] - other_box[0][0]
        dy = box[0][1] - other_box[0][1]
        dz = box[0][2] - other_box[0][2]
        dist = sqrt((dx * dx) + (dy * dy) + (dz * dz))
        dists.append((i, j, dist))

dists.sort(key=lambda x: x[2])
dprint("\n".join(str(dist) for dist in dists))

boxes = [[box] for box in list(range(len(boxes)))]
dprint(boxes)


def merge_lists_by_content(list, item1, item2):
    """
    Takes a list of list and two items. Merges the two sublists containing each item.
    Removes the original sublists after merging.
    Assumes that none of the sublists share items.
    """
    idx1 = idx2 = None
    for i, sublist in enumerate(list):
        if item1 in sublist:
            idx1 = i
        if item2 in sublist:
            idx2 = i
    if idx1 is not None and idx2 is not None and idx1 != idx2:
        list[idx1].extend(list[idx2])
        del list[idx2]


for _ in range(connectors):
    i, j, dist = dists.pop(0)
    merge_lists_by_content(boxes, i, j)
    dprint(f"Merging {i} and {j} at distance {dist}")
dprint(boxes)

# get largest boxes
boxes.sort(key=lambda x: len(x), reverse=True)

output = len(boxes[0]) * len(boxes[1]) * len(boxes[2])
print(output)
