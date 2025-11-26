"""
Two-Step Equations Generator - Solving equations requiring two operations
Generates problems that require two steps to solve
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class TwoStepEquationsGenerator:
    """Generates two-step equation problems."""

    def __init__(self, seed=None):
        """Initialize the two-step equations generator."""
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
        """Generate a single two-step equation problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple two-step: ax + b = c"""
        x = random.randint(1, 10)
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        c = a * x + b

        latex = f"{a}x + {b} = {c}"
        solution = x

        steps = [
            f"Subtract {b} from both sides: {a}x = {c - b}",
            f"Divide by {a}: x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate two-step with subtraction: ax - b = c"""
        x = random.randint(1, 10)
        a = random.randint(2, 6)
        b = random.randint(1, 15)
        c = a * x - b

        if c < 0:
            latex = f"{a}x - {b} = {c}"
        else:
            latex = f"{a}x - {b} = {c}"

        solution = x

        steps = [
            f"Add {b} to both sides: {a}x = {c + b}",
            f"Divide by {a}: x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate with negative coefficients or fractions"""
        x = random.randint(1, 8)

        equation_type = random.choice(['negative_coef', 'fraction_result', 'negative_both'])

        if equation_type == 'negative_coef':
            a = random.randint(-6, -2)
            b = random.randint(1, 10)
            c = a * x + b
            latex = f"{a}x + {b} = {c}"
        elif equation_type == 'fraction_result':
            x = random.randint(1, 10)
            a = random.randint(2, 5)
            b = random.randint(1, 10)
            c = a * x + b
            # Swap to create fraction
            latex = f"{a}x + {b} = {c}"
            solution = x
        else:  # negative_both
            a = random.randint(-5, -2)
            b = random.randint(-10, -1)
            c = a * x + b
            latex = f"{a}x {b} = {c}" if b < 0 else f"{a}x + {b} = {c}"

        solution = x

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate with distribution or variables on both sides"""
        x = random.randint(1, 6)

        equation_type = random.choice(['distribution', 'both_sides', 'fraction_coef'])

        if equation_type == 'distribution':
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            result = a * (x + b)
            latex = f"{a}(x + {b}) = {result}"
            solution = x
        elif equation_type == 'both_sides':
            a = random.randint(2, 5)
            b = random.randint(1, 8)
            c = random.randint(1, 4)
            d = a * x + b - c * x
            latex = f"{a}x + {b} = {c}x + {d}"
            solution = x
        else:  # fraction_coef
            a = random.randint(2, 4)
            b = random.randint(1, 10)
            c = x + b * a
            latex = f"\\frac{{x}}{{{a}}} + {b} = {c // a}"
            solution = x

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = TwoStepEquationsGenerator()

    print("Testing Two-Step Equations Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")