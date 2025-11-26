"""
Absolute Value Inequalities Generator - Solving inequalities with absolute value
Generates problems for solving |x| < a, |x| > a, and more complex forms
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class AbsoluteValueInequalitiesGenerator:
    """Generates absolute value inequality problems."""

    def __init__(self, seed=None):
        """Initialize the absolute value inequalities generator."""
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
        """Generate a single absolute value inequality problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple absolute value inequality: |x| < a or |x| > a"""
        a = random.randint(3, 12)
        inequality_type = random.choice(['less', 'greater', 'leq', 'geq'])

        if inequality_type == 'less':
            latex = f"|x| < {a}"
            solution = f"-{a} < x < {a}"
        elif inequality_type == 'greater':
            latex = f"|x| > {a}"
            solution = f"x < -{a} \\text{{ or }} x > {a}"
        elif inequality_type == 'leq':
            latex = f"|x| \\leq {a}"
            solution = f"-{a} \\leq x \\leq {a}"
        else:  # geq
            latex = f"|x| \\geq {a}"
            solution = f"x \\leq -{a} \\text{{ or }} x \\geq {a}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate absolute value inequality with linear expression: |x + b| < a"""
        a = random.randint(4, 10)
        b = random.randint(-8, 8)
        if b == 0:
            b = 3

        inequality_type = random.choice(['less', 'greater'])

        if b > 0:
            expr = f"x + {b}"
        elif b < 0:
            expr = f"x - {-b}"

        if inequality_type == 'less':
            latex = f"|{expr}| < {a}"
            left = -a - b
            right = a - b
            solution = f"{left} < x < {right}"
        else:  # greater
            latex = f"|{expr}| > {a}"
            left = -a - b
            right = a - b
            solution = f"x < {left} \\text{{ or }} x > {right}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate absolute value inequality with coefficient: |ax + b| < c"""
        a = random.randint(2, 4)
        b = random.randint(-10, 10)
        c = random.randint(6, 15)

        inequality_type = random.choice(['less', 'greater', 'leq', 'geq'])

        if b >= 0:
            expr = f"{a}x + {b}" if a > 1 else f"x + {b}"
        else:
            expr = f"{a}x - {-b}" if a > 1 else f"x - {-b}"

        if inequality_type in ['less', 'leq']:
            sign = '<' if inequality_type == 'less' else '\\leq'
            latex = f"|{expr}| {sign} {c}"
            # -c < ax + b < c
            left = (-c - b) / a
            right = (c - b) / a
            if left == int(left):
                left = int(left)
            if right == int(right):
                right = int(right)
            solution = f"{left} {sign} x {sign} {right}"
        else:  # greater or geq
            sign = '>' if inequality_type == 'greater' else '\\geq'
            latex = f"|{expr}| {sign} {c}"
            # ax + b < -c or ax + b > c
            left = (-c - b) / a
            right = (c - b) / a
            if left == int(left):
                left = int(left)
            if right == int(right):
                right = int(right)
            solution = f"x {sign.replace('>', '<').replace('\\geq', '\\leq')} {left} \\text{{ or }} x {sign} {right}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate complex absolute value inequality: |ax + b| < |cx + d|"""
        problem_type = random.choice(['double_abs', 'nested', 'compound'])

        if problem_type == 'double_abs':
            a = random.randint(2, 4)
            b = random.randint(-5, 5)
            c = random.randint(1, 3)
            d = random.randint(-5, 5)

            if b >= 0:
                expr1 = f"{a}x + {b}" if a > 1 else f"x + {b}"
            else:
                expr1 = f"{a}x - {-b}" if a > 1 else f"x - {-b}"

            if d >= 0:
                expr2 = f"{c}x + {d}" if c > 1 else f"x + {d}"
            else:
                expr2 = f"{c}x - {-d}" if c > 1 else f"x - {-d}"

            latex = f"|{expr1}| < |{expr2}|"
            # This is complex to solve algebraically, provide interval notation
            solution = "\\text{Solve by cases}"

        elif problem_type == 'nested':
            a = random.randint(3, 8)
            b = random.randint(2, 5)
            latex = f"||x| - {a}| < {b}"
            # |x| - a < b and |x| - a > -b
            # |x| < a + b and |x| > a - b
            upper = a + b
            lower = max(0, a - b)
            if lower == 0:
                solution = f"-{upper} < x < {upper}"
            else:
                solution = f"x < -{upper} \\text{{ or }} x > {upper} \\text{{ or }} -{lower} < x < {lower}"

        else:  # compound
            a = random.randint(2, 6)
            b = random.randint(1, 4)
            c = random.randint(8, 12)
            latex = f"{b} < |x + {a}| < {c}"
            # b < |x + a| < c means |x + a| > b AND |x + a| < c
            # For |x + a| > b: x + a < -b or x + a > b
            # For |x + a| < c: -c < x + a < c
            solution = f"{-c - a} < x < {-b - a} \\text{{ or }} {b - a} < x < {c - a}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = AbsoluteValueInequalitiesGenerator()

    print("Testing Absolute Value Inequalities Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")