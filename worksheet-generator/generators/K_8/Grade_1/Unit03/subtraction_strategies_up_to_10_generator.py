"""
Subtraction Strategies Up to 10 Generator - Grade 1 Unit 3\nGenerates subtraction strategy problems up to 10
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SubtractionStrategiesUpTo10Generator:
    """Generates subtraction strategies up to 10 problems."""

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
        a = random.randint(3, 7)
        b = random.randint(1, a)
        result = a - b
        latex = f"{a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"count back from {a}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(5, 10)
        b = random.randint(1, a)
        result = a - b
        latex = f"{a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = 10
        b = random.randint(2, 8)
        result = a - b
        latex = f"\\text{{{{Subtract from 10: }}}} {a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"10 - {b} = {result}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(6, 10)
        b = random.randint(2, a - 1)
        result = a - b
        latex = f"\\_ - {b} = {result}"
        solution = str(a)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='challenge')


def main():
    generator = SubtractionStrategiesUpTo10Generator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
