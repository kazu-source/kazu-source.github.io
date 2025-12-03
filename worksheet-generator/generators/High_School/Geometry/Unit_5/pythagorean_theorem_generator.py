"""
Pythagorean Theorem Generator
Creates problems about finding missing sides of right triangles
"""

import random
import math
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class PythagoreanTheoremGenerator:
    """Generates problems about the Pythagorean theorem."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
        # Common Pythagorean triples
        self.triples = [
            (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
            (6, 8, 10), (9, 12, 15), (12, 16, 20), (15, 20, 25),
            (10, 24, 26), (20, 21, 29), (9, 40, 41), (12, 35, 37)
        ]

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
        """Find hypotenuse given two legs using simple triples"""
        a, b, c = random.choice(self.triples[:4])  # Use simpler triples

        latex = f"\\text{{Find the hypotenuse of a right triangle with legs }} a = {a} \\text{{ and }} b = {b}."
        solution = str(c)

        steps = [
            f"\\text{{Pythagorean Theorem: }} a^2 + b^2 = c^2",
            f"{a}^2 + {b}^2 = c^2",
            f"{a**2} + {b**2} = c^2",
            f"{a**2 + b**2} = c^2",
            f"c = \\sqrt{{{a**2 + b**2}}} = {c}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Find a leg given hypotenuse and other leg"""
        a, b, c = random.choice(self.triples)

        # Randomly choose to find leg a or leg b
        if random.choice([True, False]):
            given_leg = b
            missing_leg = a
            leg_name = "a"
        else:
            given_leg = a
            missing_leg = b
            leg_name = "b"

        latex = f"\\text{{Find the missing leg of a right triangle with one leg }} = {given_leg} \\text{{ and hypotenuse }} = {c}."
        solution = str(missing_leg)

        steps = [
            f"\\text{{Pythagorean Theorem: }} a^2 + b^2 = c^2",
            f"{leg_name}^2 + {given_leg}^2 = {c}^2",
            f"{leg_name}^2 = {c}^2 - {given_leg}^2",
            f"{leg_name}^2 = {c**2} - {given_leg**2}",
            f"{leg_name}^2 = {c**2 - given_leg**2}",
            f"{leg_name} = \\sqrt{{{c**2 - given_leg**2}}} = {missing_leg}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Algebraic problems or non-integer answers"""
        problem_type = random.choice(['algebraic', 'radical'])

        if problem_type == 'algebraic':
            # Solve for x where sides are given in terms of x
            a, b, c = random.choice(self.triples[:6])
            x = random.randint(2, 5)

            # Make one side = x, scale the triple
            latex = f"\\text{{In a right triangle, legs are }} {a}x \\text{{ and }} {b}x, \\text{{ and the hypotenuse is }} {c * x}. \\text{{ Find }} x."
            solution = str(x)

            steps = [
                f"({a}x)^2 + ({b}x)^2 = ({c * x})^2",
                f"{a**2}x^2 + {b**2}x^2 = {(c*x)**2}",
                f"{a**2 + b**2}x^2 = {(c*x)**2}",
                f"\\text{{Since }} {a**2 + b**2} = {c**2}, \\text{{ the equation holds for any }} x.",
                f"\\text{{Given hypotenuse }} = {c * x}: c = {c}x, \\text{{ so }} x = {x}"
            ]
        else:
            # Non-Pythagorean triple with radical answer
            a = random.randint(3, 8)
            b = random.randint(3, 8)
            c_squared = a**2 + b**2

            # Check if it's a perfect square
            c_sqrt = int(math.sqrt(c_squared))
            if c_sqrt * c_sqrt == c_squared:
                solution = str(c_sqrt)
                c_display = str(c_sqrt)
            else:
                solution = f"\\sqrt{{{c_squared}}}"
                c_display = f"\\sqrt{{{c_squared}}}"

            latex = f"\\text{{Find the hypotenuse of a right triangle with legs }} {a} \\text{{ and }} {b}."

            steps = [
                f"c^2 = {a}^2 + {b}^2",
                f"c^2 = {a**2} + {b**2}",
                f"c^2 = {c_squared}",
                f"c = {c_display}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Word problems or multi-step applications"""
        problem_type = random.choice(['ladder', 'diagonal', 'distance', 'isosceles'])

        if problem_type == 'ladder':
            # Ladder against wall
            a, b, c = random.choice([(5, 12, 13), (8, 15, 17), (6, 8, 10)])

            latex = f"\\text{{A {c}-foot ladder leans against a wall. The base is {a} feet from the wall. How high does it reach?}}"
            solution = str(b)

            steps = [
                f"\\text{{The ladder, wall, and ground form a right triangle.}}",
                f"\\text{{Ladder (hypotenuse) = {c}, base = {a}, height = ?}}",
                f"h^2 + {a}^2 = {c}^2",
                f"h^2 = {c**2} - {a**2} = {c**2 - a**2}",
                f"h = {b} \\text{{ feet}}"
            ]

        elif problem_type == 'diagonal':
            # Rectangle diagonal
            width = random.randint(3, 8)
            height = random.randint(4, 10)
            diag_sq = width**2 + height**2
            diag = int(math.sqrt(diag_sq)) if int(math.sqrt(diag_sq))**2 == diag_sq else f"\\sqrt{{{diag_sq}}}"

            latex = f"\\text{{Find the diagonal of a rectangle with width {width} and height {height}.}}"
            solution = str(diag)

            steps = [
                f"\\text{{The diagonal forms a right triangle with the sides.}}",
                f"d^2 = {width}^2 + {height}^2",
                f"d^2 = {width**2} + {height**2} = {diag_sq}",
                f"d = {diag}"
            ]

        elif problem_type == 'distance':
            # Distance between points
            x1, y1 = random.randint(0, 3), random.randint(0, 3)
            a, b, c = random.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)])
            x2, y2 = x1 + a, y1 + b

            latex = f"\\text{{Find the distance between }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})."
            solution = str(c)

            steps = [
                f"\\text{{Distance formula uses the Pythagorean theorem.}}",
                f"d = \\sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}}",
                f"d = \\sqrt{{({x2} - {x1})^2 + ({y2} - {y1})^2}}",
                f"d = \\sqrt{{{a}^2 + {b}^2}} = \\sqrt{{{a**2 + b**2}}} = {c}"
            ]

        else:
            # Altitude of isosceles triangle
            base = random.choice([6, 8, 10, 12])
            leg = random.choice([5, 10, 13, 15])
            while leg <= base // 2:
                leg = random.choice([5, 10, 13, 15])

            half_base = base // 2
            h_squared = leg**2 - half_base**2
            h = int(math.sqrt(h_squared)) if int(math.sqrt(h_squared))**2 == h_squared else f"\\sqrt{{{h_squared}}}"

            latex = f"\\text{{Find the altitude of an isosceles triangle with base {base} and equal legs of length {leg}.}}"
            solution = str(h)

            steps = [
                f"\\text{{The altitude bisects the base, creating two right triangles.}}",
                f"\\text{{Each right triangle has leg }} \\frac{{{base}}}{{2}} = {half_base} \\text{{ and hypotenuse }} {leg}",
                f"h^2 + {half_base}^2 = {leg}^2",
                f"h^2 = {leg**2} - {half_base**2} = {h_squared}",
                f"h = {h}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = PythagoreanTheoremGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
