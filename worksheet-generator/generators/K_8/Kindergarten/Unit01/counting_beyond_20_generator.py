"""
Counting Beyond 20 Generator - Kindergarten Unit 1
Generates counting problems with quantities beyond 20
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CountingBeyond20Generator:
    """Generates counting beyond 20 problems."""

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
        num = random.randint(21, 30)
        latex = f"\\text{{Count to }} {num}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num = random.randint(21, 40)
        latex = f"\\text{{Write the number: }} {num}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num = random.randint(21, 50)
        latex = f"\\text{{What number comes after }} {num - 1}?"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        start = random.randint(21, 45)
        skip = random.randint(1, 5)
        result = start + skip
        latex = f"\\text{{Count from }} {start} \\text{{ by }} {skip}\\text{{s. What is the next number?}}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{start} + {skip} = {result}"], difficulty='challenge')


def main():
    generator = CountingBeyond20Generator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
