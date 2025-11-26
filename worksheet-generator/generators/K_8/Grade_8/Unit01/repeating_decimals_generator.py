"""
Repeating Decimals Generator - Grade 8 Unit 1
Generates problems converting between fractions and repeating decimals
Example: Convert 1/3 to decimal, or identify 0.333... as a fraction
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RepeatingDecimalsGenerator:
    """Generates repeating decimals problems."""

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
        """Generate easy problems: simple repeating decimals like 1/3, 2/3, 1/9."""
        fractions = [
            (1, 3, "0.\\overline{3}"),
            (2, 3, "0.\\overline{6}"),
            (1, 9, "0.\\overline{1}"),
            (2, 9, "0.\\overline{2}"),
            (1, 6, "0.1\\overline{6}")
        ]

        numerator, denominator, decimal = random.choice(fractions)

        if random.choice([True, False]):
            # Fraction to decimal
            latex = f"\\text{{Convert to decimal: }} \\frac{{{numerator}}}{{{denominator}}}"
            solution = decimal
            steps = [f"\\frac{{{numerator}}}{{{denominator}}} = {decimal}"]
        else:
            # Decimal to fraction
            latex = f"\\text{{Convert to fraction: }} {decimal}"
            solution = f"\\frac{{{numerator}}}{{{denominator}}}"
            steps = [f"{decimal} = \\frac{{{numerator}}}{{{denominator}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: more complex repeating decimals."""
        fractions = [
            (1, 11, "0.\\overline{09}"),
            (2, 11, "0.\\overline{18}"),
            (5, 6, "0.8\\overline{3}"),
            (4, 9, "0.\\overline{4}"),
            (5, 9, "0.\\overline{5}"),
            (7, 9, "0.\\overline{7}"),
            (8, 9, "0.\\overline{8}")
        ]

        numerator, denominator, decimal = random.choice(fractions)

        if random.choice([True, False]):
            latex = f"\\text{{Convert to decimal: }} \\frac{{{numerator}}}{{{denominator}}}"
            solution = decimal
            steps = [f"\\text{{Divide {numerator} by {denominator}}}", f"\\frac{{{numerator}}}{{{denominator}}} = {decimal}"]
        else:
            latex = f"\\text{{Convert to fraction: }} {decimal}"
            solution = f"\\frac{{{numerator}}}{{{denominator}}}"
            steps = [f"{decimal} = \\frac{{{numerator}}}{{{denominator}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: identifying patterns in repeating decimals."""
        problems = [
            {
                "question": "\\text{What is the 100th digit after the decimal point in } 0.\\overline{123}?",
                "solution": "2",
                "steps": ["\\text{Pattern repeats every 3 digits: 123}", "\\text{100 ÷ 3 = 33 remainder 1}", "\\text{The 100th digit is the 1st digit of the pattern: 2}"]
            },
            {
                "question": "\\text{What is the 50th digit after the decimal point in } 0.\\overline{12}?",
                "solution": "2",
                "steps": ["\\text{Pattern repeats every 2 digits: 12}", "\\text{50 ÷ 2 = 25 remainder 0}", "\\text{The 50th digit is the last digit of the pattern: 2}"]
            },
            {
                "question": "\\text{Express } 0.\\overline{27} \\text{ as a fraction}",
                "solution": "\\frac{3}{11}",
                "steps": ["\\text{Let x = 0.272727...}", "100x = 27.272727...", "100x - x = 27", "99x = 27", "x = \\frac{27}{99} = \\frac{3}{11}"]
            }
        ]

        problem = random.choice(problems)

        return Equation(
            latex=problem["question"],
            solution=problem["solution"],
            steps=problem["steps"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: converting complex repeating decimals to fractions."""
        problems = [
            {
                "question": "\\text{Express } 0.1\\overline{6} \\text{ as a fraction in simplest form}",
                "solution": "\\frac{1}{6}",
                "steps": [
                    "\\text{Let x = 0.1666...}",
                    "10x = 1.666...",
                    "100x = 16.666...",
                    "100x - 10x = 15",
                    "90x = 15",
                    "x = \\frac{15}{90} = \\frac{1}{6}"
                ]
            },
            {
                "question": "\\text{Express } 0.\\overline{54} \\text{ as a fraction in simplest form}",
                "solution": "\\frac{6}{11}",
                "steps": [
                    "\\text{Let x = 0.545454...}",
                    "100x = 54.545454...",
                    "100x - x = 54",
                    "99x = 54",
                    "x = \\frac{54}{99} = \\frac{6}{11}"
                ]
            },
            {
                "question": "\\text{Express } 0.8\\overline{3} \\text{ as a fraction in simplest form}",
                "solution": "\\frac{5}{6}",
                "steps": [
                    "\\text{Let x = 0.8333...}",
                    "10x = 8.333...",
                    "100x = 83.333...",
                    "100x - 10x = 75",
                    "90x = 75",
                    "x = \\frac{75}{90} = \\frac{5}{6}"
                ]
            }
        ]

        problem = random.choice(problems)

        return Equation(
            latex=problem["question"],
            solution=problem["solution"],
            steps=problem["steps"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = RepeatingDecimalsGenerator()

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
