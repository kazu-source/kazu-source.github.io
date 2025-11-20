"""
Interpreting Domain and Range Generator
Unit 6.0
"""

import random
from equation_generator import Equation

class InterpretingDomainAndRangeGenerator:
    """Generates problems for Interpreting Domain and Range."""

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
        # Basic algebraic problem
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(['+', '-', '×'])

        if op == '+':
            latex = f"{a} + {b}"
            solution = a + b
        elif op == '-':
            latex = f"{a} - {b}"
            solution = a - b
        else:
            latex = f"{a} \\times {b}"
            solution = a * b

        steps = [f"= {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """Generate a medium problem."""
        # Complex problem
        a = random.randint(2, 10)
        b = random.randint(-20, 20)
        c = random.randint(-10, 10)

        latex = f"{a}x + {b} = {c}"
        solution = (c - b) / a
        steps = [f"x = {solution:.2f}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """Generate a hard problem."""
        # Complex problem
        a = random.randint(2, 10)
        b = random.randint(-20, 20)
        c = random.randint(-10, 10)

        latex = f"{a}x + {b} = {c}"
        solution = (c - b) / a
        steps = [f"x = {solution:.2f}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """Generate a challenge problem."""
        # Complex problem
        a = random.randint(2, 10)
        b = random.randint(-20, 20)
        c = random.randint(-10, 10)

        latex = f"{a}x + {b} = {c}"
        solution = (c - b) / a
        steps = [f"x = {solution:.2f}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )
