"""
Exponent Properties Intro Generator - Grade 8 Unit 1
Generates problems introducing basic exponent properties
Example: 2³ × 2² = 2⁵, (3²)³ = 3⁶
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ExponentPropertiesIntroGenerator:
    """Generates exponent properties introduction problems."""

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
        """Generate easy problems: product rule a^m × a^n = a^(m+n)."""
        base = random.choice([2, 3, 4, 5])
        exp1 = random.randint(2, 5)
        exp2 = random.randint(2, 5)

        result_exp = exp1 + exp2

        latex = f"{base}^{{{exp1}}} \\times {base}^{{{exp2}}}"
        solution = f"{base}^{{{result_exp}}}"
        steps = [
            f"\\text{{Product rule: }} a^m \\times a^n = a^{{m+n}}",
            f"{base}^{{{exp1}}} \\times {base}^{{{exp2}}} = {base}^{{{exp1}+{exp2}}}",
            f"{base}^{{{result_exp}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: quotient rule and power rule."""
        property_type = random.choice(['quotient', 'power'])

        if property_type == 'quotient':
            # a^m ÷ a^n = a^(m-n)
            base = random.choice([2, 3, 4, 5, 6])
            exp1 = random.randint(5, 8)
            exp2 = random.randint(2, exp1-1)

            result_exp = exp1 - exp2

            latex = f"\\frac{{{base}^{{{exp1}}}}}{{{base}^{{{exp2}}}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{Quotient rule: }} \\frac{{a^m}}{{a^n}} = a^{{m-n}}",
                f"\\frac{{{base}^{{{exp1}}}}}{{{base}^{{{exp2}}}}} = {base}^{{{exp1}-{exp2}}}",
                f"{base}^{{{result_exp}}}"
            ]

        else:  # power
            # (a^m)^n = a^(mn)
            base = random.choice([2, 3, 4, 5])
            exp1 = random.randint(2, 4)
            exp2 = random.randint(2, 3)

            result_exp = exp1 * exp2

            latex = f"\\left({base}^{{{exp1}}}\\right)^{{{exp2}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{Power rule: }} (a^m)^n = a^{{mn}}",
                f"\\left({base}^{{{exp1}}}\\right)^{{{exp2}}} = {base}^{{{exp1} \\times {exp2}}}",
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
        problem_type = random.choice(['product_power', 'quotient_power', 'mixed'])

        if problem_type == 'product_power':
            # (ab)^n = a^n × b^n
            base1 = random.choice([2, 3, 4])
            base2 = random.choice([2, 3, 5])
            exp = random.randint(2, 3)

            latex = f"({base1} \\times {base2})^{{{exp}}}"
            solution = f"{base1}^{{{exp}}} \\times {base2}^{{{exp}}}"
            steps = [
                f"\\text{{Product to a power: }} (ab)^n = a^n b^n",
                f"({base1} \\times {base2})^{{{exp}}} = {base1}^{{{exp}}} \\times {base2}^{{{exp}}}"
            ]

        elif problem_type == 'quotient_power':
            # (a/b)^n = a^n / b^n
            base1 = random.choice([3, 4, 5, 6])
            base2 = random.choice([2, 3])
            exp = random.randint(2, 3)

            latex = f"\\left(\\frac{{{base1}}}{{{base2}}}\\right)^{{{exp}}}"
            solution = f"\\frac{{{base1}^{{{exp}}}}}{{{base2}^{{{exp}}}}}"
            steps = [
                f"\\text{{Quotient to a power: }} \\left(\\frac{{a}}{{b}}\\right)^n = \\frac{{a^n}}{{b^n}}",
                f"\\left(\\frac{{{base1}}}{{{base2}}}\\right)^{{{exp}}} = \\frac{{{base1}^{{{exp}}}}}{{{base2}^{{{exp}}}}}"
            ]

        else:  # mixed
            base = random.choice([2, 3, 4])
            exp1 = random.randint(2, 3)
            exp2 = random.randint(2, 3)
            exp3 = random.randint(2, 3)

            result_exp = exp1 + (exp2 * exp3)

            latex = f"{base}^{{{exp1}}} \\times \\left({base}^{{{exp2}}}\\right)^{{{exp3}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{First apply power rule: }} \\left({base}^{{{exp2}}}\\right)^{{{exp3}}} = {base}^{{{exp2 * exp3}}}",
                f"{base}^{{{exp1}}} \\times {base}^{{{exp2 * exp3}}}",
                f"\\text{{Then product rule: }} {base}^{{{exp1} + {exp2 * exp3}}} = {base}^{{{result_exp}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex expressions with multiple properties."""
        problem_type = random.choice(['simplify', 'evaluate', 'zero_exp'])

        if problem_type == 'simplify':
            base = random.choice([2, 3, 'x', 'a'])
            exp1 = random.randint(3, 5)
            exp2 = random.randint(2, 4)
            exp3 = random.randint(2, 3)

            # (a^m × a^n) / a^p
            numerator_exp = exp1 + exp2
            result_exp = numerator_exp - exp3

            latex = f"\\frac{{{base}^{{{exp1}}} \\times {base}^{{{exp2}}}}}{{{base}^{{{exp3}}}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{Numerator: }} {base}^{{{exp1}}} \\times {base}^{{{exp2}}} = {base}^{{{numerator_exp}}}",
                f"\\frac{{{base}^{{{numerator_exp}}}}}{{{base}^{{{exp3}}}}} = {base}^{{{numerator_exp} - {exp3}}}",
                f"{base}^{{{result_exp}}}"
            ]

        elif problem_type == 'evaluate':
            base = random.choice([2, 3])
            exp1 = random.randint(2, 3)
            exp2 = random.randint(2, 3)

            result_exp = exp1 * exp2
            result_value = base ** result_exp

            latex = f"\\text{{Evaluate: }} \\left({base}^{{{exp1}}}\\right)^{{{exp2}}}"
            solution = str(result_value)
            steps = [
                f"\\left({base}^{{{exp1}}}\\right)^{{{exp2}}} = {base}^{{{exp1} \\times {exp2}}}",
                f"{base}^{{{result_exp}}} = {result_value}"
            ]

        else:  # zero_exp
            base = random.choice([2, 3, 4, 5, 7])

            latex = f"{base}^0"
            solution = "1"
            steps = [
                f"\\text{{Zero exponent rule: }} a^0 = 1 \\text{{ for any }} a \\neq 0",
                f"{base}^0 = 1"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ExponentPropertiesIntroGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}\n")

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
