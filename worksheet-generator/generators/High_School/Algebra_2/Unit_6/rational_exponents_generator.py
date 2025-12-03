"""
Rational Exponents Generator
Creates problems about converting between radicals and fractional exponents
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class RationalExponentsGenerator:
    """Generates problems about rational exponents."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Convert between radical and exponential form"""
        problem_type = random.choice(['to_exponential', 'to_radical'])

        if problem_type == 'to_exponential':
            n = random.choice([2, 3, 4])
            base = random.choice(['x', 'a', 'y'])

            if n == 2:
                latex = f"\\text{{Write }} \\sqrt{{{base}}} \\text{{ using a rational exponent.}}"
            else:
                latex = f"\\text{{Write }} \\sqrt[{n}]{{{base}}} \\text{{ using a rational exponent.}}"

            solution = f"{base}^{{1/{n}}}"

            steps = [
                f"\\sqrt[n]{{x}} = x^{{1/n}}",
                f"\\sqrt[{n}]{{{base}}} = {base}^{{1/{n}}}"
            ]
        else:
            n = random.choice([2, 3, 4])
            base = random.choice(['x', 'a', 'y'])

            latex = f"\\text{{Write }} {base}^{{1/{n}}} \\text{{ as a radical.}}"

            if n == 2:
                solution = f"\\sqrt{{{base}}}"
            else:
                solution = f"\\sqrt[{n}]{{{base}}}"

            steps = [
                f"x^{{1/n}} = \\sqrt[n]{{x}}",
                f"{base}^{{1/{n}}} = {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Convert expressions with numerator > 1 in exponent"""
        problem_type = random.choice(['to_exponential', 'to_radical'])

        m = random.randint(2, 4)
        n = random.choice([2, 3])
        while m == n:
            m = random.randint(2, 4)
        base = random.choice(['x', 'a', 'b'])

        if problem_type == 'to_exponential':
            if n == 2:
                latex = f"\\text{{Write }} \\sqrt{{{base}^{m}}} \\text{{ using a rational exponent.}}"
            else:
                latex = f"\\text{{Write }} \\sqrt[{n}]{{{base}^{m}}} \\text{{ using a rational exponent.}}"

            solution = f"{base}^{{{m}/{n}}}"

            steps = [
                f"\\sqrt[n]{{x^m}} = x^{{m/n}}",
                f"\\sqrt[{n}]{{{base}^{m}}} = {base}^{{{m}/{n}}}"
            ]
        else:
            latex = f"\\text{{Write }} {base}^{{{m}/{n}}} \\text{{ as a radical.}}"

            if n == 2:
                solution = f"\\sqrt{{{base}^{m}}}"
            else:
                solution = f"\\sqrt[{n}]{{{base}^{m}}}"

            steps = [
                f"x^{{m/n}} = \\sqrt[n]{{x^m}}",
                f"{base}^{{{m}/{n}}} = {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Evaluate numerical expressions with rational exponents"""
        problem_type = random.choice(['evaluate', 'simplify'])

        if problem_type == 'evaluate':
            # Choose bases that give clean results
            options = [
                (8, "1/3", 2, "8 = 2^3, \\text{ so } 8^{1/3} = 2"),
                (16, "1/4", 2, "16 = 2^4, \\text{ so } 16^{1/4} = 2"),
                (27, "1/3", 3, "27 = 3^3, \\text{ so } 27^{1/3} = 3"),
                (16, "1/2", 4, "16^{1/2} = \\sqrt{16} = 4"),
                (25, "1/2", 5, "25^{1/2} = \\sqrt{25} = 5"),
                (8, "2/3", 4, "8^{2/3} = (8^{1/3})^2 = 2^2 = 4"),
                (27, "2/3", 9, "27^{2/3} = (27^{1/3})^2 = 3^2 = 9"),
                (16, "3/4", 8, "16^{3/4} = (16^{1/4})^3 = 2^3 = 8"),
            ]

            base, exp, result, explanation = random.choice(options)

            latex = f"\\text{{Evaluate: }} {base}^{{{exp}}}"
            solution = str(result)

            steps = [
                f"{explanation}",
                f"{base}^{{{exp}}} = {result}"
            ]
        else:
            # Simplify expression
            base = random.choice(['x', 'a'])
            m = random.randint(2, 4)
            n = random.choice([2, 3])

            latex = f"\\text{{Simplify: }} ({base}^{{{m}}})^{{1/{n}}}"
            solution = f"{base}^{{{m}/{n}}}"

            steps = [
                f"\\text{{Use power rule: }} (x^a)^b = x^{{ab}}",
                f"({base}^{{{m}}})^{{1/{n}}} = {base}^{{{m} \\cdot 1/{n}}} = {base}^{{{m}/{n}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Combine exponent rules with rational exponents"""
        problem_type = random.choice(['product', 'quotient', 'negative'])

        if problem_type == 'product':
            base = random.choice(['x', 'a'])
            # x^(1/2) * x^(1/3) = x^(5/6)
            n1, n2 = random.choice([(2, 3), (2, 4), (3, 4)])
            # LCD
            if n1 == 2 and n2 == 3:
                lcd = 6
                result_num = 3 + 2
            elif n1 == 2 and n2 == 4:
                lcd = 4
                result_num = 2 + 1
            else:
                lcd = 12
                result_num = 4 + 3

            latex = f"\\text{{Simplify: }} {base}^{{1/{n1}}} \\cdot {base}^{{1/{n2}}}"
            solution = f"{base}^{{{result_num}/{lcd}}}"

            steps = [
                f"\\text{{Use product rule: }} x^a \\cdot x^b = x^{{a+b}}",
                f"{base}^{{1/{n1}}} \\cdot {base}^{{1/{n2}}} = {base}^{{1/{n1} + 1/{n2}}}",
                f"= {base}^{{{result_num}/{lcd}}}"
            ]

        elif problem_type == 'quotient':
            base = random.choice(['x', 'a'])
            # x^(3/4) / x^(1/4) = x^(2/4) = x^(1/2)
            num1 = random.randint(2, 4)
            num2 = 1
            den = random.choice([2, 3, 4])

            result = num1 - num2

            latex = f"\\text{{Simplify: }} \\frac{{{base}^{{{num1}/{den}}}}}{{{base}^{{{num2}/{den}}}}}"
            solution = f"{base}^{{{result}/{den}}}"

            steps = [
                f"\\text{{Use quotient rule: }} \\frac{{x^a}}{{x^b}} = x^{{a-b}}",
                f"\\frac{{{base}^{{{num1}/{den}}}}}{{{base}^{{{num2}/{den}}}}} = {base}^{{{num1}/{den} - {num2}/{den}}}",
                f"= {base}^{{{result}/{den}}}"
            ]

        else:
            # Negative rational exponent
            options = [
                (4, "-1/2", "1/2", "4^{-1/2} = \\frac{1}{4^{1/2}} = \\frac{1}{2}"),
                (8, "-1/3", "1/2", "8^{-1/3} = \\frac{1}{8^{1/3}} = \\frac{1}{2}"),
                (9, "-1/2", "1/3", "9^{-1/2} = \\frac{1}{9^{1/2}} = \\frac{1}{3}"),
                (16, "-1/2", "1/4", "16^{-1/2} = \\frac{1}{16^{1/2}} = \\frac{1}{4}"),
            ]

            base, exp, result, explanation = random.choice(options)

            latex = f"\\text{{Evaluate: }} {base}^{{{exp}}}"
            solution = result

            steps = [
                f"\\text{{Negative exponent: }} x^{{-a}} = \\frac{{1}}{{x^a}}",
                f"{explanation}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = RationalExponentsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
