"""
Counting and Numbers Generator - Grade 1 Unit 1
Generates counting and number recognition problems up to 120
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CountingAndNumbersGenerator:
    """Generates counting and numbers problems."""

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
        num = random.randint(1, 30)
        latex = f"\\text{{Write the number: }} {num}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[str(num)], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num = random.randint(20, 70)
        latex = f"\\text{{What number comes after }} {num}?"
        solution = str(num + 1)
        return Equation(latex=latex, solution=solution, steps=[str(num + 1)], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num = random.randint(50, 100)
        latex = f"\\text{{What number comes before }} {num}?"
        solution = str(num - 1)
        return Equation(latex=latex, solution=solution, steps=[str(num - 1)], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        num = random.randint(70, 120)
        latex = f"\\text{{Count from }} {num} \\text{{ to }} {num + 5}"
        solution = f"{num}, {num + 1}, {num + 2}, {num + 3}, {num + 4}, {num + 5}"
        return Equation(latex=latex, solution=solution, steps=["counting sequence"], difficulty='challenge')


def main():
    generator = CountingAndNumbersGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
