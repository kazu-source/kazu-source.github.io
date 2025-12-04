"""
Dividing Polynomials by Linear Factors Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DividingPolynomialsLinearFactorsGenerator:
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
        # Cubic divided by linear (exact division)
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        # (x + a)(x^2 + bx + c)
        coef_x3 = 1
        coef_x2 = a + b
        coef_x1 = a*b + c
        coef_x0 = a * c

        latex = f"\\frac{{x^3 + {coef_x2}x^2 + {coef_x1}x + {coef_x0}}}{{x + {a}}}"
        solution = f"x^2 + {b}x + {c}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Cubic with remainder
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        r = random.randint(1, 9)

        coef_x3 = 1
        coef_x2 = a + b
        coef_x1 = a*b + c
        coef_x0 = a * c + r

        latex = f"\\frac{{x^3 + {coef_x2}x^2 + {coef_x1}x + {coef_x0}}}{{x + {a}}}"
        solution = f"x^2 + {b}x + {c} + \\frac{{{r}}}{{x + {a}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Higher degree division
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        c = random.randint(1, 4)
        d = random.randint(1, 4)

        # (x + a)(x^3 + bx^2 + cx + d)
        coef_x4 = 1
        coef_x3 = a + b
        coef_x2 = a*b + c
        coef_x1 = a*c + d
        coef_x0 = a * d

        latex = f"\\frac{{x^4 + {coef_x3}x^3 + {coef_x2}x^2 + {coef_x1}x + {coef_x0}}}{{x + {a}}}"
        solution = f"x^3 + {b}x^2 + {c}x + {d}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Division by (ax + b)
        a = random.randint(2, 3)
        b = random.randint(1, 5)
        c = random.randint(1, 4)
        d = random.randint(1, 4)

        # For simplicity, exact division
        latex = f"\\frac{{{a}x^3 + {a*c+b}x^2 + {b*c+a*d}x + {b*d}}}{{{a}x + {b}}}"
        solution = f"x^2 + {c}x + {d}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = DividingPolynomialsLinearFactorsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
