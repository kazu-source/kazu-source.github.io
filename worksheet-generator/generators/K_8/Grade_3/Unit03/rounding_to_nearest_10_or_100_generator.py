"""
Rounding to Nearest 10 or 100 Generator - Grade 3 Unit 3
Generates problems for rounding numbers to the nearest 10 or 100
Uses number line concepts to help students understand rounding
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RoundingToNearest10Or100Generator:
    """Generates rounding to nearest 10 or 100 problems."""

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
        """Generate easy problems: round to nearest 10 (numbers 10-99)."""
        # Generate number with clear rounding (0-4 or 5-9 in ones place)
        tens = random.randint(1, 9)
        ones = random.choice([1, 2, 3, 6, 7, 8])  # Clear rounding
        number = tens * 10 + ones

        if ones < 5:
            rounded = tens * 10
        else:
            rounded = (tens + 1) * 10

        latex = f"\\text{{Round }} {number} \\text{{ to the nearest 10}}"
        solution = str(rounded)

        steps = [
            f"\\text{{The number }} {number} \\text{{ is between }} {tens * 10} \\text{{ and }} {(tens + 1) * 10}",
            f"\\text{{The ones digit is }} {ones}",
            f"\\text{{Since }} {ones} {'< 5' if ones < 5 else '\\geq 5'}, \\text{{ round }} {'down' if ones < 5 else 'up'}",
            f"{number} \\text{{ rounds to }} {rounded}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: round to nearest 10 or 100 (numbers 10-999)."""
        round_to = random.choice([10, 100])

        if round_to == 10:
            number = random.randint(10, 999)
            ones = number % 10

            if ones < 5:
                rounded = (number // 10) * 10
            else:
                rounded = ((number // 10) + 1) * 10

            steps = [
                f"\\text{{Look at the ones digit: }} {ones}",
                f"\\text{{Since }} {ones} {'< 5' if ones < 5 else '\\geq 5'}, \\text{{ round }} {'down' if ones < 5 else 'up'}",
                f"{number} \\text{{ rounds to }} {rounded}"
            ]
        else:  # round to 100
            number = random.randint(100, 999)
            tens_digit = (number // 10) % 10

            if tens_digit < 5:
                rounded = (number // 100) * 100
            else:
                rounded = ((number // 100) + 1) * 100

            steps = [
                f"\\text{{Look at the tens digit: }} {tens_digit}",
                f"\\text{{Since }} {tens_digit} {'< 5' if tens_digit < 5 else '\\geq 5'}, \\text{{ round }} {'down' if tens_digit < 5 else 'up'}",
                f"{number} \\text{{ rounds to }} {rounded}"
            ]

        latex = f"\\text{{Round }} {number} \\text{{ to the nearest }} {round_to}"
        solution = str(rounded)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: mixed rounding with boundary cases."""
        round_to = random.choice([10, 100])

        if round_to == 10:
            # Include numbers ending in 5 (boundary case)
            tens = random.randint(1, 99)
            ones = random.choice([0, 4, 5, 6, 9])
            number = tens * 10 + ones

            if ones < 5:
                rounded = (number // 10) * 10
            else:
                rounded = ((number // 10) + 1) * 10
        else:  # round to 100
            hundreds = random.randint(1, 9)
            tens_digit = random.choice([0, 4, 5, 6, 9])
            ones_digit = random.randint(0, 9)
            number = hundreds * 100 + tens_digit * 10 + ones_digit

            if tens_digit < 5:
                rounded = (number // 100) * 100
            else:
                rounded = ((number // 100) + 1) * 100

        latex = f"\\text{{Round }} {number} \\text{{ to the nearest }} {round_to}"
        solution = str(rounded)

        key_digit = (number // (round_to // 10)) % 10
        steps = [
            f"\\text{{Identify the }} {round_to} \\text{{'s place and the digit to its right}}",
            f"\\text{{The key digit is }} {key_digit}",
            f"\\text{{Round }} {'down' if key_digit < 5 else 'up'} \\text{{ because }} {key_digit} {'< 5' if key_digit < 5 else '\\geq 5'}",
            f"{number} \\text{{ rounds to }} {rounded}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: word problems with rounding."""
        round_to = random.choice([10, 100])

        if round_to == 10:
            number = random.randint(15, 995)
            contexts = [
                f"A school has {number} students. Round to the nearest 10",
                f"The book has {number} pages. Round to the nearest 10",
                f"There are {number} people at the concert. Round to the nearest 10",
                f"The store sold {number} items. Round to the nearest 10"
            ]
        else:
            number = random.randint(150, 950)
            contexts = [
                f"A movie theater has {number} seats. Round to the nearest 100",
                f"The farm has {number} animals. Round to the nearest 100",
                f"The library has {number} books. Round to the nearest 100",
                f"The city has {number} houses. Round to the nearest 100"
            ]

        context = random.choice(contexts)

        if round_to == 10:
            ones = number % 10
            if ones < 5:
                rounded = (number // 10) * 10
            else:
                rounded = ((number // 10) + 1) * 10
        else:
            tens_digit = (number // 10) % 10
            if tens_digit < 5:
                rounded = (number // 100) * 100
            else:
                rounded = ((number // 100) + 1) * 100

        latex = f"\\text{{{context}. What is the rounded number?}}"
        solution = str(rounded)

        key_digit = (number // (round_to // 10)) % 10
        steps = [
            f"\\text{{Number to round: }} {number}",
            f"\\text{{Rounding to nearest }} {round_to}",
            f"\\text{{Key digit: }} {key_digit}",
            f"\\text{{Rounded: }} {rounded}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = RoundingToNearest10Or100Generator()

    print("Easy (Round to nearest 10):")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()

    print("\nMedium (Round to nearest 10 or 100):")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()

    print("\nHard (Boundary cases):")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()

    print("\nChallenge (Word problems):")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()


if __name__ == '__main__':
    main()
