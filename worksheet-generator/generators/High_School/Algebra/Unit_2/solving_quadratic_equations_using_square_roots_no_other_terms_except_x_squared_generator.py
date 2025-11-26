"""
Solving Quadratic Equations Using Square Roots (no other terms except x^2) Generator
Unit 10.0
"""

import random
from equation_generator import Equation

class SolvingQuadraticEquationsUsingSquareRootsNoOtherTermsExceptXSquaredGenerator:
    """Generates problems for Solving Quadratic Equations Using Square Roots (no other terms except x^2)."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int):
        """Generate worksheet problems."""
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str):
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self):
        """Generate an easy problem."""
        # Quadratic equation
        a = random.randint(1, 3)

        latex = f"x^2 = {a**2}"
        solution = f"x = ±{a}"
        steps = [f"x = {a} or x = -{a}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """Generate a medium problem."""
        # Complex quadratic
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)

        latex = f"{a}x^2 + {b}x + {c} = 0"
        # Use quadratic formula
        discriminant = b**2 - 4*a*c
        solution = f"Use quadratic formula"
        steps = ["Apply quadratic formula"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """Generate a hard problem."""
        # Complex quadratic
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)

        latex = f"{a}x^2 + {b}x + {c} = 0"
        # Use quadratic formula
        discriminant = b**2 - 4*a*c
        solution = f"Use quadratic formula"
        steps = ["Apply quadratic formula"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """Generate a challenge problem."""
        # Complex quadratic
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)

        latex = f"{a}x^2 + {b}x + {c} = 0"
        # Use quadratic formula
        discriminant = b**2 - 4*a*c
        solution = f"Use quadratic formula"
        steps = ["Apply quadratic formula"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )
