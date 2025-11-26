"""
Expanding and Simplifying Exponents Generator - Unit 7
Generates problems for expanding and simplifying expressions with exponents
"""

import random
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class ExpandingExponentProblem:
    """Represents an expanding exponent problem."""
    latex: str  # LaTeX formatted problem
    solution: str  # The expanded/simplified answer
    difficulty: str
    problem_type: str  # Type of expansion problem


class ExpandingExponentsGenerator:
    """Generates problems for expanding and simplifying expressions with exponents."""

    def __init__(self, seed=None):
        """Initialize the expanding exponents generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[ExpandingExponentProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of ExpandingExponentProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> ExpandingExponentProblem:
        """Generate a single expanding exponent problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> ExpandingExponentProblem:
        """Generate easy expanding problems (simple expansions)."""
        problem_type = random.choice(['expand_power', 'simplify_product', 'expand_square'])

        if problem_type == 'expand_power':
            # Expand x^3 to x·x·x
            base = random.choice(['x', 'y', 'a', 'b'])
            exp = random.randint(2, 4)
            latex = f"\\text{{Expand: }} {base}^{{{exp}}}"
            solution = " \\cdot ".join([base] * exp)

        elif problem_type == 'simplify_product':
            # Simplify x·x·x to x^3
            base = random.choice(['x', 'y', 'a', 'b'])
            exp = random.randint(2, 5)
            product = " \\cdot ".join([base] * exp)
            latex = f"\\text{{Simplify: }} {product}"
            solution = f"{base}^{{{exp}}}"

        else:  # expand_square
            # Expand (2x)^2
            coeff = random.randint(2, 5)
            base = random.choice(['x', 'y', 'a', 'b'])
            latex = f"\\text{{Expand: }} ({coeff}{base})^2"
            solution = f"{coeff**2}{base}^2"

        return ExpandingExponentProblem(
            latex=latex,
            solution=solution,
            difficulty='easy',
            problem_type=problem_type
        )

    def _generate_medium(self) -> ExpandingExponentProblem:
        """Generate medium expanding problems (multiple terms, coefficients)."""
        problem_type = random.choice(['expand_with_coeff', 'simplify_mixed', 'expand_product'])

        if problem_type == 'expand_with_coeff':
            # Expand 3x^2 fully
            coeff = random.randint(2, 6)
            base = random.choice(['x', 'y', 'a', 'b'])
            exp = random.randint(2, 3)
            latex = f"\\text{{Expand completely: }} {coeff}{base}^{{{exp}}}"
            expanded = " \\cdot ".join([base] * exp)
            solution = f"{coeff} \\cdot {expanded}"

        elif problem_type == 'simplify_mixed':
            # Simplify 2x·x·3x
            coeff1 = random.randint(2, 4)
            coeff2 = random.randint(2, 4)
            base = random.choice(['x', 'y', 'a', 'b'])
            num_terms = random.randint(2, 3)
            terms = [f"{coeff1}{base}"] + [base] * (num_terms - 1) + [f"{coeff2}{base}"]
            latex = f"\\text{{Simplify: }} {' \\cdot '.join(terms)}"
            total_coeff = coeff1 * coeff2
            total_exp = len(terms)
            solution = f"{total_coeff}{base}^{{{total_exp}}}"

        else:  # expand_product
            # Expand (xy)^3
            base1 = random.choice(['x', 'y'])
            base2 = random.choice(['a', 'b'])
            exp = random.randint(2, 3)
            latex = f"\\text{{Expand: }} ({base1}{base2})^{{{exp}}}"
            solution = f"{base1}^{{{exp}}}{base2}^{{{exp}}}"

        return ExpandingExponentProblem(
            latex=latex,
            solution=solution,
            difficulty='medium',
            problem_type=problem_type
        )

    def _generate_hard(self) -> ExpandingExponentProblem:
        """Generate hard expanding problems (complex expressions, multiple variables)."""
        problem_type = random.choice(['expand_complex', 'simplify_complex', 'expand_negative'])

        if problem_type == 'expand_complex':
            # Expand (2x^2y)^3
            coeff = random.randint(2, 4)
            exp1 = random.randint(2, 3)
            power = random.randint(2, 3)
            latex = f"\\text{{Expand: }} ({coeff}x^{{{exp1}}}y)^{{{power}}}"
            solution = f"{coeff**power}x^{{{exp1*power}}}y^{{{power}}}"

        elif problem_type == 'simplify_complex':
            # Simplify 2x^2·3x^3·x
            coeff1 = random.randint(2, 4)
            coeff2 = random.randint(2, 5)
            exp1 = random.randint(2, 3)
            exp2 = random.randint(2, 4)
            base = random.choice(['x', 'y', 'a', 'b'])
            latex = f"\\text{{Simplify: }} {coeff1}{base}^{{{exp1}}} \\cdot {coeff2}{base}^{{{exp2}}} \\cdot {base}"
            total_coeff = coeff1 * coeff2
            total_exp = exp1 + exp2 + 1
            solution = f"{total_coeff}{base}^{{{total_exp}}}"

        else:  # expand_negative
            # Expand (-2x)^3
            coeff = random.randint(2, 4)
            exp = random.randint(3, 5, 2)  # Odd exponent for negative result
            base = random.choice(['x', 'y', 'a', 'b'])
            latex = f"\\text{{Expand: }} (-{coeff}{base})^{{{exp}}}"
            result_coeff = (-coeff) ** exp
            solution = f"{result_coeff}{base}^{{{exp}}}"

        return ExpandingExponentProblem(
            latex=latex,
            solution=solution,
            difficulty='hard',
            problem_type=problem_type
        )

    def _generate_challenge(self) -> ExpandingExponentProblem:
        """Generate challenge expanding problems (very complex expressions)."""
        problem_type = random.choice(['expand_multi_var', 'simplify_fraction', 'expand_nested'])

        if problem_type == 'expand_multi_var':
            # Expand (2x^2y^3z)^4
            coeff = random.randint(2, 3)
            exp_x = random.randint(1, 3)
            exp_y = random.randint(1, 3)
            exp_z = random.randint(1, 2)
            power = random.randint(2, 3)
            latex = f"\\text{{Expand: }} ({coeff}x^{{{exp_x}}}y^{{{exp_y}}}z^{{{exp_z}}})^{{{power}}}"
            solution = f"{coeff**power}x^{{{exp_x*power}}}y^{{{exp_y*power}}}z^{{{exp_z*power}}}"

        elif problem_type == 'simplify_fraction':
            # Simplify (x^5y^3)/(x^2y)
            exp1_x = random.randint(5, 8)
            exp2_x = random.randint(2, 4)
            exp1_y = random.randint(4, 7)
            exp2_y = random.randint(1, 3)
            latex = f"\\text{{Simplify: }} \\frac{{x^{{{exp1_x}}}y^{{{exp1_y}}}}}{{x^{{{exp2_x}}}y^{{{exp2_y}}}}}"
            solution = f"x^{{{exp1_x - exp2_x}}}y^{{{exp1_y - exp2_y}}}"

        else:  # expand_nested
            # Expand and simplify (x^2)^3 · (x^3)^2
            exp1 = random.randint(2, 3)
            power1 = random.randint(2, 3)
            exp2 = random.randint(2, 3)
            power2 = random.randint(2, 3)
            base = random.choice(['x', 'y', 'a', 'b'])
            latex = f"\\text{{Expand and simplify: }} ({base}^{{{exp1}}})^{{{power1}}} \\cdot ({base}^{{{exp2}}})^{{{power2}}}"
            total_exp = exp1 * power1 + exp2 * power2
            solution = f"{base}^{{{total_exp}}}"

        return ExpandingExponentProblem(
            latex=latex,
            solution=solution,
            difficulty='challenge',
            problem_type=problem_type
        )


if __name__ == "__main__":
    # Test the generator
    gen = ExpandingExponentsGenerator()

    print("Testing Expanding Exponents Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Answer: {problem.solution}")
            print(f"   Type: {problem.problem_type}")