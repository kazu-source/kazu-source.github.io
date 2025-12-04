"""
Average Rate of Change for Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class AverageRateChangePolynomialsGenerator:
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
        # Linear function rate of change
        m = random.randint(2, 9)
        b = random.randint(-9, 9)
        x1 = random.randint(0, 5)
        x2 = x1 + random.randint(1, 5)

        latex = f"\\text{{Find the average rate of change of }} f(x) = {m}x + {b} \\text{{ from }} x = {x1} \\text{{ to }} x = {x2}"
        solution = f"{m}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Quadratic function rate of change
        a = random.randint(1, 5)
        b = random.randint(-9, 9)
        c = random.randint(-9, 9)
        x1 = random.randint(-3, 3)
        x2 = x1 + random.randint(1, 3)

        y1 = a * x1**2 + b * x1 + c
        y2 = a * x2**2 + b * x2 + c
        rate = (y2 - y1) / (x2 - x1)

        latex = f"\\text{{Find the average rate of change of }} f(x) = {a}x^2 + {b}x + {c} \\text{{ from }} x = {x1} \\text{{ to }} x = {x2}"
        solution = f"{rate:.2f}".rstrip('0').rstrip('.')

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Cubic function rate of change
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)
        x1 = random.randint(-2, 2)
        x2 = x1 + random.randint(1, 2)

        y1 = a * x1**3 + b * x1**2 + c * x1
        y2 = a * x2**3 + b * x2**2 + c * x2
        rate = (y2 - y1) / (x2 - x1)

        latex = f"\\text{{Find the average rate of change of }} f(x) = {a}x^3 + {b}x^2 + {c}x \\text{{ from }} x = {x1} \\text{{ to }} x = {x2}"
        solution = f"{rate:.2f}".rstrip('0').rstrip('.')

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Higher degree polynomial with interpretation
        a = random.randint(1, 2)
        b = random.randint(-5, 5)
        x1 = random.randint(0, 2)
        x2 = x1 + random.randint(2, 3)

        y1 = a * x1**4 + b * x1**2
        y2 = a * x2**4 + b * x2**2
        rate = (y2 - y1) / (x2 - x1)

        latex = f"\\text{{Find the average rate of change of }} f(x) = {a}x^4 + {b}x^2 \\text{{ from }} x = {x1} \\text{{ to }} x = {x2}"
        solution = f"{rate:.2f}".rstrip('0').rstrip('.')

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = AverageRateChangePolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
