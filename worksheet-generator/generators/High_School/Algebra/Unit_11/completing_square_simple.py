"""
Simplified Completing the Square Generator
"""

import random
import sys
import os
from math import sqrt
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation
from typing import List


class CompletingSquareSimpleGenerator:
    """Generator for completing the square problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate a worksheet of completing the square problems."""
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
        """Generate easy: x² + bx = c (b is even)"""
        b = random.choice([2, 4, 6, 8, -2, -4, -6, -8])
        c = random.randint(-10, 10)

        # Create LaTeX
        if b > 0:
            latex = f"x^2 + {b}x = {c}"
        else:
            latex = f"x^2 - {abs(b)}x = {c}"

        # Solve using quadratic formula for solution
        discriminant = b**2 - 4*1*(-c)
        if discriminant >= 0:
            x1 = (-b + sqrt(discriminant)) / 2
            x2 = (-b - sqrt(discriminant)) / 2
            solution = round(min(x1, x2), 2)
        else:
            solution = 0

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Complete the square"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: x² + bx + c = 0 (b can be odd)"""
        b = random.randint(-12, 12)
        while b == 0:
            b = random.randint(-12, 12)
        c = random.randint(-20, 20)

        # Create LaTeX
        latex = "x^2"
        if b > 0:
            latex += f" + {b}x"
        else:
            latex += f" - {abs(b)}x"

        if c > 0:
            latex += f" + {c}"
        elif c < 0:
            latex += f" - {abs(c)}"

        latex += " = 0"

        # Solve
        discriminant = b**2 - 4*c
        if discriminant >= 0:
            x1 = (-b + sqrt(discriminant)) / 2
            x2 = (-b - sqrt(discriminant)) / 2
            solution = round(min(x1, x2), 2)
        else:
            solution = 0

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Complete the square"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: ax² + bx + c = 0 (a ≠ 1)"""
        a = random.choice([2, 3, 4, -2, -3])
        b = random.randint(-20, 20)
        while b == 0:
            b = random.randint(-20, 20)
        c = random.randint(-30, 30)

        # Create LaTeX
        if a == 1:
            latex = "x^2"
        elif a == -1:
            latex = "-x^2"
        else:
            latex = f"{a}x^2"

        if b > 0:
            latex += f" + {b}x"
        else:
            latex += f" - {abs(b)}x"

        if c > 0:
            latex += f" + {c}"
        elif c < 0:
            latex += f" - {abs(c)}"

        latex += " = 0"

        # Solve
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            x1 = (-b + sqrt(discriminant)) / (2*a)
            x2 = (-b - sqrt(discriminant)) / (2*a)
            solution = round(min(x1, x2), 2)
        else:
            solution = 0

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Factor out the leading coefficient", "Complete the square"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: complex forms"""
        a = random.choice([2, 3, -2, -3])
        b = random.randint(-30, 30)
        while b == 0:
            b = random.randint(-30, 30)
        c = random.randint(-40, 40)
        d = random.randint(-20, 20)
        while d == 0:
            d = random.randint(-20, 20)

        # Create equation: ax² + bx + c = d
        if a == 1:
            latex = "x^2"
        elif a == -1:
            latex = "-x^2"
        else:
            latex = f"{a}x^2"

        if b > 0:
            latex += f" + {b}x"
        else:
            latex += f" - {abs(b)}x"

        if c > 0:
            latex += f" + {c}"
        elif c < 0:
            latex += f" - {abs(c)}"

        latex += f" = {d}"

        # Solve: ax² + bx + (c-d) = 0
        c_new = c - d
        discriminant = b**2 - 4*a*c_new
        if discriminant >= 0:
            x1 = (-b + sqrt(discriminant)) / (2*a)
            x2 = (-b - sqrt(discriminant)) / (2*a)
            solution = round(min(x1, x2), 2)
        else:
            solution = 0

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Move all terms to one side", "Complete the square"],
            difficulty='challenge'
        )