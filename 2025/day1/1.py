import sys

DEBUG = False

input = sys.stdin.read().strip()

instructions = [i for i in input.split("\n")]
pointer = 50
password = 0

for instruction in instructions:
    dir = instruction[0]
    value = int(instruction[1:])
    if dir == "R":
        pointer += value
        pointer %= 100
    elif dir == "L":
        pointer -= value
        pointer %= 100
    if pointer == 0:
        password += 1

    if DEBUG:
        print(f"Instruction: {instruction}, Pointer: {pointer}, Password: {password}")

print(password)
