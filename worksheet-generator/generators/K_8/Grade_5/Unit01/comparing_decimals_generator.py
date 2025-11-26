"""
Comparing Decimals Generator - Grade 5 Unit 1
Generates problems comparing decimal numbers
Example: Which is greater: 0.45 or 0.5?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingDecimalsGenerator:
    """Generates comparing decimals problems."""

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
        """Generate easy problems: compare tenths."""
        tenths1 = random.randint(1, 9)
        tenths2 = random.randint(1, 9)
        while tenths2 == tenths1:
            tenths2 = random.randint(1, 9)

        decimal1 = f"0.{tenths1}"
        decimal2 = f"0.{tenths2}"

        if tenths1 > tenths2:
            symbol = ">"
        else:
            symbol = "<"

        latex = f"\\text{{{{Compare: }}}} {decimal1} \\quad \\text{{{{and}}}} \\quad {decimal2}"
        solution = f"{decimal1} {symbol} {decimal2}"
        steps = [
            f"\\text{{{{Compare tenths place: }}}} {tenths1} \\text{{{{ vs }}}} {tenths2}",
            f"{decimal1} {symbol} {decimal2}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: compare hundredths."""
        tenths1 = random.randint(1, 8)
        hundredths1 = random.randint(0, 9)

        tenths2 = tenths1
        hundredths2 = random.randint(0, 9)
        while hundredths2 == hundredths1:
            hundredths2 = random.randint(0, 9)

        decimal1 = f"0.{tenths1}{hundredths1}"
        decimal2 = f"0.{tenths2}{hundredths2}"

        if hundredths1 > hundredths2:
            symbol = ">"
        else:
            symbol = "<"

        latex = f"\\text{{{{Compare: }}}} {decimal1} \\quad \\text{{{{and}}}} \\quad {decimal2}"
        solution = f"{decimal1} {symbol} {decimal2}"
        steps = [
            f"\\text{{{{Tenths are equal: }}}} {tenths1} = {tenths2}",
            f"\\text{{{{Compare hundredths: }}}} {hundredths1} \\text{{{{ vs }}}} {hundredths2}",
            f"{decimal1} {symbol} {decimal2}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: compare decimals with different numbers of places."""
        tenths1 = random.randint(2, 7)
        decimal1 = f"0.{tenths1}"

        tenths2 = tenths1
        hundredths2 = random.randint(1, 9)
        decimal2 = f"0.{tenths2}{hundredths2}"

        symbol = "<"

        latex = f"\\text{{{{Compare: }}}} {decimal1} \\quad \\text{{{{and}}}} \\quad {decimal2}"
        solution = f"{decimal1} {symbol} {decimal2}"
        steps = [
            f"{decimal1} = 0.{tenths1}0",
            f"\\text{{{{Compare: }}}} 0.{tenths1}0 \\text{{{{ and }}}} 0.{tenths2}{hundredths2}",
            f"0 < {hundredths2} \\text{{{{ in hundredths place}}}}",
            f"{decimal1} {symbol} {decimal2}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: order three decimals."""
        # Generate three different decimals
        decimals = []
        values = []

        for _ in range(3):
            tenths = random.randint(2, 7)
            hundredths = random.randint(0, 9)
            if random.choice([True, False]) and hundredths != 0:
                decimal = f"0.{tenths}{hundredths}"
                value = tenths * 10 + hundredths
            else:
                decimal = f"0.{tenths}"
                value = tenths * 10
            decimals.append(decimal)
            values.append(value)

        # Make sure they're all different
        while len(set(values)) < 3:
            tenths = random.randint(2, 7)
            hundredths = random.randint(0, 9)
            if random.choice([True, False]) and hundredths != 0:
                decimal = f"0.{tenths}{hundredths}"
                value = tenths * 10 + hundredths
            else:
                decimal = f"0.{tenths}"
                value = tenths * 10
            decimals[2] = decimal
            values[2] = value

        # Sort
        sorted_pairs = sorted(zip(values, decimals))
        sorted_decimals = [d for v, d in sorted_pairs]

        latex = f"\\text{{{{Order from least to greatest: }}}} {decimals[0]}, {decimals[1]}, {decimals[2]}"
        solution = f"{sorted_decimals[0]} < {sorted_decimals[1]} < {sorted_decimals[2]}"
        steps = [
            f"\\text{{{{Compare all three decimals}}}}",
            f"{sorted_decimals[0]} < {sorted_decimals[1]} < {sorted_decimals[2]}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ComparingDecimalsGenerator()

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
