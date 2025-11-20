"""
Slope Generator
Unit 4.0
"""

import random
from equation_generator import Equation

class SlopeGenerator:
    """Generates problems for Slope."""

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
        # Slope problem
        m = random.randint(-5, 5)
        b = random.randint(-10, 10)

        latex = f"y = {m}x + {b}"
        solution = f"slope = {m}, y-intercept = {b}"
        steps = [f"m = {m}, b = {b}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """Generate a medium problem."""
        # Find equation from points
        x1, y1 = random.randint(-5, 5), random.randint(-10, 10)
        x2, y2 = random.randint(-5, 5), random.randint(-10, 10)
        if x2 == x1:
            x2 += 1

        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        latex = f"\\text{{Find equation through }}({x1}, {y1})\\text{{ and }}({x2}, {y2})"
        solution = f"y = {m:.1f}x + {b:.1f}"
        steps = [f"slope = {m:.1f}", f"y = {m:.1f}x + {b:.1f}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """Generate a hard problem."""
        # Find equation from points
        x1, y1 = random.randint(-5, 5), random.randint(-10, 10)
        x2, y2 = random.randint(-5, 5), random.randint(-10, 10)
        if x2 == x1:
            x2 += 1

        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        latex = f"\\text{{Find equation through }}({x1}, {y1})\\text{{ and }}({x2}, {y2})"
        solution = f"y = {m:.1f}x + {b:.1f}"
        steps = [f"slope = {m:.1f}", f"y = {m:.1f}x + {b:.1f}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """Generate a challenge problem."""
        # Find equation from points
        x1, y1 = random.randint(-5, 5), random.randint(-10, 10)
        x2, y2 = random.randint(-5, 5), random.randint(-10, 10)
        if x2 == x1:
            x2 += 1

        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        latex = f"\\text{{Find equation through }}({x1}, {y1})\\text{{ and }}({x2}, {y2})"
        solution = f"y = {m:.1f}x + {b:.1f}"
        steps = [f"slope = {m:.1f}", f"y = {m:.1f}x + {b:.1f}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )
