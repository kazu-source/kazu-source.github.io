"""
Properties and Definitions of Transformations Generator
Creates problems about properties and definitions of transformations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class PropertiesDefinitionsTransformationsGenerator:
    """Generates problems about transformation properties and definitions."""

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
        """Basic transformation definitions"""
        definitions = [
            ("translation", "Slides a figure in a straight line", "A translation moves every point the same distance and direction."),
            ("rotation", "Turns a figure around a fixed point", "A rotation spins a figure around a center point."),
            ("reflection", "Flips a figure over a line", "A reflection creates a mirror image across a line."),
            ("dilation", "Enlarges or reduces a figure proportionally", "A dilation changes size but preserves shape."),
            ("rigid transformation", "Preserves distance and angle measures", "Translations, rotations, and reflections are rigid transformations."),
            ("isometry", "Preserves distance between points", "An isometry maintains all distances; it's another name for rigid transformation."),
            ("similarity transformation", "Preserves angle measures and produces proportional sides", "Dilations and compositions with rigid transformations produce similar figures."),
            ("center of rotation", "The fixed point around which a figure rotates", "The center of rotation does not move during the rotation."),
            ("line of reflection", "The line over which a figure is reflected", "Points on the line of reflection do not move."),
            ("center of dilation", "The fixed point from which a dilation occurs", "The center of dilation remains fixed; other points move toward or away from it.")
        ]

        term, definition, explanation = random.choice(definitions)

        latex = f"\\text{{Define: {term}}}"
        solution = definition

        steps = [
            f"\\text{{{explanation}}}",
            f"\\text{{Answer: {definition}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Identify which properties are preserved"""
        problem_type = random.choice(['preservation', 'classification', 'comparison'])

        if problem_type == 'preservation':
            transformations = [
                ("translation", "distance, angle measures, parallelism, orientation", "Translations preserve all properties including orientation."),
                ("rotation", "distance, angle measures, parallelism, orientation", "Rotations preserve all properties including orientation."),
                ("reflection", "distance, angle measures, parallelism", "Reflections preserve these but REVERSE orientation."),
                ("dilation", "angle measures, parallelism, orientation", "Dilations preserve angles and parallelism but NOT distance.")
            ]

            transform, preserved, explanation = random.choice(transformations)

            latex = f"\\text{{What properties are preserved by a {transform}?}}"
            solution = preserved

            steps = [
                f"\\text{{{explanation}}}",
                f"\\text{{Preserved: {preserved}}}"
            ]

        elif problem_type == 'classification':
            classifications = [
                ("Translation, rotation, reflection", "Rigid transformations (isometries)", "These all preserve distance and angle measures."),
                ("Translation, rotation", "Rigid transformations that preserve orientation", "These maintain the clockwise/counterclockwise order."),
                ("Reflection", "Rigid transformation that reverses orientation", "A reflection flips the figure, reversing orientation."),
                ("Dilation", "Similarity transformation", "Dilations preserve shape but not necessarily size."),
                ("Composition of rigid transformation and dilation", "Similarity transformation", "This creates a similar figure.")
            ]

            transforms, classification, explanation = random.choice(classifications)

            latex = f"\\text{{How are these transformations classified: {transforms}?}}"
            solution = classification

            steps = [
                f"\\text{{{explanation}}}",
                f"\\text{{Classification: {classification}}}"
            ]

        else:  # comparison
            comparisons = [
                ("rigid transformation", "dilation", "Rigid transformations preserve distance; dilations do not", "Distance"),
                ("translation", "reflection", "Translation preserves orientation; reflection reverses it", "Orientation"),
                ("rotation", "translation", "Rotation has a fixed center; translation has no fixed points", "Fixed points"),
                ("reflection", "rotation", "Reflection reverses orientation; rotation preserves it", "Orientation")
            ]

            trans1, trans2, difference, key = random.choice(comparisons)

            latex = f"\\text{{What key property distinguishes a {trans1} from a {trans2}?}}"
            solution = key

            steps = [
                f"\\text{{{difference}}}",
                f"\\text{{Key difference: {key}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Apply definitions to determine transformation types"""
        problem_type = random.choice(['identify', 'verify', 'counterexample'])

        if problem_type == 'identify':
            scenarios = [
                ("A figure is moved so that point A(2,3) maps to A'(5,7), and point B(4,5) maps to B'(7,9).",
                 "Translation", "The x-coordinates increase by 3 and y-coordinates increase by 4 for both points."),
                ("A figure is transformed so all points maintain the same distance from point C, and angles are preserved.",
                 "Rotation about point C", "Points staying equidistant from a fixed point indicates rotation."),
                ("A figure is transformed so that A(2,3) maps to A'(2,-3) and B(5,1) maps to B'(5,-1).",
                 "Reflection over the x-axis", "The x-coordinates stay the same while y-coordinates are negated."),
                ("A figure is transformed so that A(2,4) maps to A'(4,8) and B(3,6) maps to B'(6,12).",
                 "Dilation from origin with k=2", "All coordinates are multiplied by 2.")
            ]

            scenario, answer, explanation = random.choice(scenarios)

            latex = f"\\text{{{scenario} What transformation occurred?}}"
            solution = answer

            steps = [
                f"\\text{{{explanation}}}",
                f"\\text{{Answer: {answer}}}"
            ]

        elif problem_type == 'verify':
            verifications = [
                ("A transformation maps (1,2) to (4,5) and (3,4) to (6,7). Is this a rigid transformation?",
                 "Yes", "Distance between points: before = √8, after = √8. Distance is preserved."),
                ("A transformation maps (2,2) to (4,4) and (4,2) to (8,4). Is this a rigid transformation?",
                 "No", "Distance between points: before = 2, after = 4. Distance is not preserved."),
                ("A transformation preserves all distances but reverses orientation. Is it a rotation?",
                 "No", "It must be a reflection. Rotations preserve orientation.")
            ]

            question, answer, explanation = random.choice(verifications)

            latex = f"\\text{{{question}}}"
            solution = answer

            steps = [
                f"\\text{{{explanation}}}",
                f"\\text{{Answer: {answer}}}"
            ]

        else:  # counterexample
            latex = f"\\text{{Give a counterexample showing that dilations are not rigid transformations.}}"
            solution = "A dilation with k≠1 changes distances between points."

            steps = [
                f"\\text{{Consider a dilation with }} k = 2 \\text{{ from the origin}}",
                f"\\text{{Point }} (1,0) \\text{{ maps to }} (2,0)",
                f"\\text{{Point }} (2,0) \\text{{ maps to }} (4,0)",
                f"\\text{{Original distance: }} 2 - 1 = 1",
                f"\\text{{New distance: }} 4 - 2 = 2",
                f"\\text{{Distance is not preserved, so it's not a rigid transformation}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex problems involving composition and properties"""
        problem_type = random.choice(['composition', 'proof', 'analysis'])

        if problem_type == 'composition':
            latex = f"\\text{{A figure undergoes a reflection followed by a translation. What properties are preserved?}}"
            solution = "Distance, angle measures, and parallelism (but orientation depends on the reflection)"

            steps = [
                f"\\text{{Reflection preserves: distance, angles, parallelism (reverses orientation)}}",
                f"\\text{{Translation preserves: distance, angles, parallelism, orientation}}",
                f"\\text{{Composition preserves: distance, angles, parallelism}}",
                f"\\text{{Orientation: reversed by the reflection, not restored by translation}}"
            ]

        elif problem_type == 'proof':
            latex = f"\\text{{Prove that the composition of two reflections over parallel lines is a translation.}}"
            solution = "The composition produces a translation perpendicular to the lines with distance twice the distance between lines."

            steps = [
                f"\\text{{Let lines be }} l_1 \\text{{ and }} l_2 \\text{{, distance }} d \\text{{ apart}}",
                f"\\text{{First reflection over }} l_1 \\text{{ moves point }} P \\text{{ perpendicular to }} l_1",
                f"\\text{{Second reflection over }} l_2 \\text{{ moves point further in same direction}}",
                f"\\text{{Net effect: translation perpendicular to lines, distance }} 2d",
                f"\\text{{Orientation: reversed twice, so preserved}}"
            ]

        else:  # analysis
            latex = f"\\text{{Can a single transformation map a figure to its image if the image has reversed orientation and different size?}}"
            solution = "No, a single transformation cannot both reverse orientation and change size."

            steps = [
                f"\\text{{Transformations that change size: dilations}}",
                f"\\text{{But dilations preserve orientation}}",
                f"\\text{{Transformations that reverse orientation: reflections}}",
                f"\\text{{But reflections preserve distance (don't change size)}}",
                f"\\text{{A composition (reflection + dilation) would be needed}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = PropertiesDefinitionsTransformationsGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
