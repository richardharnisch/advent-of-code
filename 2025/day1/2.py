import sys

DEBUG = False

input = sys.stdin.read().strip()

instructions = [i for i in input.split("\n")]
pointer = 50
password = 0

if DEBUG:
    print(f"Pointer: {pointer}, Password: {password}")

for instruction in instructions:
    dir = instruction[0]
    value = int(instruction[1:])
    if dir == "R":
        pointer += value
        password += (pointer - 1) // 100
        pointer %= 100
    elif dir == "L":
        new_pointer = pointer - value
        if new_pointer < 0:
            if pointer != 0:
                password += 1
            password += (-new_pointer - 1) // 100
        pointer = new_pointer
        pointer %= 100
    if pointer == 0:
        password += 1

    if DEBUG:
        print(f"Instruction: {instruction}, Pointer: {pointer}, Password: {password}")

print(password)
