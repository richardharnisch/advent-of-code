import sys

DEBUG = True

input = sys.stdin.read().strip()

stones = [int(h) for h in input.split()]


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            first_half = int(str(stone)[: len(str(stone)) // 2])
            second_half = int(str(stone)[len(str(stone)) // 2 :])
            new_stones.append(first_half)
            new_stones.append(second_half)
        else:
            new_stones.append(stone * 2024)
    return new_stones


blinks = 25
for i in range(blinks):
    stones = blink(stones)
    print(f"Step {i + 1}: {len(stones)}") if DEBUG else None


print(len(stones))
