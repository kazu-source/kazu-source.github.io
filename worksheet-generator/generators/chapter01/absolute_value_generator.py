"""
Absolute Value Generator - Introduction to absolute value
Generates problems about evaluating absolute value expressions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class AbsoluteValueGenerator:
    """Generates problems for evaluating absolute value expressions."""

    def __init__(self, seed=None):
        """Initialize the absolute value generator."""
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
        """Generate a single absolute value problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple absolute value: |a|"""
        value = random.randint(-20, 20)

        latex = f"|{value}|"
        solution = abs(value)

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate absolute value with simple arithmetic: |a + b| or |a - b|"""
        a = random.randint(-15, 15)
        b = random.randint(-15, 15)
        op = random.choice(['+', '-'])

        if op == '+':
            latex = f"|{a} + {b}|"
            solution = abs(a + b)
        else:
            latex = f"|{a} - {b}|"
            solution = abs(a - b)

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate absolute value with multiplication: |a × b|"""
        a = random.randint(-12, 12)
        b = random.randint(-12, 12)

        latex = f"|{a} \\times {b}|"
        solution = abs(a * b)

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate nested absolute values: ||a| - |b||"""
        a = random.randint(-15, 15)
        b = random.randint(-15, 15)

        latex = f"||{a}| - |{b}||"
        solution = abs(abs(a) - abs(b))

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = AbsoluteValueGenerator()

    print("Testing Absolute Value Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")
