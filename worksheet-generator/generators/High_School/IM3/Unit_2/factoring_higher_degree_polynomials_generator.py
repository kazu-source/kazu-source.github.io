"""
Factoring Higher Degree Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FactoringHigherDegreePolynomialsGenerator:
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
        # Cubic with common factor
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        latex = f"\\text{{Factor: }} x^3 + {a+b}x^2 + {a*b}x"
        solution = f"x(x + {a})(x + {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Difference of squares with higher degree
        a = random.randint(1, 5)

        latex = f"\\text{{Factor: }} x^4 - {a**2}"
        solution = f"(x^2 + {a})(x^2 - {a})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Cubic factoring
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        # (x - a)(x - b)(x - c)
        # x^3 - (a+b+c)x^2 + (ab+ac+bc)x - abc
        sum_roots = a + b + c
        sum_products = a*b + a*c + b*c
        product_roots = a * b * c

        latex = f"\\text{{Factor: }} x^3 - {sum_roots}x^2 + {sum_products}x - {product_roots}"
        solution = f"(x - {a})(x - {b})(x - {c})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Quartic factoring
        a = random.randint(1, 3)
        b = random.randint(1, 3)

        # x^4 - (a^2 + b^2)x^2 + a^2*b^2 = (x^2 - a^2)(x^2 - b^2)
        middle_coef = a**2 + b**2
        last_coef = a**2 * b**2

        latex = f"\\text{{Factor: }} x^4 - {middle_coef}x^2 + {last_coef}"
        solution = f"(x^2 - {a**2})(x^2 - {b**2})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = FactoringHigherDegreePolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
