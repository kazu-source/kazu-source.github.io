"""
Advanced Properties of Radicals Generator - Unit 7
Generates problems about radical properties including multiplication and fractions
"""

import random
import math
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class RadicalPropertyProblem:
    """Represents a radical property problem."""
    latex: str  # LaTeX formatted problem
    solution: str  # The simplified answer
    difficulty: str
    problem_type: str  # Type of radical problem


class RadicalPropertiesGenerator:
    """Generates problems about advanced properties of radicals."""

    def __init__(self, seed=None):
        """Initialize the radical properties generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[RadicalPropertyProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of RadicalPropertyProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> RadicalPropertyProblem:
        """Generate a single radical property problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _simplify_radical(self, n: int) -> Tuple[int, int]:
        """
        Simplify a radical by factoring out perfect squares.
        Returns (coefficient, radicand) where result is coefficient * sqrt(radicand)
        """
        coefficient = 1
        radicand = n

        # Factor out perfect squares
        for i in range(int(math.sqrt(n)), 1, -1):
            if n % (i * i) == 0:
                coefficient = i
                radicand = n // (i * i)
                break

        return coefficient, radicand

    def _generate_easy(self) -> RadicalPropertyProblem:
        """Generate easy radical property problems (simple multiplication, basic simplification)."""
        problem_type = random.choice(['multiply_radicals', 'simplify_radical', 'square_root_of_square'])

        if problem_type == 'multiply_radicals':
            # √a · √b = √(ab)
            a = random.choice([2, 3, 5, 7])
            b = random.choice([2, 3, 5, 7])
            product = a * b
            latex = f"\\sqrt{{{a}}} \\cdot \\sqrt{{{b}}}"

            # Simplify the result
            coeff, rad = self._simplify_radical(product)
            if coeff == 1:
                solution = f"\\sqrt{{{rad}}}"
            elif rad == 1:
                solution = f"{coeff}"
            else:
                solution = f"{coeff}\\sqrt{{{rad}}}"

        elif problem_type == 'simplify_radical':
            # Simplify √(perfect square * prime)
            perfect = random.choice([4, 9, 16, 25])
            prime = random.choice([2, 3, 5, 7])
            n = perfect * prime
            latex = f"\\text{{Simplify: }} \\sqrt{{{n}}}"
            sqrt_perfect = int(math.sqrt(perfect))
            solution = f"{sqrt_perfect}\\sqrt{{{prime}}}"

        else:  # square_root_of_square
            # √(x²) = |x| (we'll assume x > 0 for simplicity)
            base = random.choice(['x', 'y', 'a', 'b'])
            latex = f"\\text{{Simplify (assume {base} > 0): }} \\sqrt{{{base}^2}}"
            solution = base

        return RadicalPropertyProblem(
            latex=latex,
            solution=solution,
            difficulty='easy',
            problem_type=problem_type
        )

    def _generate_medium(self) -> RadicalPropertyProblem:
        """Generate medium radical property problems (multiplication with coefficients, fractions)."""
        problem_type = random.choice(['multiply_with_coeff', 'radical_fraction', 'add_like_radicals'])

        if problem_type == 'multiply_with_coeff':
            # 2√3 · 3√2
            coeff1 = random.randint(2, 5)
            coeff2 = random.randint(2, 5)
            rad1 = random.choice([2, 3, 5, 6])
            rad2 = random.choice([2, 3, 5, 6])
            latex = f"{coeff1}\\sqrt{{{rad1}}} \\cdot {coeff2}\\sqrt{{{rad2}}}"

            total_coeff = coeff1 * coeff2
            product = rad1 * rad2
            inner_coeff, final_rad = self._simplify_radical(product)
            final_coeff = total_coeff * inner_coeff

            if final_rad == 1:
                solution = f"{final_coeff}"
            else:
                solution = f"{final_coeff}\\sqrt{{{final_rad}}}"

        elif problem_type == 'radical_fraction':
            # √(a/b) = √a/√b
            numerator = random.choice([4, 9, 16, 25, 36])
            denominator = random.choice([4, 9, 16, 25])
            latex = f"\\sqrt{{\\frac{{{numerator}}}{{{denominator}}}}}"
            sqrt_num = int(math.sqrt(numerator)) if math.sqrt(numerator).is_integer() else f"\\sqrt{{{numerator}}}"
            sqrt_den = int(math.sqrt(denominator))
            if isinstance(sqrt_num, int):
                if sqrt_num % sqrt_den == 0:
                    solution = f"{sqrt_num // sqrt_den}"
                else:
                    solution = f"\\frac{{{sqrt_num}}}{{{sqrt_den}}}"
            else:
                solution = f"\\frac{{\\sqrt{{{numerator}}}}}{{{sqrt_den}}}"

        else:  # add_like_radicals
            # 2√3 + 3√3 = 5√3
            rad = random.choice([2, 3, 5, 7])
            coeff1 = random.randint(2, 5)
            coeff2 = random.randint(2, 5)
            latex = f"{coeff1}\\sqrt{{{rad}}} + {coeff2}\\sqrt{{{rad}}}"
            solution = f"{coeff1 + coeff2}\\sqrt{{{rad}}}"

        return RadicalPropertyProblem(
            latex=latex,
            solution=solution,
            difficulty='medium',
            problem_type=problem_type
        )

    def _generate_hard(self) -> RadicalPropertyProblem:
        """Generate hard radical property problems (complex expressions, rationalizing denominators)."""
        problem_type = random.choice(['rationalize_denominator', 'complex_multiplication', 'nested_radicals'])

        if problem_type == 'rationalize_denominator':
            # 1/√a = √a/a
            a = random.choice([2, 3, 5, 7])
            latex = f"\\text{{Rationalize: }} \\frac{{1}}{{\\sqrt{{{a}}}}}"
            solution = f"\\frac{{\\sqrt{{{a}}}}}{{{a}}}"

        elif problem_type == 'complex_multiplication':
            # (√a + √b)(√a - √b) = a - b
            a = random.choice([5, 7, 8, 12])
            b = random.choice([2, 3, 5])
            if a == b:
                a += 2
            latex = f"(\\sqrt{{{a}}} + \\sqrt{{{b}}})(\\sqrt{{{a}}} - \\sqrt{{{b}}})"
            solution = f"{a - b}"

        else:  # nested_radicals
            # Simplify √(4x²y⁴)
            coeff = random.choice([4, 9, 16])
            sqrt_coeff = int(math.sqrt(coeff))
            latex = f"\\text{{Simplify (assume x, y > 0): }} \\sqrt{{{coeff}x^2y^4}}"
            solution = f"{sqrt_coeff}xy^2"

        return RadicalPropertyProblem(
            latex=latex,
            solution=solution,
            difficulty='hard',
            problem_type=problem_type
        )

    def _generate_challenge(self) -> RadicalPropertyProblem:
        """Generate challenge radical property problems (cube roots, complex rationalizations)."""
        problem_type = random.choice(['cube_root', 'complex_rationalize', 'radical_equation'])

        if problem_type == 'cube_root':
            # ∛8 · ∛27 = ∛(8·27) = 6
            a = random.choice([8, 27, 64, 125])
            b = random.choice([8, 27, 64])
            cube_root_a = int(round(a ** (1/3)))
            cube_root_b = int(round(b ** (1/3)))
            latex = f"\\sqrt[3]{{{a}}} \\cdot \\sqrt[3]{{{b}}}"
            solution = f"{cube_root_a * cube_root_b}"

        elif problem_type == 'complex_rationalize':
            # Rationalize 2/(3 + √5)
            a = random.randint(2, 4)
            b = random.randint(2, 5)
            rad = random.choice([2, 3, 5, 7])
            latex = f"\\text{{Rationalize: }} \\frac{{{a}}}{{{b} + \\sqrt{{{rad}}}}}"
            # Multiply by conjugate
            denom = b**2 - rad
            if denom > 0:
                solution = f"\\frac{{{a}({b} - \\sqrt{{{rad}}})}}{{{denom}}}"
            else:
                solution = f"\\frac{{-{a}({b} - \\sqrt{{{rad}}})}}{{{-denom}}}"

        else:  # radical_equation
            # Simplify complex radical expression
            a = random.choice([2, 3, 5])
            b = random.choice([8, 12, 18, 20])
            c = random.choice([2, 3, 5])
            coeff_b, rad_b = self._simplify_radical(b)
            latex = f"\\sqrt{{{a}}} \\cdot \\sqrt{{{b}}} + {c}\\sqrt{{{rad_b}}}"

            product = a * b
            p_coeff, p_rad = self._simplify_radical(product)

            # Check if we can combine terms
            if p_rad == rad_b:
                total_coeff = p_coeff + c
                solution = f"{total_coeff}\\sqrt{{{p_rad}}}"
            else:
                if p_coeff == 1:
                    solution = f"\\sqrt{{{p_rad}}} + {c}\\sqrt{{{rad_b}}}"
                else:
                    solution = f"{p_coeff}\\sqrt{{{p_rad}}} + {c}\\sqrt{{{rad_b}}}"

        return RadicalPropertyProblem(
            latex=latex,
            solution=solution,
            difficulty='challenge',
            problem_type=problem_type
        )


if __name__ == "__main__":
    # Test the generator
    gen = RadicalPropertiesGenerator()

    print("Testing Radical Properties Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Answer: {problem.solution}")
            print(f"   Type: {problem.problem_type}")