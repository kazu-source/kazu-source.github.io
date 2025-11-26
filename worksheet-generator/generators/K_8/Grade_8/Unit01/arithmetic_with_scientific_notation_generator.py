"""
Arithmetic with Scientific Notation Generator - Grade 8 Unit 1
Generates problems performing arithmetic operations with numbers in scientific notation
Example: (3 × 10⁴) × (2 × 10³) = 6 × 10⁷
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ArithmeticWithScientificNotationGenerator:
    """Generates arithmetic with scientific notation problems."""

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
        """Generate easy problems: multiply scientific notation numbers."""
        coef1 = random.randint(2, 5)
        coef2 = random.randint(2, 5)
        exp1 = random.randint(2, 4)
        exp2 = random.randint(2, 4)

        result_coef = coef1 * coef2
        result_exp = exp1 + exp2

        latex = f"({coef1} \\times 10^{{{exp1}}}) \\times ({coef2} \\times 10^{{{exp2}}})"
        solution = f"{result_coef} \\times 10^{{{result_exp}}}"
        steps = [
            f"\\text{{Multiply coefficients: }} {coef1} \\times {coef2} = {result_coef}",
            f"\\text{{Add exponents: }} 10^{{{exp1}}} \\times 10^{{{exp2}}} = 10^{{{result_exp}}}",
            f"{result_coef} \\times 10^{{{result_exp}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: divide or multiply with adjustment needed."""
        problem_type = random.choice(['multiply_adjust', 'divide'])

        if problem_type == 'multiply_adjust':
            # Result needs to be adjusted to proper scientific notation
            coef1 = random.randint(4, 9)
            coef2 = random.randint(4, 9)
            exp1 = random.randint(2, 4)
            exp2 = random.randint(2, 4)

            result_coef = coef1 * coef2
            result_exp = exp1 + exp2

            # Adjust if coefficient >= 10
            if result_coef >= 10:
                adjusted_coef = result_coef / 10
                adjusted_exp = result_exp + 1
                solution = f"{adjusted_coef} \\times 10^{{{adjusted_exp}}}"
                steps = [
                    f"\\text{{Multiply: }} ({coef1} \\times {coef2}) \\times 10^{{{result_exp}}} = {result_coef} \\times 10^{{{result_exp}}}",
                    f"\\text{{Adjust: }} {result_coef} = {adjusted_coef} \\times 10",
                    f"{adjusted_coef} \\times 10^{{{adjusted_exp}}}"
                ]
            else:
                solution = f"{result_coef} \\times 10^{{{result_exp}}}"
                steps = [
                    f"{coef1} \\times {coef2} = {result_coef}",
                    f"10^{{{exp1}}} \\times 10^{{{exp2}}} = 10^{{{result_exp}}}",
                    f"{result_coef} \\times 10^{{{result_exp}}}"
                ]

            latex = f"({coef1} \\times 10^{{{exp1}}}) \\times ({coef2} \\times 10^{{{exp2}}})"

        else:  # divide
            coef1 = random.randint(4, 9)
            coef2 = random.randint(2, coef1)
            exp1 = random.randint(5, 8)
            exp2 = random.randint(2, 4)

            result_coef = coef1 / coef2
            result_exp = exp1 - exp2

            if result_coef == int(result_coef):
                result_coef = int(result_coef)

            latex = f"\\frac{{{coef1} \\times 10^{{{exp1}}}}}{{{coef2} \\times 10^{{{exp2}}}}}"
            solution = f"{result_coef} \\times 10^{{{result_exp}}}"
            steps = [
                f"\\text{{Divide coefficients: }} \\frac{{{coef1}}}{{{coef2}}} = {result_coef}",
                f"\\text{{Subtract exponents: }} 10^{{{exp1} - {exp2}}} = 10^{{{result_exp}}}",
                f"{result_coef} \\times 10^{{{result_exp}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: addition/subtraction requiring same exponent."""
        problem_type = random.choice(['add', 'subtract'])

        if problem_type == 'add':
            exponent = random.randint(3, 5)
            coef1 = random.randint(2, 6)
            coef2 = random.randint(2, 6)

            result_coef = coef1 + coef2

            latex = f"({coef1} \\times 10^{{{exponent}}}) + ({coef2} \\times 10^{{{exponent}}})"
            solution = f"{result_coef} \\times 10^{{{exponent}}}"
            steps = [
                f"\\text{{Same exponent, add coefficients: }} {coef1} + {coef2} = {result_coef}",
                f"{result_coef} \\times 10^{{{exponent}}}"
            ]

        else:  # subtract
            exponent = random.randint(3, 5)
            coef1 = random.randint(5, 9)
            coef2 = random.randint(2, coef1-1)

            result_coef = coef1 - coef2

            latex = f"({coef1} \\times 10^{{{exponent}}}) - ({coef2} \\times 10^{{{exponent}}})"
            solution = f"{result_coef} \\times 10^{{{exponent}}}"
            steps = [
                f"\\text{{Same exponent, subtract coefficients: }} {coef1} - {coef2} = {result_coef}",
                f"{result_coef} \\times 10^{{{exponent}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex expressions or requiring exponent adjustment."""
        problem_type = random.choice(['add_different_exp', 'mixed_ops', 'square'])

        if problem_type == 'add_different_exp':
            # Addition with different exponents
            exp1 = random.randint(4, 6)
            exp2 = exp1 - 1
            coef1 = random.randint(2, 5)
            coef2 = random.randint(1, 9)

            # Convert to same exponent
            adjusted_coef2 = coef2 / 10
            result_coef = coef1 + adjusted_coef2

            latex = f"({coef1} \\times 10^{{{exp1}}}) + ({coef2} \\times 10^{{{exp2}}})"
            solution = f"{result_coef} \\times 10^{{{exp1}}}"
            steps = [
                f"\\text{{Adjust to same exponent: }} {coef2} \\times 10^{{{exp2}}} = {adjusted_coef2} \\times 10^{{{exp1}}}",
                f"{coef1} + {adjusted_coef2} = {result_coef}",
                f"{result_coef} \\times 10^{{{exp1}}}"
            ]

        elif problem_type == 'mixed_ops':
            # (a × 10^m) × (b × 10^n) / (c × 10^p)
            coef1 = random.randint(4, 8)
            coef2 = random.randint(2, 4)
            coef3 = random.randint(2, 4)
            exp1 = random.randint(3, 5)
            exp2 = random.randint(2, 4)
            exp3 = random.randint(2, 3)

            numerator_coef = coef1 * coef2
            numerator_exp = exp1 + exp2
            result_coef = numerator_coef / coef3
            result_exp = numerator_exp - exp3

            if result_coef == int(result_coef):
                result_coef = int(result_coef)

            latex = f"\\frac{{({coef1} \\times 10^{{{exp1}}}) \\times ({coef2} \\times 10^{{{exp2}}})}}{{{coef3} \\times 10^{{{exp3}}}}}"
            solution = f"{result_coef} \\times 10^{{{result_exp}}}"
            steps = [
                f"\\text{{Numerator: }} {coef1} \\times {coef2} = {numerator_coef}, \\text{{ exp: }} {exp1} + {exp2} = {numerator_exp}",
                f"\\frac{{{numerator_coef}}}{{{coef3}}} = {result_coef}, \\text{{ exp: }} {numerator_exp} - {exp3} = {result_exp}",
                f"{result_coef} \\times 10^{{{result_exp}}}"
            ]

        else:  # square
            coef = random.randint(2, 4)
            exp = random.randint(2, 4)

            result_coef = coef ** 2
            result_exp = exp * 2

            latex = f"({coef} \\times 10^{{{exp}}})^2"
            solution = f"{result_coef} \\times 10^{{{result_exp}}}"
            steps = [
                f"({coef})^2 = {result_coef}",
                f"(10^{{{exp}}})^2 = 10^{{{result_exp}}}",
                f"{result_coef} \\times 10^{{{result_exp}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ArithmeticWithScientificNotationGenerator()

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
