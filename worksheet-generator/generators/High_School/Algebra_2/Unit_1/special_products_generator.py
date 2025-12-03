"""
Special Products Generator
Creates problems about special polynomial products (difference of squares, perfect squares)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SpecialProductsGenerator:
    """Generates problems about special polynomial products."""

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
        """Difference of squares (a + b)(a - b) = a^2 - b^2"""
        a = random.randint(2, 10)
        b = random.randint(2, 10)

        result = a**2 - b**2

        latex = f"({a} + {b})({a} - {b})"
        solution = f"{result}"

        steps = [
            f"\\text{{Use difference of squares: }} (a+b)(a-b) = a^2 - b^2",
            f"{a}^2 - {b}^2",
            f"{a**2} - {b**2}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Perfect square trinomial or difference of squares with variables"""
        problem_type = random.choice(['perfect_square', 'difference_squares'])

        if problem_type == 'perfect_square':
            a = random.randint(1, 6)
            b = random.randint(1, 8)
            sign = random.choice(['+', '-'])

            # (ax + b)^2 = a^2x^2 + 2abx + b^2
            # (ax - b)^2 = a^2x^2 - 2abx + b^2
            first = a**2
            middle = 2 * a * b
            last = b**2

            if sign == '+':
                latex = f"({a}x + {b})^2"
                solution = f"{first}x^2 + {middle}x + {last}"
            else:
                latex = f"({a}x - {b})^2"
                solution = f"{first}x^2 - {middle}x + {last}"

            steps = [
                f"\\text{{Use }} (a \\pm b)^2 = a^2 \\pm 2ab + b^2",
                f"({a}x)^2 {sign} 2({a}x)({b}) + {b}^2",
                f"{first}x^2 {sign} {middle}x + {last}"
            ]
        else:
            # (ax + b)(ax - b) = a^2x^2 - b^2
            a = random.randint(1, 5)
            b = random.randint(2, 9)

            first = a**2
            last = b**2

            latex = f"({a}x + {b})({a}x - {b})"
            solution = f"{first}x^2 - {last}"

            steps = [
                f"\\text{{Use difference of squares}}",
                f"({a}x)^2 - {b}^2",
                solution
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Complex special products with coefficients"""
        problem_type = random.choice(['sum_cubes', 'difference_cubes', 'complex_square'])

        if problem_type == 'sum_cubes':
            # a^3 + b^3 = (a + b)(a^2 - ab + b^2)
            a = random.randint(1, 4)
            b = random.randint(1, 4)

            latex = f"(x + {a})(x^2 - {a}x + {a**2})"
            solution = f"x^3 + {a**3}"

            steps = [
                f"\\text{{Sum of cubes pattern: }} (a+b)(a^2-ab+b^2) = a^3+b^3",
                f"x^3 + {a}^3",
                solution
            ]
        elif problem_type == 'difference_cubes':
            # a^3 - b^3 = (a - b)(a^2 + ab + b^2)
            a = random.randint(1, 4)
            b = random.randint(1, 4)

            latex = f"(x - {a})(x^2 + {a}x + {a**2})"
            solution = f"x^3 - {a**3}"

            steps = [
                f"\\text{{Difference of cubes: }} (a-b)(a^2+ab+b^2) = a^3-b^3",
                f"x^3 - {a}^3",
                solution
            ]
        else:
            # (ax^2 + b)^2
            a = random.randint(1, 4)
            b = random.randint(1, 5)

            first = a**2
            middle = 2 * a * b
            last = b**2

            latex = f"({a}x^2 + {b})^2"
            solution = f"{first}x^4 + {middle}x^2 + {last}"

            steps = [
                f"\\text{{Use }} (a+b)^2 = a^2 + 2ab + b^2",
                f"({a}x^2)^2 + 2({a}x^2)({b}) + {b}^2",
                solution
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Multiple special products combined"""
        problem_type = random.choice(['nested', 'multiple_terms'])

        if problem_type == 'nested':
            # (x + a)^2(x - a)^2 = [(x + a)(x - a)]^2 = (x^2 - a^2)^2
            a = random.randint(1, 4)

            a_squared = a**2
            a_fourth = a**4

            latex = f"(x + {a})^2(x - {a})^2"
            solution = f"x^4 - {2 * a_squared}x^2 + {a_fourth}"

            steps = [
                f"\\text{{First use difference of squares: }} (x+{a})(x-{a}) = x^2 - {a_squared}",
                f"\\text{{Then square the result: }} (x^2 - {a_squared})^2",
                f"x^4 - 2({a_squared})x^2 + ({a_squared})^2",
                solution
            ]
        else:
            # (x + a)(x - a)(x^2 + a^2)
            a = random.randint(2, 4)

            a_squared = a**2
            a_fourth = a**4

            latex = f"(x + {a})(x - {a})(x^2 + {a_squared})"
            solution = f"x^4 - {a_fourth}"

            steps = [
                f"\\text{{First: }} (x+{a})(x-{a}) = x^2 - {a_squared}",
                f"\\text{{Then: }} (x^2 - {a_squared})(x^2 + {a_squared})",
                f"\\text{{Difference of squares again}}",
                f"x^4 - {a_fourth}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = SpecialProductsGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
