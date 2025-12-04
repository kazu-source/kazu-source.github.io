"""
Working with Triangles Generator
Creates problems about triangle constructions, classifications, and basic properties
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class WorkingWithTrianglesGenerator:
    """Generates problems about working with triangles."""

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
        """Basic triangle classification"""
        problem_type = random.choice(['classify_angles', 'classify_sides', 'perimeter'])

        if problem_type == 'classify_angles':
            angles = random.choice([
                ([30, 60, 90], 'right'),
                ([50, 60, 70], 'acute'),
                ([30, 40, 110], 'obtuse')
            ])

            latex = f"\\text{{Classify a triangle with angles }} {angles[0][0]}^\\circ, {angles[0][1]}^\\circ, {angles[0][2]}^\\circ."
            solution = f"{angles[1]} triangle"
            steps = [
                f"\\text{{Angles: }} {angles[0][0]}^\\circ, {angles[0][1]}^\\circ, {angles[0][2]}^\\circ",
                f"\\text{{Classification: {angles[1]} triangle}}"
            ]

        elif problem_type == 'classify_sides':
            sides = random.choice([
                ([7, 7, 7], 'equilateral'),
                ([5, 5, 8], 'isosceles'),
                ([6, 7, 8], 'scalene')
            ])

            latex = f"\\text{{Classify a triangle with sides }} {sides[0][0]}, {sides[0][1]}, {sides[0][2]}."
            solution = f"{sides[1]} triangle"
            steps = [
                f"\\text{{Sides: }} {sides[0][0]}, {sides[0][1]}, {sides[0][2]}",
                f"\\text{{Classification: {sides[1]} triangle}}"
            ]

        else:  # perimeter
            s1, s2, s3 = random.randint(5, 12), random.randint(6, 13), random.randint(7, 14)
            perim = s1 + s2 + s3

            latex = f"\\text{{Find the perimeter of a triangle with sides }} {s1}, {s2}, {s3}."
            solution = f"{perim}"
            steps = [
                f"\\text{{Perimeter}} = {s1} + {s2} + {s3} = {perim}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Triangle area and properties"""
        problem_type = random.choice(['area', 'missing_side', 'isosceles_properties'])

        if problem_type == 'area':
            base = random.randint(8, 16)
            height = random.randint(5, 12)
            area = 0.5 * base * height

            latex = f"\\text{{Find the area of a triangle with base }} {base} \\text{{ and height }} {height}."
            solution = f"{area}"
            steps = [
                f"\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}",
                f"= \\frac{{1}}{{2}} \\times {base} \\times {height} = {area}"
            ]

        elif problem_type == 'missing_side':
            perim = random.randint(30, 50)
            s1 = random.randint(8, 15)
            s2 = random.randint(8, 15)
            s3 = perim - s1 - s2

            latex = f"\\text{{A triangle has perimeter }} {perim} \\text{{ and two sides of length }} {s1} \\text{{ and }} {s2}. "
            latex += "\\text{Find the third side.}"
            solution = f"{s3}"
            steps = [
                f"\\text{{Perimeter}} = s_1 + s_2 + s_3",
                f"{perim} = {s1} + {s2} + s_3",
                f"s_3 = {perim} - {s1} - {s2} = {s3}"
            ]

        else:  # isosceles_properties
            leg = random.randint(8, 15)
            vertex_angle = random.randint(40, 100)
            base_angle = (180 - vertex_angle) / 2

            latex = f"\\text{{An isosceles triangle has legs of length }} {leg} \\text{{ and vertex angle }} {vertex_angle}^\\circ. "
            latex += "\\text{Find the base angles.}"
            solution = f"{base_angle}°"
            steps = [
                "\\text{In an isosceles triangle, base angles are equal}",
                f"\\text{{Sum of angles}} = 180^\\circ",
                f"2 \\times \\text{{base angle}} = 180^\\circ - {vertex_angle}^\\circ = {180 - vertex_angle}^\\circ",
                f"\\text{{Base angle}} = {base_angle}^\\circ"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Advanced triangle problems"""
        problem_type = random.choice(['equilateral_area', 'coordinate_triangle', 'heron_formula'])

        if problem_type == 'equilateral_area':
            side = random.randint(6, 12)
            import math
            area = (math.sqrt(3) / 4) * side * side

            latex = f"\\text{{Find the area of an equilateral triangle with side length }} {side}."
            solution = f"{area:.2f}"
            steps = [
                f"\\text{{For equilateral triangle: Area}} = \\frac{{\\sqrt{{3}}}}{{4}} s^2",
                f"= \\frac{{\\sqrt{{3}}}}{{4}} \\times {side}^2",
                f"= \\frac{{\\sqrt{{3}}}}{{4}} \\times {side * side} = {area:.2f}"
            ]

        elif problem_type == 'coordinate_triangle':
            x1, y1 = 0, 0
            x2, y2 = random.randint(4, 8), 0
            x3, y3 = random.randint(2, 6), random.randint(4, 8)

            area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

            latex = f"\\text{{Find the area of triangle with vertices }} ({x1},{y1}), ({x2},{y2}), ({x3},{y3})."
            solution = f"{area}"
            steps = [
                "\\text{Using coordinate formula: } A = \\frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)|",
                f"= \\frac{{1}}{{2}}|{x1}({y2}-{y3}) + {x2}({y3}-{y1}) + {x3}({y1}-{y2})|",
                f"= \\frac{{1}}{{2}} \\times {2 * area} = {area}"
            ]

        else:  # heron_formula
            s1, s2, s3 = 5, 6, 7
            s = (s1 + s2 + s3) / 2
            import math
            area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

            latex = f"\\text{{Use Heron's formula to find the area of a triangle with sides }} {s1}, {s2}, {s3}."
            solution = f"{area:.2f}"
            steps = [
                f"\\text{{Semi-perimeter: }} s = \\frac{{{s1} + {s2} + {s3}}}{{2}} = {s}",
                f"\\text{{Area}} = \\sqrt{{s(s-a)(s-b)(s-c)}}",
                f"= \\sqrt{{{s} \\times {s-s1} \\times {s-s2} \\times {s-s3}}}",
                f"= {area:.2f}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex triangle constructions and proofs"""
        problem_type = random.choice(['altitude_area', 'triangle_centers', 'napoleon'])

        if problem_type == 'altitude_area':
            s1, s2, s3 = 6, 8, 10  # Right triangle
            area = 0.5 * s1 * s2

            latex = f"\\text{{A triangle has sides }} {s1}, {s2}, {s3}. \\text{{ Find the altitude to the side of length }} {s3}."
            solution = f"{2 * area / s3}"
            steps = [
                f"\\text{{First find area using two legs: }} A = \\frac{{1}}{{2}} \\times {s1} \\times {s2} = {area}",
                f"\\text{{Now use: }} A = \\frac{{1}}{{2}} \\times {s3} \\times h",
                f"{area} = \\frac{{1}}{{2}} \\times {s3} \\times h",
                f"h = \\frac{{2 \\times {area}}}{{{s3}}} = {2 * area / s3}"
            ]

        elif problem_type == 'triangle_centers':
            latex = "\\text{Name the four main centers of a triangle and describe one.}"
            solution = "Centroid, circumcenter, incenter, orthocenter"
            steps = [
                "\\text{1. Centroid: intersection of medians}",
                "\\text{2. Circumcenter: intersection of perpendicular bisectors}",
                "\\text{3. Incenter: intersection of angle bisectors}",
                "\\text{4. Orthocenter: intersection of altitudes}"
            ]

        else:  # napoleon
            latex = "\\text{In an equilateral triangle with side } s, \\text{ what is the height?}"
            solution = f"h = (√3/2)s"
            steps = [
                "\\text{In an equilateral triangle, use 30-60-90 properties}",
                "\\text{The height bisects the base, creating two 30-60-90 triangles}",
                "\\text{In 30-60-90 triangle: height = } \\frac{\\sqrt{3}}{2} \\times \\text{side}",
                "h = \\frac{\\sqrt{3}}{2}s"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = WorkingWithTrianglesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")


if __name__ == '__main__':
    main()
