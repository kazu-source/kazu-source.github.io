"""
Pythagorean Theorem and Distance Generator - Grade 8 Unit 5
Generates problems using Pythagorean theorem to find distance
Example: Find distance between (1, 2) and (4, 6).
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PythagoreanTheoremAndDistanceGenerator:
    """Generates Pythagorean theorem and distance problems."""

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
        x1, y1 = 0, 0
        x2, y2 = random.randint(3, 5), random.randint(4, 6)
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        latex = f"\\text{{Find distance from }} ({x1}, {y1}) \\text{{ to }} ({x2}, {y2}) \\text{{ (nearest tenth).}}"
        solution = f"{distance:.1f}"
        steps = [
            f"d = \\sqrt{{({x2} - {x1})^2 + ({y2} - {y1})^2}}",
            f"d = \\sqrt{{{x2}^2 + {y2}^2}}",
            f"d = \\sqrt{{{x2**2 + y2**2}}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x1, y1 = random.randint(1, 5), random.randint(1, 5)
        x2, y2 = random.randint(6, 10), random.randint(6, 10)
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        latex = f"\\text{{Find distance from }} ({x1}, {y1}) \\text{{ to }} ({x2}, {y2}).}}"
        solution = f"{distance:.1f}"
        steps = [
            f"d = \\sqrt{{({x2} - {x1})^2 + ({y2} - {y1})^2}}",
            f"d = \\sqrt{{{(x2-x1)**2} + {(y2-y1)**2}}}",
            f"d = \\sqrt{{{(x2-x1)**2 + (y2-y1)**2}}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(-5, 0), random.randint(-5, 0)
        x2, y2 = random.randint(3, 8), random.randint(3, 8)
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        latex = f"\\text{{Find distance from }} ({x1}, {y1}) \\text{{ to }} ({x2}, {y2}).}}"
        solution = f"{distance:.1f}"
        steps = [
            f"d = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}}",
            f"d = \\sqrt{{{(x2-x1)**2} + {(y2-y1)**2}}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Points forming Pythagorean triple distance
        x1, y1 = 1, 2
        x2, y2 = 4, 6  # Distance = 5
        distance = 5

        latex = f"\\text{{Find exact distance from }} ({x1}, {y1}) \\text{{ to }} ({x2}, {y2}).}}"
        solution = f"{distance}"
        steps = [
            f"d = \\sqrt{{({x2} - {x1})^2 + ({y2} - {y1})^2}}",
            f"d = \\sqrt{{3^2 + 4^2}}",
            f"d = \\sqrt{{9 + 16}} = \\sqrt{{25}} = 5"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = PythagoreanTheoremAndDistanceGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
