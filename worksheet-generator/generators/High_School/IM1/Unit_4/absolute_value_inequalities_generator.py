"""
Absolute Value Inequalities Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class AbsoluteValueInequalitiesGenerator:
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
        a = random.randint(3, 10)

        latex = f"|x| < {a}"
        solution = f"-{a} < x < {a}"
        steps = [f"Absolute value less than {a}", f"x is between -{a} and {a}", f"Answer: -{a} < x < {a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(5, 15)

        latex = f"|x| > {a}"
        solution = f"x < -{a} \\text{{ or }} x > {a}"
        steps = [f"Absolute value greater than {a}", f"x is farther from 0 than {a}", f"Answer: x < -{a} or x > {a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(5, 15)

        latex = f"|{a}x + {b}| \\leq {c}"
        left = (-c - b) / a
        right = (c - b) / a
        solution = f"{left:.1f} \\leq x \\leq {right:.1f}"
        steps = [f"-{c} \\leq {a}x + {b} \\leq {c}", f"Subtract {b}: -{c} - {b} \\leq {a}x \\leq {c} - {b}", f"Divide by {a}", f"Answer: {left:.1f} \\leq x \\leq {right:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(1, 7)
        c = random.randint(8, 20)

        latex = f"|{a}x - {b}| > {c}"
        left = (b - c) / a
        right = (b + c) / a
        solution = f"x < {left:.1f} \\text{{ or }} x > {right:.1f}"
        steps = [f"{a}x - {b} > {c} or {a}x - {b} < -{c}", f"Solve first: {a}x > {c + b}, x > {right:.1f}", f"Solve second: {a}x < {b - c}, x < {left:.1f}", f"Answer: x < {left:.1f} or x > {right:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = AbsoluteValueInequalitiesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
