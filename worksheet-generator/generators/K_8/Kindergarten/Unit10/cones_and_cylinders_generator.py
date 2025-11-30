"""
Cones and Cylinders Generator - Kindergarten Unit 10
Generates problems about identifying 3D shapes: cones and cylinders
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ConesAndCylindersGenerator:
    """Generates cones and cylinders problems."""

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
        shape = random.choice(['cone', 'cylinder'])
        example = random.choice(['ice cream cone', 'party hat']) if shape == 'cone' else random.choice(['can', 'tube'])
        latex = f"\\text{{Is a {example} shaped like a cone or cylinder?}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[shape], difficulty='easy')

    def _generate_medium(self) -> Equation:
        shape = random.choice(['cone', 'cylinder'])
        obj = random.choice(['traffic cone', 'funnel']) if shape == 'cone' else random.choice(['soup can', 'paper towel roll'])
        latex = f"\\text{{What shape is a {obj}?}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[shape], difficulty='medium')

    def _generate_hard(self) -> Equation:
        shape = random.choice(['cone', 'cylinder'])
        feature = 'pointed top' if shape == 'cone' else 'flat top and bottom'
        latex = f"\\text{{A {shape} has a {feature}}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[f"{shape}: {feature}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        shapes = {
            'cone': ['ice cream cone', 'party hat', 'traffic cone'],
            'cylinder': ['can', 'tube', 'drum']
        }
        shape = random.choice(['cone', 'cylinder'])
        latex = f"\\text{{Name an object shaped like a {shape}}}"
        solution = random.choice(shapes[shape])
        return Equation(latex=latex, solution=solution, steps=[f"examples of {shape}"], difficulty='challenge')


def main():
    generator = ConesAndCylindersGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
