"""
Zeros of Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ZerosOfPolynomialsGenerator:
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
        # Find zeros of factored quadratic
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        latex = f"\\text{{Find zeros: }} f(x) = (x - {a})(x - {b})"
        solution = f"x = {a}, {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Find zeros of expanded quadratic
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        # (x - a)(x - b) = x^2 - (a+b)x + ab
        coef_x = -(a + b)
        const = a * b

        latex = f"\\text{{Find zeros: }} f(x) = x^2 + {coef_x}x + {const}"
        solution = f"x = {a}, {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Find zeros of cubic
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        latex = f"\\text{{Find zeros: }} f(x) = (x - {a})(x - {b})(x - {c})"
        solution = f"x = {a}, {b}, {c}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Zeros with multiplicity
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Find zeros and multiplicity: }} f(x) = (x - {a})^2(x - {b})"
        solution = f"x = {a} (multiplicity 2), x = {b} (multiplicity 1)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ZerosOfPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
