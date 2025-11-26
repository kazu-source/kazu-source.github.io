"""
Dividing Whole Numbers Generator - Grade 6 Unit 2
Generates problems dividing whole numbers (including long division)
Example: 144 ÷ 12 = ?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DividingWholeNumbersGenerator:
    """Generates dividing whole numbers problems."""

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
        """Generate easy problems: simple division (division facts)."""
        divisor = random.randint(2, 10)
        quotient = random.randint(2, 12)
        dividend = divisor * quotient

        latex = f"{dividend} \\div {divisor}"
        solution = str(quotient)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{dividend} \\div {divisor} = {quotient}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: two-digit dividends."""
        divisor = random.randint(2, 9)
        quotient = random.randint(10, 20)
        dividend = divisor * quotient

        latex = f"{dividend} \\div {divisor}"
        solution = str(quotient)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{dividend} \\div {divisor} = {quotient}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: three-digit dividends."""
        divisor = random.randint(10, 25)
        quotient = random.randint(10, 50)
        dividend = divisor * quotient

        latex = f"{dividend} \\div {divisor}"
        solution = str(quotient)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{dividend} \\div {divisor} = {quotient}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: larger dividends or remainders."""
        if random.choice([True, False]):
            # Larger numbers without remainder
            divisor = random.randint(15, 40)
            quotient = random.randint(20, 100)
            dividend = divisor * quotient

            latex = f"{dividend} \\div {divisor}"
            solution = str(quotient)
        else:
            # With remainder
            divisor = random.randint(10, 25)
            quotient = random.randint(10, 50)
            remainder = random.randint(1, divisor - 1)
            dividend = divisor * quotient + remainder

            latex = f"{dividend} \\div {divisor}"
            solution = f"{quotient} R{remainder}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{latex} = {solution}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = DividingWholeNumbersGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
