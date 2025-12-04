"""
Constructing Lines and Angles Generator
Creates problems about geometric constructions with compass and straightedge
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ConstructingLinesAnglesGenerator:
    """Generates problems about constructing lines and angles."""

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
        """Basic construction descriptions"""
        problem_type = random.choice(['copy_segment', 'copy_angle', 'perpendicular_bisector'])

        if problem_type == 'copy_segment':
            length = random.randint(5, 12)

            latex = f"\\text{{Describe how to copy a segment of length }} {length} \\text{{ using compass and straightedge.}}"
            solution = "Place compass at one endpoint, draw arc from other endpoint"
            steps = [
                f"\\text{{1. Draw a ray from point A}}",
                f"\\text{{2. Set compass to length }} {length}",
                "\\text{3. Place compass point at A}",
                "\\text{4. Draw arc to intersect ray at B}",
                f"\\text{{5. AB has length }} {length}"
            ]

        elif problem_type == 'copy_angle':
            angle = random.randint(40, 120)

            latex = f"\\text{{What tool is needed to copy an angle of }} {angle}^\\circ?"
            solution = "Compass and straightedge"
            steps = [
                "\\text{1. Draw arc from vertex of original angle}",
                "\\text{2. Draw same arc from new vertex}",
                "\\text{3. Measure distance between arc intersections}",
                "\\text{4. Transfer this distance to new angle}"
            ]

        else:  # perpendicular_bisector
            length = random.randint(8, 16)

            latex = f"\\text{{A segment has length }} {length}. \\text{{ Where does its perpendicular bisector intersect the segment?}}"
            solution = f"At the midpoint, {length/2} from each end"
            steps = [
                "\\text{The perpendicular bisector intersects at the midpoint}",
                f"\\text{{Midpoint}} = \\frac{{{length}}}{{2}} = {length/2}",
                f"\\text{{This is }} {length/2} \\text{{ units from each endpoint}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Construction procedures"""
        problem_type = random.choice(['angle_bisector', 'perpendicular_point', 'parallel_line'])

        if problem_type == 'angle_bisector':
            angle = random.randint(60, 120)
            half = angle / 2

            latex = f"\\text{{Construct the angle bisector of an angle measuring }} {angle}^\\circ. "
            latex += "\\text{What is the measure of each resulting angle?}"
            solution = f"{half}°"
            steps = [
                f"\\text{{Original angle: }} {angle}^\\circ",
                "\\text{Angle bisector divides angle into two equal parts}",
                f"\\text{{Each part: }} \\frac{{{angle}^\\circ}}{{2}} = {half}^\\circ"
            ]

        elif problem_type == 'perpendicular_point':
            latex = "\\text{Describe how to construct a perpendicular to a line from a point not on the line.}"
            solution = "Use compass to create symmetric arcs, connect intersections"
            steps = [
                "\\text{1. From point P, draw arc intersecting line at two points A and B}",
                "\\text{2. From A and B, draw arcs with same radius below line}",
                "\\text{3. Let these arcs intersect at Q}",
                "\\text{4. Draw line PQ - this is perpendicular to original line}"
            ]

        else:  # parallel_line
            dist = random.randint(4, 10)

            latex = f"\\text{{Construct a line parallel to a given line at distance }} {dist} \\text{{ units. }}"
            latex += "\\text{What construction is used?}"
            solution = "Perpendicular lines at two points"
            steps = [
                "\\text{1. Construct perpendicular to original line at two points}",
                f"\\text{{2. Mark points }} {dist} \\text{{ units up each perpendicular}}",
                "\\text{3. Connect these points}",
                "\\text{4. Result is parallel line}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Complex constructions"""
        problem_type = random.choice(['60_degree', '45_degree', 'divide_segment'])

        if problem_type == '60_degree':
            latex = "\\text{How can you construct a } 60^\\circ \\text{ angle using only compass and straightedge?}"
            solution = "Construct equilateral triangle"
            steps = [
                "\\text{1. Draw a ray from point A}",
                "\\text{2. Place compass at A, draw arc intersecting ray at B}",
                "\\text{3. With same radius, draw arc from B}",
                "\\text{4. Let arcs intersect at C}",
                "\\text{5. Triangle ABC is equilateral}",
                "\\text{6. Each angle measures } 60^\\circ"
            ]

        elif problem_type == '45_degree':
            latex = "\\text{Describe how to construct a } 45^\\circ \\text{ angle.}"
            solution = "Bisect a right angle"
            steps = [
                "\\text{1. Construct a perpendicular (} 90^\\circ \\text{ angle)}",
                "\\text{2. Bisect the } 90^\\circ \\text{ angle}",
                f"\\text{{3. Each resulting angle: }} \\frac{{90^\\circ}}{{2}} = 45^\\circ"
            ]

        else:  # divide_segment
            n = random.choice([3, 4, 5])

            latex = f"\\text{{How can you divide a segment into }} {n} \\text{{ equal parts using compass and straightedge?}}"
            solution = "Use parallel lines construction"
            steps = [
                "\\text{1. Draw ray from one endpoint at any angle}",
                f"\\text{{2. Mark }} {n} \\text{{ equal segments along the ray}}",
                "\\text{3. Connect last point to other endpoint of original segment}",
                f"\\text{{4. Draw parallels through other }} {n-1} \\text{{ points}}",
                f"\\text{{5. These divide original segment into }} {n} \\text{{ equal parts}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Advanced constructions and impossibilities"""
        problem_type = random.choice(['inscribed_circle', 'circumscribed_circle', 'regular_hexagon'])

        if problem_type == 'inscribed_circle':
            latex = "\\text{Describe how to construct the inscribed circle (incircle) of a triangle.}"
            solution = "Find incenter using angle bisectors"
            steps = [
                "\\text{1. Construct the three angle bisectors of the triangle}",
                "\\text{2. The incenter I is where they intersect}",
                "\\text{3. Construct perpendicular from I to any side}",
                "\\text{4. Let this perpendicular meet the side at point P}",
                "\\text{5. Draw circle with center I and radius IP}",
                "\\text{6. This circle is tangent to all three sides}"
            ]

        elif problem_type == 'circumscribed_circle':
            latex = "\\text{How do you construct the circumscribed circle (circumcircle) of a triangle?}"
            solution = "Find circumcenter using perpendicular bisectors"
            steps = [
                "\\text{1. Construct perpendicular bisectors of two sides}",
                "\\text{2. The circumcenter O is where they intersect}",
                "\\text{3. O is equidistant from all three vertices}",
                "\\text{4. Draw circle with center O passing through any vertex}",
                "\\text{5. This circle passes through all three vertices}"
            ]

        else:  # regular_hexagon
            side = random.randint(5, 10)

            latex = f"\\text{{Construct a regular hexagon with side length }} {side}. \\text{{ What angle is at each vertex?}}"
            solution = "120°"
            steps = [
                "\\text{1. Draw a circle}",
                "\\text{2. Mark a point on the circle}",
                "\\text{3. With same radius, step around circle 6 times}",
                "\\text{4. Connect the 6 points to form hexagon}",
                "\\text{Interior angle of regular hexagon:}",
                "\\frac{(6-2) \\times 180^\\circ}{6} = \\frac{720^\\circ}{6} = 120^\\circ"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ConstructingLinesAnglesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")


if __name__ == '__main__':
    main()
