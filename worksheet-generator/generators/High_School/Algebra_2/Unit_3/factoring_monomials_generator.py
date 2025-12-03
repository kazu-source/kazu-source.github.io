"""
Factoring Monomials Generator
Creates problems about factoring single terms and finding GCF
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class FactoringMonomialsGenerator:
    """Generates problems about factoring monomials."""

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
        """Factor a single monomial into prime factors"""
        # Simple numbers with small prime factors
        factors = random.choice([
            (12, "2^2 \\cdot 3"),
            (18, "2 \\cdot 3^2"),
            (20, "2^2 \\cdot 5"),
            (24, "2^3 \\cdot 3"),
            (30, "2 \\cdot 3 \\cdot 5"),
            (36, "2^2 \\cdot 3^2"),
            (45, "3^2 \\cdot 5"),
            (48, "2^4 \\cdot 3"),
        ])

        num, factored = factors

        latex = f"\\text{{Write the prime factorization of }} {num}."
        solution = factored

        steps = [
            f"\\text{{Factor out primes:}}",
            f"{num} = {factored}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Find GCF of two or three numbers"""
        problem_type = random.choice(['two_numbers', 'with_variables'])

        if problem_type == 'two_numbers':
            gcf = random.randint(2, 8)
            mult1 = random.randint(2, 6)
            mult2 = random.randint(2, 6)
            while mult1 == mult2:
                mult2 = random.randint(2, 6)

            n1 = gcf * mult1
            n2 = gcf * mult2

            latex = f"\\text{{Find the GCF of }} {n1} \\text{{ and }} {n2}."
            solution = str(gcf)

            steps = [
                f"\\text{{Factor each number:}}",
                f"{n1} = {gcf} \\times {mult1}",
                f"{n2} = {gcf} \\times {mult2}",
                f"\\text{{GCF}} = {gcf}"
            ]
        else:
            # Variables
            coef_gcf = random.randint(2, 6)
            coef1 = coef_gcf * random.randint(2, 4)
            coef2 = coef_gcf * random.randint(2, 4)

            exp1 = random.randint(2, 4)
            exp2 = random.randint(3, 5)
            exp_min = min(exp1, exp2)

            latex = f"\\text{{Find the GCF of }} {coef1}x^{{{exp1}}} \\text{{ and }} {coef2}x^{{{exp2}}}."
            solution = f"{coef_gcf}x^{{{exp_min}}}"

            steps = [
                f"\\text{{GCF of coefficients: }} \\gcd({coef1}, {coef2}) = {coef_gcf}",
                f"\\text{{For variables, take the lowest power: }} x^{{{exp_min}}}",
                f"\\text{{GCF}} = {coef_gcf}x^{{{exp_min}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Factor out GCF from polynomial"""
        gcf_coef = random.randint(2, 5)
        gcf_exp = random.randint(1, 2)

        # Generate three terms
        c1 = random.randint(1, 4)
        c2 = random.randint(1, 4)
        c3 = random.randint(1, 4)

        e1 = gcf_exp + random.randint(1, 3)
        e2 = gcf_exp + random.randint(0, 2)
        e3 = gcf_exp

        term1 = gcf_coef * c1
        term2 = gcf_coef * c2
        term3 = gcf_coef * c3

        # Build polynomial
        poly = f"{term1}x^{{{e1}}} + {term2}x^{{{e2}}} + {term3}x^{{{e3}}}"

        latex = f"\\text{{Factor completely: }} {poly}"
        solution = f"{gcf_coef}x^{{{gcf_exp}}}({c1}x^{{{e1-gcf_exp}}} + {c2}x^{{{e2-gcf_exp}}} + {c3})"

        steps = [
            f"\\text{{Find GCF of all terms: }} {gcf_coef}x^{{{gcf_exp}}}",
            f"\\text{{Factor it out:}}",
            f"{gcf_coef}x^{{{gcf_exp}}}\\left(\\frac{{{term1}x^{{{e1}}}}}{{{gcf_coef}x^{{{gcf_exp}}}}} + \\frac{{{term2}x^{{{e2}}}}}{{{gcf_coef}x^{{{gcf_exp}}}}} + \\frac{{{term3}x^{{{e3}}}}}{{{gcf_coef}x^{{{gcf_exp}}}}}\\right)",
            f"= {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Factor with multiple variables or negative leading coefficient"""
        problem_type = random.choice(['two_variables', 'negative_lead'])

        if problem_type == 'two_variables':
            gcf = random.randint(2, 4)
            c1, c2 = random.randint(1, 3), random.randint(1, 3)

            x1, y1 = random.randint(2, 4), random.randint(1, 3)
            x2, y2 = random.randint(1, 3), random.randint(2, 4)

            x_min = min(x1, x2)
            y_min = min(y1, y2)

            term1 = f"{gcf * c1}x^{{{x1}}}y^{{{y1}}}"
            term2 = f"{gcf * c2}x^{{{x2}}}y^{{{y2}}}"

            latex = f"\\text{{Factor: }} {term1} + {term2}"
            solution = f"{gcf}x^{{{x_min}}}y^{{{y_min}}}({c1}x^{{{x1-x_min}}}y^{{{y1-y_min}}} + {c2}x^{{{x2-x_min}}}y^{{{y2-y_min}}})"

            steps = [
                f"\\text{{GCF of coefficients: }} {gcf}",
                f"\\text{{Lowest power of x: }} x^{{{x_min}}}",
                f"\\text{{Lowest power of y: }} y^{{{y_min}}}",
                f"\\text{{GCF: }} {gcf}x^{{{x_min}}}y^{{{y_min}}}",
                f"\\text{{Factor it out to get: }} {solution}"
            ]
        else:
            # Negative leading coefficient
            gcf = random.randint(2, 4)
            c1, c2, c3 = random.randint(2, 5), random.randint(1, 4), random.randint(1, 3)

            poly = f"-{gcf * c1}x^3 + {gcf * c2}x^2 - {gcf * c3}x"

            latex = f"\\text{{Factor (factor out -1 first): }} {poly}"
            solution = f"-{gcf}x({c1}x^2 - {c2}x + {c3})"

            steps = [
                f"\\text{{Factor out }} -{gcf}x:",
                f"-{gcf}x\\left(\\frac{{-{gcf * c1}x^3}}{{-{gcf}x}} + \\frac{{{gcf * c2}x^2}}{{-{gcf}x}} + \\frac{{-{gcf * c3}x}}{{-{gcf}x}}\\right)",
                f"= -{gcf}x({c1}x^2 - {c2}x + {c3})"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = FactoringMonomialsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
