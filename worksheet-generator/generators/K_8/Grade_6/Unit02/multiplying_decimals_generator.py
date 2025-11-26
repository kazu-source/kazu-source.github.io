"""
Multiplying Decimals Generator - Grade 6 Unit 2
Generates problems multiplying decimal numbers
Example: 3.5 × 2.4 = ?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplyingDecimalsGenerator:
    """Generates multiplying decimals problems."""

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
        """Generate easy problems: multiplying decimals by whole numbers."""
        decimal = round(random.uniform(1.0, 5.0), 1)
        whole = random.randint(2, 9)

        result = round(decimal * whole, 1)

        latex = f"{decimal} \\times {whole}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{decimal} \\times {whole} = {result}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: multiplying tenths by tenths."""
        num1 = round(random.uniform(1.0, 9.0), 1)
        num2 = round(random.uniform(1.0, 9.0), 1)

        result = round(num1 * num2, 2)

        latex = f"{num1} \\times {num2}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num1} \\times {num2} = {result}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: multiplying hundredths."""
        num1 = round(random.uniform(1.0, 10.0), 2)
        num2 = round(random.uniform(1.0, 10.0), 2)

        result = round(num1 * num2, 2)

        latex = f"{num1} \\times {num2}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num1} \\times {num2} = {result}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multiplying three decimals or larger values."""
        if random.choice([True, False]):
            # Three decimals
            num1 = round(random.uniform(1.0, 5.0), 1)
            num2 = round(random.uniform(1.0, 5.0), 1)
            num3 = round(random.uniform(1.0, 5.0), 1)

            result = round(num1 * num2 * num3, 2)

            latex = f"{num1} \\times {num2} \\times {num3}"
            solution = str(result)
        else:
            # Larger decimals
            num1 = round(random.uniform(10.0, 50.0), 2)
            num2 = round(random.uniform(1.0, 5.0), 2)

            result = round(num1 * num2, 2)

            latex = f"{num1} \\times {num2}"
            solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{latex} = {result}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiplyingDecimalsGenerator()

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
