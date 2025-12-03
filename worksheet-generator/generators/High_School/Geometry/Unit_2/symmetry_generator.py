"""
Symmetry Generator
Creates problems about line symmetry and rotational symmetry
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SymmetryGenerator:
    """Generates problems about symmetry in geometric figures."""

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
        """Count lines of symmetry for basic shapes"""
        shapes = [
            ("equilateral triangle", 3, "An equilateral triangle has 3 lines of symmetry, one from each vertex to the midpoint of the opposite side."),
            ("square", 4, "A square has 4 lines of symmetry: 2 diagonal and 2 through midpoints of opposite sides."),
            ("rectangle (not a square)", 2, "A rectangle has 2 lines of symmetry through the midpoints of opposite sides."),
            ("regular pentagon", 5, "A regular pentagon has 5 lines of symmetry."),
            ("regular hexagon", 6, "A regular hexagon has 6 lines of symmetry."),
            ("isosceles triangle", 1, "An isosceles triangle has 1 line of symmetry from the vertex angle to the base."),
            ("circle", "infinite", "A circle has infinitely many lines of symmetry through its center."),
            ("scalene triangle", 0, "A scalene triangle has no lines of symmetry.")
        ]

        shape, lines, explanation = random.choice(shapes)

        latex = f"\\text{{How many lines of symmetry does a }} {shape} \\text{{ have?}}"
        solution = str(lines)

        steps = [
            f"\\text{{{explanation}}}",
            f"\\text{{Answer: {lines}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Rotational symmetry order and angle"""
        problem_type = random.choice(['order', 'angle'])

        shapes = [
            ("equilateral triangle", 3, 120),
            ("square", 4, 90),
            ("regular pentagon", 5, 72),
            ("regular hexagon", 6, 60),
            ("regular octagon", 8, 45),
        ]

        shape, order, angle = random.choice(shapes)

        if problem_type == 'order':
            latex = f"\\text{{What is the order of rotational symmetry for a }} {shape}\\text{{?}}"
            solution = str(order)

            steps = [
                f"\\text{{The order equals the number of times a figure maps onto itself in one full rotation.}}",
                f"\\text{{A {shape} maps onto itself {order} times in 360°.}}",
                f"\\text{{Order = {order}}}"
            ]
        else:
            latex = f"\\text{{What is the angle of rotational symmetry for a }} {shape}\\text{{?}}"
            solution = f"{angle}°"

            steps = [
                f"\\text{{Angle of rotational symmetry = }} \\frac{{360°}}{{\\text{{order}}}}",
                f"\\text{{For a {shape}: }} \\frac{{360°}}{{{order}}} = {angle}°"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Determine lines of symmetry from coordinates or identify symmetry type"""
        problem_type = random.choice(['coordinates', 'both_types'])

        if problem_type == 'coordinates':
            # Check if points have a line of symmetry
            # Create symmetric points about y-axis
            x1 = random.randint(1, 4)
            y1 = random.randint(1, 5)

            # Make a symmetric quadrilateral about y-axis
            points = [(x1, y1), (-x1, y1), (-x1, -y1), (x1, -y1)]
            random.shuffle(points)

            latex = f"\\text{{Do points }} {points[0]}, {points[1]}, {points[2]}, {points[3]} \\text{{ form a figure with line symmetry?}}"
            solution = "Yes, about both axes"

            steps = [
                f"\\text{{Check for y-axis symmetry: for each (x, y), there is (-x, y)}}",
                f"\\text{{Check for x-axis symmetry: for each (x, y), there is (x, -y)}}",
                f"\\text{{This rectangle has symmetry about both the x-axis and y-axis.}}"
            ]
        else:
            shapes = [
                ("parallelogram (not rectangle)", "Rotational symmetry only (order 2)",
                 "A parallelogram has 180° rotational symmetry but no lines of symmetry."),
                ("rhombus", "Both line and rotational symmetry",
                 "A rhombus has 2 lines of symmetry (diagonals) and order 2 rotational symmetry."),
                ("kite", "Line symmetry only",
                 "A kite has 1 line of symmetry but no rotational symmetry."),
                ("isosceles trapezoid", "Line symmetry only",
                 "An isosceles trapezoid has 1 line of symmetry but no rotational symmetry."),
                ("regular hexagon", "Both line and rotational symmetry",
                 "A regular hexagon has 6 lines of symmetry and order 6 rotational symmetry.")
            ]

            shape, answer, explanation = random.choice(shapes)

            latex = f"\\text{{What type(s) of symmetry does a }} {shape} \\text{{ have?}}"
            solution = answer

            steps = [
                f"\\text{{{explanation}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex symmetry problems involving regular polygons"""
        problem_type = random.choice(['polygon_sides', 'mapping', 'composite'])

        if problem_type == 'polygon_sides':
            # Given symmetry properties, find the polygon
            n = random.choice([5, 6, 8, 10, 12])
            angle = 360 // n

            latex = f"\\text{{A regular polygon has rotational symmetry of }} {angle}°. \\text{{ How many sides does it have?}}"
            solution = str(n)

            steps = [
                f"\\text{{Angle of rotational symmetry = }} \\frac{{360°}}{{n}}",
                f"{angle}° = \\frac{{360°}}{{n}}",
                f"n = \\frac{{360°}}{{{angle}°}} = {n}",
                f"\\text{{The polygon has {n} sides.}}"
            ]

        elif problem_type == 'mapping':
            # Determine which rotation maps a vertex to another
            n = random.choice([6, 8])
            vertices = list(range(1, n + 1))
            start = random.choice(vertices)
            positions = random.randint(1, n - 1)
            end = ((start - 1 + positions) % n) + 1
            angle = (360 // n) * positions

            latex = f"\\text{{In a regular {n}-gon with vertices labeled 1-{n}, what rotation maps vertex {start} to vertex {end}?}}"
            solution = f"{angle}° counterclockwise"

            steps = [
                f"\\text{{Each vertex is separated by }} \\frac{{360°}}{{{n}}} = {360 // n}°",
                f"\\text{{From vertex {start} to {end} is {positions} positions}}",
                f"\\text{{Rotation = {positions} × {360 // n}° = {angle}°}}"
            ]

        else:
            # Find total symmetries
            n = random.choice([4, 5, 6, 8])
            name = {4: "square", 5: "regular pentagon", 6: "regular hexagon", 8: "regular octagon"}[n]
            total = 2 * n  # n rotations + n reflections

            latex = f"\\text{{How many total symmetries (rotations and reflections) does a }} {name} \\text{{ have?}}"
            solution = str(total)

            steps = [
                f"\\text{{A regular n-gon has n rotational symmetries (including identity)}}",
                f"\\text{{and n lines of reflection.}}",
                f"\\text{{Total symmetries = {n} + {n} = {total}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SymmetryGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
