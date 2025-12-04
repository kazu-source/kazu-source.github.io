"""
Multiplying Binomials and Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MultiplyingBinomialsPolynomialsGenerator:
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
        # (x + a)(x + b)
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        latex = f"(x + {a})(x + {b})"
        solution = f"x^2 + {a+b}x + {a*b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # (ax + b)(cx + d)
        a = random.randint(2, 5)
        b = random.randint(-9, 9)
        c = random.randint(2, 5)
        d = random.randint(-9, 9)

        first = a * c
        outer_inner = a * d + b * c
        last = b * d

        latex = f"({a}x + {b})({c}x + {d})"
        solution = f"{first}x^2 + {outer_inner}x + {last}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Binomial times trinomial
        a = random.randint(1, 5)
        b = random.randint(-5, 5)
        c = random.randint(1, 5)
        d = random.randint(-5, 5)
        e = random.randint(-5, 5)

        coef_x3 = a * c
        coef_x2 = a * d + b * c
        coef_x1 = a * e + b * d
        coef_x0 = b * e

        latex = f"({a}x + {b})({c}x^2 + {d}x + {e})"
        solution = f"{coef_x3}x^3 + {coef_x2}x^2 + {coef_x1}x + {coef_x0}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Two trinomials multiplied
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)
        d = random.randint(1, 3)
        e = random.randint(-5, 5)
        f = random.randint(-5, 5)

        coef_x4 = a * d
        coef_x3 = a * e + b * d
        coef_x2 = a * f + b * e + c * d
        coef_x1 = b * f + c * e
        coef_x0 = c * f

        latex = f"({a}x^2 + {b}x + {c})({d}x^2 + {e}x + {f})"
        solution = f"{coef_x4}x^4 + {coef_x3}x^3 + {coef_x2}x^2 + {coef_x1}x + {coef_x0}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = MultiplyingBinomialsPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
