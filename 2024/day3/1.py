import re
import sys

sum = 0

data = sys.stdin.read()
for mul in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data):
    operands = re.findall(r"[0-9]{1,3}", mul)
    sum += int(operands[0]) * int(operands[1])

print(sum)
