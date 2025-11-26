"""
Whole Numbers and Integers Generator - Grade 6 Unit 6
Generates problems distinguishing whole numbers and integers
Example: Is -5 a whole number or an integer?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class WholeNumbersAndIntegersGenerator:
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problems.append(self._generate_problem(difficulty))
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
        num = random.randint(0, 20)
        latex = f"\\text{{Is }} {num} \\text{{ a whole number?}}"
        solution = "Yes"
        return Equation(latex=latex, solution=solution, steps=["Whole numbers: 0, 1, 2, 3, ..."], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num = random.randint(-20, -1)
        latex = f"\\text{{Is }} {num} \\text{{ a whole number?}}"
        solution = "No (it is an integer)"
        return Equation(latex=latex, solution=solution, steps=["Negative numbers are integers, not whole numbers"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        nums = [random.randint(-10, 20) for _ in range(5)]
        whole_nums = [n for n in nums if n >= 0]
        latex = f"\\text{{Which are whole numbers: }} {', '.join(map(str, nums))}"
        solution = ', '.join(map(str, whole_nums)) if whole_nums else "None"
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Whole numbers: }} {solution}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        nums = [random.randint(-15, 15) for _ in range(6)]
        integers = [n for n in nums]
        latex = f"\\text{{Which are integers: }} {', '.join(map(str, nums))}"
        solution = "All are integers"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='challenge')


def main():
    generator = WholeNumbersAndIntegersGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
