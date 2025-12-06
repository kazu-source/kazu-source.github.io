"""
Rounding Whole Numbers Generator - Grade 4 Unit 2
Generates problems on rounding whole numbers to various place values
Example: Round 4,527 to the nearest hundred
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RoundingWholeNumbersGenerator:
    """Generates rounding whole numbers problems."""

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
        """Generate easy problems: round 3-digit numbers to nearest 10."""
        number = random.randint(100, 999)
        ones = number % 10

        if ones < 5:
            rounded = (number // 10) * 10
        else:
            rounded = ((number // 10) + 1) * 10

        latex = f"\\text{{Round }} {number:,} \\text{{ to the nearest 10}}"
        solution = str(rounded)

        steps = [
            f"\\text{{Look at the ones digit: }} {ones}",
            f"\\text{{Since }} {ones} {'\\lt 5' if ones < 5 else '\\geq 5'}, \\text{{ round }} {'down' if ones < 5 else 'up'}",
            f"{number:,} \\text{{ rounds to }} {rounded:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: round 4-digit numbers to nearest 10, 100, or 1000."""
        number = random.randint(1000, 9999)
        round_to = random.choice([10, 100, 1000])

        if round_to == 10:
            key_digit = number % 10
            if key_digit < 5:
                rounded = (number // 10) * 10
            else:
                rounded = ((number // 10) + 1) * 10
        elif round_to == 100:
            key_digit = (number // 10) % 10
            if key_digit < 5:
                rounded = (number // 100) * 100
            else:
                rounded = ((number // 100) + 1) * 100
        else:  # 1000
            key_digit = (number // 100) % 10
            if key_digit < 5:
                rounded = (number // 1000) * 1000
            else:
                rounded = ((number // 1000) + 1) * 1000

        latex = f"\\text{{Round }} {number:,} \\text{{ to the nearest }} {round_to:,}"
        solution = f"{rounded:,}"

        steps = [
            f"\\text{{Key digit: }} {key_digit}",
            f"\\text{{Round }} {'down' if key_digit < 5 else 'up'}",
            f"{number:,} \\text{{ rounds to }} {rounded:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: round 5-6 digit numbers."""
        number = random.randint(10000, 999999)
        round_to = random.choice([10, 100, 1000, 10000])

        # Calculate rounding
        key_position = round_to // 10
        key_digit = (number // key_position) % 10

        if key_digit < 5:
            rounded = (number // round_to) * round_to
        else:
            rounded = ((number // round_to) + 1) * round_to

        latex = f"\\text{{Round }} {number:,} \\text{{ to the nearest }} {round_to:,}"
        solution = f"{rounded:,}"

        steps = [
            f"\\text{{Number: }} {number:,}",
            f"\\text{{Rounded: }} {rounded:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: word problems with rounding."""
        number = random.randint(1500, 9999)
        round_to = random.choice([10, 100, 1000])

        contexts = [
            f"A stadium has {number:,} seats. Round to the nearest {round_to:,}",
            f"A school has {number:,} books. Round to the nearest {round_to:,}",
            f"A store sold {number:,} items. Round to the nearest {round_to:,}",
            f"A town has {number:,} people. Round to the nearest {round_to:,}"
        ]

        context = random.choice(contexts)

        # Calculate rounding
        key_position = round_to // 10
        key_digit = (number // key_position) % 10

        if key_digit < 5:
            rounded = (number // round_to) * round_to
        else:
            rounded = ((number // round_to) + 1) * round_to

        latex = f"\\text{{{context}}}"
        solution = f"{rounded:,}"

        steps = [
            f"\\text{{Number: }} {number:,}",
            f"\\text{{Round to nearest }} {round_to:,}",
            f"\\text{{Rounded: }} {rounded:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = RoundingWholeNumbersGenerator()

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
