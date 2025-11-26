"""
Multi-Digit Multiplication Estimation Generator - Grade 5 Unit 5
Generates problems estimating products of multi-digit multiplication
Example: Estimate 38 × 24 by rounding to tens: 40 × 20 = 800
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiDigitMultiplicationEstimationGenerator:
    """Generates multi-digit multiplication estimation problems."""

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

    def _round_to_tens(self, n):
        """Round to nearest ten."""
        return round(n / 10) * 10

    def _round_to_hundreds(self, n):
        """Round to nearest hundred."""
        return round(n / 100) * 100

    def _generate_easy(self) -> Equation:
        """Generate easy problems: estimate 2-digit × 1-digit."""
        tens = random.randint(2, 8)
        ones = random.randint(1, 9)
        num1 = tens * 10 + ones

        num2 = random.randint(2, 9)

        rounded1 = self._round_to_tens(num1)
        estimate = rounded1 * num2

        latex = f"\\text{{{{Estimate by rounding to the nearest ten: }}}} {num1} \\times {num2}"
        solution = str(estimate)
        steps = [
            f"{num1} \\approx {rounded1}",
            f"{rounded1} \\times {num2} = {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: estimate 2-digit × 2-digit."""
        tens1 = random.randint(2, 7)
        ones1 = random.randint(1, 9)
        num1 = tens1 * 10 + ones1

        tens2 = random.randint(2, 7)
        ones2 = random.randint(1, 9)
        num2 = tens2 * 10 + ones2

        rounded1 = self._round_to_tens(num1)
        rounded2 = self._round_to_tens(num2)
        estimate = rounded1 * rounded2

        latex = f"\\text{{{{Estimate by rounding to the nearest ten: }}}} {num1} \\times {num2}"
        solution = str(estimate)
        steps = [
            f"{num1} \\approx {rounded1}, \\quad {num2} \\approx {rounded2}",
            f"{rounded1} \\times {rounded2} = {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: estimate 3-digit × 2-digit."""
        hundreds = random.randint(2, 6)
        tens = random.randint(0, 9)
        ones = random.randint(0, 9)
        num1 = hundreds * 100 + tens * 10 + ones

        tens2 = random.randint(2, 7)
        ones2 = random.randint(0, 9)
        num2 = tens2 * 10 + ones2

        rounded1 = self._round_to_hundreds(num1)
        rounded2 = self._round_to_tens(num2)
        estimate = rounded1 * rounded2

        latex = f"\\text{{{{Estimate: }}}} {num1} \\times {num2}"
        solution = str(estimate)
        steps = [
            f"{num1} \\approx {rounded1}, \\quad {num2} \\approx {rounded2}",
            f"{rounded1} \\times {rounded2} = {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: compare estimate to actual."""
        tens1 = random.randint(3, 7)
        ones1 = random.randint(2, 8)
        num1 = tens1 * 10 + ones1

        tens2 = random.randint(2, 6)
        ones2 = random.randint(2, 8)
        num2 = tens2 * 10 + ones2

        rounded1 = self._round_to_tens(num1)
        rounded2 = self._round_to_tens(num2)
        estimate = rounded1 * rounded2
        actual = num1 * num2

        difference = abs(estimate - actual)

        latex = f"\\text{{{{Estimate }}}} {num1} \\times {num2} \\text{{{{ and find the difference from the actual product.}}}}"
        solution = f"\\text{{{{Estimate: }}}} {estimate}, \\text{{{{ Actual: }}}} {actual}, \\text{{{{ Difference: }}}} {difference}"
        steps = [
            f"{num1} \\approx {rounded1}, \\quad {num2} \\approx {rounded2}",
            f"\\text{{{{Estimate: }}}} {rounded1} \\times {rounded2} = {estimate}",
            f"\\text{{{{Actual: }}}} {num1} \\times {num2} = {actual}",
            f"\\text{{{{Difference: }}}} |{estimate} - {actual}| = {difference}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiDigitMultiplicationEstimationGenerator()

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
