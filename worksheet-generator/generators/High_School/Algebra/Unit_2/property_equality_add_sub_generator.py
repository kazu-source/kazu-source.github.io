"""
Property of Equality (Add/Subtract) Generator
Teaches the addition and subtraction properties of equality
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class PropertyEqualityAddSubGenerator:
    """Generates problems teaching addition and subtraction properties of equality."""

    def __init__(self, seed=None):
        """Initialize the property of equality (add/sub) generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Equation objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single property of equality problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple one-step: x + a = b"""
        x = random.randint(1, 15)
        a = random.randint(1, 12)
        b = x + a

        latex = f"x + {a} = {b}"
        solution = x

        steps = [
            f"Subtract {a} from both sides",
            f"x + {a} - {a} = {b} - {a}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate one-step with subtraction: x - a = b"""
        x = random.randint(5, 20)
        a = random.randint(1, 15)
        b = x - a

        if b < 0:
            # Make it positive
            x = random.randint(10, 25)
            a = random.randint(1, 8)
            b = x - a

        latex = f"x - {a} = {b}"
        solution = x

        steps = [
            f"Add {a} to both sides",
            f"x - {a} + {a} = {b} + {a}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate with negative numbers or larger values"""
        equation_type = random.choice(['negative_const', 'negative_result', 'larger_numbers'])

        if equation_type == 'negative_const':
            # x + (-a) = b  or  x - a = b
            x = random.randint(5, 20)
            a = random.randint(5, 15)
            b = x - a

            latex = f"x - {a} = {b}"
            solution = x

            steps = [
                f"Add {a} to both sides",
                f"x = {b} + {a}",
                f"x = {x}"
            ]

        elif equation_type == 'negative_result':
            # Result is negative
            x = random.randint(-15, -2)
            a = random.randint(1, 10)
            b = x + a

            latex = f"x + {a} = {b}"
            solution = x

            steps = [
                f"Subtract {a} from both sides",
                f"x = {b} - {a}",
                f"x = {x}"
            ]

        else:  # larger_numbers
            x = random.randint(20, 50)
            a = random.randint(15, 40)
            operation = random.choice(['+', '-'])

            if operation == '+':
                b = x + a
                latex = f"x + {a} = {b}"
                steps = [
                    f"Subtract {a} from both sides",
                    f"x = {b} - {a}",
                    f"x = {x}"
                ]
            else:
                b = x - a
                latex = f"x - {a} = {b}"
                steps = [
                    f"Add {a} to both sides",
                    f"x = {b} + {a}",
                    f"x = {x}"
                ]

            solution = x

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate with multiple terms or variables on both sides"""
        challenge_type = random.choice(['two_terms_left', 'constant_on_right', 'reorganize'])

        if challenge_type == 'two_terms_left':
            # x + a + b = c
            x = random.randint(5, 15)
            a = random.randint(2, 8)
            b = random.randint(2, 8)
            c = x + a + b

            latex = f"x + {a} + {b} = {c}"
            solution = x

            total = a + b
            steps = [
                f"Combine constants on left: x + {total} = {c}",
                f"Subtract {total} from both sides",
                f"x = {c} - {total}",
                f"x = {x}"
            ]

        elif challenge_type == 'constant_on_right':
            # x = a + b
            x = random.randint(10, 30)
            a = random.randint(3, 15)
            b = x - a

            latex = f"x = {a} + {b}"
            solution = x

            steps = [
                f"Simplify right side: {a} + {b} = {x}",
                f"x = {x}"
            ]

        else:  # reorganize
            # a + x = b
            x = random.randint(5, 20)
            a = random.randint(3, 12)
            b = a + x

            latex = f"{a} + x = {b}"
            solution = x

            steps = [
                f"Subtract {a} from both sides",
                f"x = {b} - {a}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

