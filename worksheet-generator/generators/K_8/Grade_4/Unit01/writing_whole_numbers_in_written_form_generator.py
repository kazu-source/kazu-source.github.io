"""
Writing Whole Numbers in Written Form Generator - Grade 4 Unit 1
Generates problems on writing numbers in word form
Example: Write 3,527 in words: three thousand, five hundred twenty-seven
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class WritingWholeNumbersInWrittenFormGenerator:
    """Generates written form problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def _number_to_words(self, n: int) -> str:
        """Convert a number to words."""
        ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

        if n == 0:
            return 'zero'

        def convert_hundreds(num):
            result = []
            h = num // 100
            if h > 0:
                result.append(f"{ones[h]} hundred")

            remainder = num % 100
            if remainder >= 20:
                t = remainder // 10
                o = remainder % 10
                if o > 0:
                    result.append(f"{tens[t]}-{ones[o]}")
                else:
                    result.append(tens[t])
            elif remainder >= 10:
                result.append(teens[remainder - 10])
            elif remainder > 0:
                result.append(ones[remainder])

            return ' '.join(result)

        parts = []

        # Millions
        if n >= 1000000:
            millions = n // 1000000
            parts.append(f"{convert_hundreds(millions)} million")
            n %= 1000000

        # Thousands
        if n >= 1000:
            thousands = n // 1000
            parts.append(f"{convert_hundreds(thousands)} thousand")
            n %= 1000

        # Hundreds
        if n > 0:
            parts.append(convert_hundreds(n))

        return ', '.join(parts) if len(parts) > 1 else parts[0] if parts else 'zero'

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
        """Generate easy problems: 2-3 digit numbers."""
        number = random.randint(10, 999)
        words = self._number_to_words(number)

        latex = f"\\text{{Write }} {number:,} \\text{{ in words}}"
        solution = words

        steps = [
            f"\\text{{Number: }} {number:,}",
            f"\\text{{Words: }} {words}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 4-digit numbers."""
        number = random.randint(1000, 9999)
        words = self._number_to_words(number)

        latex = f"\\text{{Write }} {number:,} \\text{{ in words}}"
        solution = words

        steps = [
            f"\\text{{Number: }} {number:,}",
            f"\\text{{Words: }} {words}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 5-6 digit numbers."""
        number = random.randint(10000, 999999)
        words = self._number_to_words(number)

        latex = f"\\text{{Write }} {number:,} \\text{{ in words}}"
        solution = words

        steps = [
            f"\\text{{Number: }} {number:,}",
            f"\\text{{Words: }} {words}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: reverse - words to numbers."""
        number = random.randint(1000, 99999)
        words = self._number_to_words(number)

        latex = f"\\text{{Write the number: }} {words}"
        solution = f"{number:,}"

        steps = [
            f"\\text{{Words: }} {words}",
            f"\\text{{Number: }} {number:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = WritingWholeNumbersInWrittenFormGenerator()

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
