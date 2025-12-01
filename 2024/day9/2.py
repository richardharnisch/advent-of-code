import sys

disk = sys.stdin.read().strip()
DEBUG = False


class File:
    def __init__(self, name, size, pos):
        self.name = name
        self.size = size
        self.pos = pos

    def __repr__(self):
        return f"File {self.name}: {self.size} bits at pos {self.pos}"


def decompress(disk):
    out = []
    files = []
    for i, char in enumerate(disk):
        if i % 2 == 0:
            files.append(File(i // 2, int(char), len(out)))
            out.extend([str(i // 2)] * int(char))
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


def find_dots(disk, size):
    consecutive_dots = 0
    for i, slot in enumerate(disk):
        if consecutive_dots == size:
            return i - size
        if slot == ".":
            consecutive_dots += 1
        else:
            consecutive_dots = 0
    return -1


def move_file(disk, size, pos, name):
    insertion = find_dots(disk, size)
    if insertion == -1 or insertion >= pos:
        (
            print(f"Could not find {size} consecutive dots for file {name}")
            if DEBUG
            else None
        )
        print_disk(disk)
        return
    print(f"Moving {name} from {pos} to {insertion}") if DEBUG else None
    for i in range(size):
        disk[insertion + i] = name
        disk[pos + i] = "."
    print_disk(disk)


for file in files[::-1]:
    move_file(disk, file.size, file.pos, file.name)


checksum = 0
for i, char in enumerate(disk):
    checksum += i * int(char) if char != "." else 0

print(checksum)
