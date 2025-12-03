"""
Rigid Transformations Introduction Generator
Creates problems about identifying and understanding rigid transformations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class RigidTransformationsIntroGenerator:
    """Generates problems about rigid transformations concepts."""

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
        """Identify the type of transformation from description"""
        transformations = [
            ("slides a figure without rotating or flipping it", "Translation",
             "A translation moves every point the same distance in the same direction."),
            ("turns a figure around a fixed point", "Rotation",
             "A rotation turns a figure around a center point by a specific angle."),
            ("flips a figure over a line", "Reflection",
             "A reflection creates a mirror image of a figure across a line."),
            ("moves every point of a figure the same distance in the same direction", "Translation",
             "This describes a translation - a slide transformation."),
            ("creates a mirror image of a figure", "Reflection",
             "A mirror image is created by a reflection."),
            ("turns a figure 90 degrees around a point", "Rotation",
             "Turning around a point is a rotation.")
        ]

        desc, answer, explanation = random.choice(transformations)

        latex = f"\\text{{Which transformation }} {desc}\\text{{?}}"
        solution = answer

        steps = [
            f"\\text{{{explanation}}}",
            f"\\text{{Answer: {answer}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Identify transformation from coordinate rule"""
        rules = [
            ("(x, y) \\to (x + 3, y - 2)", "Translation",
             "Adding to coordinates indicates a translation (slide)."),
            ("(x, y) \\to (-x, y)", "Reflection over y-axis",
             "Negating x reflects over the y-axis."),
            ("(x, y) \\to (x, -y)", "Reflection over x-axis",
             "Negating y reflects over the x-axis."),
            ("(x, y) \\to (-y, x)", "90° counterclockwise rotation",
             "This rule represents a 90° CCW rotation about the origin."),
            ("(x, y) \\to (y, x)", "Reflection over y = x",
             "Swapping x and y reflects over the line y = x."),
            ("(x, y) \\to (-x, -y)", "180° rotation",
             "Negating both coordinates is a 180° rotation about the origin.")
        ]

        rule, answer, explanation = random.choice(rules)

        latex = f"\\text{{Identify the transformation: }} {rule}"
        solution = answer

        steps = [
            f"\\text{{Analyze how x and y change:}}",
            f"\\text{{{explanation}}}",
            f"\\text{{Answer: {answer}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Determine if a transformation is rigid and identify properties preserved"""
        problem_type = random.choice(['is_rigid', 'properties'])

        if problem_type == 'is_rigid':
            transformations = [
                ("Translation by vector (3, -4)", "Yes",
                 "Translations preserve distance and angle measures."),
                ("Rotation of 90° about the origin", "Yes",
                 "Rotations preserve distance and angle measures."),
                ("Reflection over the x-axis", "Yes",
                 "Reflections preserve distance and angle measures."),
                ("Dilation with scale factor 2", "No",
                 "Dilations change distances (not rigid), though they preserve angles."),
                ("Dilation with scale factor 0.5", "No",
                 "Dilations change the size of figures, so they are not rigid."),
                ("Rotation followed by translation", "Yes",
                 "A composition of rigid transformations is also rigid.")
            ]

            trans, answer, explanation = random.choice(transformations)

            latex = f"\\text{{Is the following transformation rigid? }} {trans}"
            solution = answer

            steps = [
                f"\\text{{A rigid transformation preserves distance and angle measures.}}",
                f"\\text{{{explanation}}}",
                f"\\text{{Answer: {answer}}}"
            ]
        else:
            properties = [
                ("distance between points", "Yes", "All rigid transformations preserve distance."),
                ("angle measures", "Yes", "All rigid transformations preserve angle measures."),
                ("orientation", "Reflections: No; Rotations/Translations: Yes",
                 "Reflections reverse orientation, but rotations and translations preserve it."),
                ("parallel lines", "Yes", "Rigid transformations map parallel lines to parallel lines."),
                ("area of figures", "Yes", "Since distances are preserved, areas are also preserved.")
            ]

            prop, answer, explanation = random.choice(properties)

            latex = f"\\text{{Do rigid transformations preserve }} {prop}\\text{{?}}"
            solution = answer

            steps = [
                f"\\text{{{explanation}}}",
                f"\\text{{Answer: {answer}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Identify a sequence of transformations or analyze composite transformations"""
        problem_type = random.choice(['sequence', 'equivalent'])

        if problem_type == 'sequence':
            # Given pre-image and image, describe possible transformation(s)
            scenarios = [
                (
                    "A(1, 2), B(3, 2), C(2, 4)",
                    "A'(-1, 2), B'(-3, 2), C'(-2, 4)",
                    "Reflection over the y-axis",
                    "Each x-coordinate is negated while y stays the same: (x,y) → (-x,y)"
                ),
                (
                    "A(1, 1), B(3, 1), C(2, 3)",
                    "A'(4, 3), B'(6, 3), C'(5, 5)",
                    "Translation by vector ⟨3, 2⟩",
                    "Each point moves right 3 and up 2."
                ),
                (
                    "A(2, 0), B(4, 0), C(3, 2)",
                    "A'(0, 2), B'(0, 4), C'(-2, 3)",
                    "90° counterclockwise rotation about origin",
                    "Each point follows (x,y) → (-y, x)."
                )
            ]

            pre, post, answer, explanation = random.choice(scenarios)

            latex = f"\\text{{Triangle with vertices }} {pre} \\text{{ is mapped to }} {post}. \\text{{ Identify the transformation.}}"
            solution = answer

            steps = [
                f"\\text{{Compare corresponding vertices:}}",
                f"\\text{{{explanation}}}",
                f"\\text{{Transformation: {answer}}}"
            ]
        else:
            # Determine equivalent single transformation
            compositions = [
                (
                    "reflection over the x-axis followed by reflection over the y-axis",
                    "180° rotation about the origin",
                    "Two perpendicular reflections equal a 180° rotation."
                ),
                (
                    "translation by ⟨2, 3⟩ followed by translation by ⟨-1, 4⟩",
                    "Translation by ⟨1, 7⟩",
                    "Add the vectors: ⟨2+(-1), 3+4⟩ = ⟨1, 7⟩"
                ),
                (
                    "90° rotation followed by another 90° rotation (both CCW about origin)",
                    "180° rotation about the origin",
                    "90° + 90° = 180° rotation."
                ),
                (
                    "reflection over y = x followed by reflection over the x-axis",
                    "90° clockwise rotation about the origin",
                    "These two reflections compose to give a rotation."
                )
            ]

            comp, answer, explanation = random.choice(compositions)

            latex = f"\\text{{What single transformation is equivalent to: }} {comp}\\text{{?}}"
            solution = answer

            steps = [
                f"\\text{{Analyze the composition:}}",
                f"\\text{{{explanation}}}",
                f"\\text{{Equivalent: {answer}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = RigidTransformationsIntroGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
