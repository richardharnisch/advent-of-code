import sys

input = sys.stdin.read().strip()

lines = input.split("\n")

output = 0

for line in lines:
    nums = []
    for _ in line:
        if _ >= "0" and _ <= "9":
            nums.append(int(_))
    output += int(nums[0]) * 10 + int(nums[-1])

print(output)
