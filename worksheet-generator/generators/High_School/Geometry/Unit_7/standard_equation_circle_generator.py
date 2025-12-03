"""
Standard Equation of a Circle Generator
Creates problems about circles in standard form (x-h)² + (y-k)² = r²
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class StandardEquationCircleGenerator:
    """Generates problems about circles in standard form."""

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

    def _format_circle_equation(self, h, k, r_sq):
        """Format (x-h)² + (y-k)² = r²"""
        if h == 0:
            x_part = "x^2"
        elif h > 0:
            x_part = f"(x - {h})^2"
        else:
            x_part = f"(x + {abs(h)})^2"

        if k == 0:
            y_part = "y^2"
        elif k > 0:
            y_part = f"(y - {k})^2"
        else:
            y_part = f"(y + {abs(k)})^2"

        return f"{x_part} + {y_part} = {r_sq}"

    def _generate_easy(self) -> Equation:
        """Identify center and radius from standard form (center at origin)"""
        r = random.randint(2, 8)
        r_sq = r ** 2

        problem_type = random.choice(['find_center', 'find_radius'])

        if problem_type == 'find_center':
            latex = f"\\text{{Find the center of the circle: }} x^2 + y^2 = {r_sq}"
            solution = "(0, 0)"
            steps = [
                f"\\text{{Standard form: }} (x - h)^2 + (y - k)^2 = r^2",
                f"\\text{{Here, }} h = 0 \\text{{ and }} k = 0",
                f"\\text{{Center: }} (0, 0)"
            ]
        else:
            latex = f"\\text{{Find the radius of the circle: }} x^2 + y^2 = {r_sq}"
            solution = str(r)
            steps = [
                f"\\text{{Standard form: }} (x - h)^2 + (y - k)^2 = r^2",
                f"r^2 = {r_sq}",
                f"r = \\sqrt{{{r_sq}}} = {r}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Identify center and radius with center not at origin"""
        h = random.randint(-6, 6)
        k = random.randint(-6, 6)
        r = random.randint(2, 6)
        r_sq = r ** 2

        eq = self._format_circle_equation(h, k, r_sq)

        problem_type = random.choice(['find_center', 'find_radius', 'find_both'])

        if problem_type == 'find_center':
            latex = f"\\text{{Find the center: }} {eq}"
            solution = f"({h}, {k})"
            steps = [
                f"\\text{{Compare to }} (x - h)^2 + (y - k)^2 = r^2",
                f"\\text{{Center is }} (h, k) = ({h}, {k})"
            ]
        elif problem_type == 'find_radius':
            latex = f"\\text{{Find the radius: }} {eq}"
            solution = str(r)
            steps = [
                f"r^2 = {r_sq}",
                f"r = {r}"
            ]
        else:
            latex = f"\\text{{Find the center and radius: }} {eq}"
            solution = f"\\text{{Center: }} ({h}, {k}), \\text{{ Radius: }} {r}"
            steps = [
                f"\\text{{Standard form: }} (x - h)^2 + (y - k)^2 = r^2",
                f"\\text{{Center: }} ({h}, {k})",
                f"\\text{{Radius: }} r = \\sqrt{{{r_sq}}} = {r}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Write equation given center and radius, or given endpoints of diameter"""
        problem_type = random.choice(['write_equation', 'from_diameter'])

        if problem_type == 'write_equation':
            h = random.randint(-5, 5)
            k = random.randint(-5, 5)
            r = random.randint(2, 6)
            r_sq = r ** 2

            latex = f"\\text{{Write the equation of a circle with center }} ({h}, {k}) \\text{{ and radius }} {r}."
            solution = self._format_circle_equation(h, k, r_sq)

            steps = [
                f"\\text{{Standard form: }} (x - h)^2 + (y - k)^2 = r^2",
                f"\\text{{Substitute: }} h = {h}, k = {k}, r = {r}",
                f"{solution}"
            ]
        else:
            # Find circle from diameter endpoints
            x1 = random.randint(-6, 0)
            y1 = random.randint(-6, 0)
            x2 = random.randint(0, 6)
            y2 = random.randint(0, 6)

            # Make coordinates even for clean center
            x1 = x1 if x1 % 2 == 0 else x1 - 1
            y1 = y1 if y1 % 2 == 0 else y1 - 1
            x2 = x2 if x2 % 2 == 0 else x2 + 1
            y2 = y2 if y2 % 2 == 0 else y2 + 1

            h = (x1 + x2) // 2
            k = (y1 + y2) // 2
            r_sq = (x2 - h) ** 2 + (y2 - k) ** 2

            latex = f"\\text{{Write the equation of a circle with diameter endpoints }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})."
            solution = self._format_circle_equation(h, k, r_sq)

            steps = [
                f"\\text{{Center = midpoint = }} \\left(\\frac{{{x1}+{x2}}}{{2}}, \\frac{{{y1}+{y2}}}{{2}}\\right) = ({h}, {k})",
                f"\\text{{Radius = distance from center to endpoint}}",
                f"r^2 = ({x2} - {h})^2 + ({y2} - {k})^2 = {r_sq}",
                f"\\text{{Equation: }} {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Check if point is on/inside/outside circle, or tangent problems"""
        problem_type = random.choice(['point_location', 'tangent', 'intersection'])

        if problem_type == 'point_location':
            h = random.randint(-4, 4)
            k = random.randint(-4, 4)
            r = random.randint(3, 5)
            r_sq = r ** 2

            location = random.choice(['on', 'inside', 'outside'])

            if location == 'on':
                # Point on circle: choose point at distance r
                px = h + r
                py = k
            elif location == 'inside':
                px = h + random.randint(1, r - 1)
                py = k
            else:
                px = h + r + random.randint(1, 3)
                py = k

            dist_sq = (px - h) ** 2 + (py - k) ** 2

            eq = self._format_circle_equation(h, k, r_sq)
            latex = f"\\text{{Is point }} ({px}, {py}) \\text{{ on, inside, or outside the circle }} {eq}?"

            if dist_sq == r_sq:
                solution = "On the circle"
                compare = "="
            elif dist_sq < r_sq:
                solution = "Inside the circle"
                compare = "<"
            else:
                solution = "Outside the circle"
                compare = ">"

            steps = [
                f"\\text{{Calculate distance from point to center:}}",
                f"d^2 = ({px} - {h})^2 + ({py} - {k})^2 = {dist_sq}",
                f"\\text{{Compare to }} r^2 = {r_sq}",
                f"\\text{{Since }} {dist_sq} {compare} {r_sq}, \\text{{ the point is {solution.lower()}}}"
            ]

        elif problem_type == 'tangent':
            h, k = 0, 0
            r = random.randint(3, 6)
            r_sq = r ** 2

            # Tangent at point on x-axis
            px, py = r, 0

            latex = f"\\text{{Find the equation of the tangent line to }} x^2 + y^2 = {r_sq} \\text{{ at point }} ({px}, {py})."
            solution = f"x = {r}"

            steps = [
                f"\\text{{At }} ({r}, 0), \\text{{ the radius is horizontal}}",
                f"\\text{{The tangent is perpendicular to the radius}}",
                f"\\text{{Tangent line: }} x = {r}"
            ]

        else:
            # Two circles: do they intersect?
            r1 = random.randint(2, 4)
            r2 = random.randint(2, 4)
            d = random.randint(1, r1 + r2 + 2)

            if d > r1 + r2:
                relation = "No intersection (circles are separate)"
            elif d == r1 + r2:
                relation = "Externally tangent (touch at one point)"
            elif abs(r1 - r2) < d < r1 + r2:
                relation = "Two intersection points"
            elif d == abs(r1 - r2):
                relation = "Internally tangent (touch at one point)"
            else:
                relation = "One circle inside the other (no intersection)"

            latex = f"\\text{{Circle 1 has center (0,0) radius {r1}. Circle 2 has center ({d},0) radius {r2}. How do they intersect?}}"
            solution = relation

            steps = [
                f"\\text{{Distance between centers: }} d = {d}",
                f"\\text{{Sum of radii: }} r_1 + r_2 = {r1 + r2}",
                f"\\text{{Difference of radii: }} |r_1 - r_2| = {abs(r1 - r2)}",
                f"\\text{{{relation}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = StandardEquationCircleGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
