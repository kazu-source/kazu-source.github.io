"""
Adding Decimals Intro Generator - Grade 5 Unit 2
Generates problems introducing decimal addition
Example: 0.3 + 0.2 = 0.5
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AddingDecimalsIntroGenerator:
    """Generates adding decimals introduction problems."""

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
        """Generate easy problems: add tenths without regrouping."""
        tenths1 = random.randint(1, 4)
        tenths2 = random.randint(1, 5 - tenths1)

        num1 = f"0.{tenths1}"
        num2 = f"0.{tenths2}"
        result = f"0.{tenths1 + tenths2}"

        latex = f"{num1} + {num2}"
        solution = result
        steps = [
            f"{num1} + {num2}",
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
        """Generate medium problems: add tenths with regrouping."""
        tenths1 = random.randint(5, 8)
        tenths2 = random.randint(3, 9)

        total_tenths = tenths1 + tenths2
        ones = total_tenths // 10
        tenths = total_tenths % 10

        num1 = f"0.{tenths1}"
        num2 = f"0.{tenths2}"
        result = f"{ones}.{tenths}" if tenths > 0 else str(ones)

        latex = f"{num1} + {num2}"
        solution = result
        steps = [
            f"{num1} + {num2}",
            f"\\text{{{{Add tenths: }}}} {tenths1} + {tenths2} = {total_tenths}",
            f"{total_tenths} \\text{{{{ tenths = }}}} {ones} \\text{{{{ one and }}}} {tenths} \\text{{{{ tenths}}}}",
            result
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: add whole numbers and tenths."""
        ones1 = random.randint(1, 5)
        tenths1 = random.randint(1, 9)
        ones2 = random.randint(1, 4)
        tenths2 = random.randint(1, 9)

        num1 = f"{ones1}.{tenths1}"
        num2 = f"{ones2}.{tenths2}"

        total_tenths = tenths1 + tenths2
        carry = total_tenths // 10
        result_tenths = total_tenths % 10
        result_ones = ones1 + ones2 + carry

        result = f"{result_ones}.{result_tenths}"

        latex = f"{num1} + {num2}"
        solution = result
        steps = [
            f"{num1} + {num2}",
            f"\\text{{{{Add tenths: }}}} {tenths1} + {tenths2} = {total_tenths}",
            f"\\text{{{{Add ones: }}}} {ones1} + {ones2} + {carry} = {result_ones}" if carry else f"\\text{{{{Add ones: }}}} {ones1} + {ones2} = {result_ones}",
            result
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: add three decimals."""
        tenths1 = random.randint(1, 5)
        tenths2 = random.randint(1, 5)
        tenths3 = random.randint(1, 5)

        num1 = f"0.{tenths1}"
        num2 = f"0.{tenths2}"
        num3 = f"0.{tenths3}"

        total_tenths = tenths1 + tenths2 + tenths3
        ones = total_tenths // 10
        tenths = total_tenths % 10

        result = f"{ones}.{tenths}" if ones > 0 else f"0.{tenths}"

        latex = f"{num1} + {num2} + {num3}"
        solution = result
        steps = [
            f"{num1} + {num2} + {num3}",
            f"\\text{{{{Add tenths: }}}} {tenths1} + {tenths2} + {tenths3} = {total_tenths}",
            f"{total_tenths} \\text{{{{ tenths = }}}} {result}",
            result
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = AddingDecimalsIntroGenerator()

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
