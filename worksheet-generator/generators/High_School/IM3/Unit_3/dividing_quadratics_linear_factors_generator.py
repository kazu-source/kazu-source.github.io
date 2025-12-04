"""
Dividing Quadratics by Linear Factors Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DividingQuadraticsLinearFactorsGenerator:
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
        # (x^2 + bx + c) / (x + a) where (x + a) is a factor
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        # (x + a)(x + b) = x^2 + (a+b)x + ab
        coef_x = a + b
        const = a * b

        latex = f"\\frac{{x^2 + {coef_x}x + {const}}}{{x + {a}}}"
        solution = f"x + {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # With remainder
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        r = random.randint(1, 9)

        # (x + a)(x + b) + r = x^2 + (a+b)x + ab + r
        coef_x = a + b
        const = a * b + r

        latex = f"\\frac{{x^2 + {coef_x}x + {const}}}{{x + {a}}}"
        solution = f"x + {b} + \\frac{{{r}}}{{x + {a}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Leading coefficient not 1
        a = random.randint(2, 4)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        # (ax + b)(x + c) = ax^2 + (ac+b)x + bc
        coef_x2 = a
        coef_x1 = a * c + b
        coef_x0 = b * c

        latex = f"\\frac{{{coef_x2}x^2 + {coef_x1}x + {coef_x0}}}{{x + {c}}}"
        solution = f"{a}x + {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex division with leading coefficient and remainder
        a = random.randint(2, 3)
        b = random.randint(1, 5)
        c = random.randint(1, 4)
        r = random.randint(1, 9)

        coef_x2 = a
        coef_x1 = a * c + b
        coef_x0 = b * c + r

        latex = f"\\frac{{{coef_x2}x^2 + {coef_x1}x + {coef_x0}}}{{x + {c}}}"
        solution = f"{a}x + {b} + \\frac{{{r}}}{{x + {c}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = DividingQuadraticsLinearFactorsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
