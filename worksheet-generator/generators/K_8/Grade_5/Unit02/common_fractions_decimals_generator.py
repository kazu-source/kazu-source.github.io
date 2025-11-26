"""
Common Fractions and Decimals Generator - Grade 5 Unit 2
Generates problems converting between common fractions and decimals
Example: Write 1/2 as a decimal: 0.5
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CommonFractionsDecimalsGenerator:
    """Generates common fractions and decimals problems."""

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
        """Generate easy problems: convert simple fractions to decimals."""
        fractions = [
            (1, 2, "0.5"),
            (1, 4, "0.25"),
            (3, 4, "0.75"),
            (1, 5, "0.2"),
            (2, 5, "0.4")
        ]

        num, den, decimal = random.choice(fractions)

        latex = f"\\text{{{{Write as a decimal: }}}} \\frac{{{num}}}{{{den}}}"
        solution = decimal
        steps = [
            f"\\frac{{{num}}}{{{den}}}",
            f"{decimal}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: convert decimals to fractions."""
        decimals = [
            ("0.5", 1, 2),
            ("0.25", 1, 4),
            ("0.75", 3, 4),
            ("0.2", 1, 5),
            ("0.4", 2, 5),
            ("0.6", 3, 5),
            ("0.8", 4, 5)
        ]

        decimal, num, den = random.choice(decimals)

        latex = f"\\text{{{{Write as a simplified fraction: }}}} {decimal}"
        solution = f"\\frac{{{num}}}{{{den}}}"
        steps = [
            f"{decimal}",
            f"\\frac{{{num}}}{{{den}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: convert less common fractions."""
        fractions = [
            (1, 8, "0.125"),
            (3, 8, "0.375"),
            (5, 8, "0.625"),
            (7, 8, "0.875"),
            (1, 10, "0.1"),
            (3, 10, "0.3"),
            (7, 10, "0.7"),
            (9, 10, "0.9")
        ]

        num, den, decimal = random.choice(fractions)

        problem_type = random.choice(['to_decimal', 'to_fraction'])

        if problem_type == 'to_decimal':
            latex = f"\\text{{{{Write as a decimal: }}}} \\frac{{{num}}}{{{den}}}"
            solution = decimal
            steps = [
                f"\\frac{{{num}}}{{{den}}}",
                f"{decimal}"
            ]
        else:
            latex = f"\\text{{{{Write as a simplified fraction: }}}} {decimal}"
            solution = f"\\frac{{{num}}}{{{den}}}"
            steps = [
                f"{decimal}",
                f"\\frac{{{num}}}{{{den}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: compare fraction and decimal."""
        fractions = [
            (1, 2, 0.5),
            (1, 4, 0.25),
            (3, 4, 0.75),
            (1, 5, 0.2),
            (2, 5, 0.4),
            (3, 5, 0.6),
            (4, 5, 0.8),
            (1, 8, 0.125),
            (3, 8, 0.375)
        ]

        num, den, frac_decimal = random.choice(fractions)

        # Generate a decimal close to but different from the fraction
        if random.choice([True, False]):
            compare_decimal = round(frac_decimal + random.choice([0.05, 0.1, -0.05, -0.1]), 2)
        else:
            compare_decimal = round(frac_decimal + random.choice([0.15, 0.2, -0.15, -0.2]), 2)

        if compare_decimal < 0:
            compare_decimal = abs(compare_decimal)

        if frac_decimal > compare_decimal:
            symbol = ">"
        elif frac_decimal < compare_decimal:
            symbol = "<"
        else:
            symbol = "="

        latex = f"\\text{{{{Compare: }}}} \\frac{{{num}}}{{{den}}} \\quad \\text{{{{and}}}} \\quad {compare_decimal}"
        solution = f"\\frac{{{num}}}{{{den}}} {symbol} {compare_decimal}"
        steps = [
            f"\\frac{{{num}}}{{{den}}} = {frac_decimal}",
            f"{frac_decimal} {symbol} {compare_decimal}",
            f"\\frac{{{num}}}{{{den}}} {symbol} {compare_decimal}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = CommonFractionsDecimalsGenerator()

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
