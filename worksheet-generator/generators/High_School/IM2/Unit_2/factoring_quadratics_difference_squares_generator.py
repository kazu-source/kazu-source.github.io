"""
Factoring Quadratics - Difference of Squares Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FactoringQuadraticsDifferenceSquaresGenerator:
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
        # Simple x² - a²
        a = random.randint(2, 8)

        latex = f"\\text{{Factor: }} x^2 - {a**2}"
        solution = f"(x + {a})(x - {a})"
        steps = [
            f"Recognize difference of squares: a² - b²",
            f"x² - {a**2} = x² - {a}²",
            f"Use formula: a² - b² = (a + b)(a - b)",
            f"(x + {a})(x - {a})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Coefficient with x
        a = random.randint(2, 6)
        b = random.randint(2, 7)

        coef = a**2
        const = b**2

        latex = f"\\text{{Factor: }} {coef}x^2 - {const}"
        solution = f"({a}x + {b})({a}x - {b})"
        steps = [
            f"Recognize difference of squares",
            f"{coef}x² - {const} = ({a}x)² - {b}²",
            f"Use formula: a² - b² = (a + b)(a - b)",
            f"= ({a}x + {b})({a}x - {b})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Factor out GCF first, then difference of squares
        gcf = random.randint(2, 5)
        a = random.randint(1, 4)
        b = random.randint(2, 5)

        coef_x2 = gcf * a**2
        const = gcf * b**2

        latex = f"\\text{{Factor completely: }} {coef_x2}x^2 - {const}"
        solution = f"{gcf}({a}x + {b})({a}x - {b})"
        steps = [
            f"First factor out GCF = {gcf}",
            f"{gcf}({a**2}x² - {b**2})",
            f"Recognize difference of squares: ({a}x)² - {b}²",
            f"{gcf}[({a}x)² - {b}²]",
            f"{gcf}({a}x + {b})({a}x - {b})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Higher powers that are perfect squares
        a = random.randint(2, 4)
        power = random.choice([2, 3])
        b = random.randint(2, 5)

        total_power = 2 * power
        const = b**2

        latex = f"\\text{{Factor: }} x^{total_power} - {const}"
        solution = f"(x^{power} + {b})(x^{power} - {b})"
        steps = [
            f"Recognize difference of squares",
            f"x^{total_power} - {const} = (x^{power})² - {b}²",
            f"Use formula: a² - b² = (a + b)(a - b)",
            f"= (x^{power} + {b})(x^{power} - {b})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FactoringQuadraticsDifferenceSquaresGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
