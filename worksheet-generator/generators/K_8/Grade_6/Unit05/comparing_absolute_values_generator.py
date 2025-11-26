"""
Comparing Absolute Values Generator - Grade 6 Unit 5
Generates problems comparing absolute values
Example: Which is greater: |−7| or |4|?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingAbsoluteValuesGenerator:
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
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        while abs(num1) == abs(num2):
            num2 = random.randint(-10, 10)
        comp = ">" if abs(num1) > abs(num2) else "<"
        latex = f"\\text{{Compare: }} |{num1}| \\quad ? \\quad |{num2}|"
        solution = f"|{num1}| {comp} |{num2}|"
        return Equation(latex=latex, solution=solution, steps=[f"{abs(num1)} {comp} {abs(num2)}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num1 = round(random.uniform(-15, 15), 1)
        num2 = round(random.uniform(-15, 15), 1)
        while abs(abs(num1) - abs(num2)) < 0.5:
            num2 = round(random.uniform(-15, 15), 1)
        comp = ">" if abs(num1) > abs(num2) else "<"
        latex = f"\\text{{Compare: }} |{num1}| \\quad ? \\quad |{num2}|"
        solution = f"|{num1}| {comp} |{num2}|"
        return Equation(latex=latex, solution=solution, steps=[f"{abs(num1)} {comp} {abs(num2)}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        nums = [random.randint(-20, 20) for _ in range(4)]
        sorted_by_abs = sorted(nums, key=abs)
        latex = f"\\text{{Order by absolute value (least to greatest): }} {', '.join(map(str, nums))}"
        solution = ', '.join(map(str, sorted_by_abs))
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Ordered: }} {solution}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        num1 = random.randint(-12, 12)
        num2 = random.randint(-12, 12)
        val1 = abs(num1) + num2
        val2 = num1 + abs(num2)
        comp = ">" if val1 > val2 else ("<" if val1 < val2 else "=")
        latex = f"\\text{{Compare: }} |{num1}| + {num2} \\quad ? \\quad {num1} + |{num2}|"
        solution = f"|{num1}| + {num2} {comp} {num1} + |{num2}|"
        return Equation(latex=latex, solution=solution, steps=[f"{abs(num1)} + {num2} {comp} {num1} + {abs(num2)}"], difficulty='challenge')


def main():
    generator = ComparingAbsoluteValuesGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
