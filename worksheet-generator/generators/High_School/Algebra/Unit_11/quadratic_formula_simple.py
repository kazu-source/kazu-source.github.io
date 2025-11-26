"""
Simplified Quadratic Formula Generator
"""

import random
import sys
import os
from math import sqrt
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation
from typing import List


class QuadraticFormulaSimpleGenerator:
    """Generator for quadratic formula problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate a worksheet of quadratic formula problems."""
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
        """Generate easy: x² + bx + c = 0 with integer solutions"""
        # Generate two integer roots
        root1 = random.randint(-8, 8)
        root2 = random.randint(-8, 8)

        # Calculate coefficients from roots: (x - root1)(x - root2) = 0
        a = 1
        b = -(root1 + root2)
        c = root1 * root2

        # Create LaTeX
        latex = "x^2"
        if b > 0:
            latex += f" + {b}x"
        elif b < 0:
            latex += f" - {abs(b)}x"

        if c > 0:
            latex += f" + {c}"
        elif c < 0:
            latex += f" - {abs(c)}"

        latex += " = 0"

        solution = min(root1, root2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Apply quadratic formula: x = (-b ± √(b²-4ac)) / 2a"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: ax² + bx + c = 0 with a ≠ 1"""
        a = random.choice([2, 3, 4, -2, -3])

        # Generate rational roots
        root1 = random.choice([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
        root2 = random.choice([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

        # Calculate b and c from roots
        b = -a * (root1 + root2)
        c = a * root1 * root2

        # Create LaTeX
        if a == 1:
            latex = "x^2"
        elif a == -1:
            latex = "-x^2"
        else:
            latex = f"{a}x^2"

        if b > 0:
            latex += f" + {b}x"
        elif b < 0:
            latex += f" - {abs(b)}x"

        if c > 0:
            latex += f" + {c}"
        elif c < 0:
            latex += f" - {abs(c)}"

        latex += " = 0"

        solution = min(root1, root2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"a = {a}, b = {b}, c = {c}", "Apply quadratic formula"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: ax² + bx + c = 0 with irrational solutions"""
        a = random.choice([1, 2, 3])
        b = random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])

        # Choose c to make discriminant positive but not perfect square
        max_c = int(b**2 / (4*a)) - 1
        if max_c > 10:
            max_c = 10
        c = random.randint(-10, max_c) if max_c > -10 else random.randint(-10, -1)

        # Create LaTeX
        if a == 1:
            latex = "x^2"
        else:
            latex = f"{a}x^2"

        if b > 0:
            latex += f" + {b}x"
        elif b < 0:
            latex += f" - {abs(b)}x"

        if c > 0:
            latex += f" + {c}"
        elif c < 0:
            latex += f" - {abs(c)}"

        latex += " = 0"

        # Calculate solution
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + sqrt(discriminant)) / (2*a)
            x2 = (-b - sqrt(discriminant)) / (2*a)
            solution = round(min(x1, x2), 2)
        else:
            solution = 0

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Calculate discriminant: b²-4ac", "Apply quadratic formula"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: needs rearranging first"""
        a = random.choice([2, 3, -2, -3])
        b1 = random.randint(1, 10)
        b2 = random.randint(1, 10)
        c = random.randint(-15, 15)

        # Create equation: ax² + b1x = b2x + c
        if a == 1:
            left_side = f"x^2 + {b1}x"
        elif a == -1:
            left_side = f"-x^2 + {b1}x"
        else:
            left_side = f"{a}x^2 + {b1}x"

        right_side = f"{b2}x"
        if c > 0:
            right_side += f" + {c}"
        elif c < 0:
            right_side += f" - {abs(c)}"

        latex = f"{left_side} = {right_side}"

        # Rearrange to standard form
        b_final = b1 - b2
        c_final = -c

        # Solve
        discriminant = b_final**2 - 4*a*c_final
        if discriminant >= 0:
            x1 = (-b_final + sqrt(discriminant)) / (2*a)
            x2 = (-b_final - sqrt(discriminant)) / (2*a)
            solution = round(min(x1, x2), 2)
        else:
            solution = 0

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Rearrange to standard form", "Apply quadratic formula"],
            difficulty='challenge'
        )