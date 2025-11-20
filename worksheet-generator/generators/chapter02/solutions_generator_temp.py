"""
What Are Solutions? Generator - Understanding what makes a value a solution
Generates problems about identifying and verifying solutions to equations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class SolutionsGenerator:
    """Generates problems about understanding solutions to equations."""

    def __init__(self, seed=None):
        """Initialize the solutions generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard'
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
        """Generate a single solutions problem."""

        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy equations - always has one solution."""
        # Simple linear equations with one solution
        x_val = random.randint(2, 10)
        const = random.randint(1, 8)
        total = x_val + const

        latex = f"x + {const} = {total}"
        solution = 1  # Always has one solution

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium equations - always
