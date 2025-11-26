"""
Volume Generator - Grade 8 Unit 6
Generates problems about volume of 3D shapes
Example: Find the volume of a cylinder with radius 3 and height 5.
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class VolumeGenerator:
    """Generates volume problems."""

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
        l, w, h = random.randint(3, 8), random.randint(3, 8), random.randint(3, 8)
        volume = l * w * h

        latex = f"\\text{{Find volume of rectangular prism: length }} {l}, \\text{{ width }} {w}, \\text{{ height }} {h}."
        solution = f"{volume} \\text{{ cubic units}}"
        steps = [
            f"V = l \\times w \\times h",
            f"V = {l} \\times {w} \\times {h}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        r = random.randint(2, 6)
        h = random.randint(4, 10)
        volume = math.pi * r**2 * h

        latex = f"\\text{{Find volume of cylinder: radius }} {r}, \\text{{ height }} {h}. \\text{{ Use }} \\pi \\approx 3.14."
        solution = f"{volume:.1f} \\text{{ cubic units}}"
        steps = [
            f"V = \\pi r^2 h",
            f"V = 3.14 \\times {r}^2 \\times {h}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        s = random.randint(4, 10)
        volume = s ** 3

        latex = f"\\text{{Find volume of cube with side length }} {s}."
        solution = f"{volume} \\text{{ cubic units}}"
        steps = [
            f"V = s^3",
            f"V = {s}^3",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        r = random.randint(3, 6)
        volume = (4/3) * math.pi * r**3

        latex = f"\\text{{Find volume of sphere with radius }} {r}."
        solution = f"{volume:.1f} \\text{{ cubic units}}"
        steps = [
            f"V = \\frac{{4}}{{3}}\\pi r^3",
            f"V = \\frac{{4}}{{3}} \\times 3.14 \\times {r}^3",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = VolumeGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
