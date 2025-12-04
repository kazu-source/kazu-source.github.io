"""
Solving Equations by Graphing Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingEquationsGraphingGenerator:
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
        # Linear equation graphically
        m = random.randint(2, 5)
        b = random.randint(1, 9)
        c = random.randint(1, 9)

        latex = f"\\text{{Solve graphically: }} {m}x + {b} = {c}"
        solution = f"x = \\frac{{{c - b}}}{{{m}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Quadratic equation graphically
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Solve graphically: }} x^2 = {a}x + {b}"
        solution = "Find x-intercepts of y = x^2 - {a}x - {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Exponential equation graphically
        b = random.choice([2, 3])
        c = random.randint(5, 20)

        latex = f"\\text{{Solve graphically: }} {b}^x = {c}"
        solution = f"Find intersection of y = {b}^x and y = {c}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex equation graphically
        a = random.randint(1, 3)
        b = random.randint(1, 5)

        latex = f"\\text{{Solve graphically: }} x^3 = {a}x + {b}"
        solution = f"Find intersections of y = x^3 and y = {a}x + {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = SolvingEquationsGraphingGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
