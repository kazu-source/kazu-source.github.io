"""
Circles and Squares Generator - Kindergarten Unit 10
Generates problems about identifying and working with circles and squares
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CirclesAndSquaresGenerator:
    """Generates circles and squares problems."""

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
        shape = random.choice(['circle', 'square'])
        latex = f"\\text{{What shape is this? (shows a {shape})}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[shape], difficulty='easy')

    def _generate_medium(self) -> Equation:
        shape = random.choice(['circle', 'square'])
        features = {
            'circle': 'round',
            'square': '4 equal sides'
        }
        latex = f"\\text{{A {shape} is {features[shape]}}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[f"{shape}: {features[shape]}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num_circles = random.randint(2, 5)
        num_squares = random.randint(2, 5)
        latex = f"\\text{{Count: {num_circles} circles and {num_squares} squares. How many shapes total?}}"
        total = num_circles + num_squares
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{num_circles} + {num_squares} = {total}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        shape = random.choice(['circle', 'square'])
        latex = f"\\text{{Draw a {shape}}}"
        solution = f"draw {shape}"
        return Equation(latex=latex, solution=solution, steps=["student draws shape"], difficulty='challenge')


def main():
    generator = CirclesAndSquaresGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
