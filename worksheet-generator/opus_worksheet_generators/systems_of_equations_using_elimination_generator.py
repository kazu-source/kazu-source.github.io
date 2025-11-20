"""
Systems of Equations Using Elimination Generator
Unit 5.0
"""

import random
from equation_generator import Equation

class SystemsOfEquationsUsingEliminationGenerator:
    """Generates problems for Systems of Equations Using Elimination."""

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
        # System of equations
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)

        latex = f"\\begin{{cases}} y = {a}x + {b} \\\\ y = {c} \\end{{cases}}"
        x_sol = (c - b) / a
        solution = f"({x_sol:.1f}, {c})"
        steps = [f"x = {x_sol:.1f}, y = {c}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """Generate a medium problem."""
        # Complex system
        a1, b1, c1 = random.randint(1, 3), random.randint(-5, 5), random.randint(-10, 10)
        a2, b2, c2 = random.randint(1, 3), random.randint(-5, 5), random.randint(-10, 10)

        latex = f"\\begin{{cases}} {a1}x + {b1}y = {c1} \\\\ {a2}x + {b2}y = {c2} \\end{{cases}}"
        solution = "Solve system"
        steps = ["Use substitution or elimination"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """Generate a hard problem."""
        # Complex system
        a1, b1, c1 = random.randint(1, 3), random.randint(-5, 5), random.randint(-10, 10)
        a2, b2, c2 = random.randint(1, 3), random.randint(-5, 5), random.randint(-10, 10)

        latex = f"\\begin{{cases}} {a1}x + {b1}y = {c1} \\\\ {a2}x + {b2}y = {c2} \\end{{cases}}"
        solution = "Solve system"
        steps = ["Use substitution or elimination"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """Generate a challenge problem."""
        # Complex system
        a1, b1, c1 = random.randint(1, 3), random.randint(-5, 5), random.randint(-10, 10)
        a2, b2, c2 = random.randint(1, 3), random.randint(-5, 5), random.randint(-10, 10)

        latex = f"\\begin{{cases}} {a1}x + {b1}y = {c1} \\\\ {a2}x + {b2}y = {c2} \\end{{cases}}"
        solution = "Solve system"
        steps = ["Use substitution or elimination"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )
