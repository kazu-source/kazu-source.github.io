"""
Exponent Properties (Integer Exponents) Generator - Grade 8 Unit 1
Generates problems applying exponent properties with integer (including negative) exponents
Example: x⁻² × x⁵ = x³, (2⁻³)² = 2⁻⁶
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ExponentPropertiesIntegerExponentsGenerator:
    """Generates exponent properties with integer exponents problems."""

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
        """Generate easy problems: product rule with mix of positive and negative exponents."""
        base = random.choice([2, 3, 4, 'x', 'a'])
        exp1 = random.randint(2, 5)
        exp2_negative = random.randint(1, 3)

        result_exp = exp1 - exp2_negative

        latex = f"{base}^{{{exp1}}} \\times {base}^{{-{exp2_negative}}}"
        solution = f"{base}^{{{result_exp}}}"
        steps = [
            f"{base}^{{{exp1}}} \\times {base}^{{-{exp2_negative}}} = {base}^{{{exp1} + (-{exp2_negative})}}",
            f"{base}^{{{result_exp}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: quotient rule and power rule with negative exponents."""
        property_type = random.choice(['quotient', 'power'])

        if property_type == 'quotient':
            base = random.choice(['x', 'y', 'a', 'b'])
            exp1 = random.randint(-3, 3)
            exp2 = random.randint(-3, 3)

            # Ensure exponents are different
            while exp1 == exp2:
                exp2 = random.randint(-3, 3)

            result_exp = exp1 - exp2

            if exp1 < 0 and exp2 < 0:
                latex = f"\\frac{{{base}^{{-{abs(exp1)}}}}}{{{base}^{{-{abs(exp2)}}}}}"
            elif exp1 < 0:
                latex = f"\\frac{{{base}^{{-{abs(exp1)}}}}}{{{base}^{{{exp2}}}}}"
            elif exp2 < 0:
                latex = f"\\frac{{{base}^{{{exp1}}}}}{{{base}^{{-{abs(exp2)}}}}}"
            else:
                latex = f"\\frac{{{base}^{{{exp1}}}}}{{{base}^{{{exp2}}}}}"

            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{Quotient rule: }} \\frac{{a^m}}{{a^n}} = a^{{m-n}}",
                f"{base}^{{{exp1} - ({exp2})}}",
                f"{base}^{{{result_exp}}}"
            ]

        else:  # power
            base = random.choice(['x', 'a', 'y'])
            inner_exp_neg = random.randint(1, 4)
            outer_exp = random.randint(2, 3)

            result_exp = -inner_exp_neg * outer_exp

            latex = f"\\left({base}^{{-{inner_exp_neg}}}\\right)^{{{outer_exp}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{Power rule: }} (a^m)^n = a^{{mn}}",
                f"\\left({base}^{{-{inner_exp_neg}}}\\right)^{{{outer_exp}}} = {base}^{{(-{inner_exp_neg}) \\times {outer_exp}}}",
                f"{base}^{{{result_exp}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: combining multiple properties."""
        problem_type = random.choice(['product_of_powers', 'quotient_complex', 'power_product'])

        if problem_type == 'product_of_powers':
            base = random.choice(['x', 'y', 'a'])
            exp1 = random.randint(-3, -1)
            exp2 = random.randint(-3, -1)

            result_exp = exp1 + exp2

            latex = f"{base}^{{{exp1}}} \\times {base}^{{{exp2}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"{base}^{{{exp1}}} \\times {base}^{{{exp2}}} = {base}^{{{exp1} + {exp2}}}",
                f"{base}^{{{result_exp}}}"
            ]

        elif problem_type == 'quotient_complex':
            base = random.choice(['a', 'b', 'x'])
            exp1 = random.randint(2, 5)
            exp2 = random.randint(2, 4)
            exp3 = random.randint(1, 3)

            numerator_exp = exp1 + exp2
            result_exp = numerator_exp - exp3

            latex = f"\\frac{{{base}^{{{exp1}}} \\times {base}^{{-{exp2}}}}}{{{base}^{{-{exp3}}}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{Numerator: }} {base}^{{{exp1}}} \\times {base}^{{-{exp2}}} = {base}^{{{exp1} - {exp2}}}",
                f"\\frac{{{base}^{{{exp1 - exp2}}}}}{{{base}^{{-{exp3}}}}} = {base}^{{{exp1 - exp2} - (-{exp3})}}",
                f"{base}^{{{result_exp}}}"
            ]

        else:  # power_product
            base1 = 'x'
            base2 = 'y'
            exp = random.randint(-3, -1)

            latex = f"({base1}{base2})^{{{exp}}}"
            solution = f"{base1}^{{{exp}}}{base2}^{{{exp}}}"
            steps = [
                f"\\text{{Product to a power: }} (ab)^n = a^n b^n",
                f"({base1}{base2})^{{{exp}}} = {base1}^{{{exp}}} {base2}^{{{exp}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: very complex expressions."""
        problem_type = random.choice(['nested_powers', 'mixed_operations', 'simplify_fraction'])

        if problem_type == 'nested_powers':
            base = random.choice(['x', 'a'])
            exp1 = random.randint(-2, 2)
            exp2 = random.randint(-2, 2)
            exp3 = random.randint(2, 3)

            # ((a^m)^n)^p
            intermediate = exp1 * exp2
            result_exp = intermediate * exp3

            latex = f"\\left[\\left({base}^{{{exp1}}}\\right)^{{{exp2}}}\\right]^{{{exp3}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{Inner power: }} \\left({base}^{{{exp1}}}\\right)^{{{exp2}}} = {base}^{{{intermediate}}}",
                f"\\left({base}^{{{intermediate}}}\\right)^{{{exp3}}} = {base}^{{{result_exp}}}"
            ]

        elif problem_type == 'mixed_operations':
            base = random.choice(['a', 'x'])
            exp1 = random.randint(2, 4)
            exp2 = random.randint(1, 3)
            exp3 = random.randint(2, 3)
            exp4 = random.randint(1, 2)

            # (a^m × a^-n) / (a^p × a^-q)
            num_exp = exp1 - exp2
            den_exp = exp3 - exp4
            result_exp = num_exp - den_exp

            latex = f"\\frac{{{base}^{{{exp1}}} \\times {base}^{{-{exp2}}}}}{{{base}^{{{exp3}}} \\times {base}^{{-{exp4}}}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{Numerator: }} {base}^{{{exp1} - {exp2}}} = {base}^{{{num_exp}}}",
                f"\\text{{Denominator: }} {base}^{{{exp3} - {exp4}}} = {base}^{{{den_exp}}}",
                f"\\frac{{{base}^{{{num_exp}}}}}{{{base}^{{{den_exp}}}}} = {base}^{{{result_exp}}}"
            ]

        else:  # simplify_fraction
            base = random.choice(['x', 'y'])
            num_exp = random.randint(-3, -1)
            den_exp = random.randint(-3, -1)

            result_exp = num_exp - den_exp

            latex = f"\\frac{{{base}^{{{num_exp}}}}}{{{base}^{{{den_exp}}}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\frac{{{base}^{{{num_exp}}}}}{{{base}^{{{den_exp}}}}} = {base}^{{{num_exp} - ({den_exp})}}",
                f"{base}^{{{result_exp}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ExponentPropertiesIntegerExponentsGenerator()

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
