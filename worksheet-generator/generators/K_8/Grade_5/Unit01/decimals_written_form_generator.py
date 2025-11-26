"""
Decimals Written Form Generator - Grade 5 Unit 1
Generates problems writing decimals in word form
Example: Write 3.45 in words: Three and forty-five hundredths
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DecimalsWrittenFormGenerator:
    """Generates decimals in written form problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

        self.ones_words = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                     'sixteen', 'seventeen', 'eighteen', 'nineteen']
        self.tens_words = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

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

    def _number_to_words(self, n):
        """Convert a number 0-99 to words."""
        if n < 10:
            return self.ones_words[n]
        elif n < 20:
            return self.teens[n - 10]
        else:
            tens = n // 10
            ones = n % 10
            if ones == 0:
                return self.tens_words[tens]
            return f"{self.tens_words[tens]}-{self.ones_words[ones]}"

    def _generate_easy(self) -> Equation:
        """Generate easy problems: write tenths in words."""
        ones = random.randint(1, 9)
        tenths = random.randint(1, 9)

        number = f"{ones}.{tenths}"

        ones_word = self.ones_words[ones].capitalize()
        tenths_word = self.ones_words[tenths]

        latex = f"\\text{{{{Write in words: }}}} {number}"
        solution = f"\\text{{{{{ones_word} and {tenths_word} tenths}}}}"
        steps = [
            f"{number}",
            f"\\text{{{{{ones_word} and {tenths_word} tenths}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: write hundredths in words."""
        ones = random.randint(1, 9)
        tenths = random.randint(0, 9)
        hundredths = random.randint(1, 9)

        number = f"{ones}.{tenths}{hundredths}"
        decimal_part = int(f"{tenths}{hundredths}")

        ones_word = self.ones_words[ones].capitalize()
        decimal_word = self._number_to_words(decimal_part)

        latex = f"\\text{{{{Write in words: }}}} {number}"
        solution = f"\\text{{{{{ones_word} and {decimal_word} hundredths}}}}"
        steps = [
            f"{number}",
            f"\\text{{{{{ones_word} and {decimal_word} hundredths}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: convert from words to number."""
        ones = random.randint(2, 9)
        tenths = random.randint(1, 9)
        hundredths = random.randint(0, 9)

        number = f"{ones}.{tenths}{hundredths}"
        decimal_part = int(f"{tenths}{hundredths}")

        ones_word = self.ones_words[ones].capitalize()
        decimal_word = self._number_to_words(decimal_part)

        words = f"{ones_word} and {decimal_word} hundredths"

        latex = f"\\text{{{{Write as a decimal: {words}}}}}"
        solution = number
        steps = [
            f"\\text{{{words}}}",
            f"{number}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: write larger numbers with decimals."""
        tens = random.randint(1, 9)
        ones = random.randint(0, 9)
        tenths = random.randint(1, 9)
        hundredths = random.randint(1, 9)

        whole_part = tens * 10 + ones
        number = f"{whole_part}.{tenths}{hundredths}"
        decimal_part = int(f"{tenths}{hundredths}")

        whole_word = self._number_to_words(whole_part).capitalize()
        decimal_word = self._number_to_words(decimal_part)

        latex = f"\\text{{{{Write in words: }}}} {number}"
        solution = f"\\text{{{{{whole_word} and {decimal_word} hundredths}}}}"
        steps = [
            f"{number}",
            f"\\text{{{{{whole_word} and {decimal_word} hundredths}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = DecimalsWrittenFormGenerator()

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
