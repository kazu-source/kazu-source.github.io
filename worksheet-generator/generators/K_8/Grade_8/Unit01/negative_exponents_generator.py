"""
Negative Exponents Generator - Grade 8 Unit 1
Generates problems with negative exponents
Example: 2⁻³ = 1/8, 3⁻² = 1/9
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class NegativeExponentsGenerator:
    """Generates negative exponents problems."""

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
        """Generate easy problems: simple negative exponents."""
        base = random.choice([2, 3, 4, 5])
        exponent = random.choice([1, 2, 3])

        denominator = base ** exponent

        latex = f"{base}^{{-{exponent}}}"
        solution = f"\\frac{{1}}{{{denominator}}}"
        steps = [
            f"\\text{{Negative exponent: }} a^{{-n}} = \\frac{{1}}{{a^n}}",
            f"{base}^{{-{exponent}}} = \\frac{{1}}{{{base}^{{{exponent}}}}}",
            f"\\frac{{1}}{{{denominator}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: evaluating negative exponents and fractions."""
        problem_type = random.choice(['evaluate', 'fraction_negative'])

        if problem_type == 'evaluate':
            base = random.choice([2, 3, 4, 5])
            exponent = random.choice([2, 3, 4])

            denominator = base ** exponent

            latex = f"\\text{{Evaluate: }} {base}^{{-{exponent}}}"
            solution = f"\\frac{{1}}{{{denominator}}}"
            steps = [
                f"{base}^{{-{exponent}}} = \\frac{{1}}{{{base}^{{{exponent}}}}}",
                f"{base}^{{{exponent}}} = {denominator}",
                f"\\frac{{1}}{{{denominator}}}"
            ]

        else:  # fraction with negative exponent
            numerator = random.choice([1, 2, 3])
            denominator = random.choice([2, 3, 4, 5])
            exponent = random.choice([1, 2])

            # (a/b)^(-n) = (b/a)^n
            new_num = denominator ** exponent
            new_den = numerator ** exponent

            latex = f"\\left(\\frac{{{numerator}}}{{{denominator}}}\\right)^{{-{exponent}}}"

            if new_den == 1:
                solution = str(new_num)
            else:
                solution = f"\\frac{{{new_num}}}{{{new_den}}}"

            steps = [
                f"\\text{{Negative exponent flips the fraction}}",
                f"\\left(\\frac{{{numerator}}}{{{denominator}}}\\right)^{{-{exponent}}} = \\left(\\frac{{{denominator}}}{{{numerator}}}\\right)^{{{exponent}}}",
                solution
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: expressions with negative exponents."""
        problem_type = random.choice(['product', 'quotient', 'simplify'])

        if problem_type == 'product':
            base = random.choice([2, 3, 4])
            exp1 = random.randint(2, 4)
            exp2 = random.randint(1, 3)

            result_exp = exp1 - exp2

            latex = f"{base}^{{{exp1}}} \\times {base}^{{-{exp2}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"{base}^{{{exp1}}} \\times {base}^{{-{exp2}}} = {base}^{{{exp1} + (-{exp2})}}",
                f"{base}^{{{result_exp}}}"
            ]

        elif problem_type == 'quotient':
            base = random.choice([2, 3, 4])
            exp1 = random.randint(1, 3)
            exp2 = random.randint(2, 4)

            result_exp = -(exp1 + exp2)

            latex = f"\\frac{{{base}^{{-{exp1}}}}}{{{base}^{{{exp2}}}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\frac{{{base}^{{-{exp1}}}}}{{{base}^{{{exp2}}}}} = {base}^{{-{exp1} - {exp2}}}",
                f"{base}^{{{result_exp}}}"
            ]

        else:  # simplify
            base = random.choice([2, 3, 'x', 'a'])
            exponent = random.choice([2, 3, 4])

            latex = f"\\frac{{1}}{{{base}^{{{exponent}}}}}"
            solution = f"{base}^{{-{exponent}}}"
            steps = [
                f"\\text{{Rewrite as negative exponent}}",
                f"\\frac{{1}}{{{base}^{{{exponent}}}}} = {base}^{{-{exponent}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex expressions."""
        problem_type = random.choice(['power', 'mixed', 'simplify_complex'])

        if problem_type == 'power':
            base = random.choice([2, 3])
            inner_exp = random.randint(2, 3)
            outer_exp = 2

            result_exp = -(inner_exp * outer_exp)

            latex = f"\\left({base}^{{-{inner_exp}}}\\right)^{{{outer_exp}}}"
            solution = f"{base}^{{{result_exp}}}"
            steps = [
                f"\\text{{Power rule: }} (a^m)^n = a^{{mn}}",
                f"\\left({base}^{{-{inner_exp}}}\\right)^{{{outer_exp}}} = {base}^{{(-{inner_exp}) \\times {outer_exp}}}",
                f"{base}^{{{result_exp}}}"
            ]

        elif problem_type == 'mixed':
            base = random.choice([2, 3, 'x'])
            exp1 = random.randint(2, 4)
            exp2 = random.randint(1, 3)

            result_exp = exp1 + exp2

            latex = f"{base}^{{-{exp1}}} \\times {base}^{{-{exp2}}}"
            solution = f"{base}^{{-{result_exp}}}"
            steps = [
                f"{base}^{{-{exp1}}} \\times {base}^{{-{exp2}}} = {base}^{{-{exp1} + (-{exp2})}}",
                f"{base}^{{-{result_exp}}}"
            ]

        else:  # simplify_complex
            base = random.choice(['x', 'a', 'y'])
            exp1 = random.randint(3, 5)
            exp2 = random.randint(5, 7)

            result_exp = exp2 - exp1

            latex = f"\\frac{{{base}^{{{exp1}}}}}{{{base}^{{{exp2}}}}}"
            solution = f"{base}^{{-{result_exp}}}"
            steps = [
                f"\\frac{{{base}^{{{exp1}}}}}{{{base}^{{{exp2}}}}} = {base}^{{{exp1} - {exp2}}}",
                f"{base}^{{-{result_exp}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = NegativeExponentsGenerator()

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
