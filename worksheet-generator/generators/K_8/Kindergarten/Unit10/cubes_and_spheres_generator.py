"""
Cubes and Spheres Generator - Kindergarten Unit 10
Generates problems about identifying 3D shapes: cubes and spheres
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CubesAndSpheresGenerator:
    """Generates cubes and spheres problems."""

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
        shape = random.choice(['cube', 'sphere'])
        example = random.choice(['box', 'dice']) if shape == 'cube' else random.choice(['ball', 'marble'])
        latex = f"\\text{{Is a {example} shaped like a cube or sphere?}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[shape], difficulty='easy')

    def _generate_medium(self) -> Equation:
        shape = random.choice(['cube', 'sphere'])
        latex = f"\\text{{What shape is a {random.choice(['box', 'dice']) if shape == 'cube' else random.choice(['ball', 'orange'])}?}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[shape], difficulty='medium')

    def _generate_hard(self) -> Equation:
        shape = random.choice(['cube', 'sphere'])
        feature = 'flat faces' if shape == 'cube' else 'round all around'
        latex = f"\\text{{A {shape} has {feature}}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[f"{shape}: {feature}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        objects = {
            'cube': ['box', 'dice', 'block'],
            'sphere': ['ball', 'orange', 'marble']
        }
        shape = random.choice(['cube', 'sphere'])
        obj = random.choice(objects[shape])
        latex = f"\\text{{Name another object shaped like a {obj}}}"
        solution = f"another {shape}"
        return Equation(latex=latex, solution=solution, steps=[f"objects like {shape}"], difficulty='challenge')


def main():
    generator = CubesAndSpheresGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
