"""
Translations Generator - Grade 8 Unit 6
Generates translation problems
Example: Translate point (2, 3) by (4, -1).
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class TranslationsGenerator:
    """Generates translations problems."""

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
        x, y = random.randint(1, 8), random.randint(1, 8)
        dx, dy = random.randint(2, 5), random.randint(2, 5)

        latex = f"\\text{{Translate }} ({x}, {y}) \\text{{ by }} ({dx}, {dy})."
        solution = f"({x + dx}, {y + dy})"
        steps = [
            f"(x + {dx}, y + {dy})",
            f"({x} + {dx}, {y} + {dy})",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x, y = random.randint(-3, 3), random.randint(-3, 3)
        dx, dy = random.randint(-4, 4), random.randint(-4, 4)

        dx_str = f"+{dx}" if dx >= 0 else str(dx)
        dy_str = f"+{dy}" if dy >= 0 else str(dy)

        latex = f"\\text{{Translate }} ({x}, {y}) \\text{{ by }} ({dx}, {dy})."
        solution = f"({x + dx}, {y + dy})"
        steps = [
            f"({x} {dx_str}, {y} {dy_str})",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x, y = random.randint(1, 6), random.randint(1, 6)
        x2, y2 = random.randint(7, 12), random.randint(7, 12)
        dx, dy = x2 - x, y2 - y

        latex = f"\\text{{What translation maps }} ({x}, {y}) \\text{{ to }} ({x2}, {y2})?"
        solution = f"({dx}, {dy})"
        steps = [
            f"\\Delta x = {x2} - {x} = {dx}",
            f"\\Delta y = {y2} - {y} = {dy}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        points = [(1, 2), (3, 4), (5, 2)]
        dx, dy = random.randint(2, 5), random.randint(-3, -1)
        translated = [(x + dx, y + dy) for x, y in points]

        latex = f"\\text{{Translate triangle with vertices }} {points[0]}, {points[1]}, {points[2]} \\text{{ by }} ({dx}, {dy})."
        solution = f"{translated[0]}, {translated[1]}, {translated[2]}"
        steps = [
            f"\\text{{Apply to each vertex}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = TranslationsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
