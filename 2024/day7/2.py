import sys

DEBUG = False


class Equation:
    def __init__(self, equation):
        self.result = int(equation.split(":")[0].strip())
        self.operands = [int(_) for _ in equation.split(":")[1].strip().split(" ")]

    def __repr__(self):
        operands = list(self.operands)
        return f"{self.result} {operands}"


def concat_numbers(a, b):
    return int(str(a) + str(b))


def solvable(target, current_result, operands):
    if current_result == target and len(operands) == 0:
        return True
    if current_result > target or len(operands) == 0:
        return False
    else:
        return (
            solvable(target, current_result + operands[0], operands[1:])
            or solvable(target, current_result * operands[0], operands[1:])
            or solvable(
                target, concat_numbers(current_result, operands[0]), operands[1:]
            )
        )


input = [Equation(_) for _ in sys.stdin.read().split("\n") if _ != ""]
print(input) if DEBUG else None

total_solvable_sum = 0
for equation in input:
    total_solvable_sum += (
        solvable(equation.result, equation.operands[0], equation.operands[1:])
        * equation.result
    )

print(total_solvable_sum)
