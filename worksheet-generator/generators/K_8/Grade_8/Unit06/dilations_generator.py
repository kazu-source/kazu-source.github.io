"""
Dilations Generator - Grade 8 Unit 6
Generates dilation problems
Example: Dilate (4, 6) by scale factor 2 from origin.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DilationsGenerator:
    """Generates dilations problems."""

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
        k = random.randint(2, 4)

        latex = f"\\text{{Dilate }} ({x}, {y}) \\text{{ by scale factor }} {k} \\text{{ from origin.}}"
        solution = f"({k * x}, {k * y})"
        steps = [
            f"(kx, ky) = ({k} \\times {x}, {k} \\times {y})",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x, y = random.randint(4, 12), random.randint(4, 12)
        k = random.choice([0.5, 0.25])
        k_frac = "\\frac{1}{2}" if k == 0.5 else "\\frac{1}{4}"

        latex = f"\\text{{Dilate }} ({x}, {y}) \\text{{ by scale factor }} {k_frac} \\text{{ from origin.}}"
        solution = f"({int(k * x)}, {int(k * y)})"
        steps = [
            f"({k} \\times {x}, {k} \\times {y})",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x, y = random.randint(2, 5), random.randint(2, 5)
        x2, y2 = random.randint(8, 15), random.randint(8, 15)

        # Calculate scale factor
        k_x = x2 / x
        k_y = y2 / y

        if abs(k_x - k_y) < 0.01:
            k = k_x
            latex = f"\\text{{What scale factor maps }} ({x}, {y}) \\text{{ to }} ({x2}, {y2})?"
            solution = f"k = {k:.0f}" if k == int(k) else f"k = {k:.1f}"
            steps = [
                f"k = \\frac{{{x2}}}{{{x}}} = {k:.1f}",
                solution
            ]
        else:
            latex = f"\\text{{Find scale factor}}"
            solution = f"k = {k_x:.1f}"
            steps = [solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        side = random.randint(4, 8)
        k = random.randint(2, 4)
        new_side = side * k

        latex = f"\\text{{A square with side }} {side} \\text{{ is dilated by }} {k}. \\text{{ Find new side length.}}"
        solution = f"{new_side}"
        steps = [
            f"\\text{{New side}} = {k} \\times {side}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = DilationsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
