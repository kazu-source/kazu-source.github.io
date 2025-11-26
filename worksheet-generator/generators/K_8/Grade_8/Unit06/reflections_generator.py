"""
Reflections Generator - Grade 8 Unit 6
Generates reflection problems
Example: Reflect (3, 4) over the x-axis.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ReflectionsGenerator:
    """Generates reflections problems."""

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
        x, y = random.randint(2, 8), random.randint(2, 8)

        latex = f"\\text{{Reflect }} ({x}, {y}) \\text{{ over the x-axis.}}"
        solution = f"({x}, {-y})"
        steps = [
            "\\text{Over x-axis: } (x, y) \\to (x, -y)",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x, y = random.randint(2, 8), random.randint(2, 8)

        latex = f"\\text{{Reflect }} ({x}, {y}) \\text{{ over the y-axis.}}"
        solution = f"({-x}, {y})"
        steps = [
            "\\text{Over y-axis: } (x, y) \\to (-x, y)",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x, y = random.randint(2, 8), random.randint(2, 8)

        latex = f"\\text{{Reflect }} ({x}, {y}) \\text{{ over the line }} y = x."
        solution = f"({y}, {x})"
        steps = [
            "\\text{Over } y = x: (x, y) \\to (y, x)",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x, y = random.randint(2, 8), random.randint(2, 8)

        latex = f"\\text{{Reflect }} ({x}, {y}) \\text{{ over the line }} y = -x."
        solution = f"({-y}, {-x})"
        steps = [
            "\\text{Over } y = -x: (x, y) \\to (-y, -x)",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = ReflectionsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
