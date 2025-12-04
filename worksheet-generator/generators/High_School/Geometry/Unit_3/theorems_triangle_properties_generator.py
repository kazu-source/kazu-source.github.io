"""
Theorems About Triangle Properties Generator
Creates problems about triangle theorems and properties
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class TheoremsTrianglePropertiesGenerator:
    """Generates problems about triangle theorems and properties."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

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
        """Basic triangle properties"""
        problem_type = random.choice(['angle_sum', 'exterior_angle', 'isosceles'])

        if problem_type == 'angle_sum':
            a1 = random.randint(40, 70)
            a2 = random.randint(40, 80)
            a3 = 180 - a1 - a2

            latex = f"\\text{{In }} \\triangle ABC, \\angle A = {a1}^\\circ \\text{{ and }} \\angle B = {a2}^\\circ. \\text{{ Find }} \\angle C."
            solution = f"{a3}°"
            steps = [
                "\\text{Sum of angles in a triangle = } 180^\\circ",
                f"\\angle A + \\angle B + \\angle C = 180^\\circ",
                f"{a1}^\\circ + {a2}^\\circ + \\angle C = 180^\\circ",
                f"\\angle C = 180^\\circ - {a1}^\\circ - {a2}^\\circ = {a3}^\\circ"
            ]

        elif problem_type == 'exterior_angle':
            a1 = random.randint(45, 70)
            a2 = random.randint(50, 75)
            ext = a1 + a2

            latex = f"\\text{{In }} \\triangle ABC, \\angle A = {a1}^\\circ \\text{{ and }} \\angle B = {a2}^\\circ. "
            latex += "\\text{Find the exterior angle at C.}"
            solution = f"{ext}°"
            steps = [
                "\\text{Exterior angle = sum of two remote interior angles}",
                f"\\text{{Exterior angle at C}} = \\angle A + \\angle B",
                f"= {a1}^\\circ + {a2}^\\circ = {ext}^\\circ"
            ]

        else:  # isosceles
            base_angle = random.randint(50, 75)
            vertex_angle = 180 - 2 * base_angle

            latex = f"\\text{{An isosceles triangle has base angles of }} {base_angle}^\\circ. \\text{{ Find the vertex angle.}}"
            solution = f"{vertex_angle}°"
            steps = [
                f"\\text{{Base angles are equal: both }} {base_angle}^\\circ",
                "\\text{Sum of angles = } 180^\\circ",
                f"\\text{{Vertex angle}} = 180^\\circ - 2({base_angle}^\\circ) = {vertex_angle}^\\circ"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Triangle inequality and relationships"""
        problem_type = random.choice(['triangle_inequality', 'longest_side', 'altitude'])

        if problem_type == 'triangle_inequality':
            s1 = random.randint(5, 10)
            s2 = random.randint(7, 12)
            valid_s3 = random.randint(abs(s1 - s2) + 1, s1 + s2 - 1)
            invalid_s3 = s1 + s2 + random.randint(1, 3)

            if random.choice([True, False]):
                latex = f"\\text{{Can a triangle have sides }} {s1}, {s2}, {valid_s3}? \\text{{ Why?}}"
                solution = "Yes"
                steps = [
                    "\\text{Check triangle inequality: sum of any two sides > third side}",
                    f"{s1} + {s2} = {s1 + s2} > {valid_s3} \\checkmark",
                    f"{s1} + {valid_s3} = {s1 + valid_s3} > {s2} \\checkmark",
                    f"{s2} + {valid_s3} = {s2 + valid_s3} > {s1} \\checkmark",
                    "\\text{Yes, a triangle can have these sides}"
                ]
            else:
                latex = f"\\text{{Can a triangle have sides }} {s1}, {s2}, {invalid_s3}? \\text{{ Why?}}"
                solution = "No"
                steps = [
                    "\\text{Check triangle inequality: sum of any two sides > third side}",
                    f"{s1} + {s2} = {s1 + s2} \\not> {invalid_s3}",
                    "\\text{Triangle inequality is violated}",
                    "\\text{No, these sides cannot form a triangle}"
                ]

        elif problem_type == 'longest_side':
            angles = sorted([random.randint(40, 60), random.randint(50, 70), random.randint(50, 80)])
            angles[2] = 180 - angles[0] - angles[1]

            latex = f"\\text{{In }} \\triangle ABC, \\angle A = {angles[0]}^\\circ, \\angle B = {angles[1]}^\\circ, \\angle C = {angles[2]}^\\circ. "
            latex += "\\text{Which side is longest?}"

            largest_angle_idx = angles.index(max(angles))
            side_names = ['BC (opposite A)', 'AC (opposite B)', 'AB (opposite C)']
            solution = side_names[largest_angle_idx]

            steps = [
                "\\text{The longest side is opposite the largest angle}",
                f"\\text{{Largest angle: }} {max(angles)}^\\circ",
                f"\\text{{This is angle }} {['A', 'B', 'C'][largest_angle_idx]}",
                f"\\text{{Longest side: }} {solution}"
            ]

        else:  # altitude
            base = random.randint(8, 16)
            area = random.randint(40, 80)
            height = (2 * area) / base

            latex = f"\\text{{A triangle has base }} {base} \\text{{ and area }} {area}. \\text{{ Find the altitude to that base.}}"
            solution = f"{height}"
            steps = [
                f"\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}",
                f"{area} = \\frac{{1}}{{2}} \\times {base} \\times h",
                f"{2 * area} = {base} \\times h",
                f"h = \\frac{{{2 * area}}}{{{base}}} = {height}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Advanced triangle theorems"""
        problem_type = random.choice(['angle_bisector', 'median', 'centroid'])

        if problem_type == 'angle_bisector':
            angle = random.randint(60, 120)
            half = angle / 2

            latex = f"\\text{{The angle bisector of }} \\angle A = {angle}^\\circ \\text{{ in }} \\triangle ABC \\text{{ divides it into two angles. Find each.}}"
            solution = f"{half}° and {half}°"
            steps = [
                "\\text{An angle bisector divides an angle into two equal parts}",
                f"\\text{{Each part}} = \\frac{{{angle}^\\circ}}{{2}} = {half}^\\circ"
            ]

        elif problem_type == 'median':
            latex = "\\text{How many medians does a triangle have, and where do they intersect?}"
            solution = "3 medians, intersecting at the centroid"
            steps = [
                "\\text{Each triangle has 3 vertices}",
                "\\text{Each vertex has a median to the opposite side}",
                "\\text{Therefore, 3 medians}",
                "\\text{They intersect at a single point called the centroid}"
            ]

        else:  # centroid
            coord = random.randint(12, 24)

            latex = f"\\text{{A median of a triangle is }} {coord} \\text{{ units long. }}"
            latex += "\\text{How far from the vertex is the centroid along this median?}"

            dist = (2 * coord) / 3
            solution = f"{dist:.1f} units"
            steps = [
                "\\text{The centroid divides each median in ratio 2:1}",
                "\\text{Distance from vertex to centroid = } \\frac{2}{3} \\times \\text{median}",
                f"= \\frac{{2}}{{3}} \\times {coord} = {dist:.1f} \\text{{ units}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex triangle theorems and proofs"""
        problem_type = random.choice(['midsegment', 'orthocenter', 'angle_bisector_theorem'])

        if problem_type == 'midsegment':
            base = random.randint(10, 24)
            midseg = base / 2

            latex = f"\\text{{The midsegment of a triangle parallel to a side of length }} {base} \\text{{ has what length?}}"
            solution = f"{midseg}"
            steps = [
                "\\text{The midsegment connects the midpoints of two sides}",
                "\\text{Midsegment Theorem: midsegment is parallel to third side}",
                "\\text{and has length equal to half the third side}",
                f"\\text{{Length}} = \\frac{{{base}}}{{2}} = {midseg}"
            ]

        elif problem_type == 'orthocenter':
            latex = "\\text{What is the orthocenter of a triangle, and how is it formed?}"
            solution = "Intersection of the three altitudes"
            steps = [
                "\\text{An altitude is perpendicular from a vertex to opposite side}",
                "\\text{Every triangle has three altitudes}",
                "\\text{The three altitudes intersect at one point}",
                "\\text{This point is called the orthocenter}"
            ]

        else:  # angle_bisector_theorem
            side1 = random.randint(6, 10)
            side2 = random.randint(8, 12)
            seg1 = random.randint(3, 5)
            seg2 = (side2 * seg1) / side1

            latex = f"\\text{{By the Angle Bisector Theorem, if sides AB = }} {side1} \\text{{ and AC = }} {side2}, "
            latex += f"\\text{{and the angle bisector divides BC such that BD = }} {seg1}, \\text{{ find DC.}}"
            solution = f"{seg2:.2f}"
            steps = [
                "\\text{Angle Bisector Theorem: } \\frac{BD}{DC} = \\frac{AB}{AC}",
                f"\\frac{{{seg1}}}{{DC}} = \\frac{{{side1}}}{{{side2}}}",
                f"DC = \\frac{{{seg1} \\times {side2}}}{{{side1}}} = {seg2:.2f}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = TheoremsTrianglePropertiesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")


if __name__ == '__main__':
    main()
