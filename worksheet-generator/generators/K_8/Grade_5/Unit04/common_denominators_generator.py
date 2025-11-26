"""
Common Denominators Generator - Grade 5 Unit 4
Generates problems finding common denominators
Example: Find the LCD of 1/4 and 1/6: 12
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CommonDenominatorsGenerator:
    """Generates common denominators problems."""

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

    def _generate_easy(self) -> Equation:
        """Generate easy problems: LCD when one divides the other."""
        small = random.choice([2, 3, 4, 5])
        multiple = random.choice([2, 3])
        large = small * multiple

        lcm = large

        latex = f"\\text{{{{Find the LCD of }}}} {small} \\text{{{{ and }}}} {large}"
        solution = str(lcm)
        steps = [
            f"\\text{{{{Multiples of {small}: }}}} {small}, {small*2}, {small*3}, {small*4}...",
            f"\\text{{{{Multiples of {large}: }}}} {large}, {large*2}...",
            f"\\text{{{{LCD = }}}} {lcm}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: LCD of two small numbers."""
        pairs = [(2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (4, 6), (6, 8)]
        den1, den2 = random.choice(pairs)

        lcm = self._lcm(den1, den2)

        latex = f"\\text{{{{Find the LCD of }}}} {den1} \\text{{{{ and }}}} {den2}"
        solution = str(lcm)
        steps = [
            f"\\text{{{{Multiples of {den1}: }}}} {', '.join([str(den1*i) for i in range(1, 6)])}...",
            f"\\text{{{{Multiples of {den2}: }}}} {', '.join([str(den2*i) for i in range(1, 6)])}...",
            f"\\text{{{{LCD = }}}} {lcm}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: LCD of three numbers."""
        num1 = random.choice([2, 3, 4])
        num2 = random.choice([3, 4, 5])
        num3 = random.choice([5, 6])

        # Make sure they're not all the same
        while num1 == num2 == num3:
            num3 = random.choice([5, 6])

        lcm_12 = self._lcm(num1, num2)
        lcm_all = self._lcm(lcm_12, num3)

        latex = f"\\text{{{{Find the LCD of }}}} {num1}, {num2}, \\text{{{{ and }}}} {num3}"
        solution = str(lcm_all)
        steps = [
            f"\\text{{{{LCD of {num1} and {num2} = }}}} {lcm_12}",
            f"\\text{{{{LCD of {lcm_12} and {num3} = }}}} {lcm_all}",
            f"\\text{{{{LCD = }}}} {lcm_all}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: convert multiple fractions to LCD."""
        den1 = random.choice([3, 4, 5, 6])
        den2 = random.choice([2, 3, 4, 5])
        while den2 == den1:
            den2 = random.choice([2, 3, 4, 5])

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)

        latex = f"\\text{{{{Rewrite }}}} \\frac{{{num1}}}{{{den1}}} \\text{{{{ and }}}} \\frac{{{num2}}}{{{den2}}} \\text{{{{ with LCD}}}}"
        solution = f"\\frac{{{new_num1}}}{{{lcm}}}, \\frac{{{new_num2}}}{{{lcm}}}"
        steps = [
            f"\\text{{{{LCD of {den1} and {den2} = }}}} {lcm}",
            f"\\frac{{{num1}}}{{{den1}}} = \\frac{{{num1} \\times {lcm // den1}}}{{{lcm}}} = \\frac{{{new_num1}}}{{{lcm}}}",
            f"\\frac{{{num2}}}{{{den2}}} = \\frac{{{num2} \\times {lcm // den2}}}{{{lcm}}} = \\frac{{{new_num2}}}{{{lcm}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = CommonDenominatorsGenerator()

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
