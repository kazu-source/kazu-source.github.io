"""
Dividing Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DividingPolynomialsGenerator:
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
        # Divide by monomial
        a = random.randint(2, 6)
        b = random.randint(2, 8)
        c = random.randint(2, 4)

        numerator_coef = a * c
        numerator_coef2 = b * c

        latex = f"\\frac{{{numerator_coef}x^2 + {numerator_coef2}x}}{{{c}x}}"
        solution = f"{a}x + {b}"
        steps = [
            f"Divide each term by {c}x",
            f"\\frac{{{numerator_coef}x^2}}{{{c}x}} = {a}x",
            f"\\frac{{{numerator_coef2}x}}{{{c}x}} = {b}",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Long division with linear divisor
        a = random.randint(1, 4)
        b = random.randint(1, 6)
        # (x + a) divides into polynomial
        # Create (x + a)(x + b) = x^2 + (a+b)x + ab
        c = a + b
        d = a * b

        latex = f"\\frac{{x^2 + {c}x + {d}}}{{x + {a}}}"
        solution = f"x + {b}"
        steps = [
            f"Use long division or synthetic division",
            f"Divide x^2 by x: x",
            f"Multiply: x(x + {a}) = x^2 + {a}x",
            f"Subtract: ({c}x + {d}) - ({a}x) = {b}x + {d}",
            f"Divide {b}x by x: {b}",
            f"Multiply: {b}(x + {a}) = {b}x + {a*b}",
            f"Remainder: 0",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Polynomial long division with remainder
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        r = random.randint(1, 8)  # remainder

        # Dividend = (x + a)(x + b) + r = x^2 + (a+b)x + ab + r
        c = a + b
        d = a * b + r

        latex = f"\\frac{{x^2 + {c}x + {d}}}{{x + {a}}}"
        solution = f"x + {b} + \\frac{{{r}}}{{x + {a}}}"
        steps = [
            f"Use long division",
            f"x^2 \\div x = x",
            f"x(x + {a}) = x^2 + {a}x",
            f"Subtract: {c}x + {d} - {a}x = {b}x + {d}",
            f"{b}x \\div x = {b}",
            f"{b}(x + {a}) = {b}x + {a*b}",
            f"Remainder: {d} - {a*b} = {r}",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Higher degree polynomial division
        a = random.randint(1, 3)
        b = random.randint(1, 4)
        c = random.randint(1, 4)

        # (x + a)(x^2 + bx + c) = x^3 + (a+b)x^2 + (ab+c)x + ac
        coef2 = a + b
        coef1 = a * b + c
        coef0 = a * c

        latex = f"\\frac{{x^3 + {coef2}x^2 + {coef1}x + {coef0}}}{{x + {a}}}"
        solution = f"x^2 + {b}x + {c}"
        steps = [
            f"Use long division",
            f"x^3 \\div x = x^2",
            f"x^2(x + {a}) = x^3 + {a}x^2",
            f"Subtract: {coef2}x^2 - {a}x^2 = {b}x^2",
            f"{b}x^2 \\div x = {b}x",
            f"{b}x(x + {a}) = {b}x^2 + {a*b}x",
            f"Continue process...",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = DividingPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
