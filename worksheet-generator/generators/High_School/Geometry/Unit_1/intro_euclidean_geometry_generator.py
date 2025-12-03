"""
Introduction to Euclidean Geometry Generator
Creates problems about points, lines, planes, and basic geometric postulates
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class IntroEuclideanGeometryGenerator:
    """Generates problems about basic Euclidean geometry concepts."""

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
        """Basic definitions and identification"""
        concepts = [
            ("has no size, only location", "Point",
             "A point has no dimension - just a position in space."),
            ("extends infinitely in two directions and has no width", "Line",
             "A line is one-dimensional, extending forever in both directions."),
            ("is a flat surface that extends infinitely in all directions", "Plane",
             "A plane is a two-dimensional flat surface."),
            ("has two endpoints", "Line segment",
             "A line segment is part of a line with two endpoints."),
            ("has one endpoint and extends infinitely in one direction", "Ray",
             "A ray starts at a point and goes on forever in one direction."),
            ("is formed by two rays with a common endpoint", "Angle",
             "An angle is formed where two rays meet at a vertex."),
            ("are points that lie on the same line", "Collinear points",
             "Collinear means 'on the same line'."),
            ("are points that lie in the same plane", "Coplanar points",
             "Coplanar means 'in the same plane'.")
        ]

        desc, answer, explanation = random.choice(concepts)

        latex = f"\\text{{What geometric term describes something that }} {desc}\\text{{?}}"
        solution = answer

        steps = [
            f"\\text{{{explanation}}}",
            f"\\text{{Answer: {answer}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Postulates and basic relationships"""
        problem_type = random.choice(['postulate', 'relationship', 'notation'])

        if problem_type == 'postulate':
            postulates = [
                ("How many points determine a unique line?", "2",
                 "Through any two points, there is exactly one line."),
                ("How many non-collinear points determine a unique plane?", "3",
                 "Through any three non-collinear points, there is exactly one plane."),
                ("How many points do two distinct lines have in common at most?", "1",
                 "Two distinct lines intersect in at most one point."),
                ("If two planes intersect, their intersection is a ___", "Line",
                 "The intersection of two planes is always a line."),
                ("How many lines can be drawn through a single point?", "Infinitely many",
                 "Through any single point, infinitely many lines can pass.")
            ]

            question, answer, explanation = random.choice(postulates)
            latex = f"\\text{{{question}}}"

        elif problem_type == 'relationship':
            relationships = [
                ("Points A, B, and C are collinear with B between A and C. If AB = 5 and BC = 8, what is AC?", "13",
                 "By the Segment Addition Postulate: AC = AB + BC = 5 + 8 = 13"),
                ("Points P, Q, and R are collinear with Q between P and R. If PR = 12 and PQ = 7, what is QR?", "5",
                 "QR = PR - PQ = 12 - 7 = 5"),
                ("If M is the midpoint of segment AB and AM = 6, what is AB?", "12",
                 "AB = 2 × AM = 2 × 6 = 12"),
                ("Ray BD bisects angle ABC. If angle ABD = 35°, what is angle ABC?", "70°",
                 "Angle ABC = 2 × angle ABD = 2 × 35° = 70°")
            ]

            question, answer, explanation = random.choice(relationships)
            latex = f"\\text{{{question}}}"

        else:
            notations = [
                ("What does the symbol \\overrightarrow{AB} represent?", "Ray AB",
                 "An arrow over two letters represents a ray starting at the first point."),
                ("What does the symbol \\overline{AB} represent?", "Line segment AB",
                 "A bar over two letters represents a line segment."),
                ("What does the symbol \\overleftrightarrow{AB} represent?", "Line AB",
                 "Arrows on both ends represent a line extending in both directions."),
                ("What does m\\angle ABC represent?", "The measure of angle ABC",
                 "The 'm' before an angle symbol means 'measure of'.")
            ]

            question, answer, explanation = random.choice(notations)
            latex = question

        solution = answer
        steps = [
            f"\\text{{{explanation}}}",
            f"\\text{{Answer: {answer}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Apply postulates to find segment lengths or angle measures"""
        problem_type = random.choice(['segment', 'angle', 'midpoint'])

        if problem_type == 'segment':
            # Algebraic segment problems
            a = random.randint(2, 5)
            b = random.randint(1, 10)
            c = random.randint(2, 5)
            d = random.randint(1, 10)

            # AC = AB + BC, solve for x
            # (ax + b) + (cx + d) = total
            x = random.randint(2, 8)
            total = (a * x + b) + (c * x + d)

            latex = f"\\text{{B is between A and C. If }} AB = {a}x + {b}, BC = {c}x + {d}, \\text{{ and }} AC = {total}, \\text{{ find }} x."
            solution = str(x)

            steps = [
                f"\\text{{Segment Addition: }} AB + BC = AC",
                f"({a}x + {b}) + ({c}x + {d}) = {total}",
                f"{a + c}x + {b + d} = {total}",
                f"{a + c}x = {total - b - d}",
                f"x = {x}"
            ]

        elif problem_type == 'angle':
            # Ray bisects angle problem
            a = random.randint(2, 4)
            b = random.randint(1, 15)
            x = random.randint(5, 15)
            angle_half = a * x + b
            angle_full = 2 * angle_half

            latex = f"\\text{{Ray BD bisects }} \\angle ABC. \\text{{ If }} m\\angle ABD = {a}x + {b} \\text{{ and }} m\\angle ABC = {angle_full}, \\text{{ find }} x."
            solution = str(x)

            steps = [
                f"\\text{{Since BD bisects }} \\angle ABC: m\\angle ABD = \\frac{{1}}{{2}} m\\angle ABC",
                f"{a}x + {b} = \\frac{{{angle_full}}}{{2}}",
                f"{a}x + {b} = {angle_half}",
                f"{a}x = {angle_half - b}",
                f"x = {x}"
            ]

        else:
            # Midpoint problem
            a = random.randint(2, 4)
            b = random.randint(1, 10)
            x = random.randint(3, 10)
            am = a * x + b
            ab = 2 * am

            latex = f"\\text{{M is the midpoint of }} \\overline{{AB}}. \\text{{ If }} AM = {a}x + {b} \\text{{ and }} AB = {ab}, \\text{{ find }} x."
            solution = str(x)

            steps = [
                f"\\text{{Since M is the midpoint: }} AM = \\frac{{1}}{{2}} AB",
                f"{a}x + {b} = \\frac{{{ab}}}{{2}}",
                f"{a}x + {b} = {am}",
                f"{a}x = {am - b}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex problems involving multiple concepts"""
        problem_type = random.choice(['two_segments', 'complementary', 'supplementary'])

        if problem_type == 'two_segments':
            # Two midpoint problem
            x = random.randint(3, 8)
            am = random.randint(5, 15)
            mb = am  # M is midpoint so AM = MB
            ab = 2 * am
            bc = random.randint(8, 20)
            ac = ab + bc

            latex = f"\\text{{M is the midpoint of }} \\overline{{AB}}. \\text{{ If }} AM = {am} \\text{{ and }} BC = {bc}, \\text{{ find }} AC."
            solution = str(ac)

            steps = [
                f"\\text{{Since M is midpoint: }} AB = 2 \\times AM = 2 \\times {am} = {ab}",
                f"\\text{{By Segment Addition: }} AC = AB + BC",
                f"AC = {ab} + {bc} = {ac}"
            ]

        elif problem_type == 'complementary':
            # Complementary angles with algebra
            a = random.randint(2, 4)
            x = random.randint(5, 15)
            angle1 = a * x
            angle2 = 90 - angle1

            latex = f"\\text{{Angles A and B are complementary. If }} m\\angle A = {a}x \\text{{ and }} m\\angle B = {angle2}, \\text{{ find }} x."
            solution = str(x)

            steps = [
                f"\\text{{Complementary angles sum to }} 90°",
                f"{a}x + {angle2} = 90",
                f"{a}x = {90 - angle2}",
                f"x = {x}"
            ]

        else:
            # Supplementary angles with algebra
            a = random.randint(2, 5)
            b = random.randint(1, 20)
            c = random.randint(2, 5)
            d = random.randint(1, 20)

            # (ax + b) + (cx + d) = 180
            x = random.randint(5, 20)
            # Adjust to make it work
            total_coef = a + c
            target = 180 - b - d
            x = target // total_coef
            if x < 5:
                x = 10
                d = 180 - (a * x + b) - (c * x)

            angle1 = a * x + b
            angle2 = c * x + d

            latex = f"\\text{{Two angles are supplementary. One measures }} {a}x + {b} \\text{{ and the other measures }} {c}x + {d}. \\text{{ Find }} x."
            solution = str(x)

            steps = [
                f"\\text{{Supplementary angles sum to }} 180°",
                f"({a}x + {b}) + ({c}x + {d}) = 180",
                f"{a + c}x + {b + d} = 180",
                f"{a + c}x = {180 - b - d}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = IntroEuclideanGeometryGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
