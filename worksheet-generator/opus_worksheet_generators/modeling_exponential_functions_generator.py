"""
Modeling Exponential Functions Generator
Unit 8.0
"""

import random
from equation_generator import Equation

class ModelingExponentialFunctionsGenerator:
    """Generates problems for Modeling Exponential Functions."""

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
        # Function evaluation
        m = random.randint(1, 5)
        b = random.randint(-10, 10)
        x = random.randint(-5, 5)

        latex = f"f(x) = {m}x + {b}, \\text{{ find }} f({x})"
        solution = m * x + b
        steps = [f"f({x}) = {m}({x}) + {b} = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """Generate a medium problem."""
        # Complex function
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)
        x = random.randint(-3, 3)

        latex = f"f(x) = {a}x^2 + {b}x + {c}, \\text{{ find }} f({x})"
        solution = a * x**2 + b * x + c
        steps = [f"f({x}) = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """Generate a hard problem."""
        # Complex function
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)
        x = random.randint(-3, 3)

        latex = f"f(x) = {a}x^2 + {b}x + {c}, \\text{{ find }} f({x})"
        solution = a * x**2 + b * x + c
        steps = [f"f({x}) = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """Generate a challenge problem."""
        # Complex function
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)
        x = random.randint(-3, 3)

        latex = f"f(x) = {a}x^2 + {b}x + {c}, \\text{{ find }} f({x})"
        solution = a * x**2 + b * x + c
        steps = [f"f({x}) = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )
