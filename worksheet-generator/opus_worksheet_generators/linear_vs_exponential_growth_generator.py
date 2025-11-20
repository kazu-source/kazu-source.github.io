"""
Linear vs Exponential Growth Generator
Unit 8.0
"""

import random
from equation_generator import Equation

class LinearVsExponentialGrowthGenerator:
    """Generates problems for Linear vs Exponential Growth."""

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
        # Exponent problem
        base = random.randint(2, 5)
        exp = random.randint(2, 4)

        latex = f"{base}^{{{exp}}}"
        solution = base ** exp
        steps = [f"{base}^{{{exp}}} = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """Generate a medium problem."""
        # Complex exponent
        a = random.randint(2, 5)
        b = random.randint(2, 4)
        c = random.randint(1, 3)

        latex = f"({a}^{{{b}}})^{{{c}}}"
        solution = a ** (b * c)
        steps = [f"= {a}^{{{b*c}}} = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """Generate a hard problem."""
        # Complex exponent
        a = random.randint(2, 5)
        b = random.randint(2, 4)
        c = random.randint(1, 3)

        latex = f"({a}^{{{b}}})^{{{c}}}"
        solution = a ** (b * c)
        steps = [f"= {a}^{{{b*c}}} = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """Generate a challenge problem."""
        # Complex exponent
        a = random.randint(2, 5)
        b = random.randint(2, 4)
        c = random.randint(1, 3)

        latex = f"({a}^{{{b}}})^{{{c}}}"
        solution = a ** (b * c)
        steps = [f"= {a}^{{{b*c}}} = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )
