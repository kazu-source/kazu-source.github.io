"""
Adding and Subtracting Fractions with Unlike Denominators Generator - Grade 5 Unit 4
Generates problems adding and subtracting fractions with different denominators
Example: 1/3 + 1/4 = 7/12
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AddingSubtractingFractionsUnlikeGenerator:
    """Generates adding and subtracting fractions with unlike denominators problems."""

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

    def _lcm(self, a, b):
        """Calculate least common multiple."""
        return abs(a * b) // self._gcd(a, b)

    def _simplify(self, num, den):
        """Simplify a fraction."""
        gcd = self._gcd(abs(num), abs(den))
        return num // gcd, den // gcd

    def _generate_easy(self) -> Equation:
        """Generate easy problems: add fractions where one denominator divides the other."""
        small_den = random.choice([2, 3, 4, 5])
        large_den = small_den * random.choice([2, 3])

        num1 = random.randint(1, small_den - 1)
        num2 = random.randint(1, large_den - 1)

        lcm = large_den
        new_num1 = num1 * (lcm // small_den)

        result_num = new_num1 + num2
        result_num, result_den = self._simplify(result_num, lcm)

        latex = f"\\frac{{{num1}}}{{{small_den}}} + \\frac{{{num2}}}{{{large_den}}}"
        solution = f"\\frac{{{result_num}}}{{{result_den}}}"
        steps = [
            f"\\text{{{{LCD = }}}} {lcm}",
            f"\\frac{{{num1}}}{{{small_den}}} = \\frac{{{new_num1}}}{{{lcm}}}",
            f"\\frac{{{new_num1}}}{{{lcm}}} + \\frac{{{num2}}}{{{lcm}}} = \\frac{{{new_num1 + num2}}}{{{lcm}}}",
            f"\\frac{{{result_num}}}{{{result_den}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: add or subtract with different denominators."""
        pairs = [(2, 3), (3, 4), (2, 5), (3, 5), (4, 6)]
        den1, den2 = random.choice(pairs)

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        operation = random.choice(['+', '-'])

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)

        if operation == '+':
            result_num = new_num1 + new_num2
        else:
            result_num = new_num1 - new_num2

        result_num, result_den = self._simplify(result_num, lcm)

        latex = f"\\frac{{{num1}}}{{{den1}}} {operation} \\frac{{{num2}}}{{{den2}}}"
        solution = f"\\frac{{{result_num}}}{{{result_den}}}"
        steps = [
            f"\\text{{{{LCD = }}}} {lcm}",
            f"\\frac{{{num1}}}{{{den1}}} = \\frac{{{new_num1}}}{{{lcm}}}, \\frac{{{num2}}}{{{den2}}} = \\frac{{{new_num2}}}{{{lcm}}}",
            f"\\frac{{{new_num1}}}{{{lcm}}} {operation} \\frac{{{new_num2}}}{{{lcm}}} = \\frac{{{new_num1} {operation} {new_num2}}}{{{lcm}}}",
            f"\\frac{{{result_num}}}{{{result_den}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: multiple operations."""
        den1 = random.choice([3, 4, 5])
        den2 = random.choice([2, 3, 4])
        den3 = random.choice([2, 3, 5])

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)
        num3 = random.randint(1, den3 - 1)

        lcm_12 = self._lcm(den1, den2)
        lcm_all = self._lcm(lcm_12, den3)

        new_num1 = num1 * (lcm_all // den1)
        new_num2 = num2 * (lcm_all // den2)
        new_num3 = num3 * (lcm_all // den3)

        result_num = new_num1 + new_num2 - new_num3
        result_num, result_den = self._simplify(result_num, lcm_all)

        latex = f"\\frac{{{num1}}}{{{den1}}} + \\frac{{{num2}}}{{{den2}}} - \\frac{{{num3}}}{{{den3}}}"
        solution = f"\\frac{{{result_num}}}{{{result_den}}}"
        steps = [
            f"\\text{{{{LCD = }}}} {lcm_all}",
            f"\\frac{{{new_num1}}}{{{lcm_all}}} + \\frac{{{new_num2}}}{{{lcm_all}}} - \\frac{{{new_num3}}}{{{lcm_all}}}",
            f"\\frac{{{result_num}}}{{{result_den}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex fractions with simplification."""
        den1 = random.choice([6, 8, 9, 10, 12])
        den2 = random.choice([4, 6, 8, 9])
        while den2 == den1:
            den2 = random.choice([4, 6, 8, 9])

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        operation = random.choice(['+', '-'])

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)

        if operation == '+':
            result_num = new_num1 + new_num2
        else:
            # Make sure result is positive
            if new_num1 < new_num2:
                new_num1, new_num2 = new_num2, new_num1
                den1, den2 = den2, den1
                num1, num2 = num2, num1
            result_num = new_num1 - new_num2

        result_num, result_den = self._simplify(result_num, lcm)

        latex = f"\\frac{{{num1}}}{{{den1}}} {operation} \\frac{{{num2}}}{{{den2}}}"
        solution = f"\\frac{{{result_num}}}{{{result_den}}}"
        steps = [
            f"\\text{{{{LCD = }}}} {lcm}",
            f"\\frac{{{new_num1}}}{{{lcm}}} {operation} \\frac{{{new_num2}}}{{{lcm}}} = \\frac{{{new_num1} {operation} {new_num2}}}{{{lcm}}}",
            f"\\text{{{{Simplify: }}}} \\frac{{{result_num}}}{{{result_den}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = AddingSubtractingFractionsUnlikeGenerator()

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
