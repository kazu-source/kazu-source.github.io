"""
Visualize Equivalent Ratios Generator - Grade 6 Unit 1
Generates problems about visualizing equivalent ratios
Example: If the ratio of red to blue is 2:3, draw an equivalent ratio with 4 red.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class VisualizeEquivalentRatiosGenerator:
    """Generates visualize equivalent ratios problems."""

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
        """Generate easy problems: doubling ratios."""
        num1 = random.randint(1, 4)
        num2 = random.randint(1, 4)
        multiplier = 2

        new_num1 = num1 * multiplier
        new_num2 = num2 * multiplier

        latex = f"\\text{{If the ratio is {num1}:{num2}, find an equivalent ratio by doubling both numbers.}}"
        solution = f"{new_num1}:{new_num2}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Multiply both by {multiplier}: {num1} \\times {multiplier} = {new_num1}, {num2} \\times {multiplier} = {new_num2}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: scaling ratios by different multipliers."""
        num1 = random.randint(2, 5)
        num2 = random.randint(2, 5)
        multiplier = random.choice([3, 4, 5])

        new_num1 = num1 * multiplier
        new_num2 = num2 * multiplier

        latex = f"\\text{{The ratio is {num1}:{num2}. Find an equivalent ratio by multiplying both numbers by {multiplier}.}}"
        solution = f"{new_num1}:{new_num2}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Multiply both by {multiplier}: {num1} \\times {multiplier} = {new_num1}, {num2} \\times {multiplier} = {new_num2}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: finding the multiplier."""
        num1 = random.randint(2, 6)
        num2 = random.randint(2, 6)
        multiplier = random.choice([2, 3, 4])

        new_num1 = num1 * multiplier

        latex = f"\\text{{The ratio {num1}:{num2} is equivalent to {new_num1}:?. Find the missing number.}}"
        solution = str(num2 * multiplier)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Multiplier is {new_num1} \\div {num1} = {multiplier}, so {num2} \\times {multiplier} = {num2 * multiplier}}}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: simplifying ratios."""
        # Start with a simplified ratio
        simple1 = random.randint(2, 5)
        simple2 = random.randint(2, 5)
        multiplier = random.choice([2, 3, 4, 5])

        # Create a ratio that needs to be simplified
        num1 = simple1 * multiplier
        num2 = simple2 * multiplier

        latex = f"\\text{{Simplify the ratio {num1}:{num2} to its lowest terms.}}"
        solution = f"{simple1}:{simple2}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Divide both by {multiplier}: {num1} \\div {multiplier} = {simple1}, {num2} \\div {multiplier} = {simple2}}}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = VisualizeEquivalentRatiosGenerator()

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
