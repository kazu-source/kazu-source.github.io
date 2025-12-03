"""
Special Products of Polynomials Generator - Unit 9
Generates problems for special products including:
- Perfect square trinomials: (a + b)² and (a - b)²
- Difference of squares: (a + b)(a - b)
- Sum and difference of cubes: (a + b)³ and (a - b)³
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SpecialProductsOfPolynomialsGenerator:
    """Generates special products of polynomials problems."""

    def __init__(self, seed=None):
        """Initialize the special products generator."""
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
        """Generate a single special products problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _format_polynomial(self, terms: dict) -> str:
        """
        Format a polynomial from a dictionary of {degree: coefficient}.
        Returns a LaTeX formatted string.
        """
        if not terms or all(coeff == 0 for coeff in terms.values()):
            return "0"

        result = []
        for degree in sorted(terms.keys(), reverse=True):
            coeff = terms[degree]
            if coeff == 0:
                continue

            if degree == 0:
                # Constant term
                if result:
                    result.append(f"{coeff:+d}")
                else:
                    result.append(str(coeff))
            elif degree == 1:
                # Linear term
                if coeff == 1:
                    term = "x" if not result else "+x"
                elif coeff == -1:
                    term = "-x"
                else:
                    term = f"{coeff:+d}x" if result else f"{coeff}x"
                result.append(term)
            else:
                # Higher degree terms
                if coeff == 1:
                    term = f"x^{{{degree}}}" if not result else f"+x^{{{degree}}}"
                elif coeff == -1:
                    term = f"-x^{{{degree}}}"
                else:
                    term = f"{coeff:+d}x^{{{degree}}}" if result else f"{coeff}x^{{{degree}}}"
                result.append(term)

        return "".join(result).replace("+-", "-")

    def _generate_easy(self) -> Equation:
        """
        Generate easy special products problems.
        Expand simple special products with small integers.
        """
        problem_type = random.choice(['square_sum', 'square_diff', 'diff_squares'])

        if problem_type == 'square_sum':
            # (x + b)² = x² + 2bx + b²
            b = random.randint(1, 5)
            latex = f"\\text{{Expand: }} (x + {b})^2"

            # Result: x² + 2bx + b²
            result = {2: 1, 1: 2*b, 0: b*b}
            solution = self._format_polynomial(result)
            steps = [f"(x + {b})^2 = x^2 + 2({b})x + {b}^2", solution]

        elif problem_type == 'square_diff':
            # (x - b)² = x² - 2bx + b²
            b = random.randint(1, 5)
            latex = f"\\text{{Expand: }} (x - {b})^2"

            # Result: x² - 2bx + b²
            result = {2: 1, 1: -2*b, 0: b*b}
            solution = self._format_polynomial(result)
            steps = [f"(x - {b})^2 = x^2 - 2({b})x + {b}^2", solution]

        else:  # diff_squares
            # (x + b)(x - b) = x² - b²
            b = random.randint(1, 6)
            latex = f"\\text{{Expand: }} (x + {b})(x - {b})"

            # Result: x² - b²
            result = {2: 1, 0: -b*b}
            solution = self._format_polynomial(result)
            steps = [f"(x + {b})(x - {b}) = x^2 - {b}^2", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """
        Generate medium special products problems.
        Expand with variables and coefficients.
        """
        problem_type = random.choice(['square_sum_coeff', 'square_diff_coeff', 'diff_squares_coeff', 'two_variables'])

        if problem_type == 'square_sum_coeff':
            # (ax + b)² = a²x² + 2abx + b²
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            latex = f"\\text{{Expand: }} ({a}x + {b})^2"

            # Result: a²x² + 2abx + b²
            result = {2: a*a, 1: 2*a*b, 0: b*b}
            solution = self._format_polynomial(result)
            steps = [f"({a}x + {b})^2 = ({a}x)^2 + 2({a}x)({b}) + {b}^2", solution]

        elif problem_type == 'square_diff_coeff':
            # (ax - b)² = a²x² - 2abx + b²
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            latex = f"\\text{{Expand: }} ({a}x - {b})^2"

            # Result: a²x² - 2abx + b²
            result = {2: a*a, 1: -2*a*b, 0: b*b}
            solution = self._format_polynomial(result)
            steps = [f"({a}x - {b})^2 = ({a}x)^2 - 2({a}x)({b}) + {b}^2", solution]

        elif problem_type == 'diff_squares_coeff':
            # (ax + b)(ax - b) = a²x² - b²
            a = random.randint(2, 4)
            b = random.randint(1, 6)
            latex = f"\\text{{Expand: }} ({a}x + {b})({a}x - {b})"

            # Result: a²x² - b²
            result = {2: a*a, 0: -b*b}
            solution = self._format_polynomial(result)
            steps = [f"({a}x + {b})({a}x - {b}) = ({a}x)^2 - {b}^2", solution]

        else:  # two_variables
            # (x + y)² = x² + 2xy + y²
            latex = f"\\text{{Expand: }} (x + y)^2"
            solution = "x^2 + 2xy + y^2"
            steps = ["(x + y)^2 = x^2 + 2xy + y^2", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """
        Generate hard special products problems.
        Factor expressions back into special product form.
        """
        problem_type = random.choice(['factor_perfect_square', 'factor_diff_squares', 'identify_and_expand'])

        if problem_type == 'factor_perfect_square':
            # Factor x² + 2bx + b² into (x + b)²
            # or x² - 2bx + b² into (x - b)²
            is_sum = random.choice([True, False])

            if is_sum:
                b = random.randint(2, 6)
                # x² + 2bx + b²
                result = {2: 1, 1: 2*b, 0: b*b}
                latex = f"\\text{{Factor: }} " + self._format_polynomial(result)
                solution = f"(x + {b})^2"
                steps = [f"\\text{{Perfect square trinomial}}", solution]
            else:
                b = random.randint(2, 6)
                # x² - 2bx + b²
                result = {2: 1, 1: -2*b, 0: b*b}
                latex = f"\\text{{Factor: }} " + self._format_polynomial(result)
                solution = f"(x - {b})^2"
                steps = [f"\\text{{Perfect square trinomial}}", solution]

        elif problem_type == 'factor_diff_squares':
            # Factor x² - b² into (x + b)(x - b)
            b = random.randint(2, 8)
            result = {2: 1, 0: -b*b}
            latex = f"\\text{{Factor: }} " + self._format_polynomial(result)
            solution = f"(x + {b})(x - {b})"
            steps = [f"\\text{{Difference of squares}}", solution]

        else:  # identify_and_expand
            # Expand a more complex perfect square
            a = random.randint(2, 3)
            b = random.randint(2, 4)
            is_sum = random.choice([True, False])

            if is_sum:
                latex = f"\\text{{Expand: }} ({a}x + {b})^2"
                result = {2: a*a, 1: 2*a*b, 0: b*b}
            else:
                latex = f"\\text{{Expand: }} ({a}x - {b})^2"
                result = {2: a*a, 1: -2*a*b, 0: b*b}

            solution = self._format_polynomial(result)
            steps = [f"\\text{{Use perfect square formula}}", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """
        Generate challenge special products problems.
        Sum/difference of cubes and multi-step problems.
        """
        problem_type = random.choice(['cube_sum', 'cube_diff', 'multi_step', 'factor_complex'])

        if problem_type == 'cube_sum':
            # (x + b)³ = x³ + 3x²b + 3xb² + b³
            b = random.randint(1, 4)
            latex = f"\\text{{Expand: }} (x + {b})^3"

            # Result: x³ + 3bx² + 3b²x + b³
            result = {3: 1, 2: 3*b, 1: 3*b*b, 0: b*b*b}
            solution = self._format_polynomial(result)
            steps = [f"(x + {b})^3 = x^3 + 3x^2({b}) + 3x({b})^2 + {b}^3", solution]

        elif problem_type == 'cube_diff':
            # (x - b)³ = x³ - 3x²b + 3xb² - b³
            b = random.randint(1, 4)
            latex = f"\\text{{Expand: }} (x - {b})^3"

            # Result: x³ - 3bx² + 3b²x - b³
            result = {3: 1, 2: -3*b, 1: 3*b*b, 0: -b*b*b}
            solution = self._format_polynomial(result)
            steps = [f"(x - {b})^3 = x^3 - 3x^2({b}) + 3x({b})^2 - {b}^3", solution]

        elif problem_type == 'multi_step':
            # Expand (x + a)² - (x - b)²
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            latex = f"\\text{{Expand: }} (x + {a})^2 - (x - {b})^2"

            # (x + a)² = x² + 2ax + a²
            # (x - b)² = x² - 2bx + b²
            # Difference: 2ax + a² - (-2bx + b²) = 2ax + 2bx + a² - b²
            result = {1: 2*a + 2*b, 0: a*a - b*b}
            solution = self._format_polynomial(result)
            steps = [
                f"(x + {a})^2 - (x - {b})^2",
                f"(x^2 + {2*a}x + {a*a}) - (x^2 - {2*b}x + {b*b})",
                solution
            ]

        else:  # factor_complex
            # Factor a²x² - b² with coefficients
            a = random.randint(2, 4)
            b = random.randint(3, 7)

            result = {2: a*a, 0: -b*b}
            latex = f"\\text{{Factor: }} " + self._format_polynomial(result)
            solution = f"({a}x + {b})({a}x - {b})"
            steps = [f"\\text{{Difference of squares}}", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = SpecialProductsOfPolynomialsGenerator()

    print("Testing Special Products of Polynomials Generator")
    print("=" * 70)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 70)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Answer: {problem.solution}")
            print(f"   Steps: {' -> '.join(problem.steps)}")
            print()
