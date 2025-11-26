"""
Adding and Subtracting Mixed Numbers Generator - Grade 5 Unit 4
Generates problems adding and subtracting mixed numbers with unlike denominators
Example: 2 1/3 + 1 1/4 = 3 7/12
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AddingSubtractingMixedNumbersGenerator:
    """Generates adding and subtracting mixed numbers problems."""

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
        """Generate easy problems: add mixed numbers, no regrouping."""
        whole1 = random.randint(1, 4)
        whole2 = random.randint(1, 4)

        den1 = random.choice([2, 4, 5])
        den2 = den1 * random.choice([1, 2])

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)

        result_frac = new_num1 + new_num2

        if result_frac < lcm:
            result_whole = whole1 + whole2
            result_num, result_den = self._simplify(result_frac, lcm)
            solution = f"{result_whole}\\frac{{{result_num}}}{{{result_den}}}"
        else:
            extra_whole = result_frac // lcm
            result_frac = result_frac % lcm
            result_whole = whole1 + whole2 + extra_whole
            result_num, result_den = self._simplify(result_frac, lcm)
            if result_frac == 0:
                solution = str(result_whole)
            else:
                solution = f"{result_whole}\\frac{{{result_num}}}{{{result_den}}}"

        latex = f"{whole1}\\frac{{{num1}}}{{{den1}}} + {whole2}\\frac{{{num2}}}{{{den2}}}"
        steps = [
            f"\\text{{{{LCD = }}}} {lcm}",
            f"{whole1}\\frac{{{new_num1}}}{{{lcm}}} + {whole2}\\frac{{{new_num2}}}{{{lcm}}}",
            solution
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: add with regrouping."""
        whole1 = random.randint(2, 6)
        whole2 = random.randint(1, 5)

        pairs = [(2, 3), (3, 4), (2, 5), (3, 5)]
        den1, den2 = random.choice(pairs)

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)

        result_frac = new_num1 + new_num2
        extra_whole = result_frac // lcm
        result_frac = result_frac % lcm
        result_whole = whole1 + whole2 + extra_whole

        result_num, result_den = self._simplify(result_frac, lcm)

        if result_frac == 0:
            solution = str(result_whole)
        else:
            solution = f"{result_whole}\\frac{{{result_num}}}{{{result_den}}}"

        latex = f"{whole1}\\frac{{{num1}}}{{{den1}}} + {whole2}\\frac{{{num2}}}{{{den2}}}"
        steps = [
            f"\\text{{{{LCD = }}}} {lcm}",
            f"\\frac{{{new_num1} + {new_num2}}}{{{lcm}}} = \\frac{{{new_num1 + new_num2}}}{{{lcm}}}",
            solution
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: subtract mixed numbers with regrouping."""
        whole1 = random.randint(4, 8)
        whole2 = random.randint(1, whole1 - 1)

        den1 = random.choice([3, 4, 5, 6])
        den2 = random.choice([2, 3, 4, 5])
        while den2 == den1:
            den2 = random.choice([2, 3, 4, 5])

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(num1 + 1, den2 - 1)  # Force regrouping

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)

        # Convert to improper fractions
        improper1 = whole1 * lcm + new_num1
        improper2 = whole2 * lcm + new_num2

        result = improper1 - improper2
        result_whole = result // lcm
        result_frac = result % lcm

        result_num, result_den = self._simplify(result_frac, lcm)

        if result_frac == 0:
            solution = str(result_whole)
        else:
            solution = f"{result_whole}\\frac{{{result_num}}}{{{result_den}}}"

        latex = f"{whole1}\\frac{{{num1}}}{{{den1}}} - {whole2}\\frac{{{num2}}}{{{den2}}}"
        steps = [
            f"\\text{{{{LCD = }}}} {lcm}",
            f"\\text{{{{Convert and subtract}}}}",
            solution
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex mixed number operations."""
        whole1 = random.randint(3, 6)
        whole2 = random.randint(2, 5)
        whole3 = random.randint(1, 4)

        den1 = random.choice([3, 4, 6])
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

        # Convert to improper fractions
        improper1 = whole1 * lcm_all + new_num1
        improper2 = whole2 * lcm_all + new_num2
        improper3 = whole3 * lcm_all + new_num3

        result = improper1 + improper2 - improper3
        result_whole = result // lcm_all
        result_frac = result % lcm_all

        result_num, result_den = self._simplify(result_frac, lcm_all)

        if result_frac == 0:
            solution = str(result_whole)
        else:
            solution = f"{result_whole}\\frac{{{result_num}}}{{{result_den}}}"

        latex = f"{whole1}\\frac{{{num1}}}{{{den1}}} + {whole2}\\frac{{{num2}}}{{{den2}}} - {whole3}\\frac{{{num3}}}{{{den3}}}"
        steps = [
            f"\\text{{{{LCD = }}}} {lcm_all}",
            solution
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = AddingSubtractingMixedNumbersGenerator()

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
