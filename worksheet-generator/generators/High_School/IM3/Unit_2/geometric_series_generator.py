"""
Geometric Series Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GeometricSeriesGenerator:
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
        # Identify geometric sequence
        a = random.randint(2, 9)
        r = random.randint(2, 4)

        term1 = a
        term2 = a * r
        term3 = a * r**2

        latex = f"\\text{{Find the common ratio: }} {term1}, {term2}, {term3}, ..."
        solution = f"r = {r}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Find sum of finite geometric series
        a = random.randint(1, 5)
        r = random.randint(2, 3)
        n = random.randint(4, 6)

        # S_n = a(1 - r^n)/(1 - r)
        sum_val = a * (1 - r**n) // (1 - r)

        latex = f"\\text{{Find sum: }} {a} + {a*r} + {a*r**2} + ... \\text{{ ({n} terms)}}"
        solution = f"S_{n} = {sum_val}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Infinite geometric series
        a = random.randint(1, 9)
        r_num = random.randint(1, 3)
        r_den = random.randint(4, 6)

        # S = a/(1-r) for |r| < 1
        latex = f"\\text{{Find sum of infinite series: }} {a} + {a}\\cdot\\frac{{{r_num}}}{{{r_den}}} + {a}\\cdot\\left(\\frac{{{r_num}}}{{{r_den}}}\\right)^2 + ..."
        solution = f"S = \\frac{{{a*r_den}}}{{{r_den - r_num}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Geometric series formula derivation/application
        a = random.randint(2, 5)
        r = random.randint(2, 3)
        n = random.randint(5, 8)

        sum_val = a * (r**n - 1) // (r - 1)

        latex = f"\\text{{Find }} S_n \\text{{ for }} a = {a}, r = {r}, n = {n}"
        solution = f"S_{n} = {sum_val}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = GeometricSeriesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
