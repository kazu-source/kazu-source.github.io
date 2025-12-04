"""
Higher Degree Polynomial Factorization Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class HigherDegreePolynomialFactorizationGenerator:
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
        # x^3 + ax^2 + bx with common factor x
        a = random.randint(2, 8)
        b = random.randint(2, 10)

        latex = f"x^3 + {a}x^2 + {b}x"
        solution = f"x(x^2 + {a}x + {b})"
        steps = [
            f"Factor out x",
            f"x(x^2 + {a}x + {b})",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Cubic with grouping: x^3 + ax^2 + bx + ab = (x^2)(x+a) + b(x+a)
        a = random.randint(2, 6)
        b = random.randint(2, 6)

        latex = f"x^3 + {a}x^2 + {b}x + {a*b}"
        solution = f"(x^2 + {b})(x + {a})"
        steps = [
            f"Group terms: (x^3 + {a}x^2) + ({b}x + {a*b})",
            f"Factor each group: x^2(x + {a}) + {b}(x + {a})",
            f"Factor out common binomial: (x + {a})(x^2 + {b})",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # x^4 - a^2 (difference of squares with higher powers)
        a = random.randint(2, 6)
        a_sq = a * a

        latex = f"x^4 - {a_sq}"
        solution = f"(x^2 + {a})(x^2 - {a})"
        steps = [
            f"Recognize as difference of squares: (x^2)^2 - {a}^2",
            f"Factor: (x^2 + {a})(x^2 - {a})",
            f"x^2 - {a} can be factored further over reals if desired",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Factor by grouping with 4 terms
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        c = random.randint(2, 5)

        # ax^3 + bx^2 + acx + bc = x^2(ax+b) + c(ax+b)
        coef1 = a
        coef2 = b
        coef3 = a * c
        coef4 = b * c

        latex = f"{coef1}x^3 + {coef2}x^2 + {coef3}x + {coef4}"
        solution = f"(x^2 + {c})({a}x + {b})"
        steps = [
            f"Group: ({coef1}x^3 + {coef2}x^2) + ({coef3}x + {coef4})",
            f"Factor first group: x^2({a}x + {b})",
            f"Factor second group: {c}({a}x + {b})",
            f"Factor out ({a}x + {b}): (x^2 + {c})({a}x + {b})",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = HigherDegreePolynomialFactorizationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
