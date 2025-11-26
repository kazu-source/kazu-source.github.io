"""
Decimals Different Forms Generator - Grade 5 Unit 1
Generates problems converting decimals between different forms
Example: Write 0.35 as a fraction: 35/100
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DecimalsDifferentFormsGenerator:
    """Generates decimals in different forms problems."""

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

    def _gcd(self, a, b):
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return a

    def _generate_easy(self) -> Equation:
        """Generate easy problems: convert tenths to fraction."""
        tenths = random.randint(1, 9)
        decimal = f"0.{tenths}"

        latex = f"\\text{{{{Write as a fraction: }}}} {decimal}"
        solution = f"\\frac{{{tenths}}}{{10}}"
        steps = [
            f"{decimal}",
            f"\\frac{{{tenths}}}{{10}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: convert hundredths to simplified fraction."""
        tenths = random.randint(1, 9)
        hundredths = random.randint(0, 9)

        numerator = tenths * 10 + hundredths
        denominator = 100

        decimal = f"0.{tenths}{hundredths}"

        # Simplify
        gcd = self._gcd(numerator, denominator)
        simplified_num = numerator // gcd
        simplified_den = denominator // gcd

        latex = f"\\text{{{{Write as a simplified fraction: }}}} {decimal}"
        solution = f"\\frac{{{simplified_num}}}{{{simplified_den}}}"

        if gcd > 1:
            steps = [
                f"{decimal} = \\frac{{{numerator}}}{{100}}",
                f"\\text{{{{Divide by GCD({gcd}): }}}} \\frac{{{simplified_num}}}{{{simplified_den}}}"
            ]
        else:
            steps = [
                f"{decimal} = \\frac{{{numerator}}}{{100}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: convert fraction to decimal."""
        denominators = [10, 100, 4, 5, 20, 25, 50]
        denominator = random.choice(denominators)

        if denominator == 10:
            numerator = random.randint(1, 9)
            decimal = f"0.{numerator}"
        elif denominator == 100:
            numerator = random.randint(1, 99)
            if numerator < 10:
                decimal = f"0.0{numerator}"
            else:
                decimal = f"0.{numerator}"
        elif denominator == 4:
            numerator = random.choice([1, 3])
            decimal = "0.25" if numerator == 1 else "0.75"
        elif denominator == 5:
            numerator = random.randint(1, 4)
            decimal = str(numerator * 0.2)
        elif denominator == 20:
            numerator = random.randint(1, 19)
            decimal = str(numerator / 20)
        elif denominator == 25:
            numerator = random.randint(1, 24)
            decimal = str(numerator / 25)
        else:  # 50
            numerator = random.randint(1, 49)
            decimal = str(numerator / 50)

        latex = f"\\text{{{{Write as a decimal: }}}} \\frac{{{numerator}}}{{{denominator}}}"
        solution = decimal
        steps = [
            f"\\frac{{{numerator}}}{{{denominator}}}",
            f"{decimal}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: convert between all three forms."""
        problem_type = random.choice(['expanded_to_fraction', 'fraction_to_expanded'])

        if problem_type == 'expanded_to_fraction':
            ones = random.randint(1, 5)
            tenths = random.randint(1, 9)
            hundredths = random.randint(1, 9)

            decimal_part = tenths * 10 + hundredths

            expanded = f"{ones} + 0.{tenths} + 0.0{hundredths}"

            latex = f"\\text{{{{Write as a mixed number: }}}} {expanded}"
            solution = f"{ones}\\frac{{{decimal_part}}}{{100}}"
            steps = [
                expanded,
                f"= {ones}.{tenths}{hundredths}",
                f"= {ones}\\frac{{{decimal_part}}}{{100}}"
            ]
        else:
            ones = random.randint(1, 5)
            numerator = random.randint(1, 99)

            if numerator < 10:
                decimal = f"{ones}.0{numerator}"
            else:
                decimal = f"{ones}.{numerator}"

            latex = f"\\text{{{{Write in expanded form: }}}} {ones}\\frac{{{numerator}}}{{100}}"
            solution = f"{ones} + \\frac{{{numerator}}}{{100}}"
            steps = [
                f"{ones}\\frac{{{numerator}}}{{100}}",
                f"= {decimal}",
                f"= {ones} + \\frac{{{numerator}}}{{100}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = DecimalsDifferentFormsGenerator()

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
