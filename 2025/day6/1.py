import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = [line.split() for line in sys.stdin.read().strip().split("\n")]
output = 0

for problem in range(len(input[0])):
    if input[-1][problem] == "+":
        answer = 0
        for i in range(len(input) - 1):
            answer += int(input[i][problem])
    else:
        answer = 1
        for i in range(len(input) - 1):
            answer *= int(input[i][problem])
    output += answer

print(output)
