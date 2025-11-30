"""
Ordering Objects Generator - Kindergarten Unit 8
Generates problems about ordering objects by size or other attributes
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class OrderingObjectsGenerator:
    """Generates ordering objects problems."""

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
        obj = random.choice(['balls', 'boxes', 'cars'])
        latex = f"\\text{{{{Put 3 {obj} in order from smallest to biggest}}}}"
        solution = "smallest, medium, biggest"
        return Equation(latex=latex, solution=solution, steps=["order by size"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        obj = random.choice(['sticks', 'pencils', 'ribbons'])
        latex = f"\\text{{{{Order these {obj} from shortest to longest}}}}"
        solution = "shortest to longest"
        return Equation(latex=latex, solution=solution, steps=["order by length"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        nums = random.sample(range(1, 10), 3)
        nums_str = ', '.join(map(str, nums))
        sorted_nums = ', '.join(map(str, sorted(nums)))
        latex = f"\\text{{{{Put these numbers in order: {nums_str}}}}}"
        solution = sorted_nums
        return Equation(latex=latex, solution=solution, steps=["order numbers"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        obj = random.choice(['towers', 'stacks', 'lines'])
        latex = f"\\text{{{{Make 3 {obj} and put them in order from tallest to shortest}}}}"
        solution = "tallest, middle, shortest"
        return Equation(latex=latex, solution=solution, steps=["order by height"], difficulty='challenge')


def main():
    generator = OrderingObjectsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
