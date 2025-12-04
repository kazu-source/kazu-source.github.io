"""
What is an Equation Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class WhatIsAnEquationGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        a = random.randint(1, 10)
        b = random.randint(1, 15)

        latex = f"\\text{{Is }} x + {a} = {b} \\text{{ an equation?}}"
        solution = "Yes"
        steps = ["Has an equals sign", "Has a variable", "Answer: Yes, it is an equation"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(1, 12)
        x_val = random.randint(1, 5)
        c = a * x_val + b

        latex = f"\\text{{Is }} x = {x_val} \\text{{ a solution to }} {a}x + {b} = {c}?"
        solution = "Yes"
        steps = [f"Substitute x = {x_val}", f"{a}({x_val}) + {b} = {a*x_val} + {b} = {c}", f"{c} = {c}", "Answer: Yes"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 7)
        b = random.randint(1, 10)
        x_val = random.randint(2, 6)
        wrong_val = x_val + random.randint(1, 3)
        c = a * x_val + b

        latex = f"\\text{{Is }} x = {wrong_val} \\text{{ a solution to }} {a}x + {b} = {c}?"
        solution = "No"
        steps = [f"Substitute x = {wrong_val}", f"{a}({wrong_val}) + {b} = {a*wrong_val} + {b} = {a*wrong_val + b}", f"{a*wrong_val + b} \\neq {c}", "Answer: No"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(1, 10)

        latex = f"\\text{{Write an equation where }} x = {c} \\text{{ is the solution}}"
        solution = f"Example: x + {b} = {c + b} or {a}x = {a*c}"
        steps = [f"If x = {c}, create equation", f"Option 1: x + {b} = {c+b}", f"Option 2: {a}x = {a*c}", "Many answers possible"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = WhatIsAnEquationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
