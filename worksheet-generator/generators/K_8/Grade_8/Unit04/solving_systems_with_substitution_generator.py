"""
Solving Systems with Substitution Generator - Grade 8 Unit 4
Generates problems about solving systems using substitution method
Example: Solve: y = 2x + 1, y = x + 3
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SolvingSystemsWithSubstitutionGenerator:
    """Generates solving systems with substitution problems."""

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
        x = random.randint(1, 6)
        m1, m2 = random.randint(1, 4), random.randint(2, 5)
        b = random.randint(1, 8)
        y = m1 * x + b
        c = y - m2 * x

        latex = f"\\text{{Solve: }} y = {m1}x + {b}, y = {m2}x + {c}"
        solution = f"({x}, {y})"
        steps = [
            f"{m1}x + {b} = {m2}x + {c}",
            f"{m1 - m2}x = {c - b}",
            f"x = {x}",
            f"y = {m1}({x}) + {b} = {y}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x, y = random.randint(2, 6), random.randint(5, 15)
        a, b, c = random.randint(2, 4), random.randint(1, 3), random.randint(2, 5)

        # y = mx + b format for first equation
        m1 = random.randint(2, 5)
        b1 = y - m1 * x

        # ax + by = c format for second equation
        c_val = a * x + b * y

        latex = f"\\text{{Solve: }} y = {m1}x + {b1}, {a}x + {b}y = {c_val}"
        solution = f"({x}, {y})"
        steps = [
            f"\\text{{Substitute }} y = {m1}x + {b1} \\text{{ into equation 2}}",
            f"{a}x + {b}({m1}x + {b1}) = {c_val}",
            f"{a + b * m1}x + {b * b1} = {c_val}",
            f"x = {x}, y = {y}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x, y = random.randint(1, 6), random.randint(3, 12)
        a, b, c, d = random.randint(2, 4), random.randint(2, 4), random.randint(1, 3), random.randint(2, 5)

        val1 = a * x + b * y
        val2 = c * x + d * y

        latex = f"\\text{{Solve: }} {a}x + {b}y = {val1}, {c}x + {d}y = {val2}"
        solution = f"({x}, {y})"
        steps = [
            f"\\text{{Solve first for }} y: y = \\frac{{{val1} - {a}x}}{{{b}}}",
            f"\\text{{Substitute into second equation}}",
            f"x = {x}, y = {y}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x, y = random.randint(2, 5), random.randint(4, 10)
        a, b = random.randint(2, 4), random.randint(2, 4)

        # Create system with fractions
        val1 = a * x - b * y
        val2 = a * x + b * y

        latex = f"\\text{{Solve: }} {a}x - {b}y = {val1}, {a}x + {b}y = {val2}"
        solution = f"({x}, {y})"
        steps = [
            f"\\text{{From eq 1: }} x = \\frac{{{val1} + {b}y}}{{{a}}}",
            f"\\text{{Substitute into eq 2}}",
            f"y = {y}, x = {x}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = SolvingSystemsWithSubstitutionGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
