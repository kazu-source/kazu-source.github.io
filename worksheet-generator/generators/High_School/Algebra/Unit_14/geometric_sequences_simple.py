"""
Simplified Geometric Sequences Generator
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation
from typing import List


class GeometricSequencesSimpleGenerator:
    """Generator for geometric sequences problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate a worksheet of geometric sequences problems."""
        problems = []
        for _ in range(num_problems):
            if difficulty == 'easy':
                problem = self._generate_easy()
            elif difficulty == 'medium':
                problem = self._generate_medium()
            elif difficulty == 'hard':
                problem = self._generate_hard()
            else:  # challenge
                problem = self._generate_challenge()
            problems.append(problem)
        return problems

    def _generate_easy(self) -> Equation:
        """Generate easy: Find next term or common ratio"""
        problem_type = random.choice(['next_term', 'common_ratio'])

        # Generate sequence with simple ratio
        a1 = random.choice([1, 2, 3, 4, 5])
        r = random.choice([2, 3, -2, 0.5])

        # Generate first few terms
        terms = [a1 * (r ** i) for i in range(4)]

        # Format as integers or simple decimals
        formatted_terms = []
        for t in terms:
            if t == int(t):
                formatted_terms.append(str(int(t)))
            else:
                formatted_terms.append(str(t))

        seq_str = ", ".join(formatted_terms)

        if problem_type == 'next_term':
            latex = f"\\text{{Next term: }} {seq_str}, ..."
            solution = a1 * (r ** 4)
        else:  # common_ratio
            latex = f"\\text{{Common ratio: }} {seq_str}, ..."
            solution = r

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Find ratio between consecutive terms"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: Find nth term"""
        a1 = random.choice([2, 3, 4, 5])
        r = random.choice([2, 3, -2])
        n = random.randint(5, 8)

        # Show first few terms
        terms = [a1 * (r ** i) for i in range(3)]
        seq_str = ", ".join(map(str, terms))

        latex = f"\\text{{Find }} a_{{{n}}} \\text{{ for: }} {seq_str}, ..."

        # Calculate nth term: a_n = a_1 * r^(n-1)
        solution = a1 * (r ** (n - 1))

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"Use formula: a_n = a_1 * r^(n-1)"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: Find sum of first n terms"""
        a1 = random.choice([2, 3, 4, 5])
        r = random.choice([2, 3])
        n = random.randint(5, 7)

        # Show first few terms
        terms = [a1 * (r ** i) for i in range(3)]
        seq_str = ", ".join(map(str, terms))

        latex = f"\\text{{Sum of first }} {n} \\text{{ terms: }} {seq_str}, ..."

        # Calculate sum: S_n = a_1 * (1 - r^n) / (1 - r) for r ≠ 1
        if r != 1:
            solution = int(a1 * (1 - r**n) / (1 - r))
        else:
            solution = a1 * n

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Use formula: S_n = a_1 * (1 - r^n) / (1 - r)"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Find term number or exponential growth problem"""
        problem_type = random.choice(['find_n', 'growth'])

        if problem_type == 'find_n':
            a1 = random.choice([2, 3, 4])
            r = random.choice([2, 3])
            n = random.randint(4, 6)
            target = a1 * (r ** (n - 1))

            # Show first few terms
            terms = [a1 * (r ** i) for i in range(3)]
            seq_str = ", ".join(map(str, terms))

            latex = f"\\text{{Which term equals }} {target} \\text{{: }} {seq_str}, ..."
            solution = n

        else:  # growth
            initial = random.choice([100, 200, 500])
            rate = random.choice([1.1, 1.2, 1.5])  # 10%, 20%, or 50% growth
            years = random.randint(3, 5)

            percent = int((rate - 1) * 100)
            latex = f"\\text{{Investment: \\$}}{initial} \\text{{ grows }} {percent}\\% \\text{{ yearly. Value after }} {years} \\text{{ years?}}"

            # Calculate: A = P * r^t
            solution = round(initial * (rate ** years))

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Apply geometric sequence or exponential growth formula"],
            difficulty='challenge'
        )