"""
Factoring Quadratics (leads into factored form of next section) Generator
Unit 9.0
"""

import random
from equation_generator import Equation

class FactoringQuadraticsLeadsIntoFactoredFormOfNextSectionGenerator:
    """Generates problems for Factoring Quadratics (leads into factored form of next section)."""

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
        # Polynomial problem
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"x^2 + {a+b}x + {a*b}"
        solution = f"(x + {a})(x + {b})"
        steps = [f"Factor: {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """Generate a medium problem."""
        # Complex polynomial
        a = random.randint(2, 5)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)

        latex = f"{a}x^2 + {b}x + {c}"
        solution = "Factored form"
        steps = ["Factor the polynomial"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """Generate a hard problem."""
        # Complex polynomial
        a = random.randint(2, 5)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)

        latex = f"{a}x^2 + {b}x + {c}"
        solution = "Factored form"
        steps = ["Factor the polynomial"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """Generate a challenge problem."""
        # Complex polynomial
        a = random.randint(2, 5)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)

        latex = f"{a}x^2 + {b}x + {c}"
        solution = "Factored form"
        steps = ["Factor the polynomial"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )
