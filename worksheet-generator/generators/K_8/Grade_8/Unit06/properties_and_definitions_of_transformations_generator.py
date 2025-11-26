"""
Properties and Definitions of Transformations Generator - Grade 8 Unit 6
Generates problems about properties of transformations
Example: Which transformations preserve angle measures?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PropertiesAndDefinitionsOfTransformationsGenerator:
    """Generates properties and definitions of transformations problems."""

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
        latex = "\\text{Does a translation preserve distance?}"
        solution = "\\text{Yes}"
        steps = ["\\text{Translations are rigid motions}", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        latex = "\\text{Which transformation changes the size of a figure?}"
        solution = "\\text{Dilation}"
        steps = ["\\text{Dilations scale figures}", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{A figure is rotated 90°, then reflected. Is this a rigid motion?}"
        solution = "\\text{Yes, composition of rigid motions is rigid}"
        steps = [
            "\\text{Both preserve distance}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{What transformation maps } (x, y) \\to (y, x)?"
        solution = "\\text{Reflection over } y = x"
        steps = [
            "\\text{Swapping coordinates reflects over } y = x",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = PropertiesAndDefinitionsOfTransformationsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
