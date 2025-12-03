"""
Polynomial Addition and Subtraction Generator
Creates problems about adding and subtracting polynomials
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class PolynomialAddSubtractGenerator:
    """Generates problems about adding and subtracting polynomials."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Add or subtract simple binomials"""
        a1 = random.randint(1, 9)
        b1 = random.randint(-10, 10)
        a2 = random.randint(1, 9)
        b2 = random.randint(-10, 10)

        operation = random.choice(['+', '-'])

        if operation == '+':
            result_a = a1 + a2
            result_b = b1 + b2
            latex = f"({a1}x + {b1}) + ({a2}x + {b2})"
        else:
            result_a = a1 - a2
            result_b = b1 - b2
            latex = f"({a1}x + {b1}) - ({a2}x + {b2})"

        if result_b >= 0:
            solution = f"{result_a}x + {result_b}"
        else:
            solution = f"{result_a}x - {abs(result_b)}"

        steps = [
            f"\\text{{Combine like terms}}",
            f"({a1} {operation} {a2})x + ({b1} {operation} {b2})",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Add or subtract trinomials"""
        a1 = random.randint(1, 5)
        b1 = random.randint(-8, 8)
        c1 = random.randint(-10, 10)

        a2 = random.randint(1, 5)
        b2 = random.randint(-8, 8)
        c2 = random.randint(-10, 10)

        operation = random.choice(['+', '-'])

        if operation == '+':
            result_a = a1 + a2
            result_b = b1 + b2
            result_c = c1 + c2
            latex = f"({a1}x^2 + {b1}x + {c1}) + ({a2}x^2 + {b2}x + {c2})"
        else:
            result_a = a1 - a2
            result_b = b1 - b2
            result_c = c1 - c2
            latex = f"({a1}x^2 + {b1}x + {c1}) - ({a2}x^2 + {b2}x + {c2})"

        solution = f"{result_a}x^2 + {result_b}x + {result_c}"

        steps = [
            f"\\text{{Combine like terms}}",
            f"({a1} {operation} {a2})x^2 + ({b1} {operation} {b2})x + ({c1} {operation} {c2})",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Add or subtract polynomials with multiple variables"""
        a1 = random.randint(1, 5)
        b1 = random.randint(-6, 6)
        c1 = random.randint(-8, 8)

        a2 = random.randint(1, 5)
        b2 = random.randint(-6, 6)
        c2 = random.randint(-8, 8)

        operation = random.choice(['+', '-'])

        if operation == '+':
            result_a = a1 + a2
            result_b = b1 + b2
            result_c = c1 + c2
            latex = f"({a1}x^2 + {b1}xy + {c1}y^2) + ({a2}x^2 + {b2}xy + {c2}y^2)"
        else:
            result_a = a1 - a2
            result_b = b1 - b2
            result_c = c1 - c2
            latex = f"({a1}x^2 + {b1}xy + {c1}y^2) - ({a2}x^2 + {b2}xy + {c2}y^2)"

        solution = f"{result_a}x^2 + {result_b}xy + {result_c}y^2"

        steps = [
            f"\\text{{Combine like terms}}",
            f"({a1} {operation} {a2})x^2 + ({b1} {operation} {b2})xy + ({c1} {operation} {c2})y^2",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex polynomial operations with multiple terms"""
        a1 = random.randint(1, 4)
        b1 = random.randint(-5, 5)
        c1 = random.randint(-6, 6)
        d1 = random.randint(-8, 8)

        a2 = random.randint(1, 4)
        b2 = random.randint(-5, 5)
        c2 = random.randint(-6, 6)
        d2 = random.randint(-8, 8)

        a3 = random.randint(1, 3)
        b3 = random.randint(-4, 4)
        c3 = random.randint(-5, 5)
        d3 = random.randint(-7, 7)

        result_a = a1 + a2 - a3
        result_b = b1 + b2 - b3
        result_c = c1 + c2 - c3
        result_d = d1 + d2 - d3

        latex = f"({a1}x^3 + {b1}x^2 + {c1}x + {d1}) + ({a2}x^3 + {b2}x^2 + {c2}x + {d2}) - ({a3}x^3 + {b3}x^2 + {c3}x + {d3})"
        solution = f"{result_a}x^3 + {result_b}x^2 + {result_c}x + {result_d}"

        steps = [
            f"\\text{{Combine like terms}}",
            f"({a1} + {a2} - {a3})x^3 + ({b1} + {b2} - {b3})x^2 + ({c1} + {c2} - {c3})x + ({d1} + {d2} - {d3})",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = PolynomialAddSubtractGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
