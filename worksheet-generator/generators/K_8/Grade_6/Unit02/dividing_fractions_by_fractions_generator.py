"""
Dividing Fractions by Fractions Generator - Grade 6 Unit 2
Generates problems dividing fractions by fractions
Example: 1/2 ÷ 1/3 = ?
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DividingFractionsByFractionsGenerator:
    """Generates dividing fractions by fractions problems."""

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
        """Generate easy problems: unit fractions divided by unit fractions."""
        den1 = random.choice([2, 3, 4])
        den2 = random.choice([2, 3, 4])

        # Result: (1/den1) ÷ (1/den2) = den2/den1
        result_num = den2
        result_den = den1
        result_num, result_den = self._simplify_fraction(result_num, result_den)

        latex = f"\\frac{{1}}{{{den1}}} \\div \\frac{{1}}{{{den2}}}"
        if result_den == 1:
            solution = str(result_num)
        else:
            solution = f"\\frac{{{result_num}}}{{{result_den}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{1}}{{{den1}}} \\times \\frac{{{den2}}}{{1}} = \\frac{{{den2}}}{{{den1}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: fractions divided by unit fractions."""
        num1 = random.randint(1, 4)
        den1 = random.choice([2, 3, 4, 5])
        den2 = random.choice([2, 3, 4])

        # Result: (num1/den1) ÷ (1/den2) = (num1 * den2)/den1
        result_num = num1 * den2
        result_den = den1
        result_num, result_den = self._simplify_fraction(result_num, result_den)

        latex = f"\\frac{{{num1}}}{{{den1}}} \\div \\frac{{1}}{{{den2}}}"
        if result_den == 1:
            solution = str(result_num)
        else:
            solution = f"\\frac{{{result_num}}}{{{result_den}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{{num1}}}{{{den1}}} \\times \\frac{{{den2}}}{{1}} = \\frac{{{result_num}}}{{{result_den}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: fractions divided by fractions."""
        num1 = random.randint(1, 5)
        den1 = random.choice([2, 3, 4, 5, 6])
        num2 = random.randint(1, 4)
        den2 = random.choice([2, 3, 4, 5])

        # Result: (num1/den1) ÷ (num2/den2) = (num1 * den2)/(den1 * num2)
        result_num = num1 * den2
        result_den = den1 * num2
        result_num, result_den = self._simplify_fraction(result_num, result_den)

        latex = f"\\frac{{{num1}}}{{{den1}}} \\div \\frac{{{num2}}}{{{den2}}}"
        if result_den == 1:
            solution = str(result_num)
        else:
            solution = f"\\frac{{{result_num}}}{{{result_den}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{{num1}}}{{{den1}}} \\times \\frac{{{den2}}}{{{num2}}} = \\frac{{{result_num}}}{{{result_den}}}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex fractions with simplification."""
        num1 = random.randint(2, 6)
        den1 = random.choice([3, 4, 5, 6, 8])
        num2 = random.randint(2, 5)
        den2 = random.choice([3, 4, 5, 6])

        # Result: (num1/den1) ÷ (num2/den2) = (num1 * den2)/(den1 * num2)
        result_num = num1 * den2
        result_den = den1 * num2
        result_num, result_den = self._simplify_fraction(result_num, result_den)

        latex = f"\\frac{{{num1}}}{{{den1}}} \\div \\frac{{{num2}}}{{{den2}}}"
        if result_den == 1:
            solution = str(result_num)
        else:
            solution = f"\\frac{{{result_num}}}{{{result_den}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{{num1}}}{{{den1}}} \\times \\frac{{{den2}}}{{{num2}}} = \\frac{{{num1 * den2}}}{{{den1 * num2}}} = \\frac{{{result_num}}}{{{result_den}}}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = DividingFractionsByFractionsGenerator()

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
