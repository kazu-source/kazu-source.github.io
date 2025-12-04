"""
Factoring Quadratics by Grouping Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FactoringQuadraticsGroupingGenerator:
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
        # Simple grouping with clear common factors
        a = random.randint(1, 3)
        b = random.randint(1, 4)
        c = random.randint(1, 3)

        # (ax + b)(x + c) = ax² + acx + bx + bc
        term1 = a
        term2 = a * c
        term3 = b
        term4 = b * c
        middle = term2 + term3

        latex = f"\\text{{Factor by grouping: }} {term1}x^2 + {middle}x + {term4}"
        solution = f"({a}x + {b})(x + {c})"
        steps = [
            f"Split middle term: {middle}x = {term2}x + {term3}x",
            f"{term1}x² + {term2}x + {term3}x + {term4}",
            f"Group: ({term1}x² + {term2}x) + ({term3}x + {term4})",
            f"Factor each group: {a}x(x + {c}) + {b}(x + {c})",
            f"Factor out (x + {c}): ({a}x + {b})(x + {c})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Grouping with larger coefficients
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = random.randint(1, 4)

        # (ax + b)(x + c) = ax² + (ac+b)x + bc
        coef_x2 = a
        coef_const = b * c
        middle = a * c + b

        latex = f"\\text{{Factor by grouping: }} {coef_x2}x^2 + {middle}x + {coef_const}"
        solution = f"({a}x + {b})(x + {c})"
        steps = [
            f"Find two numbers that multiply to {a}×{coef_const} = {a*coef_const}",
            f"and add to {middle}",
            f"Numbers are {a*c} and {b}",
            f"{a}x² + {a*c}x + {b}x + {coef_const}",
            f"{a}x(x + {c}) + {b}(x + {c})",
            f"({a}x + {b})(x + {c})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Grouping with negative terms
        a = random.randint(2, 4)
        b = random.randint(1, 5)
        c = random.randint(1, 4)

        # (ax - b)(x - c) = ax² - (ac+b)x + bc
        coef_x2 = a
        coef_const = b * c
        middle = -(a * c + b)

        latex = f"\\text{{Factor by grouping: }} {coef_x2}x^2 - {abs(middle)}x + {coef_const}"
        solution = f"({a}x - {b})(x - {c})"
        steps = [
            f"Find two numbers that multiply to {a}×{coef_const} = {a*coef_const}",
            f"and add to {middle}",
            f"Numbers are -{a*c} and -{b}",
            f"{a}x² - {a*c}x - {b}x + {coef_const}",
            f"{a}x(x - {c}) - {b}(x - {c})",
            f"({a}x - {b})(x - {c})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Grouping with mixed signs
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = random.randint(1, 4)

        # (ax + b)(x - c) = ax² + (-ac+b)x - bc
        coef_x2 = a
        coef_const = -b * c
        middle = -a * c + b

        latex = f"\\text{{Factor by grouping: }} {coef_x2}x^2 {'+' if middle >= 0 else ''}{middle}x - {b*c}"
        solution = f"({a}x + {b})(x - {c})"
        steps = [
            f"Find two numbers that multiply to {a}×(-{b*c}) = {-a*b*c}",
            f"and add to {middle}",
            f"Numbers are -{a*c} and {b}",
            f"{a}x² - {a*c}x + {b}x - {b*c}",
            f"{a}x(x - {c}) + {b}(x - {c})",
            f"({a}x + {b})(x - {c})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FactoringQuadraticsGroupingGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
