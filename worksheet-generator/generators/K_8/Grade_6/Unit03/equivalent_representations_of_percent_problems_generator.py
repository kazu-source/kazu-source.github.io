"""
Equivalent Representations of Percent Problems Generator - Grade 6 Unit 3
Generates problems converting between fractions, decimals, and percents
Example: Express 0.45 as a percent and a fraction
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EquivalentRepresentationsOfPercentProblemsGenerator:
    """Generates equivalent representations problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
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
        """Generate easy problems: common percents to fractions and decimals."""
        representations = [
            (25, "\\frac{1}{4}", "0.25"),
            (50, "\\frac{1}{2}", "0.5"),
            (75, "\\frac{3}{4}", "0.75"),
            (10, "\\frac{1}{10}", "0.1"),
            (20, "\\frac{1}{5}", "0.2")
        ]

        percent, fraction, decimal = random.choice(representations)

        if random.choice([True, False]):
            latex = f"\\text{{Express {percent}\\% as a fraction and decimal.}}"
            solution = f"{fraction} \\text{{ and }} {decimal}"
        else:
            latex = f"\\text{{Express {decimal} as a percent and fraction.}}"
            solution = f"{percent}\\% \\text{{ and }} {fraction}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{percent}\\% = {fraction} = {decimal}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: less common conversions."""
        from math import gcd

        # Generate a simple fraction
        numerators = [1, 2, 3, 4, 6, 7, 8, 9]
        denominators = [5, 8, 10, 20, 25]

        num = random.choice(numerators)
        denom = random.choice(denominators)

        # Simplify
        g = gcd(num, denom)
        num = num // g
        denom = denom // g

        decimal = num / denom
        percent = decimal * 100

        latex = f"\\text{{Express }} \\frac{{{num}}}{{{denom}}} \\text{{ as a decimal and percent.}}"
        solution = f"{decimal} \\text{{ and }} {percent:.0f}\\%"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\frac{{{num}}}{{{denom}}} = {num} \\div {denom} = {decimal}",
                f"{decimal} \\times 100 = {percent:.0f}\\%"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: three-way conversions with non-terminating decimals."""
        representations = [
            ("\\frac{1}{3}", "0.\\overline{3}", "33.\\overline{3}"),
            ("\\frac{2}{3}", "0.\\overline{6}", "66.\\overline{6}"),
            ("\\frac{1}{6}", "0.1\\overline{6}", "16.\\overline{6}"),
            ("\\frac{5}{6}", "0.8\\overline{3}", "83.\\overline{3}")
        ]

        fraction, decimal, percent = random.choice(representations)

        latex = f"\\text{{Express }} {fraction} \\text{{ as a decimal and percent (use repeating decimal notation).}}"
        solution = f"{decimal} \\text{{ and }} {percent}\\%"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{fraction} = {decimal}",
                f"{decimal} = {percent}\\%"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: ordering mixed representations."""
        # Create 4 different representations
        values = []

        # Add a percent
        percent1 = random.randint(30, 80)
        values.append((percent1 / 100, f"{percent1}\\%"))

        # Add a decimal
        decimal1 = round(random.uniform(0.2, 0.9), 2)
        values.append((decimal1, str(decimal1)))

        # Add a fraction
        fractions = [(1, 4, 0.25), (3, 4, 0.75), (2, 5, 0.4), (3, 5, 0.6), (4, 5, 0.8)]
        num, denom, dec_val = random.choice(fractions)
        values.append((dec_val, f"\\frac{{{num}}}{{{denom}}}"))

        # Add another percent
        percent2 = random.randint(20, 90)
        while abs(percent2 - percent1) < 10:
            percent2 = random.randint(20, 90)
        values.append((percent2 / 100, f"{percent2}\\%"))

        # Sort by value
        values.sort(key=lambda x: x[0])
        ordered = ", ".join([v[1] for v in values])

        latex = f"\\text{{Order from least to greatest: {values[2][1]}, {values[0][1]}, {values[3][1]}, {values[1][1]}}}"
        solution = ordered

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Ordered: }} {ordered}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = EquivalentRepresentationsOfPercentProblemsGenerator()

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
