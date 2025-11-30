"""
Addition With Two Digits Generator - Grade 1 Unit 7
Generates two-digit addition problems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AdditionWithTwoDigitsGenerator:
    """Generates addition with two digits problems."""

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
        a = random.randint(10, 30)
        b = random.randint(10, 20)
        total = a + b
        latex = f"{a} + {b} = "
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{total}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(20, 60)
        b = random.randint(10, 40)
        total = a + b
        if total > 99:
            b = 99 - a
            total = a + b
        latex = f"{a} + {b} = "
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} = {total}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(30, 70)
        b = random.randint(10, 50)
        total = a + b
        if total > 99:
            b = 99 - a
            total = a + b
        latex = f"{a} + {b} = "
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{total}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        total = random.randint(50, 99)
        a = random.randint(20, total - 20)
        b = total - a
        latex = f"{a} + \\_ = {total}"
        solution = str(b)
        return Equation(latex=latex, solution=solution, steps=[f"missing addend: {b}"], difficulty='challenge')


def main():
    generator = AdditionWithTwoDigitsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
