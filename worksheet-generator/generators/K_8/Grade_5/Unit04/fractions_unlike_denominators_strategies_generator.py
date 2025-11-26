"""
Fractions Unlike Denominators Strategies Generator - Grade 5 Unit 4
Generates problems exploring strategies for adding/subtracting fractions with unlike denominators
Example: What common denominator can we use for 1/3 + 1/4?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class FractionsUnlikeDenominatorsStrategiesGenerator:
    """Generates strategies for fractions with unlike denominators problems."""

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

    def _lcm(self, a, b):
        """Calculate least common multiple."""
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        return abs(a * b) // gcd(a, b)

    def _generate_easy(self) -> Equation:
        """Generate easy problems: identify common denominator for simple fractions."""
        denominators = [(2, 4), (3, 6), (2, 6), (4, 8), (5, 10)]
        den1, den2 = random.choice(denominators)

        lcm = self._lcm(den1, den2)

        latex = f"\\text{{{{What common denominator can we use for }}}} \\frac{{1}}{{{den1}}} \\text{{{{ and }}}} \\frac{{1}}{{{den2}}}?"
        solution = str(lcm)
        steps = [
            f"\\text{{{{Find multiples of {den1}: }}}} {den1}, {den1*2}, {den1*3}, ...",
            f"\\text{{{{Find multiples of {den2}: }}}} {den2}, {den2*2}, {den2*3}, ...",
            f"\\text{{{{Least common multiple: }}}} {lcm}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: convert to common denominator."""
        denominators = [(2, 3), (3, 4), (2, 5), (3, 5), (4, 6)]
        den1, den2 = random.choice(denominators)
        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)

        latex = f"\\text{{{{Rewrite with common denominators: }}}} \\frac{{{num1}}}{{{den1}}} \\text{{{{ and }}}} \\frac{{{num2}}}{{{den2}}}"
        solution = f"\\frac{{{new_num1}}}{{{lcm}}} \\text{{{{ and }}}} \\frac{{{new_num2}}}{{{lcm}}}"
        steps = [
            f"\\text{{{{LCD = }}}} {lcm}",
            f"\\frac{{{num1}}}{{{den1}}} = \\frac{{{num1} \\times {lcm // den1}}}{{{den1} \\times {lcm // den1}}} = \\frac{{{new_num1}}}{{{lcm}}}",
            f"\\frac{{{num2}}}{{{den2}}} = \\frac{{{num2} \\times {lcm // den2}}}{{{den2} \\times {lcm // den2}}} = \\frac{{{new_num2}}}{{{lcm}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: use benchmark fractions to estimate."""
        denominators = [(3, 4), (4, 5), (2, 5), (5, 6)]
        den1, den2 = random.choice(denominators)

        # Choose numerators to make fractions close to 1/2 or 1
        if random.choice([True, False]):
            num1 = den1 // 2  # close to 1/2
            num2 = den2 // 2
            benchmark = "\\frac{1}{2}"
        else:
            num1 = den1 - 1  # close to 1
            num2 = den2 - 1
            benchmark = "1"

        latex = f"\\text{{{{Is }}}} \\frac{{{num1}}}{{{den1}}} + \\frac{{{num2}}}{{{den2}}} \\text{{{{ close to {benchmark}, 1, or 2?}}}}"

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)
        sum_num = new_num1 + new_num2

        if sum_num < lcm * 0.75:
            estimate = "\\text{{close to }} \\frac{1}{2}"
        elif sum_num < lcm * 1.5:
            estimate = "\\text{{close to 1}}"
        else:
            estimate = "\\text{{close to 2}}"

        solution = estimate
        steps = [
            f"\\frac{{{num1}}}{{{den1}}} \\approx {num1/den1:.2f}",
            f"\\frac{{{num2}}}{{{den2}}} \\approx {num2/den2:.2f}",
            f"\\text{{{{Sum ≈ }}}} {num1/den1 + num2/den2:.2f}",
            estimate
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: compare different strategies."""
        den1 = random.choice([3, 4, 5, 6])
        den2 = random.choice([2, 3, 4, 5])
        while den2 == den1:
            den2 = random.choice([2, 3, 4, 5])

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        lcm = self._lcm(den1, den2)
        product = den1 * den2

        latex = f"\\text{{{{For }}}} \\frac{{{num1}}}{{{den1}}} + \\frac{{{num2}}}{{{den2}}}\\text{{{{, which is better: LCD = {lcm} or product = {product}?}}}}"

        if lcm < product:
            solution = f"\\text{{{{LCD = {lcm} (smaller, easier)}}}}"
            reason = "smaller"
        else:
            solution = f"\\text{{{{Either works (they're equal)}}}}"
            reason = "equal"

        steps = [
            f"\\text{{{{LCD of {den1} and {den2} = }}}} {lcm}",
            f"\\text{{{{Product of {den1} and {den2} = }}}} {product}",
            f"\\text{{{{{lcm} is {reason}, so use LCD}}}}",
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = FractionsUnlikeDenominatorsStrategiesGenerator()

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
