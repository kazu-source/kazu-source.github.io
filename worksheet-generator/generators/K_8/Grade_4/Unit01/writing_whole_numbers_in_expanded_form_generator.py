"""
Writing Whole Numbers in Expanded Form Generator - Grade 4 Unit 1
Generates problems on writing numbers in expanded form
Example: Write 3,527 in expanded form: 3,000 + 500 + 20 + 7
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class WritingWholeNumbersInExpandedFormGenerator:
    """Generates expanded form problems."""

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
        """Generate easy problems: 3-digit numbers."""
        number = random.randint(100, 999)
        digits = [int(d) for d in str(number)]

        parts = []
        if digits[0] > 0:
            parts.append(f"{digits[0] * 100}")
        if digits[1] > 0:
            parts.append(f"{digits[1] * 10}")
        if digits[2] > 0:
            parts.append(f"{digits[2]}")

        expanded = " + ".join(parts)
        latex = f"\\text{{Write }} {number:,} \\text{{ in expanded form}}"
        solution = expanded

        steps = [
            f"\\text{{Hundreds: }} {digits[0]} \\times 100 = {digits[0] * 100}",
            f"\\text{{Tens: }} {digits[1]} \\times 10 = {digits[1] * 10}",
            f"\\text{{Ones: }} {digits[2]}",
            f"\\text{{Expanded form: }} {expanded}"
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
        digits = [int(d) for d in str(number)]

        parts = []
        if digits[0] > 0:
            parts.append(f"{digits[0] * 1000:,}")
        if digits[1] > 0:
            parts.append(f"{digits[1] * 100}")
        if digits[2] > 0:
            parts.append(f"{digits[2] * 10}")
        if digits[3] > 0:
            parts.append(f"{digits[3]}")

        expanded = " + ".join(parts)
        latex = f"\\text{{Write }} {number:,} \\text{{ in expanded form}}"
        solution = expanded

        steps = [
            f"\\text{{Expanded form: }} {expanded}"
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
        num_str = str(number)
        digits = [int(d) for d in num_str]

        if len(num_str) == 5:
            multipliers = [10000, 1000, 100, 10, 1]
        else:
            multipliers = [100000, 10000, 1000, 100, 10, 1]

        parts = []
        for i, digit in enumerate(digits):
            if digit > 0:
                parts.append(f"{digit * multipliers[i]:,}")

        expanded = " + ".join(parts)
        latex = f"\\text{{Write }} {number:,} \\text{{ in expanded form}}"
        solution = expanded

        steps = [
            f"\\text{{Expanded form: }} {expanded}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: reverse - given expanded form, find number."""
        number = random.randint(1000, 99999)
        num_str = str(number)
        digits = [int(d) for d in num_str]

        if len(num_str) == 4:
            multipliers = [1000, 100, 10, 1]
        else:
            multipliers = [10000, 1000, 100, 10, 1]

        parts = []
        for i, digit in enumerate(digits):
            if digit > 0:
                parts.append(f"{digit * multipliers[i]:,}")

        expanded = " + ".join(parts)
        latex = f"\\text{{What number is represented by: }} {expanded}?"
        solution = f"{number:,}"

        steps = [
            f"\\text{{Add the parts: }} {expanded}",
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
    generator = WritingWholeNumbersInExpandedFormGenerator()

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
