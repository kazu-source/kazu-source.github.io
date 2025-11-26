"""
Powers of Fractions and Decimals Generator - Grade 6 Unit 4
Generates problems evaluating powers of fractions and decimals
Example: Evaluate (1/2)^3
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PowersOfFractionsAndDecimalsGenerator:
    """Generates powers of fractions and decimals problems."""

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
        """Generate easy problems: simple fractions squared."""
        fractions = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4)]
        num, denom = random.choice(fractions)

        result_num = num ** 2
        result_denom = denom ** 2

        latex = f"\\text{{Evaluate: }} \\left(\\frac{{{num}}}{{{denom}}}\\right)^{{2}}"
        solution = f"\\frac{{{result_num}}}{{{result_denom}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\left(\\frac{{{num}}}{{{denom}}}\\right)^{{2}} = \\frac{{{num}^{{2}}}}{{{denom}^{{2}}}} = \\frac{{{result_num}}}{{{result_denom}}}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: decimals squared."""
        decimals = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        decimal = random.choice(decimals)

        result = decimal ** 2

        latex = f"\\text{{Evaluate: }} {decimal}^{{2}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{decimal}^{{2}} = {decimal} \\times {decimal} = {result}"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: fractions cubed."""
        fractions = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5), (2, 5)]
        num, denom = random.choice(fractions)

        result_num = num ** 3
        result_denom = denom ** 3

        latex = f"\\text{{Evaluate: }} \\left(\\frac{{{num}}}{{{denom}}}\\right)^{{3}}"
        solution = f"\\frac{{{result_num}}}{{{result_denom}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\left(\\frac{{{num}}}{{{denom}}}\\right)^{{3}} = \\frac{{{num}^{{3}}}}{{{denom}^{{3}}}} = \\frac{{{result_num}}}{{{result_denom}}}"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: comparing or operating on powers."""
        if random.choice([True, False]):
            # Compare two powers
            dec1 = random.choice([0.2, 0.3, 0.4, 0.5])
            dec2 = random.choice([0.2, 0.3, 0.4, 0.5])

            val1 = dec1 ** 2
            val2 = dec2 ** 2

            if val1 > val2:
                comp = ">"
            elif val1 < val2:
                comp = "<"
            else:
                comp = "="

            latex = f"\\text{{Compare: }} {dec1}^{{2}} \\quad ? \\quad {dec2}^{{2}}"
            solution = f"{dec1}^{{2}} {comp} {dec2}^{{2}}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"{dec1}^{{2}} = {val1}",
                    f"{dec2}^{{2}} = {val2}",
                    solution
                ],
                difficulty='challenge'
            )
        else:
            # Add two powers of fractions
            num1, denom1 = random.choice([(1, 2), (1, 4)])
            result1_num = num1 ** 2
            result1_denom = denom1 ** 2

            num2, denom2 = random.choice([(1, 2), (1, 4)])
            result2_num = num2 ** 2
            result2_denom = denom2 ** 2

            # Find common denominator and add
            from math import gcd
            common_denom = (result1_denom * result2_denom) // gcd(result1_denom, result2_denom)
            sum_num = (result1_num * common_denom // result1_denom) + (result2_num * common_denom // result2_denom)

            # Simplify
            g = gcd(sum_num, common_denom)
            final_num = sum_num // g
            final_denom = common_denom // g

            latex = f"\\text{{Evaluate: }} \\left(\\frac{{{num1}}}{{{denom1}}}\\right)^{{2}} + \\left(\\frac{{{num2}}}{{{denom2}}}\\right)^{{2}}"
            solution = f"\\frac{{{final_num}}}{{{final_denom}}}" if final_denom != 1 else str(final_num)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\left(\\frac{{{num1}}}{{{denom1}}}\\right)^{{2}} = \\frac{{{result1_num}}}{{{result1_denom}}}",
                    f"\\left(\\frac{{{num2}}}{{{denom2}}}\\right)^{{2}} = \\frac{{{result2_num}}}{{{result2_denom}}}",
                    f"\\text{{Sum}} = {solution}"
                ],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = PowersOfFractionsAndDecimalsGenerator()

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
