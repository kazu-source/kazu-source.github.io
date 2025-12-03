"""
Reflections Generator
Creates problems about reflecting points and shapes over lines
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ReflectionsGenerator:
    """Generates problems about reflections on the coordinate plane."""

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
        """Reflect a point over the x-axis or y-axis"""
        x = random.randint(-6, 6)
        y = random.randint(-6, 6)
        while x == 0 or y == 0:
            x = random.randint(-6, 6)
            y = random.randint(-6, 6)

        axis = random.choice(['x', 'y'])

        if axis == 'x':
            new_x, new_y = x, -y
            rule = "(x, y) \\to (x, -y)"
            line = "x\\text{-axis}"
        else:
            new_x, new_y = -x, y
            rule = "(x, y) \\to (-x, y)"
            line = "y\\text{-axis}"

        latex = f"\\text{{Reflect point }} ({x}, {y}) \\text{{ over the }} {line}."
        solution = f"({new_x}, {new_y})"

        steps = [
            f"\\text{{Rule for reflection over }} {line}: {rule}",
            f"({x}, {y}) \\to ({new_x}, {new_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Reflect a point over y = x or y = -x"""
        x = random.randint(-6, 6)
        y = random.randint(-6, 6)
        while x == 0 or y == 0 or x == y or x == -y:
            x = random.randint(-6, 6)
            y = random.randint(-6, 6)

        line_type = random.choice(['y=x', 'y=-x'])

        if line_type == 'y=x':
            new_x, new_y = y, x
            rule = "(x, y) \\to (y, x)"
            line = "y = x"
        else:
            new_x, new_y = -y, -x
            rule = "(x, y) \\to (-y, -x)"
            line = "y = -x"

        latex = f"\\text{{Reflect point }} ({x}, {y}) \\text{{ over the line }} {line}."
        solution = f"({new_x}, {new_y})"

        steps = [
            f"\\text{{Rule for reflection over }} {line}: {rule}",
            f"({x}, {y}) \\to ({new_x}, {new_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Reflect a point over a horizontal or vertical line not at origin"""
        problem_type = random.choice(['horizontal', 'vertical'])

        if problem_type == 'horizontal':
            # Reflect over y = k
            k = random.randint(-4, 4)
            while k == 0:
                k = random.randint(-4, 4)

            x = random.randint(-6, 6)
            y = random.randint(-6, 6)
            while y == k:
                y = random.randint(-6, 6)

            new_x = x
            new_y = 2 * k - y

            latex = f"\\text{{Reflect point }} ({x}, {y}) \\text{{ over the line }} y = {k}."
            solution = f"({new_x}, {new_y})"

            steps = [
                f"\\text{{Line of reflection: }} y = {k}",
                f"\\text{{Distance from point to line: }} |{y} - {k}| = {abs(y - k)}",
                f"\\text{{New y-coordinate: }} {k} + ({k} - {y}) = {new_y}",
                f"\\text{{x-coordinate stays same: }} {x}",
                f"\\text{{Result: }} ({new_x}, {new_y})"
            ]
        else:
            # Reflect over x = h
            h = random.randint(-4, 4)
            while h == 0:
                h = random.randint(-4, 4)

            x = random.randint(-6, 6)
            y = random.randint(-6, 6)
            while x == h:
                x = random.randint(-6, 6)

            new_x = 2 * h - x
            new_y = y

            latex = f"\\text{{Reflect point }} ({x}, {y}) \\text{{ over the line }} x = {h}."
            solution = f"({new_x}, {new_y})"

            steps = [
                f"\\text{{Line of reflection: }} x = {h}",
                f"\\text{{Distance from point to line: }} |{x} - {h}| = {abs(x - h)}",
                f"\\text{{New x-coordinate: }} {h} + ({h} - {x}) = {new_x}",
                f"\\text{{y-coordinate stays same: }} {y}",
                f"\\text{{Result: }} ({new_x}, {new_y})"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Find the line of reflection or reflect a shape"""
        problem_type = random.choice(['find_line', 'reflect_triangle'])

        if problem_type == 'find_line':
            # Give pre-image and image, find the line of reflection
            line_type = random.choice(['x-axis', 'y-axis', 'y=x', 'horizontal', 'vertical'])

            if line_type == 'x-axis':
                x, y = random.randint(1, 5), random.randint(1, 5)
                new_x, new_y = x, -y
                line_answer = "y = 0 \\text{ (x-axis)}"
            elif line_type == 'y-axis':
                x, y = random.randint(1, 5), random.randint(1, 5)
                new_x, new_y = -x, y
                line_answer = "x = 0 \\text{ (y-axis)}"
            elif line_type == 'y=x':
                x, y = random.randint(1, 5), random.randint(2, 6)
                while x == y:
                    y = random.randint(2, 6)
                new_x, new_y = y, x
                line_answer = "y = x"
            elif line_type == 'horizontal':
                k = random.randint(1, 3)
                x = random.randint(-4, 4)
                y = random.randint(k + 1, k + 4)
                new_x, new_y = x, 2 * k - y
                line_answer = f"y = {k}"
            else:
                h = random.randint(1, 3)
                x = random.randint(h + 1, h + 4)
                y = random.randint(-4, 4)
                new_x, new_y = 2 * h - x, y
                line_answer = f"x = {h}"

            latex = f"\\text{{Point }} A({x}, {y}) \\text{{ is reflected to }} A'({new_x}, {new_y}). \\text{{ Find the line of reflection.}}"
            solution = line_answer

            steps = [
                f"\\text{{Midpoint of }} A \\text{{ and }} A': \\left(\\frac{{{x}+{new_x}}}{{2}}, \\frac{{{y}+{new_y}}}{{2}}\\right) = ({(x+new_x)/2}, {(y+new_y)/2})",
                f"\\text{{The line of reflection passes through the midpoint}}",
                f"\\text{{Line of reflection: }} {line_answer}"
            ]
        else:
            # Reflect a triangle over x-axis or y-axis
            axis = random.choice(['x', 'y'])
            x1, y1 = random.randint(1, 3), random.randint(1, 3)
            x2, y2 = x1 + random.randint(1, 3), y1
            x3, y3 = x1 + random.randint(0, 2), y1 + random.randint(1, 3)

            if axis == 'x':
                new_x1, new_y1 = x1, -y1
                new_x2, new_y2 = x2, -y2
                new_x3, new_y3 = x3, -y3
                line = "x\\text{-axis}"
            else:
                new_x1, new_y1 = -x1, y1
                new_x2, new_y2 = -x2, y2
                new_x3, new_y3 = -x3, y3
                line = "y\\text{-axis}"

            latex = f"\\text{{Reflect }} \\triangle ABC \\text{{ with }} A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3}) \\text{{ over the }} {line}."
            solution = f"A'({new_x1}, {new_y1}), B'({new_x2}, {new_y2}), C'({new_x3}, {new_y3})"

            steps = [
                f"\\text{{Apply reflection over }} {line} \\text{{ to each vertex:}}",
                f"A({x1}, {y1}) \\to A'({new_x1}, {new_y1})",
                f"B({x2}, {y2}) \\to B'({new_x2}, {new_y2})",
                f"C({x3}, {y3}) \\to C'({new_x3}, {new_y3})"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = ReflectionsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
