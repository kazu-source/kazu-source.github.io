"""
Sorting Objects Generator - Kindergarten Unit 8
Generates problems about sorting objects by attributes
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SortingObjectsGenerator:
    """Generates sorting objects problems."""

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
        attribute = random.choice(['color', 'size', 'shape'])
        obj = random.choice(['blocks', 'toys', 'buttons'])
        latex = f"\\text{{Sort the {obj} by {attribute}}}"
        solution = f"sorted by {attribute}"
        return Equation(latex=latex, solution=solution, steps=[f"group by {attribute}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        colors = ['red', 'blue', 'green']
        color = random.choice(colors)
        obj = random.choice(['circles', 'squares', 'stars'])
        latex = f"\\text{{{{Put all the {color} {obj} in one group}}}}"
        solution = f"{color} {obj}"
        return Equation(latex=latex, solution=solution, steps=["sort by color"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        sizes = ['big', 'small']
        obj = random.choice(['balls', 'boxes', 'cars'])
        latex = f"\\text{{How many groups when you sort {obj} by size?}}"
        solution = "2"
        return Equation(latex=latex, solution=solution, steps=["big and small"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        attr1 = random.choice(['red', 'blue'])
        attr2 = random.choice(['big', 'small'])
        latex = f"\\text{{Find objects that are both {attr1} and {attr2}}}"
        solution = f"{attr1} and {attr2}"
        return Equation(latex=latex, solution=solution, steps=["two attributes"], difficulty='challenge')


def main():
    generator = SortingObjectsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
