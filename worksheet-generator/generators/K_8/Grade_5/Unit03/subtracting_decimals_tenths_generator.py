"""
Subtracting Decimals (Tenths) Generator - Grade 5 Unit 3
Generates problems subtracting decimals in tenths
Example: 5.8 - 2.3 = 3.5
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SubtractingDecimalsTenthsGenerator:
    """Generates subtracting decimals (tenths) problems."""

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
        """Generate easy problems: subtract tenths, no regrouping."""
        ones1 = random.randint(3, 8)
        tenths1 = random.randint(5, 9)
        ones2 = random.randint(1, ones1 - 1)
        tenths2 = random.randint(1, tenths1)

        num1 = f"{ones1}.{tenths1}"
        num2 = f"{ones2}.{tenths2}"
        result = f"{ones1 - ones2}.{tenths1 - tenths2}"

        latex = f"{num1} - {num2}"
        solution = result
        steps = [
            f"{num1} - {num2}",
            f"\\text{{{{Subtract ones: }}}} {ones1} - {ones2} = {ones1 - ones2}",
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
        """Generate medium problems: subtract with regrouping."""
        ones1 = random.randint(4, 9)
        tenths1 = random.randint(0, 4)
        ones2 = random.randint(1, ones1 - 1)
        tenths2 = random.randint(5, 9)

        num1 = f"{ones1}.{tenths1}"
        num2 = f"{ones2}.{tenths2}"

        result = round(ones1 + tenths1/10 - ones2 - tenths2/10, 1)

        latex = f"{num1} - {num2}"
        solution = str(result)
        steps = [
            f"{num1} - {num2}",
            f"\\text{{{{Regroup to subtract tenths}}}}",
            str(result)
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: subtract larger numbers with tenths."""
        tens1 = random.randint(2, 6)
        ones1 = random.randint(0, 9)
        tenths1 = random.randint(0, 9)

        tens2 = random.randint(1, tens1)
        ones2 = random.randint(0, 9) if tens2 < tens1 else random.randint(0, ones1)
        tenths2 = random.randint(0, 9)

        num1_val = tens1 * 10 + ones1
        num2_val = tens2 * 10 + ones2

        num1 = f"{num1_val}.{tenths1}"
        num2 = f"{num2_val}.{tenths2}"

        result = round(num1_val + tenths1/10 - num2_val - tenths2/10, 1)

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
        """Generate challenge problems: multi-step subtraction."""
        ones1 = random.randint(10, 20)
        tenths1 = random.randint(0, 9)
        ones2 = random.randint(2, 6)
        tenths2 = random.randint(0, 9)
        ones3 = random.randint(1, 5)
        tenths3 = random.randint(0, 9)

        num1 = f"{ones1}.{tenths1}"
        num2 = f"{ones2}.{tenths2}"
        num3 = f"{ones3}.{tenths3}"

        result = round(ones1 + tenths1/10 - ones2 - tenths2/10 - ones3 - tenths3/10, 1)

        latex = f"{num1} - {num2} - {num3}"
        solution = str(result)
        steps = [
            f"{num1} - {num2} - {num3}",
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
    generator = SubtractingDecimalsTenthsGenerator()

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
