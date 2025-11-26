"""
Rational Numbers on Number Line Generator - Grade 6 Unit 5
Generates problems on plotting rational numbers on a number line
Example: Plot -2.5 on a number line
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RationalNumbersOnNumberLineGenerator:
    """Generates rational numbers on number line problems."""

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
        num = random.randint(-10, 10)
        latex = f"\\text{{What integer is located at position }} {num} \\text{{ on the number line?}}"
        solution = str(num)
        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{The integer is }} {num}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        num = round(random.uniform(-5, 5), 1)
        latex = f"\\text{{Plot }} {num} \\text{{ on a number line. Between which two integers does it lie?}}"
        lower = int(num) if num >= 0 else int(num) - 1
        upper = lower + 1
        solution = f"\\text{{Between }} {lower} \\text{{ and }} {upper}"
        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num} \\text{{ is between }} {lower} \\text{{ and }} {upper}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        numerator = random.randint(-15, 15)
        denominator = random.choice([2, 4, 5])
        if numerator % denominator == 0:
            numerator += 1
        latex = f"\\text{{Where is }} \\frac{{{numerator}}}{{{denominator}}} \\text{{ on the number line?}}"
        decimal_val = numerator / denominator
        solution = f"{decimal_val:.2f}"
        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{{numerator}}}{{{denominator}}} = {decimal_val:.2f}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        nums = [round(random.uniform(-5, 5), 1) for _ in range(3)]
        nums.sort()
        latex = f"\\text{{Order these numbers on a number line: }} {nums[1]}, {nums[2]}, {nums[0]}"
        solution = f"{nums[0]}, {nums[1]}, {nums[2]}"
        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Ordered: }} {solution}"],
            difficulty='challenge'
        )


def main():
    generator = RationalNumbersOnNumberLineGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
