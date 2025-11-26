"""
Comparing Negative Numbers Generator - Grade 6 Unit 5
Generates problems comparing negative numbers
Example: Which is greater: -5 or -8?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingNegativeNumbersGenerator:
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
        num1 = -random.randint(1, 10)
        num2 = -random.randint(1, 10)
        while num1 == num2:
            num2 = -random.randint(1, 10)
        comp = ">" if num1 > num2 else "<"
        latex = f"\\text{{Compare: }} {num1} \\quad ? \\quad {num2}"
        solution = f"{num1} {comp} {num2}"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num1 = random.choice([random.randint(-20, -1), random.randint(1, 20)])
        num2 = random.choice([random.randint(-20, -1), random.randint(1, 20)])
        while num1 == num2:
            num2 = random.choice([random.randint(-20, -1), random.randint(1, 20)])
        comp = ">" if num1 > num2 else "<"
        latex = f"\\text{{Compare: }} {num1} \\quad ? \\quad {num2}"
        solution = f"{num1} {comp} {num2}"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num1 = round(random.uniform(-10, 10), 1)
        num2 = round(random.uniform(-10, 10), 1)
        while abs(num1 - num2) < 0.5:
            num2 = round(random.uniform(-10, 10), 1)
        comp = ">" if num1 > num2 else "<"
        latex = f"\\text{{Compare: }} {num1} \\quad ? \\quad {num2}"
        solution = f"{num1} {comp} {num2}"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        nums = [random.randint(-15, 15) for _ in range(4)]
        nums = list(set(nums))[:4]
        sorted_nums = sorted(nums)
        latex = f"\\text{{Order from least to greatest: }} {', '.join(map(str, nums))}"
        solution = ', '.join(map(str, sorted_nums))
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Ordered: }} {solution}"], difficulty='challenge')


def main():
    generator = ComparingNegativeNumbersGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
