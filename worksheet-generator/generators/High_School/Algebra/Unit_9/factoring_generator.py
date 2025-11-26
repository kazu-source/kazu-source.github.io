"""
Factoring Generator - Unit 9
Generates problems for factoring monomials, polynomials with common factors, quadratics, and special patterns
"""

import random
import math
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class FactoringProblem:
    """Represents a factoring problem."""
    latex: str  # LaTeX formatted problem
    solution: str  # The factored form
    difficulty: str
    problem_type: str  # Type of factoring


class FactoringGenerator:
    """Generates factoring problems."""

    def __init__(self, seed=None):
        """Initialize the factoring generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[FactoringProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of FactoringProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> FactoringProblem:
        """Generate a single factoring problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _gcd(self, a: int, b: int) -> int:
        """Find the greatest common divisor."""
        return math.gcd(abs(a), abs(b))

    def _generate_easy(self) -> FactoringProblem:
        """Generate easy factoring problems (common factors, simple monomials)."""
        problem_type = random.choice(['factor_monomial', 'common_factor', 'factor_by_grouping_simple'])

        if problem_type == 'factor_monomial':
            # Factor out a monomial
            common = random.randint(2, 6)
            exp = random.randint(1, 3)
            term1_coeff = common * random.randint(2, 5)
            term2_coeff = common * random.randint(2, 5)

            latex = f"\\text{{Factor: }} {term1_coeff}x^{{{exp + 1}}} + {term2_coeff}x^{{{exp}}}"
            solution = f"{common}x^{{{exp}}}({term1_coeff // common}x + {term2_coeff // common})"

        elif problem_type == 'common_factor':
            # Factor out common numerical factor
            common = random.randint(2, 8)
            a = common * random.randint(1, 5)
            b = common * random.randint(1, 5)
            c = common * random.randint(1, 5)

            latex = f"\\text{{Factor: }} {a}x^2 + {b}x + {c}"
            solution = f"{common}({a // common}x^2 + {b // common}x + {c // common})"

        else:  # factor_by_grouping_simple
            # Simple grouping: ax + bx + ay + by
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            latex = f"\\text{{Factor by grouping: }} {a}x + {b}x + {a}y + {b}y"
            solution = f"(x + y)({a} + {b})"

        return FactoringProblem(
            latex=latex,
            solution=solution,
            difficulty='easy',
            problem_type=problem_type
        )

    def _generate_medium(self) -> FactoringProblem:
        """Generate medium factoring problems (simple quadratics, difference of squares)."""
        problem_type = random.choice(['factor_quadratic_simple', 'difference_of_squares', 'common_binomial'])

        if problem_type == 'factor_quadratic_simple':
            # Factor x^2 + bx + c where b and c are small
            # We want (x + p)(x + q) = x^2 + (p+q)x + pq
            p = random.randint(-6, 6)
            q = random.randint(-6, 6)
            if p == 0:
                p = 1
            if q == 0:
                q = 1

            b = p + q
            c = p * q

            # Format the quadratic
            if b == 0:
                latex = f"\\text{{Factor: }} x^2 {c:+d}"
            elif b == 1:
                latex = f"\\text{{Factor: }} x^2 + x {c:+d}"
            elif b == -1:
                latex = f"\\text{{Factor: }} x^2 - x {c:+d}"
            else:
                latex = f"\\text{{Factor: }} x^2 {b:+d}x {c:+d}"

            latex = latex.replace("+-", "-")

            # Format the solution
            factor1 = f"(x {p:+d})".replace("+-", "-")
            factor2 = f"(x {q:+d})".replace("+-", "-")
            solution = f"{factor1}{factor2}"

        elif problem_type == 'difference_of_squares':
            # Factor a^2 - b^2
            a_coeff = random.randint(1, 5)
            b_val = random.randint(1, 8)

            if a_coeff == 1:
                latex = f"\\text{{Factor: }} x^2 - {b_val**2}"
                solution = f"(x + {b_val})(x - {b_val})"
            else:
                latex = f"\\text{{Factor: }} {a_coeff**2}x^2 - {b_val**2}"
                solution = f"({a_coeff}x + {b_val})({a_coeff}x - {b_val})"

        else:  # common_binomial
            # Factor out a common binomial
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            latex = f"\\text{{Factor: }} x(x + {a}) + {b}(x + {a})"
            solution = f"(x + {a})(x + {b})"

        return FactoringProblem(
            latex=latex,
            solution=solution,
            difficulty='medium',
            problem_type=problem_type
        )

    def _generate_hard(self) -> FactoringProblem:
        """Generate hard factoring problems (complex quadratics, perfect square trinomials)."""
        problem_type = random.choice(['factor_quadratic_complex', 'perfect_square_trinomial', 'factor_by_grouping'])

        if problem_type == 'factor_quadratic_complex':
            # Factor ax^2 + bx + c where a > 1
            # We want (px + q)(rx + s) = prx^2 + (ps + qr)x + qs
            p = random.randint(1, 3)
            q = random.randint(-5, 5)
            r = random.randint(1, 3)
            s = random.randint(-5, 5)

            if q == 0:
                q = 1
            if s == 0:
                s = 1

            a = p * r
            b = p * s + q * r
            c = q * s

            # Format the problem
            latex = f"\\text{{Factor: }} {a}x^2 {b:+d}x {c:+d}".replace("+-", "-")

            # Format the solution
            factor1 = f"({p}x {q:+d})" if p > 1 else f"(x {q:+d})"
            factor2 = f"({r}x {s:+d})" if r > 1 else f"(x {s:+d})"
            solution = f"{factor1}{factor2}".replace("+-", "-")

        elif problem_type == 'perfect_square_trinomial':
            # Factor (ax + b)^2
            a = random.randint(1, 4)
            b = random.randint(1, 6)

            # Expand to get a^2x^2 + 2abx + b^2
            coeff_x2 = a * a
            coeff_x = 2 * a * b
            const = b * b

            if a == 1:
                latex = f"\\text{{Factor: }} x^2 + {coeff_x}x + {const}"
                solution = f"(x + {b})^2"
            else:
                latex = f"\\text{{Factor: }} {coeff_x2}x^2 + {coeff_x}x + {const}"
                solution = f"({a}x + {b})^2"

        else:  # factor_by_grouping
            # More complex grouping
            # ac*x^2 + ad*x + bc*x + bd = (ax + b)(cx + d)
            a = random.randint(2, 4)
            b = random.randint(-5, 5)
            c = random.randint(2, 4)
            d = random.randint(-5, 5)

            if b == 0:
                b = 1
            if d == 0:
                d = 1

            term1 = a * c
            term2 = a * d
            term3 = b * c
            term4 = b * d

            latex = f"\\text{{Factor by grouping: }} {term1}x^2 {term2:+d}x {term3:+d}x {term4:+d}".replace("+-", "-")

            factor1 = f"({a}x {b:+d})".replace("+-", "-")
            factor2 = f"({c}x {d:+d})".replace("+-", "-")
            solution = f"{factor1}{factor2}"

        return FactoringProblem(
            latex=latex,
            solution=solution,
            difficulty='hard',
            problem_type=problem_type
        )

    def _generate_challenge(self) -> FactoringProblem:
        """Generate challenge factoring problems (sum/difference of cubes, complex patterns)."""
        problem_type = random.choice(['sum_difference_cubes', 'factor_completely', 'complex_grouping'])

        if problem_type == 'sum_difference_cubes':
            # Factor a^3 ± b^3
            is_sum = random.choice([True, False])
            a = random.randint(1, 3)
            b = random.randint(1, 4)

            if is_sum:
                # a^3 + b^3 = (a + b)(a^2 - ab + b^2)
                if a == 1:
                    latex = f"\\text{{Factor: }} x^3 + {b**3}"
                    solution = f"(x + {b})(x^2 - {b}x + {b**2})"
                else:
                    latex = f"\\text{{Factor: }} {a**3}x^3 + {b**3}"
                    solution = f"({a}x + {b})({a**2}x^2 - {a*b}x + {b**2})"
            else:
                # a^3 - b^3 = (a - b)(a^2 + ab + b^2)
                if a == 1:
                    latex = f"\\text{{Factor: }} x^3 - {b**3}"
                    solution = f"(x - {b})(x^2 + {b}x + {b**2})"
                else:
                    latex = f"\\text{{Factor: }} {a**3}x^3 - {b**3}"
                    solution = f"({a}x - {b})({a**2}x^2 + {a*b}x + {b**2})"

        elif problem_type == 'factor_completely':
            # Factor completely - first take out common factor, then factor quadratic
            common = random.randint(2, 4)
            p = random.randint(-4, 4)
            q = random.randint(-4, 4)
            if p == 0:
                p = 1
            if q == 0:
                q = 1

            # Start with common(x + p)(x + q) and expand
            a = common
            b = common * (p + q)
            c = common * p * q

            latex = f"\\text{{Factor completely: }} {a}x^2 {b:+d}x {c:+d}".replace("+-", "-")

            factor1 = f"(x {p:+d})".replace("+-", "-")
            factor2 = f"(x {q:+d})".replace("+-", "-")
            solution = f"{common}{factor1}{factor2}"

        else:  # complex_grouping
            # Factor x^4 - y^4 (difference of squares twice)
            latex = f"\\text{{Factor completely: }} x^4 - 16"
            solution = f"(x^2 + 4)(x + 2)(x - 2)"

        return FactoringProblem(
            latex=latex,
            solution=solution,
            difficulty='challenge',
            problem_type=problem_type
        )


if __name__ == "__main__":
    # Test the generator
    gen = FactoringGenerator()

    print("Testing Factoring Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Answer: {problem.solution}")
            print(f"   Type: {problem.problem_type}")