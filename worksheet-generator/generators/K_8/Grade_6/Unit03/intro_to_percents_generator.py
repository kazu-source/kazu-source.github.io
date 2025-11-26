"""
Intro to Percents Generator - Grade 6 Unit 3
Generates problems introducing percent concepts
Example: What is 50% expressed as a fraction?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IntroToPercentsGenerator:
    """Generates intro to percents problems."""

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
        """Generate easy problems: simple percents to fractions."""
        percents = [25, 50, 75, 10, 20, 30, 40, 60, 70, 80, 90, 100]
        percent = random.choice(percents)

        # Simplify the fraction
        from math import gcd
        g = gcd(percent, 100)
        numerator = percent // g
        denominator = 100 // g

        latex = f"\\text{{Express {percent}\\% as a fraction in simplest form.}}"
        solution = f"\\frac{{{numerator}}}{{{denominator}}}" if denominator != 1 else str(numerator)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{percent}\\% = \\frac{{{percent}}}{{100}}",
                f"\\text{{Simplified: }} \\frac{{{numerator}}}{{{denominator}}}" if denominator != 1 else f"= {numerator}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: percents to decimals and vice versa."""
        if random.choice([True, False]):
            # Percent to decimal
            percent = random.choice([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 12, 38, 62, 88])
            decimal = percent / 100

            latex = f"\\text{{Convert {percent}\\% to a decimal.}}"
            solution = str(decimal)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"{percent}\\% = {percent} \\div 100 = {decimal}"
                ],
                difficulty='medium'
            )
        else:
            # Decimal to percent
            decimal = round(random.uniform(0.1, 0.99), 2)
            percent = decimal * 100

            latex = f"\\text{{Convert {decimal} to a percent.}}"
            solution = f"{percent:.0f}\\%"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"{decimal} \\times 100 = {percent:.0f}\\%"
                ],
                difficulty='medium'
            )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: fraction to percent conversions."""
        fractions = [
            (1, 4, 25), (3, 4, 75), (1, 5, 20), (2, 5, 40), (3, 5, 60), (4, 5, 80),
            (1, 2, 50), (1, 10, 10), (3, 10, 30), (7, 10, 70), (9, 10, 90)
        ]

        num, denom, percent = random.choice(fractions)

        latex = f"\\text{{Convert }} \\frac{{{num}}}{{{denom}}} \\text{{ to a percent.}}"
        solution = f"{percent}\\%"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\frac{{{num}}}{{{denom}}} = {num} \\div {denom} = {percent/100}",
                f"{percent/100} \\times 100 = {percent}\\%"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: percent greater than 100%."""
        percent = random.choice([110, 125, 150, 175, 200, 250, 300])

        # Convert to mixed number or improper fraction
        numerator = percent
        denominator = 100
        from math import gcd
        g = gcd(numerator, denominator)
        num = numerator // g
        denom = denominator // g

        latex = f"\\text{{Express {percent}\\% as a fraction or mixed number in simplest form.}}"

        if num >= denom:
            whole = num // denom
            remainder = num % denom
            if remainder == 0:
                solution = str(whole)
            else:
                solution = f"{whole}\\frac{{{remainder}}}{{{denom}}}"
        else:
            solution = f"\\frac{{{num}}}{{{denom}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{percent}\\% = \\frac{{{percent}}}{{100}} = \\frac{{{num}}}{{{denom}}}",
                f"\\text{{As mixed number: }} {solution}"
            ],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = IntroToPercentsGenerator()

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
