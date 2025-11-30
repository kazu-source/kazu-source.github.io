"""
Coin Values Generator - Kindergarten Unit 9
Generates problems about coin values and simple counting
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CoinValuesGenerator:
    """Generates coin values problems."""

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
        num_pennies = random.randint(1, 5)
        latex = f"\\text{{How many cents in {num_pennies} penn{'y' if num_pennies == 1 else 'ies'}?}}"
        solution = f"{num_pennies} cents"
        return Equation(latex=latex, solution=solution, steps=[f"{num_pennies} × 1 = {num_pennies}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num_nickels = random.randint(1, 3)
        total = num_nickels * 5
        latex = f"\\text{{How many cents in {num_nickels} nickel{'s' if num_nickels > 1 else ''}?}}"
        solution = f"{total} cents"
        return Equation(latex=latex, solution=solution, steps=[f"{num_nickels} × 5 = {total}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num_pennies = random.randint(1, 4)
        num_nickels = random.randint(1, 2)
        total = num_pennies + (num_nickels * 5)
        latex = f"\\text{{{num_pennies} penn{'y' if num_pennies == 1 else 'ies'} and {num_nickels} nickel{'s' if num_nickels > 1 else ''} = ? cents}}"
        solution = f"{total} cents"
        return Equation(latex=latex, solution=solution, steps=[f"{num_pennies} + {num_nickels * 5} = {total}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        num_dimes = random.randint(1, 2)
        total = num_dimes * 10
        latex = f"\\text{{What is the value of {num_dimes} dime{'s' if num_dimes > 1 else ''}?}}"
        solution = f"{total} cents"
        return Equation(latex=latex, solution=solution, steps=[f"{num_dimes} × 10 = {total}"], difficulty='challenge')


def main():
    generator = CoinValuesGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
