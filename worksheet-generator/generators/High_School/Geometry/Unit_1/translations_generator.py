"""
Translations Generator
Creates problems about translating points and shapes on a coordinate plane
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class TranslationsGenerator:
    """Generates problems about translations on the coordinate plane."""

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
        """Translate a single point by a vector with positive values"""
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)
        dx = random.randint(1, 5)
        dy = random.randint(1, 5)

        new_x = x + dx
        new_y = y + dy

        latex = f"\\text{{Translate point }} ({x}, {y}) \\text{{ by vector }} \\langle {dx}, {dy} \\rangle"
        solution = f"({new_x}, {new_y})"

        steps = [
            f"\\text{{Apply translation: }} (x + dx, y + dy)",
            f"x' = {x} + {dx} = {new_x}",
            f"y' = {y} + {dy} = {new_y}",
            f"\\text{{New point: }} ({new_x}, {new_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Translate a point with positive and negative vector components"""
        x = random.randint(-8, 8)
        y = random.randint(-8, 8)
        dx = random.randint(-6, 6)
        dy = random.randint(-6, 6)
        while dx == 0 and dy == 0:
            dx = random.randint(-6, 6)
            dy = random.randint(-6, 6)

        new_x = x + dx
        new_y = y + dy

        latex = f"\\text{{Translate point }} ({x}, {y}) \\text{{ by vector }} \\langle {dx}, {dy} \\rangle"
        solution = f"({new_x}, {new_y})"

        steps = [
            f"\\text{{Apply translation: }} (x + dx, y + dy)",
            f"x' = {x} + ({dx}) = {new_x}",
            f"y' = {y} + ({dy}) = {new_y}",
            f"\\text{{New point: }} ({new_x}, {new_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Find the translation vector given original and image points"""
        x1 = random.randint(-8, 8)
        y1 = random.randint(-8, 8)
        dx = random.randint(-7, 7)
        dy = random.randint(-7, 7)
        while dx == 0 and dy == 0:
            dx = random.randint(-7, 7)
            dy = random.randint(-7, 7)

        x2 = x1 + dx
        y2 = y1 + dy

        latex = f"\\text{{Point }} A({x1}, {y1}) \\text{{ is translated to }} A'({x2}, {y2}). \\text{{ Find the translation vector.}}"
        solution = f"\\langle {dx}, {dy} \\rangle"

        steps = [
            f"\\text{{Translation vector}} = (x_2 - x_1, y_2 - y_1)",
            f"dx = {x2} - {x1} = {dx}",
            f"dy = {y2} - {y1} = {dy}",
            f"\\text{{Translation vector: }} \\langle {dx}, {dy} \\rangle"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Translate a triangle and find the coordinates of all vertices"""
        problem_type = random.choice(['triangle', 'composition'])

        if problem_type == 'triangle':
            # Generate triangle vertices
            x1, y1 = random.randint(-5, 3), random.randint(-5, 3)
            x2, y2 = x1 + random.randint(2, 4), y1 + random.randint(0, 3)
            x3, y3 = x1 + random.randint(0, 2), y1 + random.randint(2, 4)

            dx = random.randint(-4, 4)
            dy = random.randint(-4, 4)
            while dx == 0 and dy == 0:
                dx = random.randint(-4, 4)
                dy = random.randint(-4, 4)

            new_x1, new_y1 = x1 + dx, y1 + dy
            new_x2, new_y2 = x2 + dx, y2 + dy
            new_x3, new_y3 = x3 + dx, y3 + dy

            latex = f"\\text{{Translate }} \\triangle ABC \\text{{ with vertices }} A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3}) \\text{{ by }} \\langle {dx}, {dy} \\rangle"
            solution = f"A'({new_x1}, {new_y1}), B'({new_x2}, {new_y2}), C'({new_x3}, {new_y3})"

            steps = [
                f"\\text{{Apply translation to each vertex}}",
                f"A' = ({x1} + {dx}, {y1} + {dy}) = ({new_x1}, {new_y1})",
                f"B' = ({x2} + {dx}, {y2} + {dy}) = ({new_x2}, {new_y2})",
                f"C' = ({x3} + {dx}, {y3} + {dy}) = ({new_x3}, {new_y3})"
            ]
        else:
            # Composition of two translations
            x = random.randint(-5, 5)
            y = random.randint(-5, 5)
            dx1 = random.randint(-4, 4)
            dy1 = random.randint(-4, 4)
            dx2 = random.randint(-4, 4)
            dy2 = random.randint(-4, 4)

            total_dx = dx1 + dx2
            total_dy = dy1 + dy2
            new_x = x + total_dx
            new_y = y + total_dy

            latex = f"\\text{{Point }} ({x}, {y}) \\text{{ is translated by }} \\langle {dx1}, {dy1} \\rangle \\text{{ then by }} \\langle {dx2}, {dy2} \\rangle. \\text{{ Find the final position.}}"
            solution = f"({new_x}, {new_y})"

            steps = [
                f"\\text{{First translation: }} ({x} + {dx1}, {y} + {dy1}) = ({x + dx1}, {y + dy1})",
                f"\\text{{Second translation: }} ({x + dx1} + {dx2}, {y + dy1} + {dy2}) = ({new_x}, {new_y})",
                f"\\text{{Or combine vectors: }} \\langle {dx1} + {dx2}, {dy1} + {dy2} \\rangle = \\langle {total_dx}, {total_dy} \\rangle",
                f"\\text{{Final point: }} ({new_x}, {new_y})"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = TranslationsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
