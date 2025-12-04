"""
Proofs of General Theorems Generator
Creates problems about proving general geometric theorems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ProofsGeneralTheoremsGenerator:
    """Generates problems about proving general geometric theorems."""

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
        """Basic proof concepts"""
        problem_type = random.choice(['vertical_angles', 'linear_pair', 'corresponding'])

        if problem_type == 'vertical_angles':
            angle = random.randint(50, 130)

            latex = f"\\text{{Two lines intersect forming an angle of }} {angle}^\\circ. \\text{{ Find the vertical angle.}}"
            solution = f"{angle}°"
            steps = [
                "\\text{Vertical angles are congruent}",
                f"\\text{{Vertical angle}} = {angle}^\\circ"
            ]

        elif problem_type == 'linear_pair':
            angle = random.randint(60, 120)
            supplement = 180 - angle

            latex = f"\\text{{Two angles form a linear pair. If one angle is }} {angle}^\\circ, \\text{{ find the other.}}"
            solution = f"{supplement}°"
            steps = [
                "\\text{Linear pairs are supplementary (sum to } 180^\\circ)",
                f"\\text{{Other angle}} = 180^\\circ - {angle}^\\circ = {supplement}^\\circ"
            ]

        else:  # corresponding
            angle = random.randint(70, 110)

            latex = f"\\text{{Two parallel lines are cut by a transversal. If one angle is }} {angle}^\\circ, "
            latex += "\\text{what is the corresponding angle?}"
            solution = f"{angle}°"
            steps = [
                "\\text{Corresponding angles are congruent when lines are parallel}",
                f"\\text{{Corresponding angle}} = {angle}^\\circ"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Two-column proof setup"""
        problem_type = random.choice(['alternate_interior', 'triangle_sum', 'exterior_angle'])

        if problem_type == 'alternate_interior':
            angle = random.randint(65, 115)

            latex = f"\\text{{Parallel lines cut by transversal. If one interior angle is }} {angle}^\\circ, "
            latex += "\\text{find the alternate interior angle.}"
            solution = f"{angle}°"
            steps = [
                "\\text{Given: Lines are parallel}",
                "\\text{Alternate interior angles are congruent when lines are parallel}",
                f"\\text{{Alternate interior angle}} = {angle}^\\circ"
            ]

        elif problem_type == 'triangle_sum':
            latex = "\\text{Prove: The sum of angles in a triangle is } 180^\\circ."
            solution = "Use parallel lines and alternate interior angles"
            steps = [
                "\\text{Draw line parallel to base through opposite vertex}",
                "\\text{Alternate interior angles are congruent}",
                "\\text{The three angles at the vertex form a straight line}",
                "\\text{Therefore, sum of triangle's angles = } 180^\\circ"
            ]

        else:  # exterior_angle
            a1 = random.randint(50, 70)
            a2 = random.randint(60, 80)
            ext = a1 + a2

            latex = f"\\text{{Prove: An exterior angle of a triangle equals the sum of the two remote interior angles. }}"
            latex += f"\\text{{If the remote interior angles are }} {a1}^\\circ \\text{{ and }} {a2}^\\circ, \\text{{ find the exterior angle.}}"
            solution = f"{ext}°"
            steps = [
                f"\\text{{Remote interior angles: }} {a1}^\\circ \\text{{ and }} {a2}^\\circ",
                f"\\text{{Third interior angle}} = 180^\\circ - {a1}^\\circ - {a2}^\\circ = {180 - a1 - a2}^\\circ",
                f"\\text{{Exterior angle}} = 180^\\circ - {180 - a1 - a2}^\\circ = {ext}^\\circ",
                f"\\text{{Alternatively: }} {a1}^\\circ + {a2}^\\circ = {ext}^\\circ"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Complete proofs"""
        problem_type = random.choice(['base_angles', 'perpendicular_bisector', 'parallelogram_diagonals'])

        if problem_type == 'base_angles':
            latex = "\\text{Prove: Base angles of an isosceles triangle are congruent.}"
            solution = "Use SAS and CPCTC"
            steps = [
                "\\text{Given: Triangle ABC with AB = AC}",
                "\\text{Draw altitude from A to BC, meeting at D}",
                "\\text{In triangles ABD and ACD:}",
                "\\text{AB = AC (given), AD = AD (reflexive), BD = CD (altitude bisects base)}",
                "\\text{By SSS, } \\triangle ABD \\cong \\triangle ACD",
                "\\text{Therefore } \\angle B = \\angle C \\text{ by CPCTC}"
            ]

        elif problem_type == 'perpendicular_bisector':
            latex = "\\text{Prove: Any point on the perpendicular bisector of a segment is equidistant from the endpoints.}"
            solution = "Use SAS congruence"
            steps = [
                "\\text{Given: Line } l \\text{ is perpendicular bisector of } \\overline{AB}, \\text{ P on } l",
                "\\text{Let M be midpoint of AB}",
                "\\text{In triangles AMP and BMP:}",
                "AM = BM \\text{ (M is midpoint)}",
                "PM = PM \\text{ (reflexive)}",
                "\\angle AMP = \\angle BMP = 90^\\circ \\text{ (perpendicular)}",
                "\\text{By SAS, } \\triangle AMP \\cong \\triangle BMP",
                "\\text{Therefore PA = PB by CPCTC}"
            ]

        else:  # parallelogram_diagonals
            latex = "\\text{Prove: The diagonals of a parallelogram bisect each other.}"
            solution = "Use ASA or alternate interior angles"
            steps = [
                "\\text{Given: Parallelogram ABCD with diagonals AC and BD intersecting at E}",
                "\\text{AB } \\parallel \\text{ DC, so } \\angle BAC = \\angle DCA \\text{ (alternate interior)}",
                "\\text{AB } \\parallel \\text{ DC, so } \\angle ABD = \\angle CDB \\text{ (alternate interior)}",
                "AB = DC \\text{ (opposite sides of parallelogram)}",
                "\\text{By ASA, } \\triangle ABE \\cong \\triangle CDE",
                "\\text{Therefore AE = CE and BE = DE by CPCTC}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex proof problems"""
        problem_type = random.choice(['concurrence', 'ptolemy', 'ceva'])

        if problem_type == 'concurrence':
            latex = "\\text{Prove: The perpendicular bisectors of a triangle are concurrent.}"
            solution = "Use equidistant property and circumcenter"
            steps = [
                "\\text{Let } l_1 \\text{ and } l_2 \\text{ be perpendicular bisectors of AB and BC}",
                "\\text{Let P be their intersection}",
                "P \\text{ is equidistant from A and B (on } l_1)",
                "P \\text{ is equidistant from B and C (on } l_2)",
                "\\text{Therefore PA = PB = PC}",
                "\\text{Since PA = PC, P is on perpendicular bisector of AC}",
                "\\text{All three perpendicular bisectors pass through P}"
            ]

        elif problem_type == 'ptolemy':
            latex = "\\text{State Ptolemy's Theorem for a cyclic quadrilateral.}"
            solution = "Product of diagonals = sum of products of opposite sides"
            steps = [
                "\\text{Ptolemy's Theorem: In cyclic quadrilateral ABCD:}",
                "AC \\cdot BD = AB \\cdot CD + BC \\cdot AD",
                "\\text{The product of the diagonals equals}",
                "\\text{the sum of products of opposite sides}"
            ]

        else:  # ceva
            latex = "\\text{State Ceva's Theorem about concurrent cevians in a triangle.}"
            solution = "Product of ratios equals 1"
            steps = [
                "\\text{Ceva's Theorem: Three cevians AA', BB', CC' are concurrent iff:}",
                "\\frac{BA'}{A'C} \\cdot \\frac{CB'}{B'A} \\cdot \\frac{AC'}{C'B} = 1",
                "\\text{This applies to medians, altitudes, angle bisectors}",
                "\\text{All of which are concurrent}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ProofsGeneralTheoremsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")


if __name__ == '__main__':
    main()
