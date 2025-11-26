"""
Adding Decimals (Tenths) Generator - Grade 5 Unit 2
Generates problems adding decimals in tenths
Example: 2.3 + 1.5 = 3.8
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AddingDecimalsTenthsGenerator:
    """Generates adding decimals (tenths) problems."""

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
        """Generate easy problems: add one-digit with tenths, no regrouping."""
        ones1 = random.randint(1, 4)
        tenths1 = random.randint(1, 4)
        ones2 = random.randint(1, 4)
        tenths2 = random.randint(1, 5 - tenths1)

        num1 = f"{ones1}.{tenths1}"
        num2 = f"{ones2}.{tenths2}"
        result = f"{ones1 + ones2}.{tenths1 + tenths2}"

        latex = f"{num1} + {num2}"
        solution = result
        steps = [
            f"{num1} + {num2}",
            f"\\text{{{{Add ones: }}}} {ones1} + {ones2} = {ones1 + ones2}",
            f"\\text{{{{Add tenths: }}}} {tenths1} + {tenths2} = {tenths1 + tenths2}",
            result
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: add with regrouping in tenths."""
        ones1 = random.randint(2, 6)
        tenths1 = random.randint(5, 8)
        ones2 = random.randint(1, 5)
        tenths2 = random.randint(3, 9)

        total_tenths = tenths1 + tenths2
        carry = total_tenths // 10
        result_tenths = total_tenths % 10
        result_ones = ones1 + ones2 + carry

        num1 = f"{ones1}.{tenths1}"
        num2 = f"{ones2}.{tenths2}"
        result = f"{result_ones}.{result_tenths}"

        latex = f"{num1} + {num2}"
        solution = result
        steps = [
            f"{num1} + {num2}",
            f"\\text{{{{Add tenths: }}}} {tenths1} + {tenths2} = {total_tenths} = {carry} \\text{{{{ one and }}}} {result_tenths} \\text{{{{ tenths}}}}",
            f"\\text{{{{Add ones: }}}} {ones1} + {ones2} + {carry} = {result_ones}",
            result
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: add larger numbers with tenths."""
        tens1 = random.randint(1, 5)
        ones1 = random.randint(0, 9)
        tenths1 = random.randint(1, 9)

        tens2 = random.randint(1, 4)
        ones2 = random.randint(0, 9)
        tenths2 = random.randint(1, 9)

        num1_val = tens1 * 10 + ones1
        num2_val = tens2 * 10 + ones2

        num1 = f"{num1_val}.{tenths1}"
        num2 = f"{num2_val}.{tenths2}"

        result_val = round(num1_val + num2_val + (tenths1 + tenths2) / 10, 1)

        latex = f"{num1} + {num2}"
        solution = str(result_val)
        steps = [
            f"{num1} + {num2}",
            f"{result_val}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: add multiple decimals with tenths."""
        ones1 = random.randint(1, 5)
        tenths1 = random.randint(1, 9)
        ones2 = random.randint(1, 5)
        tenths2 = random.randint(1, 9)
        ones3 = random.randint(1, 5)
        tenths3 = random.randint(1, 9)

        num1 = f"{ones1}.{tenths1}"
        num2 = f"{ones2}.{tenths2}"
        num3 = f"{ones3}.{tenths3}"

        result = round(ones1 + ones2 + ones3 + (tenths1 + tenths2 + tenths3) / 10, 1)

        latex = f"{num1} + {num2} + {num3}"
        solution = str(result)
        steps = [
            f"{num1} + {num2} + {num3}",
            f"{result}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = AddingDecimalsTenthsGenerator()

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
