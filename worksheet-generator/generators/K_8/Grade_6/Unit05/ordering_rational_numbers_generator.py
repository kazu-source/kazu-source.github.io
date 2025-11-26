"""
Ordering Rational Numbers Generator - Grade 6 Unit 5
Generates problems ordering rational numbers including negatives
Example: Order from least to greatest: -1/2, 0.3, -0.8, 1/4
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class OrderingRationalNumbersGenerator:
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
        nums = [random.randint(-10, 10) for _ in range(4)]
        sorted_nums = sorted(nums)
        latex = f"\\text{{Order from least to greatest: }} {', '.join(map(str, nums))}"
        solution = ', '.join(map(str, sorted_nums))
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Ordered: }} {solution}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        nums_decimal = [round(random.uniform(-5, 5), 1) for _ in range(4)]
        sorted_nums = sorted(nums_decimal)
        latex = f"\\text{{Order from least to greatest: }} {', '.join(map(str, nums_decimal))}"
        solution = ', '.join(map(str, sorted_nums))
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Ordered: }} {solution}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Mix integers, decimals, and fractions
        values = []
        labels = []
        values.append(random.randint(-5, 5))
        labels.append(str(values[-1]))
        dec = round(random.uniform(-3, 3), 1)
        values.append(dec)
        labels.append(str(dec))
        num, denom = random.choice([(1, 2), (1, 4), (3, 4), (-1, 2)])
        values.append(num/denom)
        labels.append(f"\\frac{{{num}}}{{{denom}}}")
        paired = list(zip(values, labels))
        random.shuffle(paired)
        sorted_paired = sorted(paired, key=lambda x: x[0])
        latex = f"\\text{{Order: }} {', '.join([p[1] for p in paired])}"
        solution = ', '.join([p[1] for p in sorted_paired])
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Ordered: }} {solution}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        values = []
        labels = []
        for _ in range(5):
            choice = random.randint(1, 3)
            if choice == 1:
                v = random.randint(-8, 8)
                values.append(v)
                labels.append(str(v))
            elif choice == 2:
                v = round(random.uniform(-5, 5), 2)
                values.append(v)
                labels.append(str(v))
            else:
                num = random.randint(-3, 3)
                denom = random.choice([2, 4, 5])
                v = num / denom
                values.append(v)
                labels.append(f"\\frac{{{num}}}{{{denom}}}")
        paired = list(zip(values, labels))
        random.shuffle(paired)
        sorted_paired = sorted(paired, key=lambda x: x[0])
        latex = f"\\text{{Order from least to greatest: }} {', '.join([p[1] for p in paired[:4]])}"
        solution = ', '.join([p[1] for p in sorted_paired[:4]])
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Ordered: }} {solution}"], difficulty='challenge')


def main():
    generator = OrderingRationalNumbersGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
