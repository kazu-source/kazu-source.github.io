"""
Multiplying Monomials and Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MultiplyingMonomialsPolynomialsGenerator:
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
        # Monomial times binomial
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)

        latex = f"{a}x({b}x + {c})"
        solution = f"{a*b}x^2 + {a*c}x"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Monomial times trinomial
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(-9, 9)
        d = random.randint(-9, 9)

        latex = f"{a}x^2({b}x^2 + {c}x + {d})"
        solution = f"{a*b}x^4 + {a*c}x^3 + {a*d}x^2"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Negative monomial times polynomial
        a = random.randint(-5, -2)
        b = random.randint(1, 5)
        c = random.randint(-9, 9)
        d = random.randint(-9, 9)
        e = random.randint(-9, 9)

        latex = f"{a}x({b}x^3 + {c}x^2 + {d}x + {e})"
        solution = f"{a*b}x^4 + {a*c}x^3 + {a*d}x^2 + {a*e}x"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex monomial times polynomial
        a = random.randint(2, 4)
        b = random.randint(2, 4)
        c = random.randint(1, 5)
        d = random.randint(-9, 9)
        e = random.randint(-9, 9)

        latex = f"{a}x^2y({c}x^2y + {d}xy^2 + {e})"
        solution = f"{a*c}x^4y^2 + {a*d}x^3y^3 + {a*e}x^2y"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = MultiplyingMonomialsPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
