"""
Simple Inequalities Generator - One-step and two-step inequalities
Generates problems for solving basic inequalities
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class SimpleInequalitiesGenerator:
    """Generates simple inequality problems."""

    def __init__(self, seed=None):
        """Initialize the simple inequalities generator."""
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
        """Generate a single inequality problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate one-step inequality: x + a < b or ax < b"""
        inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])
        problem_type = random.choice(['add_sub', 'mult_div'])

        if problem_type == 'add_sub':
            a = random.randint(1, 10)
            b = random.randint(5, 20)
            x = b - a

            if random.choice([True, False]):
                latex = f"x + {a} {inequality_sign} {b}"
                if inequality_sign in ['<', '\\leq']:
                    solution = f"x {inequality_sign} {x}"
                else:
                    solution = f"x {inequality_sign} {x}"
            else:
                latex = f"x - {a} {inequality_sign} {b - 2*a}"
                solution = f"x {inequality_sign} {b - a}"
        else:  # mult_div
            a = random.randint(2, 6)
            b = random.randint(10, 30)
            latex = f"{a}x {inequality_sign} {b}"

            if inequality_sign in ['<', '\\leq']:
                solution = f"x {inequality_sign} {b // a}"
            else:
                solution = f"x {inequality_sign} {b // a}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate two-step inequality: ax + b < c"""
        inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        x = random.randint(1, 10)
        c = a * x + b

        latex = f"{a}x + {b} {inequality_sign} {c}"

        if inequality_sign in ['<', '\\leq']:
            solution = f"x {inequality_sign} {x}"
        else:
            solution = f"x {inequality_sign} {x}"

        steps = [
            f"Subtract {b}: {a}x {inequality_sign} {c - b}",
            f"Divide by {a}: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate inequality with negative coefficient (flip sign)"""
        inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])
        a = random.randint(-5, -2)
        b = random.randint(1, 10)
        x = random.randint(1, 8)
        c = a * x + b

        latex = f"{a}x + {b} {inequality_sign} {c}"

        # Flip inequality when dividing by negative
        flipped_sign = {
            '<': '>',
            '>': '<',
            '\\leq': '\\geq',
            '\\geq': '\\leq'
        }[inequality_sign]

        solution = f"x {flipped_sign} {x}"

        steps = [
            f"Subtract {b}: {a}x {inequality_sign} {c - b}",
            f"Divide by {a} (flip sign): {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate inequality with variables on both sides"""
        inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])
        a = random.randint(3, 6)
        b = random.randint(1, 8)
        c = random.randint(1, 3)
        # Ensure a != c to avoid division by zero
        while a == c:
            a = random.randint(3, 6)
        x = random.randint(2, 10)
        d = a * x + b - c * x

        latex = f"{a}x + {b} {inequality_sign} {c}x + {d}"

        coef_diff = a - c
        const_diff = d - b

        if coef_diff > 0:
            final_x = const_diff / coef_diff
            solution = f"x {inequality_sign} {int(final_x) if final_x == int(final_x) else final_x:.1f}"
        else:
            flipped_sign = {
                '<': '>',
                '>': '<',
                '\\leq': '\\geq',
                '\\geq': '\\leq'
            }[inequality_sign]
            final_x = const_diff / coef_diff
            solution = f"x {flipped_sign} {int(final_x) if final_x == int(final_x) else final_x:.1f}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = SimpleInequalitiesGenerator()

    print("Testing Simple Inequalities Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")