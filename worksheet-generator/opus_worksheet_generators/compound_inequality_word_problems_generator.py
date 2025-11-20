"""
Compound Inequality Word Problems Generator
Unit 3.0
"""

import random
from equation_generator import Equation

class CompoundInequalityWordProblemsGenerator:
    """Generates problems for Compound Inequality Word Problems."""

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
        # Word problem
        scenarios = [
            ("apples", "bought", "ate"),
            ("books", "had", "gave away"),
            ("coins", "collected", "spent")
        ]
        item, action1, action2 = random.choice(scenarios)
        a = random.randint(5, 20)
        b = random.randint(1, a-1)

        latex = f"\\text{{A person {action1} {a} {item} and {action2} {b}. How many are left?}}"
        solution = a - b
        steps = [f"{a} - {b} = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """Generate a medium problem."""
        # More complex word problem
        a = random.randint(10, 50)
        b = random.randint(5, 20)
        c = random.randint(2, 10)

        latex = f"\\text{{Complex problem with values {a}, {b}, and {c}}}"
        solution = (a + b) * c
        steps = [f"({a} + {b}) × {c} = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """Generate a hard problem."""
        # More complex word problem
        a = random.randint(10, 50)
        b = random.randint(5, 20)
        c = random.randint(2, 10)

        latex = f"\\text{{Complex problem with values {a}, {b}, and {c}}}"
        solution = (a + b) * c
        steps = [f"({a} + {b}) × {c} = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """Generate a challenge problem."""
        # More complex word problem
        a = random.randint(10, 50)
        b = random.randint(5, 20)
        c = random.randint(2, 10)

        latex = f"\\text{{Complex problem with values {a}, {b}, and {c}}}"
        solution = (a + b) * c
        steps = [f"({a} + {b}) × {c} = {solution}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )
