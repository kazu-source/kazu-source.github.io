"""
Dividing Fractions and Whole Numbers Generator - Grade 6 Unit 2
Generates problems dividing fractions by whole numbers and vice versa
Example: 1/2 ÷ 3 = ? or 6 ÷ 1/2 = ?
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DividingFractionsAndWholeNumbersGenerator:
    """Generates dividing fractions and whole numbers problems."""

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

    def _gcd(self, a: int, b: int) -> int:
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return a

    def _simplify_fraction(self, num: int, den: int) -> tuple:
        """Simplify a fraction."""
        gcd = self._gcd(abs(num), abs(den))
        return num // gcd, den // gcd

    def _generate_easy(self) -> Equation:
        """Generate easy problems: unit fractions divided by whole numbers."""
        denominator = random.choice([2, 3, 4])
        divisor = random.choice([2, 3])

        result_num = 1
        result_den = denominator * divisor

        latex = f"\\frac{{1}}{{{denominator}}} \\div {divisor}"
        solution = f"\\frac{{{result_num}}}{{{result_den}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{1}}{{{denominator}}} \\times \\frac{{1}}{{{divisor}}} = \\frac{{{result_num}}}{{{result_den}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: fractions divided by whole numbers."""
        numerator = random.randint(1, 5)
        denominator = random.choice([2, 3, 4, 5, 6])
        divisor = random.choice([2, 3, 4])

        result_num = numerator
        result_den = denominator * divisor
        result_num, result_den = self._simplify_fraction(result_num, result_den)

        latex = f"\\frac{{{numerator}}}{{{denominator}}} \\div {divisor}"
        solution = f"\\frac{{{result_num}}}{{{result_den}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{{numerator}}}{{{denominator}}} \\times \\frac{{1}}{{{divisor}}} = \\frac{{{result_num}}}{{{result_den}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: whole numbers divided by fractions."""
        whole = random.randint(2, 8)
        frac_num = 1
        frac_den = random.choice([2, 3, 4, 5])

        result_num = whole * frac_den
        result_den = frac_num

        latex = f"{whole} \\div \\frac{{{frac_num}}}{{{frac_den}}}"
        if result_den == 1:
            solution = str(result_num)
        else:
            result_num, result_den = self._simplify_fraction(result_num, result_den)
            solution = f"\\frac{{{result_num}}}{{{result_den}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{whole} \\times \\frac{{{frac_den}}}{{{frac_num}}} = {result_num}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: whole numbers divided by non-unit fractions."""
        whole = random.randint(3, 10)
        frac_num = random.randint(2, 4)
        frac_den = random.choice([3, 4, 5, 6])

        # Ensure fraction is proper
        while frac_num >= frac_den:
            frac_den = random.choice([3, 4, 5, 6])

        result_num = whole * frac_den
        result_den = frac_num
        result_num, result_den = self._simplify_fraction(result_num, result_den)

        latex = f"{whole} \\div \\frac{{{frac_num}}}{{{frac_den}}}"
        if result_den == 1:
            solution = str(result_num)
        else:
            solution = f"\\frac{{{result_num}}}{{{result_den}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{whole} \\times \\frac{{{frac_den}}}{{{frac_num}}} = \\frac{{{result_num}}}{{{result_den}}}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = DividingFractionsAndWholeNumbersGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
