"""
Transformations and Congruence Generator
Creates problems about using transformations to establish congruence
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class TransformationsAndCongruenceGenerator:
    """Generates problems about transformations and congruence."""

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
        """Basic congruence from single transformation"""
        problem_type = random.choice(['single_transformation', 'congruent_or_not', 'identify'])

        if problem_type == 'single_transformation':
            transformation = random.choice(['reflection', 'rotation', 'translation'])

            latex = f"\\text{{Triangle ABC is mapped to triangle DEF by a {transformation}. Are the triangles congruent?}}"
            solution = "Yes"
            steps = [
                f"\\text{{{transformation.capitalize()}s are rigid transformations}}",
                "\\text{Rigid transformations preserve distances and angles}",
                "\\text{Therefore, } \\triangle ABC \\cong \\triangle DEF"
            ]

        elif problem_type == 'congruent_or_not':
            transform = random.choice(['dilation', 'reflection'])

            if transform == 'dilation':
                k = random.choice([2, 0.5, 3])
                latex = f"\\text{{A square is dilated with scale factor }} k = {k}. \\text{{ Is the image congruent to the original?}}"
                solution = "No" if k != 1 else "Yes"
                steps = [
                    "\\text{Dilations are not rigid transformations}",
                    f"\\text{{With }} k = {k} \\neq 1, \\text{{ the size changes}}",
                    "\\text{Therefore, the figures are similar but not congruent}"
                ] if k != 1 else [
                    "\\text{With } k = 1, \\text{ the dilation is the identity}",
                    "\\text{The image is identical to the original}"
                ]
            else:
                latex = "\\text{A rectangle is reflected across a line. Is the image congruent to the original?}"
                solution = "Yes"
                steps = [
                    "\\text{Reflections are rigid transformations}",
                    "\\text{Rigid transformations preserve all distances and angles}",
                    "\\text{Therefore, the image is congruent to the original}"
                ]

        else:  # identify
            latex = "\\text{Which type of transformation always produces a congruent image: dilation, reflection, or both?}"
            solution = "Reflection only"
            steps = [
                "\\text{Reflections are rigid transformations - always congruent}",
                "\\text{Dilations with } k \\neq 1 \\text{ change size - similar but not congruent}",
                "\\text{Answer: Reflection only (unless dilation has } k = 1)"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Sequence of transformations for congruence"""
        problem_type = random.choice(['sequence', 'verify_congruence', 'coordinates'])

        if problem_type == 'sequence':
            angle = random.choice([90, 180, 270])
            dx = random.randint(3, 7)

            latex = f"\\text{{Pentagon ABCDE is rotated }} {angle}^\\circ \\text{{ about the origin, then translated }} {dx} \\text{{ units right.}}"
            latex += " \\text{Is the final image congruent to the original?}"
            solution = "Yes"
            steps = [
                "\\text{Both rotations and translations are rigid transformations}",
                "\\text{A composition of rigid transformations is rigid}",
                "\\text{Rigid transformations preserve congruence}",
                "\\text{Therefore, the final image is congruent to the original}"
            ]

        elif problem_type == 'verify_congruence':
            side1 = random.randint(5, 12)
            side2 = random.randint(5, 12)

            latex = f"\\text{{Rectangle ABCD with sides }} {side1} \\times {side2} \\text{{ is reflected across the y-axis to form A'B'C'D'. }}"
            latex += "\\text{Verify that ABCD } \\cong \\text{ A'B'C'D'.}"
            solution = f"Yes, all corresponding sides and angles are equal"
            steps = [
                "\\text{Reflection preserves all distances}",
                f"\\text{{Original sides: }} {side1} \\times {side2}",
                f"\\text{{Image sides: }} {side1} \\times {side2}",
                "\\text{All angles remain } 90^\\circ",
                "\\text{Therefore, } ABCD \\cong A'B'C'D'"
            ]

        else:  # coordinates
            x1, y1 = random.randint(1, 5), random.randint(1, 5)
            x2, y2 = random.randint(1, 5), random.randint(6, 10)
            x3, y3 = random.randint(6, 10), random.randint(1, 5)

            latex = f"\\text{{Triangle with vertices A}}({x1},{y1}), \\text{{B}}({x2},{y2}), \\text{{C}}({x3},{y3}) \\text{{ is reflected across the x-axis. }}"
            latex += "\\text{Find one side length of the image to verify congruence.}"

            import math
            ab = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            solution = f"A'B' = {ab:.2f}"
            steps = [
                f"\\text{{After reflection: A'}}({x1},{-y1}), \\text{{B'}}({x2},{-y2}), \\text{{C'}}({x3},{-y3})",
                f"A'B' = \\sqrt{{({x2}-{x1})^2 + ({-y2}-({-y1}))^2}}",
                f"A'B' = \\sqrt{{({x2-x1})^2 + ({y1-y2})^2}} = {ab:.2f}",
                "\\text{This equals AB, confirming congruence}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Finding the transformation that proves congruence"""
        problem_type = random.choice(['describe_transformation', 'multiple_steps', 'prove_congruent'])

        if problem_type == 'describe_transformation':
            x1, y1 = random.randint(2, 5), random.randint(2, 5)
            x2, y2 = -x1, y1

            latex = f"\\text{{Point A}}({x1},{y1}) \\text{{ maps to A'}}({x2},{y2}). \\text{{ Describe the transformation.}}"
            solution = "Reflection across the y-axis"
            steps = [
                f"\\text{{The x-coordinate changes sign: }} {x1} \\to {x2}",
                f"\\text{{The y-coordinate stays the same: }} {y1} \\to {y2}",
                "\\text{This is the rule for reflection across the y-axis}",
                "\\text{Answer: Reflection across the y-axis}"
            ]

        elif problem_type == 'multiple_steps':
            latex = "\\text{Triangle ABC is congruent to triangle DEF. Describe a sequence of rigid transformations that maps ABC to DEF.}"
            solution = "Multiple valid answers (translate, then rotate/reflect as needed)"
            steps = [
                "\\text{Step 1: Translate so that A maps to D}",
                "\\text{Step 2: Rotate about D so that AB aligns with DE}",
                "\\text{Step 3: If needed, reflect across DE so C maps to F}",
                "\\text{This sequence of rigid transformations proves congruence}"
            ]

        else:  # prove_congruent
            s1 = random.randint(6, 10)
            s2 = random.randint(6, 10)

            latex = f"\\text{{Two triangles both have sides }} {s1}, {s2}, {s1}. \\text{{ Prove they are congruent using transformations.}}"
            solution = "Congruent by SSS, can map one to other with rigid transformations"
            steps = [
                "\\text{Both triangles are isosceles with same dimensions}",
                "\\text{By SSS, they are congruent}",
                "\\text{Since they're congruent, there exists a sequence of rigid transformations}",
                "\\text{(translation + rotation + possible reflection) that maps one to the other}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex congruence proofs"""
        problem_type = random.choice(['minimum_transformations', 'orientation', 'general_proof'])

        if problem_type == 'minimum_transformations':
            latex = "\\text{What is the minimum number of reflections needed to map any triangle to any congruent triangle?}"
            solution = "At most 3 reflections"
            steps = [
                "\\text{Any rigid transformation is a composition of reflections}",
                "\\text{Translation = 2 reflections (across parallel lines)}",
                "\\text{Rotation = 2 reflections (across intersecting lines)}",
                "\\text{Reflection = 1 reflection}",
                "\\text{Any mapping needs at most: 2 (to align) + 1 (to orient) = 3 reflections}"
            ]

        elif problem_type == 'orientation':
            latex = "\\text{Two congruent triangles have opposite orientation. What type of transformation maps one to the other?}"
            solution = "Must include a reflection (odd number of reflections)"
            steps = [
                "\\text{Translations and rotations preserve orientation}",
                "\\text{Reflections reverse orientation}",
                "\\text{If orientations are opposite, need odd number of reflections}",
                "\\text{Simplest: 1 reflection, or 3 reflections}",
                "\\text{Answer: Transformation must include reflection}"
            ]

        else:  # general_proof
            latex = "\\text{Prove: If two figures are congruent, there exists a sequence of rigid transformations mapping one to the other.}"
            solution = "Congruence is defined by the existence of such transformations"
            steps = [
                "\\text{By definition, figures are congruent if:}",
                "\\text{- All corresponding distances are equal}",
                "\\text{- All corresponding angles are equal}",
                "\\text{Rigid transformations preserve distances and angles}",
                "\\text{Translation aligns a point, rotation aligns a direction}",
                "\\text{Reflection (if needed) corrects orientation}",
                "\\text{Therefore, such a sequence always exists}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = TransformationsAndCongruenceGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")


if __name__ == '__main__':
    main()
