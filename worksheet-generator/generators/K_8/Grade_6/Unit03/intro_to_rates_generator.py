"""
Intro to Rates Generator - Grade 6 Unit 3
Generates problems introducing basic rate concepts
Example: A car travels 120 miles in 2 hours. What is the rate in miles per hour?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IntroToRatesGenerator:
    """Generates intro to rates problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Equation objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy problems: simple unit rates with whole number results."""
        contexts = [
            ("miles", "hour", [60, 120, 180, 240], [2, 3, 4]),
            ("dollars", "item", [10, 20, 30, 40], [2, 5]),
            ("pages", "minute", [6, 9, 12, 15], [3]),
            ("cookies", "batch", [12, 24, 36], [2, 3, 4])
        ]

        unit1, unit2, numerators, denominators = random.choice(contexts)
        numerator = random.choice(numerators)
        denominator = random.choice(denominators)
        rate = numerator // denominator

        latex = f"\\text{{If you have {numerator} {unit1} in {denominator} {unit2}s, what is the rate in {unit1} per {unit2}?}}"
        solution = f"{rate} {unit1} per {unit2}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Rate}} = \\frac{{{numerator} \\text{{ {unit1}}}}}{{{denominator} \\text{{ {unit2}s}}}}",
                f"\\text{{Rate}} = {rate} \\text{{ {unit1} per {unit2}}}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: unit rates requiring division."""
        contexts = [
            ("miles", "gallon", (240, 360, 480), (12, 15, 16)),
            ("words", "minute", (150, 180, 210, 240), (5, 6)),
            ("dollars", "hour", (90, 120, 150), (6, 8, 10)),
            ("meters", "second", (100, 150, 200), (5, 10))
        ]

        unit1, unit2, nums, denoms = random.choice(contexts)
        numerator = random.choice(nums)
        denominator = random.choice(denoms)
        rate = numerator / denominator

        latex = f"\\text{{A person travels {numerator} {unit1} in {denominator} {unit2}s. Find the unit rate.}}"
        solution = f"{rate:.1f} {unit1} per {unit2}" if rate % 1 else f"{int(rate)} {unit1} per {unit2}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{numerator} \\div {denominator} = {rate:.1f}" if rate % 1 else f"{numerator} \\div {denominator} = {int(rate)}",
                f"\\text{{Unit rate: {solution}}}"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: comparing two rates."""
        unit1, unit2 = random.choice([("miles", "gallon"), ("dollars", "pound"), ("pages", "hour")])

        num1 = random.randint(10, 20) * 10
        denom1 = random.choice([4, 5, 8, 10])
        rate1 = num1 / denom1

        num2 = random.randint(10, 20) * 10
        denom2 = random.choice([4, 5, 8, 10])
        rate2 = num2 / denom2

        better = "Option A" if rate1 > rate2 else "Option B"

        latex = f"\\text{{Option A: {num1} {unit1} per {denom1} {unit2}s. Option B: {num2} {unit1} per {denom2} {unit2}s.}}"
        latex += f"\\text{{ Which option has a better rate?}}"
        solution = better

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Option A: }} {num1} \\div {denom1} = {rate1:.1f}",
                f"\\text{{Option B: }} {num2} \\div {denom2} = {rate2:.1f}",
                f"\\text{{Better rate: {better}}}"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step rate problems."""
        distance = random.randint(8, 15) * 20
        time = random.choice([2, 3, 4])
        rate = distance / time
        new_time = random.choice([5, 6, 7])
        new_distance = rate * new_time

        latex = f"\\text{{A train travels {distance} miles in {time} hours.}}"
        latex += f"\\text{{ At the same rate, how far will it travel in {new_time} hours?}}"
        solution = f"{new_distance:.0f} miles"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Rate}} = {distance} \\div {time} = {rate:.1f} \\text{{ miles/hour}}",
                f"\\text{{Distance}} = {rate:.1f} \\times {new_time} = {new_distance:.0f} \\text{{ miles}}"
            ],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = IntroToRatesGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
