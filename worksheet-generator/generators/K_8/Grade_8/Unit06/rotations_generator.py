"""
Rotations Generator - Grade 8 Unit 6
Generates rotation problems
Example: Rotate (3, 4) by 90° counterclockwise around origin.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RotationsGenerator:
    """Generates rotations problems."""

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
        x, y = random.randint(2, 6), random.randint(2, 6)

        latex = f"\\text{{Rotate }} ({x}, {y}) \\text{{ by 90° CCW around origin.}}"
        solution = f"({-y}, {x})"
        steps = [
            "\\text{90° CCW: } (x, y) \\to (-y, x)",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x, y = random.randint(2, 6), random.randint(2, 6)

        latex = f"\\text{{Rotate }} ({x}, {y}) \\text{{ by 180° around origin.}}"
        solution = f"({-x}, {-y})"
        steps = [
            "\\text{180°: } (x, y) \\to (-x, -y)",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x, y = random.randint(2, 6), random.randint(2, 6)

        latex = f"\\text{{Rotate }} ({x}, {y}) \\text{{ by 270° CCW around origin.}}"
        solution = f"({y}, {-x})"
        steps = [
            "\\text{270° CCW: } (x, y) \\to (y, -x)",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x, y = random.randint(2, 5), random.randint(2, 5)

        latex = f"\\text{{Rotate }} ({x}, {y}) \\text{{ by 90° CW around origin.}}"
        solution = f"({y}, {-x})"
        steps = [
            "\\text{90° CW = 270° CCW}",
            "\\text{270° CCW: } (x, y) \\to (y, -x)",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = RotationsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
