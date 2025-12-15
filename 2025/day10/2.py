import sys
import os
from tqdm import tqdm
from z3 import Int, Solver, Sum, sat, Or

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0


class Machine:
    def __init__(self, definition: str):
        inputs = definition.split(" ")
        lights = len(inputs[0]) - 2
        self.lights = [0 for light in range(lights)]
        self.target = [int(target) for target in inputs[-1][1:-1].split(",")]
        buttons = [tuple(map(int, pair[1:-1].split(","))) for pair in inputs[1:-1]]
        self.buttons = []
        for button in buttons:
            button_vector = [int(i in button) for i in range(lights)]
            self.buttons.append(button_vector)
        self.solutions = self.solve_equations_z3_terms()
        self.solution_presses = [sum(sol.values()) for sol in self.solutions]
        self.min_presses = min(self.solution_presses)

    def __repr__(self):
        str = f"""{{   target  = {self.target},
    state   = {self.lights},
    buttons = {self.buttons}}}"""
        return str

    def equation_representation(self) -> List[Tuple[List[str], int]]:
        equations = []
        for light_index in range(len(self.lights)):
            terms: List[str] = []
            for button_index in range(len(self.buttons)):
                if self.buttons[button_index][light_index] != 0:
                    terms.append(number_to_letter(button_index))
            equations.append((terms, self.target[light_index]))  # (lhs terms, rhs)
        return equations

    def solve_equations_z3_terms(self):
        names = sorted(
            {name for terms, _ in self.equation_representation() for name in terms}
        )
        vars_ = {name: Int(name) for name in names}
        s = Solver()
        s.add(*[vars_[name] >= 0 for name in names])

        for terms, rhs in self.equation_representation():
            s.add(Sum([vars_[t] for t in terms]) == rhs)

        sols = []
        while s.check() == sat:
            m = s.model()
            sol = {name: m[vars_[name]].as_long() for name in names}
            sols.append(sol)
            s.add(Or(*[vars_[name] != m[vars_[name]] for name in names]))
        return sols


input = sys.stdin.read().strip().split("\n")
machines = [Machine(line) for line in input]
for i, machine in enumerate(machines):
    dprint(machine)
    dprint(f"Machine {i} equation representation:", level=2)
    dprint_list(machine.equation_representation(), level=2)
    dprint(f"Machine {i} Z3 solutions:", level=2)
    dprint_list(machine.solve_equations_z3_terms(), level=2)
    dprint(f"Machine {i} minimum presses: {machine.min_presses}")

dprint(" + ".join([str(machine.min_presses) for machine in machines]), ":", sep="")
print(sum(machine.min_presses for machine in machines))
