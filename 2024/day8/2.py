import sys
import numpy as np

DEBUG = False

input = sys.stdin.read().strip()

antennas = input.split("\n")

antinodes = [[0 for i in range(len(antennas[0]))] for j in range(len(antennas))]


def get_positions(antennas, char):
    positions = []
    for i, line in enumerate(antennas):
        for j, c in enumerate(line):
            if c == char:
                positions.append((i, j))
    return positions


def unique_chars(antennas):
    chars = set()
    for line in antennas:
        for char in line:
            if char != ".":
                chars.add(char)
    print("Unique chars:", "".join(chars)) if DEBUG else None
    return chars


def add_antinodes(antinodes, pos1, pos2):
    x_delta = pos1[0] - pos2[0]
    y_delta = pos1[1] - pos2[1]

    idx = 0
    node1 = (pos1[0] + (x_delta * idx), pos1[1] + (y_delta * idx))
    while (
        node1[0] >= 0
        and node1[0] < len(antinodes)
        and node1[1] >= 0
        and node1[1] < len(antinodes[0])
    ):
        antinodes[node1[0]][node1[1]] = 1
        idx += 1
        node1 = (pos1[0] + (x_delta * idx), pos1[1] + (y_delta * idx))

    idx = 0
    node2 = (pos1[0] - (x_delta * idx), pos1[1] - (y_delta * idx))
    while (
        node2[0] >= 0
        and node2[0] < len(antinodes)
        and node2[1] >= 0
        and node2[1] < len(antinodes[0])
    ):
        antinodes[node2[0]][node2[1]] = 1
        idx += 1
        node2 = (pos1[0] - (x_delta * idx), pos1[1] - (y_delta * idx))


for char in unique_chars(antennas):
    positions = get_positions(antennas, char)
    for pos1 in positions:
        for pos2 in positions:
            if pos1 != pos2:
                add_antinodes(antinodes, pos1, pos2)

print(np.sum(antinodes))

if DEBUG:
    for line in antinodes:
        print("".join(["#" if i == 1 else "." for i in line]))
