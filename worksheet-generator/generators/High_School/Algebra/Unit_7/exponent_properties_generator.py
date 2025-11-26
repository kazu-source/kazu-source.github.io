"""
Exponent Properties Generator - Unit 7
Generates problems about properties of exponents including product rule, quotient rule, and power rule
"""

import random
from dataclasses import dataclass
from typing import List, Tuple
from fractions import Fraction


@dataclass
class ExponentPropertyProblem:
    """Represents an exponent property problem."""
    latex: str  # LaTeX formatted problem
    solution: str  # The answer (can be string for expressions)
    difficulty: str
    problem_type: str  # Type of property being tested


class ExponentPropertiesGenerator:
    """Generates problems about properties of exponents."""

    def __init__(self, seed=None):
        """Initialize the exponent properties generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[ExponentPropertyProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of ExponentPropertyProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> ExponentPropertyProblem:
        """Generate a single exponent property problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> ExponentPropertyProblem:
        """Generate easy exponent property problems (product rule, simple power rule)."""
        problem_type = random.choice(['product_rule', 'power_rule', 'quotient_rule'])

        if problem_type == 'product_rule':
            # x^a * x^b = x^(a+b)
            base = random.choice(['x', 'y', 'a', 'b'])
            exp1 = random.randint(2, 5)
            exp2 = random.randint(2, 5)
            solution_exp = exp1 + exp2
            latex = f"{base}^{{{exp1}}} \\cdot {base}^{{{exp2}}}"
            solution = f"{base}^{{{solution_exp}}}"

        elif problem_type == 'power_rule':
            # (x^a)^b = x^(a*b)
            base = random.choice(['x', 'y', 'a', 'b'])
            exp1 = random.randint(2, 4)
            exp2 = random.randint(2, 3)
            solution_exp = exp1 * exp2
            latex = f"({base}^{{{exp1}}})^{{{exp2}}}"
            solution = f"{base}^{{{solution_exp}}}"

        else:  # quotient_rule
            # x^a / x^b = x^(a-b)
            base = random.choice(['x', 'y', 'a', 'b'])
            exp1 = random.randint(5, 8)
            exp2 = random.randint(2, 4)
            solution_exp = exp1 - exp2
            latex = f"\\frac{{{base}^{{{exp1}}}}}{{{base}^{{{exp2}}}}}"
            solution = f"{base}^{{{solution_exp}}}"

        return ExponentPropertyProblem(
            latex=latex,
            solution=solution,
            difficulty='easy',
            problem_type=problem_type
        )

    def _generate_medium(self) -> ExponentPropertyProblem:
        """Generate medium exponent property problems (combined rules, negative exponents)."""
        problem_type = random.choice(['combined_product', 'negative_exponent', 'zero_exponent'])

        if problem_type == 'combined_product':
            # x^a * x^b * x^c
            base = random.choice(['x', 'y', 'm', 'n'])
            exp1 = random.randint(2, 4)
            exp2 = random.randint(2, 4)
            exp3 = random.randint(1, 3)
            solution_exp = exp1 + exp2 + exp3
            latex = f"{base}^{{{exp1}}} \\cdot {base}^{{{exp2}}} \\cdot {base}^{{{exp3}}}"
            solution = f"{base}^{{{solution_exp}}}"

        elif problem_type == 'negative_exponent':
            # x^(-a) = 1/x^a
            base = random.choice(['x', 'y', 'a', 'b'])
            exp = random.randint(2, 5)
            latex = f"{base}^{{-{exp}}}"
            solution = f"\\frac{{1}}{{{base}^{{{exp}}}}}"

        else:  # zero_exponent
            # x^0 = 1 (x ≠ 0)
            base = random.choice(['x', 'y', '(2x)', '(3a)'])
            latex = f"{base}^0"
            solution = "1"

        return ExponentPropertyProblem(
            latex=latex,
            solution=solution,
            difficulty='medium',
            problem_type=problem_type
        )

    def _generate_hard(self) -> ExponentPropertyProblem:
        """Generate hard exponent property problems (multiple variables, complex combinations)."""
        problem_type = random.choice(['multi_variable', 'complex_quotient', 'mixed_operations'])

        if problem_type == 'multi_variable':
            # x^a * y^b * x^c * y^d = x^(a+c) * y^(b+d)
            exp1_x = random.randint(2, 4)
            exp2_x = random.randint(1, 3)
            exp1_y = random.randint(2, 4)
            exp2_y = random.randint(1, 3)
            latex = f"x^{{{exp1_x}}} \\cdot y^{{{exp1_y}}} \\cdot x^{{{exp2_x}}} \\cdot y^{{{exp2_y}}}"
            solution = f"x^{{{exp1_x + exp2_x}}}y^{{{exp1_y + exp2_y}}}"

        elif problem_type == 'complex_quotient':
            # (x^a * y^b) / (x^c * y^d)
            exp1_x = random.randint(5, 8)
            exp2_x = random.randint(2, 4)
            exp1_y = random.randint(5, 8)
            exp2_y = random.randint(2, 4)
            latex = f"\\frac{{x^{{{exp1_x}}} \\cdot y^{{{exp1_y}}}}}{{x^{{{exp2_x}}} \\cdot y^{{{exp2_y}}}}}"
            solution = f"x^{{{exp1_x - exp2_x}}}y^{{{exp1_y - exp2_y}}}"

        else:  # mixed_operations
            # (x^a)^b * x^c
            base = random.choice(['x', 'y', 'a', 'b'])
            exp1 = random.randint(2, 3)
            exp2 = random.randint(2, 3)
            exp3 = random.randint(2, 4)
            solution_exp = exp1 * exp2 + exp3
            latex = f"({base}^{{{exp1}}})^{{{exp2}}} \\cdot {base}^{{{exp3}}}"
            solution = f"{base}^{{{solution_exp}}}"

        return ExponentPropertyProblem(
            latex=latex,
            solution=solution,
            difficulty='hard',
            problem_type=problem_type
        )

    def _generate_challenge(self) -> ExponentPropertyProblem:
        """Generate challenge exponent property problems (fractional exponents, complex expressions)."""
        problem_type = random.choice(['fractional_exponent', 'complex_multi_term', 'nested_powers'])

        if problem_type == 'fractional_exponent':
            # x^(1/2) * x^(1/2) = x^1 = x
            base = random.choice(['x', 'y', 'a', 'b'])
            num1 = random.randint(1, 3)
            den1 = random.randint(2, 4)
            num2 = random.randint(1, 3)
            den2 = random.randint(2, 4)
            # Calculate sum of fractions
            result_frac = Fraction(num1, den1) + Fraction(num2, den2)
            latex = f"{base}^{{{num1}/{den1}}} \\cdot {base}^{{{num2}/{den2}}}"
            if result_frac.denominator == 1:
                solution = f"{base}^{{{result_frac.numerator}}}"
            else:
                solution = f"{base}^{{{result_frac.numerator}/{result_frac.denominator}}}"

        elif problem_type == 'complex_multi_term':
            # (x^a * y^b * z^c)^d
            exp_x = random.randint(2, 3)
            exp_y = random.randint(2, 3)
            exp_z = random.randint(1, 2)
            power = random.randint(2, 3)
            latex = f"(x^{{{exp_x}}} \\cdot y^{{{exp_y}}} \\cdot z^{{{exp_z}}})^{{{power}}}"
            solution = f"x^{{{exp_x * power}}}y^{{{exp_y * power}}}z^{{{exp_z * power}}}"

        else:  # nested_powers
            # ((x^a)^b)^c
            base = random.choice(['x', 'y', 'm', 'n'])
            exp1 = random.randint(2, 3)
            exp2 = random.randint(2, 3)
            exp3 = random.randint(2, 3)
            solution_exp = exp1 * exp2 * exp3
            latex = f"(({base}^{{{exp1}}})^{{{exp2}}})^{{{exp3}}}"
            solution = f"{base}^{{{solution_exp}}}"

        return ExponentPropertyProblem(
            latex=latex,
            solution=solution,
            difficulty='challenge',
            problem_type=problem_type
        )


if __name__ == "__main__":
    # Test the generator
    gen = ExponentPropertiesGenerator()

    print("Testing Exponent Properties Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. Simplify: {problem.latex}")
            print(f"   Answer: {problem.solution}")
            print(f"   Type: {problem.problem_type}")