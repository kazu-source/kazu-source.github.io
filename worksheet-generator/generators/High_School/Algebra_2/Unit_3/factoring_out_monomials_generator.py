"""
Factoring Out Monomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FactoringOutMonomialsGenerator:
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
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(1, 8)

        latex = f"{a}x^2 + {a*b}x"
        solution = f"{a}x(x + {b})"
        steps = [
            f"Factor out common monomial {a}x",
            f"{a}x^2 = {a}x \\cdot x",
            f"{a*b}x = {a}x \\cdot {b}",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        gcf = random.randint(2, 5)
        a = random.randint(2, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 8)

        coef1 = gcf * a
        coef2 = gcf * b
        coef3 = gcf * c

        latex = f"{coef1}x^3 + {coef2}x^2 + {coef3}x"
        solution = f"{gcf}x({a}x^2 + {b}x + {c})"
        steps = [
            f"Identify GCF: {gcf}x",
            f"Divide each term by {gcf}x",
            f"{coef1}x^3 \\div {gcf}x = {a}x^2",
            f"{coef2}x^2 \\div {gcf}x = {b}x",
            f"{coef3}x \\div {gcf}x = {c}",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        gcf = random.randint(2, 5)
        pow_x = random.randint(2, 4)
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 6)

        coef1 = gcf * a
        coef2 = gcf * b
        coef3 = gcf * c

        latex = f"{coef1}x^{{{pow_x+2}}} + {coef2}x^{{{pow_x+1}}} + {coef3}x^{{{pow_x}}}"
        solution = f"{gcf}x^{{{pow_x}}}({a}x^2 + {b}x + {c})"
        steps = [
            f"Find GCF of coefficients: {gcf}",
            f"Find lowest power of x: x^{{{pow_x}}}",
            f"GCF = {gcf}x^{{{pow_x}}}",
            f"Factor out: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        gcf = random.randint(2, 4)
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)

        coef1 = gcf * a
        coef2 = gcf * b
        coef3 = gcf * c
        coef4 = gcf * d

        x_pow = random.randint(1, 2)
        y_pow = random.randint(1, 2)

        latex = f"{coef1}x^{{{x_pow+2}}}y^{{{y_pow+1}}} + {coef2}x^{{{x_pow+1}}}y^{{{y_pow+1}}} + {coef3}x^{{{x_pow}}}y^{{{y_pow+1}}} + {coef4}x^{{{x_pow}}}y^{{{y_pow}}}"
        solution = f"{gcf}x^{{{x_pow}}}y^{{{y_pow}}}({a}x^2y + {b}xy + {c}y + {d})"
        steps = [
            f"GCF of coefficients: {gcf}",
            f"Lowest x power: x^{{{x_pow}}}",
            f"Lowest y power: y^{{{y_pow}}}",
            f"Monomial GCF: {gcf}x^{{{x_pow}}}y^{{{y_pow}}}",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FactoringOutMonomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
