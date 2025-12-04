"""
Special Products of Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SpecialProductsPolynomialsGenerator:
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
        # Perfect square: (x + a)^2
        a = random.randint(1, 9)

        latex = f"(x + {a})^2"
        solution = f"x^2 + {2*a}x + {a**2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Difference of squares: (a + b)(a - b)
        a = random.randint(2, 9)
        b = random.randint(1, 9)

        latex = f"({a}x + {b})({a}x - {b})"
        solution = f"{a**2}x^2 - {b**2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Perfect square trinomial: (ax + b)^2
        a = random.randint(2, 5)
        b = random.randint(1, 9)

        latex = f"({a}x + {b})^2"
        solution = f"{a**2}x^2 + {2*a*b}x + {b**2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Sum and difference of cubes or complex special product
        pattern = random.choice(['cube_sum', 'cube_diff', 'square_binomial'])

        if pattern == 'cube_sum':
            a = random.randint(1, 5)
            latex = f"(x + {a})(x^2 - {a}x + {a**2})"
            solution = f"x^3 + {a**3}"
        elif pattern == 'cube_diff':
            a = random.randint(1, 5)
            latex = f"(x - {a})(x^2 + {a}x + {a**2})"
            solution = f"x^3 - {a**3}"
        else:
            a = random.randint(2, 5)
            b = random.randint(1, 5)
            latex = f"({a}x - {b})^2"
            solution = f"{a**2}x^2 - {2*a*b}x + {b**2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = SpecialProductsPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
