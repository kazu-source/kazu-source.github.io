"""
Exponents Generator - Introduction to exponents and powers
Generates problems about basic exponent evaluation
"""

import random
from dataclasses import dataclass
from typing import List


@dataclass
class ExponentProblem:
    """Represents an exponent problem."""
    latex: str  # LaTeX formatted problem
    solution: int  # The answer
    difficulty: str


class ExponentsGenerator:
    """Generates problems introducing exponents."""

    def __init__(self, seed=None):
        """Initialize the exponents generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[ExponentProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard'
            num_problems: Number of problems to generate

        Returns:
            List of ExponentProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> ExponentProblem:
        """Generate a single exponent problem."""

        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> ExponentProblem:
        """Generate easy exponent problems (small bases and exponents)."""
        problem_type = random.choice(['simple', 'squared', 'cubed'])

        if problem_type == 'simple':
            # Simple powers: 2^3, 3^2, etc.
            base = random.randint(2, 5)
            exp = random.randint(2, 3)
            solution = base ** exp
            latex = f"{base}^{{{exp}}}"

        elif problem_type == 'squared':
            # Specifically squared numbers
            base = random.randint(2, 10)
            solution = base ** 2
            latex = f"{base}^2"

        else:  # cubed
            # Specifically cubed numbers
            base = random.randint(2, 5)
            solution = base ** 3
            latex = f"{base}^3"

        return ExponentProblem(latex=latex, solution=solution, difficulty='easy')

    def _generate_medium(self) -> ExponentProblem:
        """Generate medium exponent problems."""
        problem_type = random.choice(['larger_base', 'larger_exp', 'power_of_10'])

        if problem_type == 'larger_base':
            # Larger bases with smaller exponents
            base = random.randint(6, 12)
            exp = random.randint(2, 3)
            solution = base ** exp
            latex = f"{base}^{{{exp}}}"

        elif problem_type == 'larger_exp':
            # Smaller bases with larger exponents
            base = random.randint(2, 4)
            exp = random.randint(4, 5)
            solution = base ** exp
            latex = f"{base}^{{{exp}}}"

        else:  # power_of_10
            # Powers of 10
            exp = random.randint(2, 4)
            solution = 10 ** exp
            latex = f"10^{{{exp}}}"

        return ExponentProblem(latex=latex, solution=solution, difficulty='medium')

    def _generate_hard(self) -> ExponentProblem:
        """Generate hard exponent problems."""
        problem_type = random.choice(['large_power', 'negative_base', 'expression'])

        if problem_type == 'large_power':
            # Larger exponents
            base = random.randint(2, 7)
            exp = random.randint(4, 6)
            solution = base ** exp
            latex = f"{base}^{{{exp}}}"

        elif problem_type == 'negative_base':
            # Negative bases (even exponents to keep positive)
            base = -random.randint(2, 6)
            exp = 2 * random.randint(1, 3)  # Even exponent
            solution = base ** exp
            latex = f"({base})^{{{exp}}}"

        else:  # expression
            # Simple expression with exponent
            base = random.randint(2, 5)
            exp = random.randint(2, 3)
            add = random.randint(1, 5)
            solution = base ** exp + add
            latex = f"{base}^{{{exp}}} + {add}"

        return ExponentProblem(latex=latex, solution=solution, difficulty='hard')

    def _generate_challenge(self) -> ExponentProblem:
        """Generate challenge exponent problems (larger numbers, combined operations, multi-step)."""
        problem_type = random.choice(['very_large_power', 'multiple_exponents', 'complex_expression', 'negative_exponent_product'])

        if problem_type == 'very_large_power':
            # Very large exponents requiring careful calculation
            base = random.randint(2, 5)
            exp = random.randint(7, 9)
            solution = base ** exp
            latex = f"{base}^{{{exp}}}"

        elif problem_type == 'multiple_exponents':
            # Multiple exponential terms to add/subtract
            base1 = random.randint(2, 4)
            exp1 = random.randint(3, 5)
            base2 = random.randint(2, 4)
            exp2 = random.randint(3, 5)
            solution = base1 ** exp1 + base2 ** exp2
            latex = f"{base1}^{{{exp1}}} + {base2}^{{{exp2}}}"

        elif problem_type == 'complex_expression':
            # Expression with exponents and multiple operations
            base = random.randint(2, 5)
            exp = random.randint(3, 5)
            mult = random.randint(2, 4)
            add = random.randint(5, 15)
            solution = mult * (base ** exp) + add
            latex = f"{mult} \\cdot {base}^{{{exp}}} + {add}"

        else:  # negative_exponent_product
            # Product of negative base with larger exponent
            base = -random.randint(2, 5)
            exp = 2 * random.randint(2, 4)  # Even exponent
            mult = random.randint(2, 6)
            solution = mult * (base ** exp)
            latex = f"{mult} \\cdot ({base})^{{{exp}}}"

        return ExponentProblem(latex=latex, solution=solution, difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = ExponentsGenerator()

    print("Testing Exponents Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex} = {problem.solution}")
