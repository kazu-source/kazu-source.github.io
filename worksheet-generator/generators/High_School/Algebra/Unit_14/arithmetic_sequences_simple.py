"""
Simplified Arithmetic Sequences Generator
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation
from typing import List


class ArithmeticSequencesSimpleGenerator:
    """Generator for arithmetic sequences problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate a worksheet of arithmetic sequences problems."""
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
        """Generate easy: Find next term or common difference"""
        problem_type = random.choice(['next_term', 'common_diff'])

        # Generate sequence
        a1 = random.randint(-10, 10)
        d = random.randint(-5, 5)
        while d == 0:
            d = random.randint(-5, 5)

        # Generate first few terms
        terms = [a1 + i * d for i in range(4)]
        seq_str = ", ".join(map(str, terms))

        if problem_type == 'next_term':
            latex = f"\\text{{Next term: }} {seq_str}, ..."
            solution = a1 + 4 * d
        else:  # common_diff
            latex = f"\\text{{Common difference: }} {seq_str}, ..."
            solution = d

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Find pattern between consecutive terms"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: Find nth term"""
        a1 = random.randint(-20, 20)
        d = random.randint(-10, 10)
        while d == 0:
            d = random.randint(-10, 10)
        n = random.randint(10, 25)

        # Show first few terms
        terms = [a1 + i * d for i in range(3)]
        seq_str = ", ".join(map(str, terms))

        latex = f"\\text{{Find }} a_{{{n}}} \\text{{ for: }} {seq_str}, ..."

        # Calculate nth term: a_n = a_1 + (n-1)d
        solution = a1 + (n - 1) * d

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"Use formula: a_n = a_1 + (n-1)d"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: Find sum of first n terms"""
        a1 = random.randint(-10, 10)
        d = random.randint(-5, 5)
        while d == 0:
            d = random.randint(-5, 5)
        n = random.randint(10, 20)

        # Show first few terms
        terms = [a1 + i * d for i in range(3)]
        seq_str = ", ".join(map(str, terms))

        latex = f"\\text{{Sum of first }} {n} \\text{{ terms: }} {seq_str}, ..."

        # Calculate sum: S_n = n/2 * (2a_1 + (n-1)d)
        solution = n * (2 * a1 + (n - 1) * d) // 2

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Use formula: S_n = n/2 * (2a_1 + (n-1)d)"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Find term number or complex sum"""
        problem_type = random.choice(['find_n', 'partial_sum'])

        if problem_type == 'find_n':
            a1 = random.randint(-10, 10)
            d = random.randint(2, 5)  # Positive for simplicity
            n = random.randint(15, 30)
            target = a1 + (n - 1) * d

            # Show first few terms
            terms = [a1 + i * d for i in range(3)]
            seq_str = ", ".join(map(str, terms))

            latex = f"\\text{{Which term equals }} {target} \\text{{: }} {seq_str}, ..."
            solution = n

        else:  # partial_sum
            a1 = random.randint(1, 10)
            d = random.randint(2, 5)
            m = random.randint(5, 10)
            n = random.randint(m + 10, m + 20)

            latex = f"\\text{{Sum from term }} {m} \\text{{ to }} {n} \\text{{ with }} a_1={a1}, d={d}"

            # Sum from m to n = S_n - S_(m-1)
            sum_n = n * (2 * a1 + (n - 1) * d) // 2
            sum_m_minus_1 = (m - 1) * (2 * a1 + (m - 2) * d) // 2 if m > 1 else 0
            solution = sum_n - sum_m_minus_1

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Apply arithmetic sequence formulas"],
            difficulty='challenge'
        )