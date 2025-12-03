"""
Rotations Generator
Creates problems about rotating points and shapes around a center point
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class RotationsGenerator:
    """Generates problems about rotations on the coordinate plane."""

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

    def _rotate_point(self, x, y, angle, cx=0, cy=0):
        """Rotate point (x,y) around center (cx,cy) by angle degrees."""
        # Translate to origin
        x -= cx
        y -= cy

        # Apply rotation rules for 90, 180, 270 degrees
        if angle == 90:
            new_x, new_y = -y, x
        elif angle == 180:
            new_x, new_y = -x, -y
        elif angle == 270:
            new_x, new_y = y, -x
        else:
            new_x, new_y = x, y

        # Translate back
        new_x += cx
        new_y += cy

        return new_x, new_y

    def _generate_easy(self) -> Equation:
        """Rotate a point 90 degrees counterclockwise about the origin"""
        x = random.randint(1, 6)
        y = random.randint(1, 6)

        new_x, new_y = self._rotate_point(x, y, 90)

        latex = f"\\text{{Rotate point }} ({x}, {y}) \\text{{ by }} 90^\\circ \\text{{ counterclockwise about the origin.}}"
        solution = f"({new_x}, {new_y})"

        steps = [
            f"\\text{{Rule for }} 90^\\circ \\text{{ CCW: }} (x, y) \\to (-y, x)",
            f"({x}, {y}) \\to (-{y}, {x})",
            f"\\text{{Result: }} ({new_x}, {new_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Rotate a point 180 or 270 degrees about the origin"""
        x = random.randint(-6, 6)
        y = random.randint(-6, 6)
        while x == 0 and y == 0:
            x = random.randint(-6, 6)
            y = random.randint(-6, 6)

        angle = random.choice([180, 270])
        new_x, new_y = self._rotate_point(x, y, angle)

        if angle == 180:
            rule = "(x, y) \\to (-x, -y)"
            step2 = f"({x}, {y}) \\to ({-x}, {-y})"
        else:
            rule = "(x, y) \\to (y, -x)"
            step2 = f"({x}, {y}) \\to ({y}, {-x})"

        latex = f"\\text{{Rotate point }} ({x}, {y}) \\text{{ by }} {angle}^\\circ \\text{{ counterclockwise about the origin.}}"
        solution = f"({new_x}, {new_y})"

        steps = [
            f"\\text{{Rule for }} {angle}^\\circ \\text{{ CCW: }} {rule}",
            step2,
            f"\\text{{Result: }} ({new_x}, {new_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Rotate a point about a center other than the origin"""
        # Center of rotation
        cx = random.randint(-3, 3)
        cy = random.randint(-3, 3)

        # Point to rotate (offset from center)
        offset_x = random.randint(1, 4) * random.choice([1, -1])
        offset_y = random.randint(1, 4) * random.choice([1, -1])
        x = cx + offset_x
        y = cy + offset_y

        angle = random.choice([90, 180, 270])
        new_x, new_y = self._rotate_point(x, y, angle, cx, cy)

        if angle == 90:
            rule = "(x-h, y-k) \\to (-(y-k)+h, (x-h)+k)"
        elif angle == 180:
            rule = "(x-h, y-k) \\to (-(x-h)+h, -(y-k)+k)"
        else:
            rule = "(x-h, y-k) \\to ((y-k)+h, -(x-h)+k)"

        latex = f"\\text{{Rotate point }} ({x}, {y}) \\text{{ by }} {angle}^\\circ \\text{{ counterclockwise about }} ({cx}, {cy})."
        solution = f"({new_x}, {new_y})"

        steps = [
            f"\\text{{Center of rotation: }} ({cx}, {cy})",
            f"\\text{{Translate to origin: }} ({x} - {cx}, {y} - {cy}) = ({x - cx}, {y - cy})",
            f"\\text{{Apply }} {angle}^\\circ \\text{{ rotation}}",
            f"\\text{{Translate back and get: }} ({new_x}, {new_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Find the angle of rotation or rotate a shape"""
        problem_type = random.choice(['find_angle', 'rotate_triangle'])

        if problem_type == 'find_angle':
            # Give pre-image and image, find angle
            x = random.randint(1, 5)
            y = random.randint(1, 5)
            angle = random.choice([90, 180, 270])
            new_x, new_y = self._rotate_point(x, y, angle)

            latex = f"\\text{{Point }} A({x}, {y}) \\text{{ is rotated about the origin to }} A'({new_x}, {new_y}). \\text{{ Find the angle of rotation (CCW).}}"
            solution = f"{angle}^\\circ"

            steps = [
                f"\\text{{Check each rotation rule:}}",
                f"90^\\circ: ({x}, {y}) \\to ({-y}, {x})",
                f"180^\\circ: ({x}, {y}) \\to ({-x}, {-y})",
                f"270^\\circ: ({x}, {y}) \\to ({y}, {-x})",
                f"\\text{{The rotation that gives }} ({new_x}, {new_y}) \\text{{ is }} {angle}^\\circ"
            ]
        else:
            # Rotate a triangle
            x1, y1 = random.randint(1, 4), random.randint(1, 4)
            x2, y2 = x1 + random.randint(1, 3), y1
            x3, y3 = x1, y1 + random.randint(1, 3)

            angle = random.choice([90, 180, 270])
            new_x1, new_y1 = self._rotate_point(x1, y1, angle)
            new_x2, new_y2 = self._rotate_point(x2, y2, angle)
            new_x3, new_y3 = self._rotate_point(x3, y3, angle)

            latex = f"\\text{{Rotate }} \\triangle ABC \\text{{ with }} A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3}) \\text{{ by }} {angle}^\\circ \\text{{ CCW about origin.}}"
            solution = f"A'({new_x1}, {new_y1}), B'({new_x2}, {new_y2}), C'({new_x3}, {new_y3})"

            steps = [
                f"\\text{{Apply }} {angle}^\\circ \\text{{ rotation to each vertex:}}",
                f"A({x1}, {y1}) \\to A'({new_x1}, {new_y1})",
                f"B({x2}, {y2}) \\to B'({new_x2}, {new_y2})",
                f"C({x3}, {y3}) \\to C'({new_x3}, {new_y3})"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = RotationsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
