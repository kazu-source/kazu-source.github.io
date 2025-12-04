"""
Polynomial Identities Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PolynomialIdentitiesGenerator:
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
        # Verify simple identity
        a = random.randint(2, 9)

        latex = f"\\text{{Verify: }} (x + {a})^2 = x^2 + {2*a}x + {a**2}"
        solution = "True (perfect square identity)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Difference of squares identity
        a = random.randint(2, 9)
        b = random.randint(2, 9)

        latex = f"\\text{{Expand using identity: }} ({a}x + {b})({a}x - {b})"
        solution = f"{a**2}x^2 - {b**2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Sum of cubes identity
        a = random.randint(2, 5)

        latex = f"\\text{{Factor using identity: }} x^3 + {a**3}"
        solution = f"(x + {a})(x^2 - {a}x + {a**2})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex polynomial identity
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        # (a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3
        latex = f"\\text{{Expand: }} (x + {a})^3"
        solution = f"x^3 + {3*a}x^2 + {3*a**2}x + {a**3}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = PolynomialIdentitiesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
