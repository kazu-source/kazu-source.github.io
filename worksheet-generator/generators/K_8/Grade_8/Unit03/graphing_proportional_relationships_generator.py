"""
Graphing Proportional Relationships Generator - Grade 8 Unit 3
Generates problems about graphing proportional relationships
Example: Graph y = 3x
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class GraphingProportionalRelationshipsGenerator:
    """Generates graphing proportional relationships problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
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
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy problems: identify if relationship is proportional."""
        k = random.randint(2, 8)

        latex = f"\text{{{{Is }}}} y = {k}x \text{{{{ a proportional relationship?}}}}"
        solution = "\text{Yes, it passes through the origin}"
        steps = [
            f"y = {k}x",
            "\text{When } x = 0, y = 0",
            "\text{Passes through origin, so proportional}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: find constant of proportionality."""
        k = random.randint(2, 10)
        x = random.randint(2, 6)
        y = k * x

        latex = f"\text{{{{A proportional relationship passes through }}}} ({x}, {y}). \text{{{{ Find the constant of proportionality.}}}}"
        solution = f"k = {k}"
        steps = [
            f"y = kx",
            f"{y} = k \cdot {x}",
            f"k = \frac{{{y}}}{{{x}}} = {k}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: write equation from graph or table."""
        k = random.randint(2, 8)
        points = [(i, k * i) for i in range(1, 4)]

        latex = f"\text{{{{A graph passes through }}}} {points[0]}, {points[1]}, {points[2]}. \text{{{{ Write the equation.}}}}"
        solution = f"y = {k}x"
        steps = [
            f"\text{{{{Find }}}} k \text{{{{ using }}}} {points[0]}",
            f"k = \frac{{{points[0][1]}}}{{{points[0][0]}}} = {k}",
            f"y = {k}x"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: compare proportional relationships."""
        k1 = random.randint(3, 8)
        k2 = random.randint(2, k1 - 1)

        latex = f"\text{{{{Which is steeper: }}}} y = {k1}x \text{{{{ or }}}} y = {k2}x?"
        solution = f"y = {k1}x \text{{{{ is steeper}}}}"
        steps = [
            f"\text{{{{Compare constants: }}}} {k1} > {k2}",
            f"y = {k1}x \text{{{{ is steeper}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = GraphingProportionalRelationshipsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
