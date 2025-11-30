"""
Ordering Numbers Generator - Grade 1 Unit06
Generates ordering numbers problems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class OrderingNumbersGenerator:
    """Generates ordering numbers problems."""

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
        nums = random.sample(range(1, 30), 3)
        latex = f"\\text{{Order these: {', '.join(map(str, nums))}}}"
        solution = ', '.join(map(str, sorted(nums)))
        return Equation(latex=latex, solution=solution, steps=["ascending order"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        nums = random.sample(range(10, 70), 4)
        latex = f"\\text{{Put in order from smallest to largest: {', '.join(map(str, nums))}}}"
        solution = ', '.join(map(str, sorted(nums)))
        return Equation(latex=latex, solution=solution, steps=["smallest to largest"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        nums = random.sample(range(30, 99), 4)
        latex = f"\\text{{Order from greatest to least: {', '.join(map(str, nums))}}}"
        solution = ', '.join(map(str, sorted(nums, reverse=True)))
        return Equation(latex=latex, solution=solution, steps=["greatest to least"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        nums = random.sample(range(20, 99), 5)
        sorted_nums = sorted(nums)
        missing_idx = random.randint(1, 3)
        nums_with_blank = [str(n) if i != missing_idx else '___' for i, n in enumerate(sorted_nums)]
        latex = f"\\text{{Fill in: {', '.join(nums_with_blank)}}}"
        solution = str(sorted_nums[missing_idx])
        return Equation(latex=latex, solution=solution, steps=["find missing number"], difficulty='challenge')


def main():
    generator = OrderingNumbersGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
