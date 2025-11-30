"""
Addition Up to 10 Generator - Kindergarten Unit 4
Generates basic addition problems with sums up to 10
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AdditionUpTo10Generator:
    """Generates addition up to 10 problems."""

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
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        total = a + b
        latex = f"{a} + {b} = "
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} = {total}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(1, 9)
        b = random.randint(1, 10 - a)
        total = a + b
        latex = f"{a} + {b} = "
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} = {total}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        total = random.randint(5, 10)
        a = random.randint(1, total - 1)
        b = total - a
        item = random.choice(['pencils', 'crayons', 'stickers', 'cookies'])
        latex = f"\\text{{{a} {item} plus {b} {item} equals?}}"
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} = {total}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        total = random.randint(6, 10)
        a = random.randint(2, total - 2)
        b = total - a
        latex = f"{a} + \\_ = {total}"
        solution = str(b)
        return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} = {total}"], difficulty='challenge')


def main():
    generator = AdditionUpTo10Generator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
