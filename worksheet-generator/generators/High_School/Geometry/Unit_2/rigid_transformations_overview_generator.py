"""
Rigid Transformations Overview Generator
Creates problems reviewing all rigid transformation types
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class RigidTransformationsOverviewGenerator:
    """Generates problems about rigid transformations overview."""

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
        """Identify transformation type"""
        transformations = [
            ("translation", "slides", "All points move the same distance in the same direction"),
            ("rotation", "turns", "All points move around a fixed center point"),
            ("reflection", "flips", "All points are mirrored across a line"),
        ]

        name, action, description = random.choice(transformations)

        problem_type = random.choice(['identify', 'describe'])

        if problem_type == 'identify':
            latex = f"\\text{{A transformation that {action} a figure is called a:}}"
            solution = f"\\text{{{name}}}"
            steps = [
                f"\\text{{A {name} {action} a figure.}}",
                f"\\text{{{description}}}"
            ]
        else:
            latex = f"\\text{{Describe what a {name} does to a figure.}}"
            solution = f"\\text{{{description}}}"
            steps = [
                f"\\text{{A {name} {action} the figure.}}",
                f"\\text{{{description}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Identify transformation from coordinates"""
        x, y = random.randint(1, 5), random.randint(1, 5)

        transform_type = random.choice(['translation', 'reflection_x', 'reflection_y', 'rotation_180'])

        if transform_type == 'translation':
            dx, dy = random.randint(2, 5), random.randint(2, 5)
            x2, y2 = x + dx, y + dy
            answer = "translation"
            explanation = f"\\text{{The point moved {dx} right and {dy} up}}"
        elif transform_type == 'reflection_x':
            x2, y2 = x, -y
            answer = "reflection over x-axis"
            explanation = f"\\text{{The y-coordinate changed sign: }} (x, y) \\to (x, -y)"
        elif transform_type == 'reflection_y':
            x2, y2 = -x, y
            answer = "reflection over y-axis"
            explanation = f"\\text{{The x-coordinate changed sign: }} (x, y) \\to (-x, y)"
        else:
            x2, y2 = -x, -y
            answer = "180° rotation about origin"
            explanation = f"\\text{{Both coordinates changed sign: }} (x, y) \\to (-x, -y)"

        latex = f"\\text{{Point }} A({x}, {y}) \\text{{ maps to }} A'({x2}, {y2}). \\text{{ Identify the transformation.}}"
        solution = f"\\text{{{answer}}}"

        steps = [
            f"\\text{{Original: }} ({x}, {y})",
            f"\\text{{Image: }} ({x2}, {y2})",
            explanation
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Properties preserved by rigid transformations"""
        properties = [
            ("distance", True, "Rigid transformations preserve distance between points"),
            ("angle measure", True, "Rigid transformations preserve angle measures"),
            ("orientation", False, "Reflections reverse orientation; rotations and translations preserve it"),
            ("area", True, "Rigid transformations preserve area"),
            ("perimeter", True, "Rigid transformations preserve perimeter"),
        ]

        prop, all_preserve, explanation = random.choice(properties)

        if prop == "orientation":
            latex = f"\\text{{Which rigid transformation(s) reverse orientation?}}"
            solution = f"\\text{{Reflection}}"
            steps = [
                f"\\text{{Translations preserve orientation}}",
                f"\\text{{Rotations preserve orientation}}",
                f"\\text{{Reflections reverse orientation}}"
            ]
        else:
            transform = random.choice(['translations', 'rotations', 'reflections', 'all rigid transformations'])
            latex = f"\\text{{Do {transform} preserve {prop}?}}"
            solution = f"\\text{{Yes}}"
            steps = [
                f"\\text{{{explanation}}}",
                f"\\text{{Yes, {transform} preserve {prop}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Composition of transformations"""
        x, y = random.randint(1, 4), random.randint(1, 4)

        problem_type = random.choice(['double_reflection', 'translate_rotate'])

        if problem_type == 'double_reflection':
            # Reflection over x-axis then y-axis = 180° rotation
            x1, y1 = x, -y  # After x-axis reflection
            x2, y2 = -x1, y1  # After y-axis reflection

            latex = f"\\text{{Point }} P({x}, {y}) \\text{{ is reflected over the x-axis, then the y-axis. Find }} P''."
            solution = f"P'' = ({x2}, {y2})"

            steps = [
                f"\\text{{Original: }} P({x}, {y})",
                f"\\text{{After x-axis reflection: }} P'({x1}, {y1})",
                f"\\text{{After y-axis reflection: }} P''({x2}, {y2})",
                f"\\text{{Note: Two perpendicular reflections = 180° rotation}}"
            ]
        else:
            # Translation then 90° rotation
            dx, dy = random.randint(2, 4), random.randint(2, 4)
            x1, y1 = x + dx, y + dy  # After translation
            x2, y2 = -y1, x1  # After 90° rotation about origin

            latex = f"\\text{{Point }} P({x}, {y}) \\text{{ is translated }} {dx} \\text{{ right and }} {dy} \\text{{ up, then rotated 90° counterclockwise about origin.}}"
            solution = f"P'' = ({x2}, {y2})"

            steps = [
                f"\\text{{Original: }} P({x}, {y})",
                f"\\text{{After translation: }} P'({x1}, {y1})",
                f"\\text{{90° CCW rotation: }} (x, y) \\to (-y, x)",
                f"P'' = ({x2}, {y2})"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = RigidTransformationsOverviewGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
