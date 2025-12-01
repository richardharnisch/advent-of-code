import sys
import re

DEBUG = False

input = sys.stdin.read().strip()

lines = input.split("\n")

output = 0
pattern = r"(\d|zero|one|two|three|four|five|six|seven|eight|nine)"


def to_int(num):
    if num.isdigit():
        return int(num)
    else:
        word_to_num = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        return word_to_num[num]


for line in lines:
    matches = [match[0] for match in re.findall(r"(?=({}))".format(pattern), line)]
    output += to_int(matches[0]) * 10 + to_int(matches[-1])
    print(f"{line} -> {to_int(matches[0])*10 + to_int(matches[-1])}") if DEBUG else None

print(output)
