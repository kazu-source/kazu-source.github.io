"""
Multi-Digit Division Generator - Grade 5 Unit 5
Generates multi-digit division problems
Example: 156 ÷ 12 = 13
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiDigitDivisionGenerator:
    """Generates multi-digit division problems."""

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
        """Generate easy problems: 2-digit ÷ 1-digit, no remainder."""
        divisor = random.randint(3, 9)
        quotient = random.randint(5, 15)
        dividend = divisor * quotient

        latex = f"{dividend} \\div {divisor}"
        solution = str(quotient)
        steps = [
            f"{dividend} \\div {divisor}",
            f"= {quotient}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 2-digit or 3-digit ÷ 1-digit with remainder."""
        divisor = random.randint(4, 9)
        quotient = random.randint(10, 40)
        remainder = random.randint(1, divisor - 1)
        dividend = divisor * quotient + remainder

        latex = f"{dividend} \\div {divisor}"
        solution = f"{quotient} \\text{{{{ R }}}} {remainder}"
        steps = [
            f"{dividend} \\div {divisor}",
            f"= {quotient} \\text{{{{ R }}}} {remainder}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 3-digit ÷ 2-digit."""
        divisor = random.randint(12, 25)
        quotient = random.randint(10, 35)

        if random.choice([True, False]):
            # No remainder
            dividend = divisor * quotient
            solution = str(quotient)
            steps = [
                f"{dividend} \\div {divisor}",
                f"= {quotient}"
            ]
        else:
            # With remainder
            remainder = random.randint(1, divisor - 1)
            dividend = divisor * quotient + remainder
            solution = f"{quotient} \\text{{{{ R }}}} {remainder}"
            steps = [
                f"{dividend} \\div {divisor}",
                f"= {quotient} \\text{{{{ R }}}} {remainder}"
            ]

        latex = f"{dividend} \\div {divisor}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: 4-digit ÷ 2-digit."""
        divisor = random.randint(15, 35)
        quotient = random.randint(40, 150)

        if random.choice([True, False, False]):  # Less likely to have no remainder
            # No remainder
            dividend = divisor * quotient
            solution = str(quotient)
            steps = [
                f"{dividend} \\div {divisor}",
                f"= {quotient}"
            ]
        else:
            # With remainder
            remainder = random.randint(1, divisor - 1)
            dividend = divisor * quotient + remainder
            solution = f"{quotient} \\text{{{{ R }}}} {remainder}"
            steps = [
                f"{dividend} \\div {divisor}",
                f"= {quotient} \\text{{{{ R }}}} {remainder}"
            ]

        latex = f"{dividend} \\div {divisor}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiDigitDivisionGenerator()

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
