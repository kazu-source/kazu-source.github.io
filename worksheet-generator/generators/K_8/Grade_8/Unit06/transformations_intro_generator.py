"""
Transformations Intro Generator - Grade 8 Unit 6
Generates introductory transformation problems
Example: Identify the transformation: translation, rotation, reflection, or dilation?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class TransformationsIntroGenerator:
    """Generates transformations intro problems."""

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
        transformations = ['translation', 'rotation', 'reflection', 'dilation']
        transformation = random.choice(transformations)

        descriptions = {
            'translation': "A figure slides 5 units right.",
            'rotation': "A figure turns 90° around a point.",
            'reflection': "A figure flips over a line.",
            'dilation': "A figure enlarges by scale factor 2."
        }

        latex = f"\\text{{Identify the transformation: {descriptions[transformation]}}}"
        solution = f"\\text{{{transformation.capitalize()}}}"
        steps = [solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        latex = "\\text{Which transformation preserves distance and angle measures?}"
        solution = "\\text{Translation, Rotation, and Reflection (rigid motions)}"
        steps = ["\\text{Dilation changes size}", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{A point } (3, 4) \\text{ is translated } (x, y) \\to (x + 2, y - 1). \\text{ Find new point.}"
        solution = "(5, 3)"
        steps = [
            "(3 + 2, 4 - 1)",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Which transformations are isometries (preserve distance)?}"
        solution = "\\text{Translations, Rotations, Reflections}"
        steps = [
            "\\text{Isometries preserve distance}",
            "\\text{Dilations do not}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = TransformationsIntroGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
