"""
Triangle Angles Generator - Grade 8 Unit 5
Generates problems about triangle angle relationships
Example: A triangle has angles 60°, 70°, and x°. Find x.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class TriangleAnglesGenerator:
    """Generates triangle angles problems."""

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
        angle1 = random.randint(40, 70)
        angle2 = random.randint(40, 70)
        angle3 = 180 - angle1 - angle2

        latex = f"\\text{{A triangle has angles }} {angle1}°, {angle2}°, \\text{{ and }} x°. \\text{{ Find }} x."
        solution = f"x = {angle3}°"
        steps = [
            f"{angle1} + {angle2} + x = 180",
            f"x = 180 - {angle1} - {angle2}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x = random.randint(15, 40)
        angle1 = 2 * x
        angle2 = 3 * x
        angle3 = 180 - angle1 - angle2

        latex = f"\\text{{A triangle has angles }} 2x°, 3x°, \\text{{ and }} {angle3}°. \\text{{ Find }} x."
        solution = f"x = {x}°"
        steps = [
            f"2x + 3x + {angle3} = 180",
            f"5x = {180 - angle3}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x = random.randint(10, 25)
        angle1 = x + 20
        angle2 = 2 * x
        angle3 = 180 - angle1 - angle2

        latex = f"\\text{{Triangle angles are }} (x + 20)°, 2x°, \\text{{ and }} {angle3}°. \\text{{ Find all angles.}}"
        solution = f"{angle1}°, {angle2}°, {angle3}°"
        steps = [
            f"(x + 20) + 2x + {angle3} = 180",
            f"3x + {20 + angle3} = 180",
            f"x = {x}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        base_angle = random.randint(65, 75)
        vertex_angle = 180 - 2 * base_angle

        latex = f"\\text{{An isosceles triangle has base angles of }} {base_angle}° \\text{{ each. Find the vertex angle.}}"
        solution = f"{vertex_angle}°"
        steps = [
            f"{base_angle} + {base_angle} + x = 180",
            f"x = 180 - {2 * base_angle}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = TriangleAnglesGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
