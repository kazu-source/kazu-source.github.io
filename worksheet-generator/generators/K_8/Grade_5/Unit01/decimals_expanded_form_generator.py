"""
Decimals Expanded Form Generator - Grade 5 Unit 1
Generates problems writing decimals in expanded form
Example: Write 3.45 in expanded form: 3 + 0.4 + 0.05
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DecimalsExpandedFormGenerator:
    """Generates decimals in expanded form problems."""

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
        """Generate easy problems: expand single digit with tenths."""
        ones = random.randint(1, 9)
        tenths = random.randint(1, 9)

        number = f"{ones}.{tenths}"

        latex = f"\\text{{{{Write in expanded form: }}}} {number}"
        solution = f"{ones} + 0.{tenths}"
        steps = [
            f"{number}",
            f"{ones} + 0.{tenths}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: expand with hundredths."""
        ones = random.randint(1, 9)
        tenths = random.randint(0, 9)
        hundredths = random.randint(1, 9)

        number = f"{ones}.{tenths}{hundredths}"

        latex = f"\\text{{{{Write in expanded form: }}}} {number}"

        if tenths == 0:
            solution = f"{ones} + 0.0{hundredths}"
            steps = [
                f"{number}",
                f"{ones} + 0.0{hundredths}"
            ]
        else:
            solution = f"{ones} + 0.{tenths} + 0.0{hundredths}"
            steps = [
                f"{number}",
                f"{ones} + 0.{tenths} + 0.0{hundredths}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: convert from expanded form to standard form."""
        ones = random.randint(1, 9)
        tenths = random.randint(1, 9)
        hundredths = random.randint(1, 9)

        expanded = f"{ones} + 0.{tenths} + 0.0{hundredths}"
        number = f"{ones}.{tenths}{hundredths}"

        latex = f"\\text{{{{Write in standard form: }}}} {expanded}"
        solution = number
        steps = [
            expanded,
            f"= {number}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: expanded form with fractions."""
        ones = random.randint(2, 9)
        tenths = random.randint(1, 9)
        hundredths = random.randint(1, 9)

        number = f"{ones}.{tenths}{hundredths}"

        latex = f"\\text{{{{Write in expanded form using fractions: }}}} {number}"
        solution = f"{ones} + \\frac{{{tenths}}}{{10}} + \\frac{{{hundredths}}}{{100}}"
        steps = [
            f"{number}",
            f"{ones} + \\frac{{{tenths}}}{{10}} + \\frac{{{hundredths}}}{{100}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = DecimalsExpandedFormGenerator()

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
