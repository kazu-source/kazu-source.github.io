"""
Triangles and Rectangles Generator - Kindergarten Unit 10
Generates problems about identifying and working with triangles and rectangles
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class TrianglesAndRectanglesGenerator:
    """Generates triangles and rectangles problems."""

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
        shape = random.choice(['triangle', 'rectangle'])
        latex = f"\\text{{Is this a triangle or rectangle? (shows {shape})}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[shape], difficulty='easy')

    def _generate_medium(self) -> Equation:
        shape = random.choice(['triangle', 'rectangle'])
        features = {
            'triangle': '3 sides',
            'rectangle': '4 sides with opposite sides equal'
        }
        latex = f"\\text{{How many sides does a {shape} have?}}"
        solution = "3" if shape == 'triangle' else "4"
        return Equation(latex=latex, solution=solution, steps=[features[shape]], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num_tri = random.randint(2, 4)
        num_rect = random.randint(2, 4)
        total = num_tri + num_rect
        latex = f"\\text{{{num_tri} triangles and {num_rect} rectangles make how many shapes?}}"
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{num_tri} + {num_rect} = {total}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        shapes = ['triangle', 'rectangle']
        shape = random.choice(shapes)
        latex = f"\\text{{Find all the {shape}s in the picture}}"
        solution = f"count {shape}s"
        return Equation(latex=latex, solution=solution, steps=["identify and count"], difficulty='challenge')


def main():
    generator = TrianglesAndRectanglesGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
