"""
Proofs with Transformations Generator
Creates problems about proving geometric properties using transformations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ProofsWithTransformationsGenerator:
    """Generates problems about proofs using transformations."""

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
        """Basic transformation proof concepts"""
        problem_type = random.choice(['reflection_property', 'rotation_property', 'translation_property'])

        if problem_type == 'reflection_property':
            latex = "\\text{Prove that a reflection preserves distances. If } AB = 5 \\text{, what is } A'B' \\text{ after reflection?}"
            solution = "5"
            steps = [
                "\\text{Reflections are rigid transformations}",
                "\\text{Rigid transformations preserve distances}",
                "\\text{Therefore, } A'B' = AB = 5"
            ]

        elif problem_type == 'rotation_property':
            angle = random.choice([30, 45, 60, 90])
            latex = f"\\text{{After rotating }} \\angle ABC \\text{{ by }} {angle}^\\circ, \\text{{ what is the measure of }} \\angle A'B'C' \\text{{ if }} \\angle ABC = 72^\\circ?"
            solution = "72°"
            steps = [
                "\\text{Rotations preserve angle measures}",
                f"\\text{{The rotation amount ({angle}°) does not affect the angle measure}}",
                "\\text{Therefore, } \\angle A'B'C' = 72^\\circ"
            ]

        else:  # translation_property
            vec_x = random.randint(3, 8)
            vec_y = random.randint(2, 7)
            latex = f"\\text{{Triangle ABC is translated by vector }} \\langle {vec_x}, {vec_y} \\rangle. \\text{{ Is }} \\triangle A'B'C' \\cong \\triangle ABC? \\text{{ Why?}}"
            solution = "Yes, translations preserve size and shape"
            steps = [
                "\\text{Translations are rigid transformations}",
                "\\text{Rigid transformations preserve distances and angles}",
                "\\text{Therefore, } \\triangle A'B'C' \\cong \\triangle ABC"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Apply transformations to prove congruence"""
        problem_type = random.choice(['prove_congruent', 'sequence_proof', 'isosceles'])

        if problem_type == 'prove_congruent':
            x1, y1 = random.randint(1, 4), random.randint(1, 4)
            x2, y2 = random.randint(6, 9), random.randint(1, 4)

            latex = f"\\text{{Points A}}({x1}, {y1}) \\text{{ and B}}({x2}, {y2}) \\text{{ are reflected across the x-axis to A' and B'. }}"
            latex += "\\text{Prove } AB = A'B'."
            solution = "Equal by reflection property"
            steps = [
                f"\\text{{A' = }}({x1}, {-y1}), \\text{{ B' = }}({x2}, {-y2})",
                "\\text{Reflections preserve distances}",
                "\\text{Therefore, } AB = A'B'"
            ]

        elif problem_type == 'sequence_proof':
            angle = random.choice([90, 180])
            dx = random.randint(3, 6)

            latex = f"\\text{{A segment is rotated }} {angle}^\\circ \\text{{ about the origin, then translated }} {dx} \\text{{ units right. }}"
            latex += "\\text{Does the length change?}"
            solution = "No"
            steps = [
                "\\text{Both rotations and translations are rigid transformations}",
                "\\text{Rigid transformations preserve distances}",
                "\\text{The composition preserves length}",
                "\\text{Therefore, the length does not change}"
            ]

        else:  # isosceles
            base = random.randint(6, 12)
            latex = f"\\text{{An isosceles triangle has a line of symmetry through its vertex angle. }}"
            latex += f"\\text{{If the base is }} {base}, \\text{{ prove the two legs are equal.}}"
            solution = "Legs are equal by reflection symmetry"
            steps = [
                "\\text{Reflect the triangle across the line of symmetry}",
                "\\text{The triangle maps to itself}",
                "\\text{Each leg maps to the other leg}",
                "\\text{Reflections preserve length, so the legs are equal}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Multi-step transformation proofs"""
        problem_type = random.choice(['parallelogram', 'perpendicular_bisector', 'composition'])

        if problem_type == 'parallelogram':
            latex = "\\text{Given parallelogram ABCD, prove that opposite sides are congruent using transformations.}"
            solution = "180° rotation about center maps AB to CD and BC to AD"
            steps = [
                "\\text{Let O be the intersection of the diagonals}",
                "\\text{Rotate the parallelogram 180° about O}",
                "\\text{Point A maps to C, B maps to D}",
                "\\text{Therefore AB maps to CD}",
                "\\text{Rotations preserve distance, so } AB \\cong CD",
                "\\text{Similarly, } BC \\cong AD"
            ]

        elif problem_type == 'perpendicular_bisector':
            latex = "\\text{Prove that any point on the perpendicular bisector of } \\overline{AB} \\text{ is equidistant from A and B.}"
            solution = "Reflection maps A to B, fixing points on the bisector"
            steps = [
                "\\text{Let P be a point on the perpendicular bisector of } \\overline{AB}",
                "\\text{Reflect across the perpendicular bisector}",
                "\\text{A maps to B (by definition of perpendicular bisector)}",
                "\\text{P maps to itself (it's on the line of reflection)}",
                "\\text{Reflections preserve distance, so } PA = PB"
            ]

        else:  # composition
            latex = "\\text{A triangle is reflected across line } l, \\text{ then reflected across line } m \\parallel l. \\text{ What single transformation is equivalent?}"
            solution = "Translation perpendicular to the lines"
            steps = [
                "\\text{Let d be the distance between lines } l \\text{ and } m",
                "\\text{First reflection moves points distance } 2d_1 \\text{ perpendicular to } l",
                "\\text{Second reflection moves points distance } 2d_2 \\text{ perpendicular to } m",
                "\\text{Combined: translation by } 2d \\text{ perpendicular to both lines}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex proofs involving multiple concepts"""
        problem_type = random.choice(['angle_bisector', 'rhombus', 'glide_reflection'])

        if problem_type == 'angle_bisector':
            latex = "\\text{Prove that the angle bisector of an angle is the set of all points equidistant from the two sides.}"
            solution = "Reflection across angle bisector swaps the sides"
            steps = [
                "\\text{Let P be on the angle bisector of } \\angle BAC",
                "\\text{Reflect across the angle bisector}",
                "\\text{Ray AB maps to ray AC}",
                "\\text{P maps to itself (on the line of reflection)}",
                "\\text{The perpendicular from P to AB maps to perpendicular to AC}",
                "\\text{Reflections preserve distance}",
                "\\text{Therefore, P is equidistant from AB and AC}"
            ]

        elif problem_type == 'rhombus':
            latex = "\\text{Prove that the diagonals of a rhombus are perpendicular using transformations.}"
            solution = "Reflection symmetry implies perpendicular diagonals"
            steps = [
                "\\text{A rhombus has all sides congruent}",
                "\\text{It has a line of symmetry through opposite vertices}",
                "\\text{This line of symmetry is one diagonal}",
                "\\text{Reflection swaps the other two vertices}",
                "\\text{The line connecting them (other diagonal) must be perpendicular}",
                "\\text{(A line and its perpendicular bisector are perpendicular)}"
            ]

        else:  # glide_reflection
            d = random.randint(4, 8)
            latex = f"\\text{{A figure is reflected across the x-axis, then translated }} {d} \\text{{ units right. }}"
            latex += "\\text{This composition is called a glide reflection. Prove that reversing the order gives the same result.}"
            solution = "Both orders produce the same glide reflection"
            steps = [
                "\\text{Method 1: Reflect, then translate}",
                f"\\text{{Point }} (x, y) \\to (x, -y) \\to (x + {d}, -y)",
                "\\text{Method 2: Translate, then reflect}",
                f"\\text{{Point }} (x, y) \\to (x + {d}, y) \\to (x + {d}, -y)",
                "\\text{Both methods give the same final position}",
                "\\text{Therefore, the operations commute for this glide reflection}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ProofsWithTransformationsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")


if __name__ == '__main__':
    main()
