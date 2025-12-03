"""
Dilations Generator
Creates problems about dilating points and shapes from a center point
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class DilationsGenerator:
    """Generates problems about dilations on the coordinate plane."""

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
        """Dilate a point from the origin with integer scale factor"""
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        k = random.randint(2, 4)

        new_x = k * x
        new_y = k * y

        latex = f"\\text{{Dilate point }} ({x}, {y}) \\text{{ by scale factor }} {k} \\text{{ centered at the origin.}}"
        solution = f"({new_x}, {new_y})"

        steps = [
            f"\\text{{For dilation centered at origin: }} (x, y) \\to (kx, ky)",
            f"({x}, {y}) \\to ({k} \\cdot {x}, {k} \\cdot {y})",
            f"\\text{{Result: }} ({new_x}, {new_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Dilate with fractional scale factor or identify enlargement/reduction"""
        problem_type = random.choice(['fractional', 'identify'])

        if problem_type == 'fractional':
            x = random.randint(2, 8) * 2  # Even numbers for clean division
            y = random.randint(2, 8) * 2
            k_num = 1
            k_den = 2

            new_x = x // 2
            new_y = y // 2

            latex = f"\\text{{Dilate point }} ({x}, {y}) \\text{{ by scale factor }} \\frac{{1}}{{2}} \\text{{ centered at the origin.}}"
            solution = f"({new_x}, {new_y})"

            steps = [
                f"\\text{{Scale factor }} \\frac{{1}}{{2}} \\text{{ means reduction by half}}",
                f"({x}, {y}) \\to (\\frac{{{x}}}{{2}}, \\frac{{{y}}}{{2}})",
                f"\\text{{Result: }} ({new_x}, {new_y})"
            ]
        else:
            k = random.choice([0.5, 2, 3, 0.25, 4])
            if k > 1:
                answer = "Enlargement"
                explanation = f"Scale factor {k} > 1, so the image is larger than the pre-image."
            else:
                answer = "Reduction"
                explanation = f"Scale factor {k} < 1, so the image is smaller than the pre-image."

            latex = f"\\text{{A dilation has scale factor }} {k}. \\text{{ Is this an enlargement or reduction?}}"
            solution = answer

            steps = [
                f"\\text{{If scale factor > 1: enlargement}}",
                f"\\text{{If scale factor < 1: reduction}}",
                f"\\text{{{explanation}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Dilate from a center other than the origin"""
        # Center of dilation
        cx = random.randint(-3, 3)
        cy = random.randint(-3, 3)

        # Point to dilate
        x = cx + random.randint(1, 4) * random.choice([1, -1])
        y = cy + random.randint(1, 4) * random.choice([1, -1])

        k = random.randint(2, 3)

        # Dilation formula: (x', y') = (cx + k(x - cx), cy + k(y - cy))
        new_x = cx + k * (x - cx)
        new_y = cy + k * (y - cy)

        latex = f"\\text{{Dilate point }} ({x}, {y}) \\text{{ by scale factor }} {k} \\text{{ centered at }} ({cx}, {cy})."
        solution = f"({new_x}, {new_y})"

        steps = [
            f"\\text{{Formula: }} (x', y') = (c_x + k(x - c_x), c_y + k(y - c_y))",
            f"x' = {cx} + {k}({x} - {cx}) = {cx} + {k}({x - cx}) = {cx} + {k * (x - cx)} = {new_x}",
            f"y' = {cy} + {k}({y} - {cy}) = {cy} + {k}({y - cy}) = {cy} + {k * (y - cy)} = {new_y}",
            f"\\text{{Result: }} ({new_x}, {new_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Find scale factor, center, or dilate a shape"""
        problem_type = random.choice(['find_scale', 'find_center', 'dilate_triangle'])

        if problem_type == 'find_scale':
            # Given pre-image and image, find scale factor
            x1 = random.randint(1, 4)
            y1 = random.randint(1, 4)
            k = random.randint(2, 4)
            x2 = k * x1
            y2 = k * y1

            latex = f"\\text{{Point }} ({x1}, {y1}) \\text{{ is dilated to }} ({x2}, {y2}) \\text{{ from the origin. Find the scale factor.}}"
            solution = str(k)

            steps = [
                f"\\text{{Scale factor }} k = \\frac{{x'}}{{x}} = \\frac{{{x2}}}{{{x1}}} = {k}",
                f"\\text{{Verify: }} \\frac{{y'}}{{y}} = \\frac{{{y2}}}{{{y1}}} = {k} \\checkmark"
            ]

        elif problem_type == 'find_center':
            # Given pre-image, image, and scale factor, verify center
            cx, cy = 0, 0  # Keep it simple - origin
            x = random.randint(2, 5)
            y = random.randint(2, 5)
            k = 2

            new_x = k * x
            new_y = k * y

            latex = f"\\text{{Point }} ({x}, {y}) \\text{{ is dilated to }} ({new_x}, {new_y}) \\text{{ with scale factor }} {k}. \\text{{ Find the center.}}"
            solution = f"({cx}, {cy})"

            steps = [
                f"\\text{{Let center be }} (c_x, c_y)",
                f"\\text{{Using }} x' = c_x + k(x - c_x):",
                f"{new_x} = c_x + {k}({x} - c_x)",
                f"\\text{{Solving: }} c_x = 0",
                f"\\text{{Similarly: }} c_y = 0",
                f"\\text{{Center: }} (0, 0)"
            ]

        else:
            # Dilate a triangle
            x1, y1 = random.randint(1, 3), random.randint(1, 3)
            x2, y2 = x1 + random.randint(1, 2), y1
            x3, y3 = x1, y1 + random.randint(1, 2)
            k = 2

            new_x1, new_y1 = k * x1, k * y1
            new_x2, new_y2 = k * x2, k * y2
            new_x3, new_y3 = k * x3, k * y3

            latex = f"\\text{{Dilate }} \\triangle ABC \\text{{ with }} A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3}) \\text{{ by factor }} {k} \\text{{ from origin.}}"
            solution = f"A'({new_x1}, {new_y1}), B'({new_x2}, {new_y2}), C'({new_x3}, {new_y3})"

            steps = [
                f"\\text{{Apply dilation to each vertex:}}",
                f"A({x1}, {y1}) \\to A'({k} \\cdot {x1}, {k} \\cdot {y1}) = ({new_x1}, {new_y1})",
                f"B({x2}, {y2}) \\to B'({k} \\cdot {x2}, {k} \\cdot {y2}) = ({new_x2}, {new_y2})",
                f"C({x3}, {y3}) \\to C'({k} \\cdot {x3}, {k} \\cdot {y3}) = ({new_x3}, {new_y3})"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = DilationsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
