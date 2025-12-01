import sys

disk = sys.stdin.read().strip()
DEBUG = False


def decompress(disk):
    out = []
    files = 0
    for i, char in enumerate(disk):
        if i % 2 == 0:
            out.extend([str(i // 2)] * int(char))
            files += int(char)
        else:
            out.extend(["."] * int(char))
    return out, files


def print_disk(disk):
    if DEBUG:
        for char in disk:
            print(char, end="")
        print()


disk, files = decompress(disk)
if DEBUG:
    print_disk(disk)
    print(f"Files: {files}")


dots = []
for i, char in enumerate(disk):
    if char == ".":
        dots.append(i)

print(dots) if DEBUG else None

dot_position = dots.pop(0)

for _, char in enumerate(disk[::-1]):
    i = len(disk) - _ - 1
    if char != ".":
        print(f"Moving {char} from {i} to {dot_position}") if DEBUG else None
        disk[i], disk[dot_position] = disk[dot_position], disk[i]
        print_disk(disk)
        dot_position = dots.pop(0)
        if dot_position >= files:
            break


checksum = 0
for i, char in enumerate(disk):
    checksum += i * int(char) if char != "." else 0

print(checksum)
