"""
Systems of Equations Intro Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SystemsOfEquationsIntroGenerator:
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
        latex = f"\\text{{What is a system of equations?}}"
        solution = "Two or more equations with the same variables"
        steps = ["A system has multiple equations", "All equations share the same variables", "Answer: Two or more equations with same variables"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x_val = random.randint(1, 5)
        y_val = random.randint(2, 8)
        a = random.randint(2, 5)
        b = random.randint(1, 4)

        c1 = x_val + y_val
        c2 = a * x_val + b * y_val

        latex = f"\\text{{Is }} ({x_val}, {y_val}) \\text{{ a solution to }} x + y = {c1}, {a}x + {b}y = {c2}?"
        solution = "Yes"
        steps = [f"Check first: {x_val} + {y_val} = {c1} ✓", f"Check second: {a}({x_val}) + {b}({y_val}) = {c2} ✓", "Answer: Yes"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x_val = random.randint(2, 6)
        y_val = random.randint(1, 5)
        wrong_x = x_val + 1

        c1 = x_val + y_val
        c2 = 2 * wrong_x + y_val

        latex = f"\\text{{Is }} ({wrong_x}, {y_val}) \\text{{ a solution to }} x + y = {c1}, 2x + y = {c2}?"
        solution = "No"
        steps = [f"Check first: {wrong_x} + {y_val} = {wrong_x + y_val} ≠ {c1}", "First equation fails", "Answer: No"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a1 = random.randint(2, 5)
        b1 = random.randint(1, 4)
        a2 = random.randint(1, 4)
        b2 = random.randint(2, 5)
        c1 = random.randint(10, 25)
        c2 = random.randint(15, 30)

        latex = f"\\text{{Write a system: }} {a1}x + {b1}y = {c1} \\text{{ and }} {a2}x + {b2}y = {c2}"
        solution = f"System: {a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}"
        steps = ["A system has two equations", "Both use variables x and y", "Solution is a point (x,y) that satisfies both"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SystemsOfEquationsIntroGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
