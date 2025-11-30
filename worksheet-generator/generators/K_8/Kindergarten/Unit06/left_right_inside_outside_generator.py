"""
Left Right Inside Outside Generator - Kindergarten Unit 6
Generates problems about directional and positional words
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class LeftRightInsideOutsideGenerator:
    """Generates left, right, inside, outside problems."""

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
        direction = random.choice(['left', 'right'])
        obj = random.choice(['ball', 'car', 'toy', 'book'])
        latex = f"\\text{{The {obj} is on the {direction}}}"
        solution = direction
        return Equation(latex=latex, solution=solution, steps=[f"on the {direction}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        position = random.choice(['inside', 'outside'])
        obj1 = random.choice(['cat', 'toy', 'ball'])
        obj2 = random.choice(['box', 'house', 'circle'])
        latex = f"\\text{{The {obj1} is {position} the {obj2}}}"
        solution = position
        return Equation(latex=latex, solution=solution, steps=[f"{position} the {obj2}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        direction = random.choice(['left', 'right'])
        position = random.choice(['inside', 'outside'])
        latex = f"\\text{{Draw a star on the {direction} and {position} the circle}}"
        solution = f"{direction}, {position}"
        return Equation(latex=latex, solution=solution, steps=["two positions"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        obj = random.choice(['circle', 'square', 'triangle'])
        container = random.choice(['box', 'rectangle', 'circle'])
        side = random.choice(['left side', 'right side'])
        latex = f"\\text{{Draw a {obj} inside the {container} on the {side}}}"
        solution = f"inside, {side}"
        return Equation(latex=latex, solution=solution, steps=["combined positions"], difficulty='challenge')


def main():
    generator = LeftRightInsideOutsideGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
