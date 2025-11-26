"""
Parts of a Term Generator - Identifying parts of algebraic terms
Generates problems about identifying coefficients, variables, and exponents
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class PartsOfTermGenerator:
    """Generates problems for identifying parts of algebraic terms."""

    def __init__(self, seed=None):
        """Initialize the parts of term generator."""
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
        """Generate a single parts of term problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple term: identify coefficient in ax"""
        coef = random.randint(2, 12)
        var = random.choice(['x', 'y', 'z', 'a', 'b'])

        part_type = random.choice(['coefficient', 'variable'])

        if part_type == 'coefficient':
            latex = f"\\text{{What is the coefficient in {coef}{var}?}}"
            solution = str(coef)
        else:
            latex = f"\\text{{What is the variable in {coef}{var}?}}"
            solution = var

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate term with exponent: identify parts in ax^n"""
        coef = random.randint(2, 9)
        var = random.choice(['x', 'y', 'z'])
        exp = random.randint(2, 5)

        part_type = random.choice(['coefficient', 'variable', 'exponent'])

        if part_type == 'coefficient':
            latex = f"\\text{{What is the coefficient in {coef}{var}^{exp}?}}"
            solution = str(coef)
        elif part_type == 'variable':
            latex = f"\\text{{What is the variable in {coef}{var}^{exp}?}}"
            solution = var
        else:
            latex = f"\\text{{What is the exponent in {coef}{var}^{exp}?}}"
            solution = str(exp)

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate term with negative coefficient or fraction"""
        coef_choices = [-5, -3, -2, 2, 3, 5, '\\frac{1}{2}', '\\frac{3}{4}', '\\frac{2}{3}']
        coef = random.choice(coef_choices)
        var = random.choice(['x', 'y', 'm', 'n'])
        exp = random.randint(2, 4)

        part_type = random.choice(['coefficient', 'variable', 'exponent'])

        if isinstance(coef, str):  # fraction
            coef_display = coef
            coef_answer = coef
        else:
            coef_display = coef if coef < 0 else f"{coef}"
            coef_answer = str(coef)

        if part_type == 'coefficient':
            latex = f"\\text{{What is the coefficient in {coef_display}{var}^{exp}?}}"
            solution = coef_answer
        elif part_type == 'variable':
            latex = f"\\text{{What is the variable in {coef_display}{var}^{exp}?}}"
            solution = var
        else:
            latex = f"\\text{{What is the exponent in {coef_display}{var}^{exp}?}}"
            solution = str(exp)

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate term with multiple variables: identify parts in ax^m y^n"""
        coef = random.randint(2, 8)
        var1 = 'x'
        var2 = 'y'
        exp1 = random.randint(2, 4)
        exp2 = random.randint(1, 3)

        part_type = random.choice(['coefficient', 'variables', 'exponent_sum', 'degree'])

        if part_type == 'coefficient':
            latex = f"\\text{{What is the coefficient in {coef}{var1}^{exp1}{var2}^{exp2}?}}"
            solution = str(coef)
        elif part_type == 'variables':
            latex = f"\\text{{List all variables in {coef}{var1}^{exp1}{var2}^{exp2}}}"
            solution = f"{var1}, {var2}"
        elif part_type == 'exponent_sum':
            latex = f"\\text{{What is the sum of exponents in {coef}{var1}^{exp1}{var2}^{exp2}?}}"
            solution = str(exp1 + exp2)
        else:  # degree
            latex = f"\\text{{What is the degree of {coef}{var1}^{exp1}{var2}^{exp2}?}}"
            solution = str(exp1 + exp2)

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = PartsOfTermGenerator()

    print("Testing Parts of Term Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")