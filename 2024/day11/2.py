import sys

DEBUG = True

input = sys.stdin.read().strip()

stone_line = [int(h) for h in input.split()]

stones = {}


def add_stone(stone, num):
    if stone not in stones:
        stones[stone] = 0
    stones[stone] += num


for stone in stone_line:
    add_stone(stone, 1)


def blink(stones):
    new_stones = {}
    for num in list(stones.keys()):
        if num == 0:
            if 1 not in new_stones:
                new_stones[1] = 0
            new_stones[1] += stones[num]
        elif len(str(num)) % 2 == 0:
            first_half = int(str(num)[: len(str(num)) // 2])
            second_half = int(str(num)[len(str(num)) // 2 :])
            if first_half not in new_stones:
                new_stones[first_half] = 0
            if second_half not in new_stones:
                new_stones[second_half] = 0
            new_stones[first_half] += stones[num]
            new_stones[second_half] += stones[num]
        else:
            new_num = num * 2024
            if new_num not in new_stones:
                new_stones[new_num] = 0
            new_stones[new_num] += stones[num]
    return new_stones


if DEBUG:
    total_stones = 0
    for num in list(stones.keys()):
        total_stones += stones[num]
    print(f"Step 0: {total_stones}\n")

blinks = 75
for i in range(blinks):
    stones = blink(stones)
    if DEBUG:
        total_stones = 0
        for num in list(stones.keys()):
            total_stones += stones[num]
        print(f"Step {i + 1}: {total_stones}\n")


total_stones = 0

for num in list(stones.keys()):
    total_stones += stones[num]

print(total_stones)
