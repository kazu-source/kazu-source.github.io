"""
Generator for Completing the Square problems.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation
from typing import List


class CompletingTheSquareGenerator:
    """Generator for completing the square problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate a worksheet of completing the square problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Problem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            if problem:
                problems.append(problem)
        return problems

    def generate_problem(self, difficulty: str) -> Equation:
        """
        Generate a single completing the square problem.

        Args:
            difficulty: Problem difficulty level

        Returns:
            Equation object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        elif difficulty == 'challenge':
            return self._generate_challenge()
        else:
            raise ValueError(f"Unknown difficulty: {difficulty}")

    def _generate_easy(self) -> Equation:
        """
        Generate an easy completing the square problem.
        x² + bx = c (where b is even)
        """
        # Generate coefficients
        b = random.choice([2, 4, 6, 8, 10, -2, -4, -6, -8, -10])
        c = random.randint(-20, 20)

        # Calculate the value to complete the square
        half_b = b // 2
        complete = half_b ** 2

        # Problem text
        if b > 0:
            problem_latex = f"x^2 + {b}x"
        else:
            problem_latex = f"x^2 - {abs(b)}x"

        if c != 0:
            if c > 0:
                problem_latex += f" + {c}"
            else:
                problem_latex += f" - {abs(c)}"

        problem_latex += " = 0"

        # Solution (completing the square form)
        if half_b > 0:
            solution_text = f"(x + {half_b})^2 = {complete - c}"
        else:
            solution_text = f"(x - {abs(half_b)})^2 = {complete - c}"

        # Steps for completing the square
        steps = [
            f"Move constant to right side",
            f"Complete the square by adding ({half_b})^2 = {complete} to both sides",
            f"Factor the left side",
            solution_text
        ]

        # Calculate actual x solutions
        from math import sqrt
        discriminant = complete - c
        if discriminant >= 0:
            x1 = -half_b + sqrt(discriminant)
            x2 = -half_b - sqrt(discriminant)
            solution = min(x1, x2)  # Return smaller solution
        else:
            solution = 0  # No real solution

        return Equation(
            latex=problem_latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Problem:
        """
        Generate a medium completing the square problem.
        x² + bx + c = 0 (b can be odd)
        """
        # Generate coefficients
        b = random.randint(-12, 12)
        while b == 0:
            b = random.randint(-12, 12)
        c = random.randint(-30, 30)

        # Calculate the value to complete the square
        if b % 2 == 0:
            half_b = b // 2
            complete = half_b ** 2

            # Problem text
            if b > 0:
                problem_text = f"x² + {b}x"
            else:
                problem_text = f"x² - {abs(b)}x"

            if c != 0:
                if c > 0:
                    problem_text += f" + {c}"
                else:
                    problem_text += f" - {abs(c)}"

            problem_text += " = 0"

            # Solution
            if half_b > 0:
                solution_text = f"(x + {half_b})² = {complete - c}"
            else:
                solution_text = f"(x - {abs(half_b)})² = {complete - c}"
        else:
            # For odd b, use fractions
            numerator = b
            denominator = 2
            complete_num = b ** 2
            complete_den = 4

            # Problem text
            if b > 0:
                problem_text = f"x² + {b}x"
            else:
                problem_text = f"x² - {abs(b)}x"

            if c != 0:
                if c > 0:
                    problem_text += f" + {c}"
                else:
                    problem_text += f" - {abs(c)}"

            problem_text += " = 0"

            # Solution with fractions
            if numerator > 0:
                solution_text = f"(x + {numerator}/2)² = {complete_num}/4 - {c}"
            else:
                solution_text = f"(x - {abs(numerator)}/2)² = {complete_num}/4 - {c}"

        return Problem(
            problem_type="completing_the_square",
            question=f"Complete the square: {problem_text}",
            answer=solution_text,
            difficulty=2
        )

    def _generate_hard(self) -> Problem:
        """
        Generate a hard completing the square problem.
        ax² + bx + c = 0 (a ≠ 1)
        """
        # Generate coefficients
        a = random.choice([2, 3, 4, 5, -2, -3, -4, -5])
        b = random.randint(-20, 20)
        while b == 0:
            b = random.randint(-20, 20)
        c = random.randint(-30, 30)

        # Problem text
        if a == 1:
            problem_text = "x²"
        elif a == -1:
            problem_text = "-x²"
        elif a > 0:
            problem_text = f"{a}x²"
        else:
            problem_text = f"{a}x²"

        if b > 0:
            problem_text += f" + {b}x"
        else:
            problem_text += f" - {abs(b)}x"

        if c != 0:
            if c > 0:
                problem_text += f" + {c}"
            else:
                problem_text += f" - {abs(c)}"

        problem_text += " = 0"

        # First factor out a
        if a > 0:
            factored = f"{a}(x² + {b}/{a}x + {c}/{a}) = 0"
        else:
            factored = f"{a}(x² + {b}/{a}x + {c}/{a}) = 0"

        # Then complete the square
        b_over_a = b / a
        half_b_over_a = b_over_a / 2

        if half_b_over_a == int(half_b_over_a):
            half_b_over_a = int(half_b_over_a)
            if half_b_over_a > 0:
                solution_text = f"{a}(x + {half_b_over_a})² = {a * half_b_over_a**2 - c}"
            else:
                solution_text = f"{a}(x - {abs(half_b_over_a)})² = {a * half_b_over_a**2 - c}"
        else:
            # Use fraction form
            solution_text = f"{a}(x + {b}/{2*a})² = ..."

        return Problem(
            problem_type="completing_the_square",
            question=f"Complete the square: {problem_text}",
            answer=solution_text,
            difficulty=3
        )

    def _generate_challenge(self) -> Problem:
        """
        Generate a challenge completing the square problem.
        ax² + bx + c = d (both sides non-zero, complex coefficients)
        """
        # Generate coefficients
        a = random.choice([2, 3, 4, 5, 6, -2, -3, -4, -5, -6])
        b = random.randint(-30, 30)
        while b == 0:
            b = random.randint(-30, 30)
        c = random.randint(-40, 40)
        d = random.randint(-20, 20)
        while d == 0:
            d = random.randint(-20, 20)

        # Problem text
        left_side = ""
        if a == 1:
            left_side = "x²"
        elif a == -1:
            left_side = "-x²"
        else:
            left_side = f"{a}x²"

        if b > 0:
            left_side += f" + {b}x"
        else:
            left_side += f" - {abs(b)}x"

        if c != 0:
            if c > 0:
                left_side += f" + {c}"
            else:
                left_side += f" - {abs(c)}"

        problem_text = f"{left_side} = {d}"

        # Move d to the left side
        c_minus_d = c - d

        # Factor out a
        b_over_a = b / a
        c_minus_d_over_a = c_minus_d / a

        # Complete the square
        half_b_over_a = b_over_a / 2

        if half_b_over_a == int(half_b_over_a):
            half_b_over_a = int(half_b_over_a)
            complete = half_b_over_a ** 2

            if half_b_over_a > 0:
                solution_text = f"{a}(x + {half_b_over_a})² = {a * complete - c + d}"
            else:
                solution_text = f"{a}(x - {abs(half_b_over_a)})² = {a * complete - c + d}"
        else:
            # Complex fraction form
            solution_text = f"{a}(x + {b}/{2*a})² = ..."

        return Problem(
            problem_type="completing_the_square",
            question=f"Complete the square: {problem_text}",
            answer=solution_text,
            difficulty=4
        )