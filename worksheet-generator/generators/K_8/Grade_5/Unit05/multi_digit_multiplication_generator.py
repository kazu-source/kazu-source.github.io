"""
Multi-Digit Multiplication Generator - Grade 5 Unit 5
Generates multi-digit multiplication problems
Example: 24 × 36 = 864
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiDigitMultiplicationGenerator:
    """Generates multi-digit multiplication problems."""

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
        """Generate easy problems: 2-digit × 1-digit."""
        tens = random.randint(2, 8)
        ones = random.randint(1, 9)
        num1 = tens * 10 + ones

        num2 = random.randint(2, 9)

        product = num1 * num2

        latex = f"{num1} \\times {num2}"
        solution = str(product)
        steps = [
            f"{num1} \\times {num2}",
            f"= {product}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 2-digit × 2-digit."""
        tens1 = random.randint(2, 7)
        ones1 = random.randint(1, 9)
        num1 = tens1 * 10 + ones1

        tens2 = random.randint(2, 7)
        ones2 = random.randint(1, 9)
        num2 = tens2 * 10 + ones2

        product = num1 * num2

        latex = f"{num1} \\times {num2}"
        solution = str(product)
        steps = [
            f"{num1} \\times {num2}",
            f"= {product}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 3-digit × 2-digit."""
        hundreds = random.randint(2, 6)
        tens = random.randint(0, 9)
        ones = random.randint(0, 9)
        num1 = hundreds * 100 + tens * 10 + ones

        tens2 = random.randint(2, 7)
        ones2 = random.randint(1, 9)
        num2 = tens2 * 10 + ones2

        product = num1 * num2

        latex = f"{num1} \\times {num2}"
        solution = str(product)
        steps = [
            f"{num1} \\times {num2}",
            f"= {product}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: 3-digit × 3-digit."""
        hundreds1 = random.randint(1, 5)
        tens1 = random.randint(0, 9)
        ones1 = random.randint(0, 9)
        num1 = hundreds1 * 100 + tens1 * 10 + ones1

        hundreds2 = random.randint(1, 4)
        tens2 = random.randint(0, 9)
        ones2 = random.randint(0, 9)
        num2 = hundreds2 * 100 + tens2 * 10 + ones2

        product = num1 * num2

        latex = f"{num1} \\times {num2}"
        solution = str(product)
        steps = [
            f"{num1} \\times {num2}",
            f"= {product}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiDigitMultiplicationGenerator()

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
