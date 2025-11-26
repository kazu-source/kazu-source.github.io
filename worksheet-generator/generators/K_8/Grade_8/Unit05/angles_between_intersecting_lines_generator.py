"""
Angles Between Intersecting Lines Generator - Grade 8 Unit 5
Generates problems about angles formed by intersecting lines
Example: Two lines intersect. If one angle is 65°, find the vertical angle.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AnglesBetweenIntersectingLinesGenerator:
    """Generates angles between intersecting lines problems."""

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
        angle = random.randint(30, 80)

        latex = f"\\text{{Two lines intersect forming a }} {angle}° \\text{{ angle. Find the vertical angle.}}"
        solution = f"{angle}°"
        steps = ["\\text{Vertical angles are equal}", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        angle = random.randint(40, 85)
        supplementary = 180 - angle

        latex = f"\\text{{Two lines intersect. One angle is }} {angle}°. \\text{{ Find an adjacent angle.}}"
        solution = f"{supplementary}°"
        steps = [
            "\\text{Adjacent angles are supplementary}",
            f"180° - {angle}° = {supplementary}°"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x = random.randint(15, 45)
        angle = 3 * x

        latex = f"\\text{{Two lines intersect. One angle is }} 3x° \\text{{ and its supplement is }} (180 - 3x)°. \\text{{ If }} x = {x}, \\text{{ find all angles.}}"
        solution = f"{angle}° \\text{{ and }} {180 - angle}°"
        steps = [
            f"\\text{{Angle 1: }} 3({x}) = {angle}°",
            f"\\text{{Angle 2: }} 180 - {angle} = {180 - angle}°",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x = random.randint(10, 30)
        angle1 = 2 * x + 10
        angle2 = 180 - angle1

        latex = f"\\text{{Angles }} (2x + 10)° \\text{{ and }} (3x - 20)° \\text{{ are supplementary. Find }} x."
        # Solve: 2x + 10 + 3x - 20 = 180
        x_solution = (180 + 10) / 5
        solution = f"x = {x_solution}"
        steps = [
            f"2x + 10 + 3x - 20 = 180",
            f"5x - 10 = 180",
            f"5x = 190",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = AnglesBetweenIntersectingLinesGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
