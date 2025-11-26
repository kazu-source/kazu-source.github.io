"""
Intro to Systems of Equations Generator - Grade 8 Unit 4
Generates introductory systems of equations problems
Example: Does (2, 3) satisfy both y = x + 1 and y = 2x - 1?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IntroToSystemsOfEquationsGenerator:
    """Generates intro to systems of equations problems."""

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
        x, y = random.randint(1, 6), random.randint(2, 10)
        m1, b1 = random.randint(1, 4), y - random.randint(1, 4) * x
        y_check = m1 * x + b1

        is_solution = (y == y_check)

        latex = f"\\text{{Is }} ({x}, {y}) \\text{{ a solution to }} y = {m1}x + {b1}?"
        solution = "\\text{Yes}" if is_solution else "\\text{No}"
        steps = [
            f"{y} = {m1}({x}) + {b1}",
            f"{y} = {y_check}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x, y = random.randint(1, 6), random.randint(5, 15)
        m1, b1 = random.randint(1, 3), y - random.randint(1, 3) * x
        m2, b2 = random.randint(2, 5), y - random.randint(2, 5) * x

        y1 = m1 * x + b1
        y2 = m2 * x + b2

        is_solution = (y == y1 and y == y2)

        latex = f"\\text{{Is }} ({x}, {y}) \\text{{ a solution to both }} y = {m1}x + {b1} \\text{{ and }} y = {m2}x + {b2}?"
        solution = "\\text{Yes}" if is_solution else "\\text{No}"
        steps = [
            f"\\text{{Check eq 1: }} {y} = {m1}({x}) + {b1} = {y1}",
            f"\\text{{Check eq 2: }} {y} = {m2}({x}) + {b2} = {y2}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x = random.randint(2, 6)
        m1, m2 = random.randint(2, 5), random.randint(1, 4)
        b1, b2 = random.randint(1, 8), random.randint(3, 10)
        y = m1 * x + b1

        latex = f"\\text{{Find y if }} ({x}, y) \\text{{ is a solution to }} y = {m1}x + {b1}"
        solution = f"y = {y}"
        steps = [
            f"y = {m1}({x}) + {b1}",
            f"y = {y}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        m1, m2 = random.randint(2, 5), random.randint(1, 4)
        b1, b2 = random.randint(1, 6), random.randint(5, 12)

        # Find intersection
        if m1 != m2:
            x = (b2 - b1) / (m1 - m2)
            y = m1 * x + b1
        else:
            x, y = 2, 10

        latex = f"\\text{{Find the solution to }} y = {m1}x + {b1} \\text{{ and }} y = {m2}x + {b2}"
        solution = f"({x:.1f}, {y:.1f})" if x != int(x) else f"({int(x)}, {int(y)})"
        steps = [
            f"{m1}x + {b1} = {m2}x + {b2}",
            f"{m1 - m2}x = {b2 - b1}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = IntroToSystemsOfEquationsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
