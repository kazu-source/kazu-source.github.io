"""
Counting Up to 10 Generator - Kindergarten Unit 1
Generates counting problems with quantities up to 10
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CountingUpTo10Generator:
    """Generates counting up to 10 problems."""

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
        num = random.randint(1, 10)
        latex = f"\\text{{Count: }} {'● ' * num}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num = random.randint(6, 10)
        latex = f"\\text{{How many?}} \\\\ {'○ ' * num}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num = random.randint(1, 10)
        item = random.choice(['pencils', 'crayons', 'erasers', 'toys'])
        latex = f"\\text{{There are {num} {item}. Write the number.}}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        num1 = random.randint(1, 8)
        num2 = random.randint(1, 10 - num1)
        total = num1 + num2
        latex = f"{num1} \\text{{ and }} {num2} \\text{{ make how many?}}"
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{num1} + {num2} = {total}"], difficulty='challenge')


def main():
    generator = CountingUpTo10Generator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
