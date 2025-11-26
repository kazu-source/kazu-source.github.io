"""
Property of Equality (Mult/Div) Generator
Teaches the multiplication and division properties of equality
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class PropertyEqualityMultDivGenerator:
    """Generates problems teaching multiplication and division properties of equality."""

    def __init__(self, seed=None):
        """Initialize the property of equality (mult/div) generator."""
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
        """Generate simple division: ax = b"""
        x = random.randint(2, 12)
        a = random.randint(2, 8)
        b = a * x

        latex = f"{a}x = {b}"
        solution = x

        steps = [
            f"Divide both sides by {a}",
            f"\\frac{{{a}x}}{{{a}}} = \\frac{{{b}}}{{{a}}}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate with fraction: x/a = b"""
        x = random.randint(4, 30)
        # Find divisors of x for cleaner problems
        divisors = [i for i in range(2, 10) if x % i == 0]
        if divisors:
            a = random.choice(divisors)
        else:
            a = random.randint(2, 5)
        b = x // a if x % a == 0 else x / a

        latex = f"\\frac{{x}}{{{a}}} = {int(b) if b == int(b) else b}"
        solution = x

        steps = [
            f"Multiply both sides by {a}",
            f"\\frac{{x}}{{{a}}} \\cdot {a} = {int(b) if b == int(b) else b} \\cdot {a}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate with negative coefficients or larger numbers"""
        equation_type = random.choice(['negative_coef', 'larger_numbers', 'negative_result'])

        if equation_type == 'negative_coef':
            # -ax = b
            x = random.randint(2, 10)
            a = random.randint(2, 8)
            b = -a * x

            latex = f"-{a}x = {b}"
            solution = x

            steps = [
                f"Divide both sides by -{a}",
                f"x = \\frac{{{b}}}{{-{a}}}",
                f"x = {x}"
            ]

        elif equation_type == 'negative_result':
            # ax = -b (negative result)
            x = random.randint(-12, -2)
            a = random.randint(2, 7)
            b = a * x

            latex = f"{a}x = {b}"
            solution = x

            steps = [
                f"Divide both sides by {a}",
                f"x = \\frac{{{b}}}{{{a}}}",
                f"x = {x}"
            ]

        else:  # larger_numbers
            x = random.randint(10, 30)
            a = random.randint(5, 12)
            operation = random.choice(['multiply', 'divide'])

            if operation == 'multiply':
                b = a * x
                latex = f"{a}x = {b}"
                steps = [
                    f"Divide both sides by {a}",
                    f"x = \\frac{{{b}}}{{{a}}}",
                    f"x = {x}"
                ]
            else:  # divide
                # Make x divisible by a for cleaner answer
                x = random.randint(5, 15) * a
                b = x // a
                latex = f"\\frac{{x}}{{{a}}} = {b}"
                steps = [
                    f"Multiply both sides by {a}",
                    f"x = {b} \\cdot {a}",
                    f"x = {x}"
                ]

            solution = x

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate with fractions or decimals"""
        challenge_type = random.choice(['fraction_coef', 'mixed_operations', 'decimal'])

        if challenge_type == 'fraction_coef':
            # (a/b)x = c
            x = random.randint(4, 20)
            numerator = random.randint(2, 5)
            denominator = random.choice([2, 3, 4, 5])
            # Make sure x is divisible by denominator for cleaner answer
            x = random.randint(2, 8) * denominator
            c = (numerator * x) // denominator

            latex = f"\\frac{{{numerator}}}{{{denominator}}}x = {c}"
            solution = x

            steps = [
                f"Multiply both sides by \\frac{{{denominator}}}{{{numerator}}}",
                f"x = {c} \\cdot \\frac{{{denominator}}}{{{numerator}}}",
                f"x = {x}"
            ]

        elif challenge_type == 'mixed_operations':
            # 2x = 3x - a (requires subtraction then division)
            x = random.randint(5, 20)
            a = x  # So that 3x - x = 2x, and 2x = a

            latex = f"2x = 3x - {a}"
            solution = x

            steps = [
                f"Subtract 3x from both sides",
                f"-x = -{a}",
                f"Divide by -1",
                f"x = {x}"
            ]

        else:  # decimal
            # ax = b with decimal result
            a = random.choice([2, 4, 5])
            b = random.randint(10, 50)
            x = b / a

            latex = f"{a}x = {b}"
            solution = x

            steps = [
                f"Divide both sides by {a}",
                f"x = \\frac{{{b}}}{{{a}}}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

