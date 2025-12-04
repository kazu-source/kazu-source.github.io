"""
Theorems About Quadrilateral Properties Generator
Creates problems about quadrilateral theorems and properties
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class TheoremsQuadrilateralPropertiesGenerator:
    """Generates problems about quadrilateral theorems and properties."""

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
        """Basic quadrilateral properties"""
        problem_type = random.choice(['angle_sum', 'rectangle', 'square', 'parallelogram'])

        if problem_type == 'angle_sum':
            a1 = random.randint(70, 100)
            a2 = random.randint(80, 110)
            a3 = random.randint(70, 100)
            a4 = 360 - a1 - a2 - a3

            latex = f"\\text{{In quadrilateral ABCD, if }} \\angle A = {a1}^\\circ, \\angle B = {a2}^\\circ, \\angle C = {a3}^\\circ, \\text{{ find }} \\angle D."
            solution = f"{a4}°"
            steps = [
                "\\text{Sum of angles in a quadrilateral = } 360^\\circ",
                f"{a1}^\\circ + {a2}^\\circ + {a3}^\\circ + \\angle D = 360^\\circ",
                f"\\angle D = 360^\\circ - {a1 + a2 + a3}^\\circ = {a4}^\\circ"
            ]

        elif problem_type == 'rectangle':
            length = random.randint(8, 15)
            width = random.randint(5, 10)
            perim = 2 * (length + width)

            latex = f"\\text{{A rectangle has length }} {length} \\text{{ and width }} {width}. \\text{{ Find its perimeter.}}"
            solution = f"{perim}"
            steps = [
                f"\\text{{Perimeter}} = 2(\\text{{length}} + \\text{{width}})",
                f"= 2({length} + {width}) = 2 \\times {length + width} = {perim}"
            ]

        elif problem_type == 'square':
            side = random.randint(6, 12)
            area = side * side

            latex = f"\\text{{A square has side length }} {side}. \\text{{ Find its area.}}"
            solution = f"{area}"
            steps = [
                f"\\text{{Area}} = \\text{{side}}^2 = {side}^2 = {area}"
            ]

        else:  # parallelogram
            a1 = random.randint(60, 100)
            a2 = 180 - a1

            latex = f"\\text{{In parallelogram ABCD, if }} \\angle A = {a1}^\\circ, \\text{{ find }} \\angle B."
            solution = f"{a2}°"
            steps = [
                "\\text{Consecutive angles in a parallelogram are supplementary}",
                f"\\angle A + \\angle B = 180^\\circ",
                f"\\angle B = 180^\\circ - {a1}^\\circ = {a2}^\\circ"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Properties of special quadrilaterals"""
        problem_type = random.choice(['rhombus', 'trapezoid', 'kite', 'parallelogram_sides'])

        if problem_type == 'rhombus':
            side = random.randint(7, 15)
            perim = 4 * side

            latex = f"\\text{{A rhombus has one side of length }} {side}. \\text{{ Find its perimeter.}}"
            solution = f"{perim}"
            steps = [
                "\\text{A rhombus has all four sides equal}",
                f"\\text{{Perimeter}} = 4 \\times {side} = {perim}"
            ]

        elif problem_type == 'trapezoid':
            b1 = random.randint(8, 14)
            b2 = random.randint(16, 24)
            h = random.randint(6, 10)
            area = 0.5 * (b1 + b2) * h

            latex = f"\\text{{A trapezoid has bases }} {b1} \\text{{ and }} {b2} \\text{{ with height }} {h}. \\text{{ Find its area.}}"
            solution = f"{area}"
            steps = [
                f"\\text{{Area}} = \\frac{{1}}{{2}}(b_1 + b_2)h",
                f"= \\frac{{1}}{{2}}({b1} + {b2}) \\times {h}",
                f"= \\frac{{1}}{{2}} \\times {b1 + b2} \\times {h} = {area}"
            ]

        elif problem_type == 'kite':
            d1 = random.randint(8, 16)
            d2 = random.randint(10, 18)
            area = 0.5 * d1 * d2

            latex = f"\\text{{A kite has diagonals of length }} {d1} \\text{{ and }} {d2}. \\text{{ Find its area.}}"
            solution = f"{area}"
            steps = [
                f"\\text{{Area}} = \\frac{{1}}{{2}} d_1 d_2",
                f"= \\frac{{1}}{{2}} \\times {d1} \\times {d2} = {area}"
            ]

        else:  # parallelogram_sides
            side1 = random.randint(8, 15)
            side2 = random.randint(10, 18)

            latex = f"\\text{{A parallelogram has adjacent sides of length }} {side1} \\text{{ and }} {side2}. "
            latex += "\\text{What are the lengths of the other two sides?}"
            solution = f"{side1} and {side2}"
            steps = [
                "\\text{Opposite sides of a parallelogram are equal}",
                f"\\text{{The four sides are: }} {side1}, {side2}, {side1}, {side2}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Advanced quadrilateral theorems"""
        problem_type = random.choice(['parallelogram_diagonals', 'rectangle_diagonal', 'rhombus_angles'])

        if problem_type == 'parallelogram_diagonals':
            d1_half = random.randint(5, 10)
            d2_half = random.randint(6, 11)

            latex = f"\\text{{The diagonals of a parallelogram bisect each other. }}"
            latex += f"\\text{{If one diagonal is divided into segments of }} {d1_half} \\text{{ and }} {d1_half}, "
            latex += "\\text{what is the total length of this diagonal?}"
            solution = f"{2 * d1_half}"
            steps = [
                "\\text{Diagonals bisect each other, so both halves are equal}",
                f"\\text{{Total length}} = {d1_half} + {d1_half} = {2 * d1_half}"
            ]

        elif problem_type == 'rectangle_diagonal':
            length = random.randint(6, 12)
            width = random.randint(8, 14)
            import math
            diagonal = math.sqrt(length**2 + width**2)

            latex = f"\\text{{Find the diagonal of a rectangle with dimensions }} {length} \\times {width}."
            solution = f"{diagonal:.2f}"
            steps = [
                "\\text{Use Pythagorean theorem: } d^2 = l^2 + w^2",
                f"d^2 = {length}^2 + {width}^2 = {length**2} + {width**2} = {length**2 + width**2}",
                f"d = \\sqrt{{{length**2 + width**2}}} = {diagonal:.2f}"
            ]

        else:  # rhombus_angles
            angle = random.randint(50, 80)
            d1 = random.randint(10, 16)
            d2 = random.randint(12, 18)

            latex = f"\\text{{In a rhombus, one angle measures }} {angle}^\\circ. \\text{{ Find the adjacent angle.}}"
            solution = f"{180 - angle}°"
            steps = [
                "\\text{A rhombus is a parallelogram}",
                "\\text{Consecutive angles in a parallelogram are supplementary}",
                f"\\text{{Adjacent angle}} = 180^\\circ - {angle}^\\circ = {180 - angle}^\\circ"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex quadrilateral proofs and properties"""
        problem_type = random.choice(['prove_parallelogram', 'cyclic_quadrilateral', 'varignon'])

        if problem_type == 'prove_parallelogram':
            latex = "\\text{Prove: If both pairs of opposite sides of a quadrilateral are parallel, it is a parallelogram.}"
            solution = "This is the definition of a parallelogram"
            steps = [
                "\\text{Given: Quadrilateral ABCD with AB } \\parallel \\text{ DC and AD } \\parallel \\text{ BC}",
                "\\text{By definition, a parallelogram has both pairs of opposite sides parallel}",
                "\\text{Therefore, ABCD is a parallelogram by definition}"
            ]

        elif problem_type == 'cyclic_quadrilateral':
            a1 = random.randint(70, 110)
            a2 = 180 - a1

            latex = f"\\text{{In a cyclic quadrilateral, opposite angles are supplementary. }}"
            latex += f"\\text{{If one angle is }} {a1}^\\circ, \\text{{ what is the opposite angle?}}"
            solution = f"{a2}°"
            steps = [
                "\\text{In a cyclic quadrilateral, opposite angles sum to } 180^\\circ",
                f"\\text{{Opposite angle}} = 180^\\circ - {a1}^\\circ = {a2}^\\circ"
            ]

        else:  # varignon
            latex = "\\text{Varignon's Theorem: What shape is formed by connecting the midpoints of the sides of any quadrilateral?}"
            solution = "A parallelogram"
            steps = [
                "\\text{Varignon's Theorem states:}",
                "\\text{The midpoints of any quadrilateral form a parallelogram}",
                "\\text{This is true regardless of the original quadrilateral's shape}",
                "\\text{The area of this parallelogram is half the area of the original quadrilateral}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = TheoremsQuadrilateralPropertiesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")


if __name__ == '__main__':
    main()
