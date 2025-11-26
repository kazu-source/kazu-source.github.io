"""
Subtracting Decimals (Hundredths) Generator - Grade 5 Unit 3
Generates problems subtracting decimals in hundredths
Example: 5.67 - 2.34 = 3.33
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SubtractingDecimalsHundredthsGenerator:
    """Generates subtracting decimals (hundredths) problems."""

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
        """Generate easy problems: subtract hundredths, no regrouping."""
        ones1 = random.randint(3, 8)
        tenths1 = random.randint(5, 9)
        hundredths1 = random.randint(5, 9)

        ones2 = random.randint(1, ones1 - 1)
        tenths2 = random.randint(1, tenths1)
        hundredths2 = random.randint(1, hundredths1)

        num1 = f"{ones1}.{tenths1}{hundredths1}"
        num2 = f"{ones2}.{tenths2}{hundredths2}"
        result = f"{ones1 - ones2}.{tenths1 - tenths2}{hundredths1 - hundredths2}"

        latex = f"{num1} - {num2}"
        solution = result
        steps = [
            f"{num1} - {num2}",
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
        ones1 = random.randint(5, 12)
        tenths1 = random.randint(0, 9)
        hundredths1 = random.randint(0, 9)

        ones2 = random.randint(1, ones1 - 1)
        tenths2 = random.randint(0, 9)
        hundredths2 = random.randint(0, 9)

        num1 = f"{ones1}.{tenths1}{hundredths1}"
        num2 = f"{ones2}.{tenths2}{hundredths2}"

        result = round(ones1 + tenths1/10 + hundredths1/100 - ones2 - tenths2/10 - hundredths2/100, 2)

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
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: subtract larger decimals."""
        ones1 = random.randint(20, 60)
        decimal1 = random.randint(10, 99)

        ones2 = random.randint(5, ones1 - 1)
        decimal2 = random.randint(10, 99)

        num1 = f"{ones1}.{decimal1}"
        num2 = f"{ones2}.{decimal2}"

        result = round(ones1 + decimal1/100 - ones2 - decimal2/100, 2)

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
        """Generate challenge problems: subtract with different decimal places."""
        ones1 = random.randint(15, 40)
        tenths1 = random.randint(0, 9)
        hundredths1 = random.randint(1, 9)

        ones2 = random.randint(5, ones1 - 2)
        tenths2 = random.randint(0, 9)

        num1 = f"{ones1}.{tenths1}{hundredths1}"
        num2 = f"{ones2}.{tenths2}"

        result = round(ones1 + tenths1/10 + hundredths1/100 - ones2 - tenths2/10, 2)

        latex = f"{num1} - {num2}"
        solution = str(result)
        steps = [
            f"{num1} - {num2}",
            f"{num1} - {num2}0",
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
    generator = SubtractingDecimalsHundredthsGenerator()

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
