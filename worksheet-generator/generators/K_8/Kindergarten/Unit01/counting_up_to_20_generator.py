"""
Counting Up to 20 Generator - Kindergarten Unit 1
Generates counting problems with quantities up to 20
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CountingUpTo20Generator:
    """Generates counting up to 20 problems."""

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
        num = random.randint(11, 15)
        latex = f"\\text{{Count and write the number: }} {num} \\text{{ objects}}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num = random.randint(11, 20)
        latex = f"\\text{{How many? }} {num}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num = random.randint(11, 20)
        item = random.choice(['blocks', 'marbles', 'buttons', 'beads'])
        latex = f"\\text{{Count the {item}: }} {num}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        num1 = random.randint(10, 15)
        num2 = random.randint(1, 20 - num1)
        total = num1 + num2
        latex = f"{num1} \\text{{ and }} {num2} \\text{{ more makes?}}"
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{num1} + {num2} = {total}"], difficulty='challenge')


def main():
    generator = CountingUpTo20Generator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
