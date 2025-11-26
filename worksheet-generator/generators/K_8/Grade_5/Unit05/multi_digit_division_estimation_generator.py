"""
Multi-Digit Division Estimation Generator - Grade 5 Unit 5
Generates problems estimating quotients of multi-digit division
Example: Estimate 184 ÷ 6 by using compatible numbers: 180 ÷ 6 = 30
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiDigitDivisionEstimationGenerator:
    """Generates multi-digit division estimation problems."""

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

    def _find_compatible_dividend(self, divisor, target):
        """Find a compatible number close to target that divides evenly."""
        # Find multiples of divisor near target
        quotient = round(target / divisor)
        return divisor * quotient, quotient

    def _generate_easy(self) -> Equation:
        """Generate easy problems: 2-digit ÷ 1-digit estimation."""
        divisor = random.randint(3, 9)

        # Create a dividend close to but not exactly divisible
        quotient_base = random.randint(5, 15)
        dividend_base = divisor * quotient_base
        dividend = dividend_base + random.randint(1, divisor - 1)

        compatible, estimate = self._find_compatible_dividend(divisor, dividend)

        latex = f"\\text{{{{Estimate using compatible numbers: }}}} {dividend} \\div {divisor}"
        solution = str(estimate)
        steps = [
            f"{dividend} \\approx {compatible}",
            f"{compatible} \\div {divisor} = {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 3-digit ÷ 1-digit estimation."""
        divisor = random.randint(4, 9)

        # Create a dividend
        quotient_base = random.randint(20, 60)
        dividend_base = divisor * quotient_base
        dividend = dividend_base + random.randint(1, divisor - 1)

        compatible, estimate = self._find_compatible_dividend(divisor, dividend)

        latex = f"\\text{{{{Estimate using compatible numbers: }}}} {dividend} \\div {divisor}"
        solution = str(estimate)
        steps = [
            f"{dividend} \\approx {compatible}",
            f"{compatible} \\div {divisor} = {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 3-digit ÷ 2-digit estimation."""
        divisor = random.randint(12, 25)

        # Create a dividend
        quotient_base = random.randint(10, 30)
        dividend_base = divisor * quotient_base
        dividend = dividend_base + random.randint(1, divisor - 1)

        compatible, estimate = self._find_compatible_dividend(divisor, dividend)

        latex = f"\\text{{{{Estimate using compatible numbers: }}}} {dividend} \\div {divisor}"
        solution = str(estimate)
        steps = [
            f"{dividend} \\approx {compatible}",
            f"{compatible} \\div {divisor} = {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: estimate and compare to actual."""
        divisor = random.randint(6, 12)

        quotient_base = random.randint(15, 40)
        dividend_base = divisor * quotient_base
        dividend = dividend_base + random.randint(1, divisor - 1)

        compatible, estimate = self._find_compatible_dividend(divisor, dividend)
        actual = dividend // divisor
        remainder = dividend % divisor

        latex = f"\\text{{{{Estimate }}}} {dividend} \\div {divisor} \\text{{{{ and compare to actual quotient.}}}}"
        solution = f"\\text{{{{Estimate: }}}} {estimate}, \\text{{{{ Actual: }}}} {actual} \\text{{{{ R }}}} {remainder}"
        steps = [
            f"{dividend} \\approx {compatible}",
            f"\\text{{{{Estimate: }}}} {compatible} \\div {divisor} = {estimate}",
            f"\\text{{{{Actual: }}}} {dividend} \\div {divisor} = {actual} \\text{{{{ R }}}} {remainder}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiDigitDivisionEstimationGenerator()

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
