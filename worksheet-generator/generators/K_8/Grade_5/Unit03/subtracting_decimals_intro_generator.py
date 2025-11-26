"""
Subtracting Decimals Intro Generator - Grade 5 Unit 3
Generates problems introducing decimal subtraction
Example: 0.7 - 0.3 = 0.4
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SubtractingDecimalsIntroGenerator:
    """Generates subtracting decimals introduction problems."""

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
        """Generate easy problems: subtract tenths without regrouping."""
        tenths1 = random.randint(5, 9)
        tenths2 = random.randint(1, tenths1 - 1)

        num1 = f"0.{tenths1}"
        num2 = f"0.{tenths2}"
        result = f"0.{tenths1 - tenths2}"

        latex = f"{num1} - {num2}"
        solution = result
        steps = [
            f"{num1} - {num2}",
            f"\\text{{{{Subtract tenths: }}}} {tenths1} - {tenths2} = {tenths1 - tenths2}",
            result
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: subtract with regrouping from ones."""
        ones1 = random.randint(2, 8)
        tenths1 = random.randint(0, 3)
        tenths2 = random.randint(5, 9)

        num1 = f"{ones1}.{tenths1}"
        num2 = f"0.{tenths2}"

        # Need to regroup
        result_ones = ones1 - 1
        result_tenths = 10 + tenths1 - tenths2

        result = f"{result_ones}.{result_tenths}"

        latex = f"{num1} - {num2}"
        solution = result
        steps = [
            f"{num1} - {num2}",
            f"\\text{{{{Regroup: }}}} {ones1}.{tenths1} = {ones1 - 1}.{10 + tenths1}",
            f"\\text{{{{Subtract: }}}} {result_ones}.{result_tenths}",
            result
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: subtract whole numbers and tenths."""
        ones1 = random.randint(5, 12)
        tenths1 = random.randint(0, 9)
        ones2 = random.randint(1, ones1 - 1)
        tenths2 = random.randint(0, 9)

        num1 = f"{ones1}.{tenths1}"
        num2 = f"{ones2}.{tenths2}"

        result = round(ones1 + tenths1/10 - ones2 - tenths2/10, 1)

        latex = f"{num1} - {num2}"
        solution = str(result)
        steps = [
            f"{num1} - {num2}",
            str(result)
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: subtract from whole number."""
        ones1 = random.randint(5, 15)
        ones2 = random.randint(1, ones1 - 1)
        tenths2 = random.randint(1, 9)

        num1 = str(ones1)
        num2 = f"{ones2}.{tenths2}"

        result = round(ones1 - ones2 - tenths2/10, 1)

        latex = f"{num1} - {num2}"
        solution = str(result)
        steps = [
            f"{num1} - {num2}",
            f"{num1}.0 - {num2}",
            str(result)
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = SubtractingDecimalsIntroGenerator()

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
