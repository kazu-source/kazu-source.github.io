"""
More and Less Generator - Kindergarten Unit 2
Generates problems about comparing quantities using more and less
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MoreAndLessGenerator:
    """Generates more and less comparison problems."""

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
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
        while num1 == num2:
            num2 = random.randint(1, 5)
        if num1 > num2:
            latex = f"\\text{{Which is more: }} {num1} \\text{{ or }} {num2}?"
            solution = str(num1)
        else:
            latex = f"\\text{{Which is more: }} {num1} \\text{{ or }} {num2}?"
            solution = str(num2)
        return Equation(latex=latex, solution=solution, steps=[f"{solution} is more"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        while num1 == num2:
            num2 = random.randint(1, 10)
        if num1 < num2:
            latex = f"\\text{{Which is less: }} {num1} \\text{{ or }} {num2}?"
            solution = str(num1)
        else:
            latex = f"\\text{{Which is less: }} {num1} \\text{{ or }} {num2}?"
            solution = str(num2)
        return Equation(latex=latex, solution=solution, steps=[f"{solution} is less"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num1 = random.randint(5, 15)
        diff = random.randint(1, 3)
        num2 = num1 + diff
        item = random.choice(['apples', 'toys', 'stickers', 'cookies'])
        latex = f"\\text{{Tom has }} {num1} \\text{{ {item}. Lisa has }} {num2} \\text{{ {item}. Who has more?}}"
        solution = "Lisa"
        return Equation(latex=latex, solution=solution, steps=[f"{num2} > {num1}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        num1 = random.randint(10, 20)
        num2 = num1 - random.randint(1, 5)
        latex = f"\\text{{Circle the number that is less: }} {num1} \\text{{ or }} {num2}"
        solution = str(num2)
        return Equation(latex=latex, solution=solution, steps=[f"{num2} < {num1}"], difficulty='challenge')


def main():
    generator = MoreAndLessGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
