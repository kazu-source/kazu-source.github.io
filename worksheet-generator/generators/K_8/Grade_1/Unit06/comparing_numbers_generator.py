"""
Comparing Numbers Generator - Grade 1 Unit06
Generates comparing numbers problems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingNumbersGenerator:
    """Generates comparing numbers problems."""

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
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        while a == b:
            b = random.randint(10, 50)
        latex = f"\\text{{Which is greater: {a} or {b}?}}"
        solution = str(max(a, b))
        return Equation(latex=latex, solution=solution, steps=[f"{solution} > {min(a, b)}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(20, 80)
        b = random.randint(20, 80)
        while a == b:
            b = random.randint(20, 80)
        symbol = '>' if a > b else '<'
        latex = f"{a} \\_ {b}"
        solution = symbol
        return Equation(latex=latex, solution=solution, steps=[f"{a} {symbol} {b}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(30, 99)
        b = random.randint(30, 99)
        while a == b:
            b = random.randint(30, 99)
        if a > b:
            solution = "greater than"
        else:
            solution = "less than"
        latex = f"\\text{{Is {a} greater than or less than {b}?}}"
        return Equation(latex=latex, solution=solution, steps=[f"{a} vs {b}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        nums = random.sample(range(20, 90), 3)
        nums_str = ', '.join(map(str, nums))
        sorted_nums = sorted(nums)
        latex = f"\\text{{Order from least to greatest: {nums_str}}}"
        solution = ', '.join(map(str, sorted_nums))
        return Equation(latex=latex, solution=solution, steps=["order numbers"], difficulty='challenge')


def main():
    generator = ComparingNumbersGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
