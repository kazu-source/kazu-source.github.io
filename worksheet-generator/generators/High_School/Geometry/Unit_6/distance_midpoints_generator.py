"""
Distance and Midpoints Generator
Creates problems about the distance formula and midpoint formula
"""

import random
import math
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class DistanceMidpointsGenerator:
    """Generates problems about distance and midpoint formulas."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
        self.pythagorean_triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)]

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
        """Basic midpoint problems with even coordinates"""
        x1 = random.randint(-6, 6) * 2  # Even for clean midpoints
        y1 = random.randint(-6, 6) * 2
        x2 = random.randint(-6, 6) * 2
        y2 = random.randint(-6, 6) * 2

        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2

        latex = f"\\text{{Find the midpoint of }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})."
        solution = f"({mid_x}, {mid_y})"

        steps = [
            f"\\text{{Midpoint formula: }} M = \\left(\\frac{{x_1 + x_2}}{{2}}, \\frac{{y_1 + y_2}}{{2}}\\right)",
            f"M = \\left(\\frac{{{x1} + {x2}}}{{2}}, \\frac{{{y1} + {y2}}}{{2}}\\right)",
            f"M = \\left(\\frac{{{x1 + x2}}}{{2}}, \\frac{{{y1 + y2}}}{{2}}\\right)",
            f"M = ({mid_x}, {mid_y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Distance problems with Pythagorean triple distances"""
        a, b, c = random.choice(self.pythagorean_triples)
        x1 = random.randint(-5, 5)
        y1 = random.randint(-5, 5)

        # Create second point using Pythagorean triple
        x2 = x1 + a
        y2 = y1 + b

        latex = f"\\text{{Find the distance between }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})."
        solution = str(c)

        steps = [
            f"\\text{{Distance formula: }} d = \\sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}}",
            f"d = \\sqrt{{({x2} - {x1})^2 + ({y2} - {y1})^2}}",
            f"d = \\sqrt{{{a}^2 + {b}^2}}",
            f"d = \\sqrt{{{a**2} + {b**2}}}",
            f"d = \\sqrt{{{c**2}}} = {c}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Find missing endpoint given midpoint, or distance with radical answer"""
        problem_type = random.choice(['find_endpoint', 'radical_distance'])

        if problem_type == 'find_endpoint':
            # Given one endpoint and midpoint, find other endpoint
            x1 = random.randint(-8, 8)
            y1 = random.randint(-8, 8)
            mid_x = random.randint(-5, 5)
            mid_y = random.randint(-5, 5)

            # Calculate x2, y2
            x2 = 2 * mid_x - x1
            y2 = 2 * mid_y - y1

            latex = f"\\text{{If }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2}) \\text{{ are endpoints, with midpoint }} ({mid_x}, {mid_y}). \\text{{ If one endpoint is }} ({x1}, {y1}), \\text{{ find the other.}}"
            solution = f"({x2}, {y2})"

            steps = [
                f"\\text{{Using midpoint formula backwards:}}",
                f"x_2 = 2 \\cdot m_x - x_1 = 2({mid_x}) - {x1} = {x2}",
                f"y_2 = 2 \\cdot m_y - y_1 = 2({mid_y}) - {y1} = {y2}",
                f"\\text{{Other endpoint: }} ({x2}, {y2})"
            ]
        else:
            # Distance with radical (non-perfect square)
            x1 = random.randint(-5, 5)
            y1 = random.randint(-5, 5)
            dx = random.randint(1, 5)
            dy = random.randint(1, 5)

            x2 = x1 + dx
            y2 = y1 + dy

            dist_sq = dx**2 + dy**2
            # Check if perfect square
            sqrt_dist = int(math.sqrt(dist_sq))
            if sqrt_dist * sqrt_dist == dist_sq:
                solution = str(sqrt_dist)
            else:
                solution = f"\\sqrt{{{dist_sq}}}"

            latex = f"\\text{{Find the distance between }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})."

            steps = [
                f"d = \\sqrt{{({x2} - {x1})^2 + ({y2} - {y1})^2}}",
                f"d = \\sqrt{{{dx}^2 + {dy}^2}}",
                f"d = \\sqrt{{{dx**2} + {dy**2}}}",
                f"d = {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Applications: perimeter, classify triangle/quadrilateral"""
        problem_type = random.choice(['perimeter', 'classify', 'on_segment'])

        if problem_type == 'perimeter':
            # Find perimeter of triangle
            a, b, c = (3, 4, 5)
            x1, y1 = 0, 0
            x2, y2 = a, 0
            x3, y3 = 0, b

            d12 = a
            d23 = c
            d13 = b
            perimeter = d12 + d23 + d13

            latex = f"\\text{{Find the perimeter of triangle with vertices }} A(0, 0), B({a}, 0), C(0, {b})."
            solution = str(perimeter)

            steps = [
                f"\\text{{Find each side length:}}",
                f"AB = \\sqrt{{({a}-0)^2 + (0-0)^2}} = {a}",
                f"BC = \\sqrt{{(0-{a})^2 + ({b}-0)^2}} = \\sqrt{{{a**2}+{b**2}}} = {c}",
                f"AC = \\sqrt{{(0-0)^2 + ({b}-0)^2}} = {b}",
                f"\\text{{Perimeter}} = {a} + {c} + {b} = {perimeter}"
            ]

        elif problem_type == 'classify':
            # Is the triangle isosceles, equilateral, or scalene?
            triangle_type = random.choice(['isosceles', 'right'])

            if triangle_type == 'isosceles':
                x1, y1 = 0, 0
                x2, y2 = 6, 0
                x3, y3 = 3, 4

                latex = f"\\text{{Classify the triangle with vertices }} A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3})."
                solution = "Isosceles"

                steps = [
                    f"AB = \\sqrt{{(6-0)^2 + (0-0)^2}} = 6",
                    f"AC = \\sqrt{{(3-0)^2 + (4-0)^2}} = 5",
                    f"BC = \\sqrt{{(3-6)^2 + (4-0)^2}} = 5",
                    f"\\text{{Since AC = BC, the triangle is isosceles.}}"
                ]
            else:
                x1, y1 = 0, 0
                x2, y2 = 3, 0
                x3, y3 = 0, 4

                latex = f"\\text{{Classify the triangle with vertices }} A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3})."
                solution = "Right triangle"

                steps = [
                    f"AB = 3, AC = 4, BC = 5",
                    f"\\text{{Check: }} 3^2 + 4^2 = 9 + 16 = 25 = 5^2",
                    f"\\text{{Since }} AB^2 + AC^2 = BC^2, \\text{{ it's a right triangle.}}"
                ]

        else:
            # Check if point is on segment
            x1 = random.randint(-5, 0)
            y1 = random.randint(-5, 0)
            x2 = random.randint(1, 5)
            y2 = random.randint(1, 5)
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2

            latex = f"\\text{{Is point }} ({mid_x}, {mid_y}) \\text{{ on the segment from }} ({x1}, {y1}) \\text{{ to }} ({x2}, {y2})?"
            solution = "Yes (it's the midpoint)"

            steps = [
                f"\\text{{Check if distances add up:}}",
                f"d(A, P) + d(P, B) \\stackrel{{?}}{{=}} d(A, B)",
                f"\\text{{Or check if P is the midpoint.}}",
                f"\\text{{Midpoint}} = \\left(\\frac{{{x1}+{x2}}}{{2}}, \\frac{{{y1}+{y2}}}{{2}}\\right) = ({mid_x}, {mid_y}) \\checkmark"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = DistanceMidpointsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
