"""
Multiplication as Equal Groups Generator - Grade 3 Unit 1
Generates problems focused on understanding multiplication as repeated addition of equal groups
Example: 3 groups of 4 = 3 × 4 = 12
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplicationAsEqualGroupsGenerator:
    """Generates multiplication as equal groups problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
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
        """Generate easy problems: small numbers (1-5)."""
        num_groups = random.randint(2, 5)
        items_per_group = random.randint(2, 5)
        product = num_groups * items_per_group

        latex = f"{num_groups} \\times {items_per_group}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num_groups} \\text{{ groups of }} {items_per_group} = {product}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: numbers up to 10."""
        num_groups = random.randint(2, 10)
        items_per_group = random.randint(2, 10)
        product = num_groups * items_per_group

        latex = f"{num_groups} \\times {items_per_group}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num_groups} \\text{{ groups of }} {items_per_group} = {product}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: include word context."""
        num_groups = random.randint(3, 10)
        items_per_group = random.randint(3, 10)
        product = num_groups * items_per_group

        contexts = [
            f"There are {num_groups} bags with {items_per_group} apples in each bag",
            f"A classroom has {num_groups} rows with {items_per_group} students in each row",
            f"The garden has {num_groups} boxes with {items_per_group} flowers in each box",
            f"There are {num_groups} baskets with {items_per_group} eggs in each basket"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}. How many in total?}}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num_groups} \\times {items_per_group} = {product}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: larger numbers and contexts."""
        num_groups = random.randint(5, 12)
        items_per_group = random.randint(5, 12)
        product = num_groups * items_per_group

        contexts = [
            f"A store has {num_groups} shelves with {items_per_group} books on each shelf",
            f"There are {num_groups} teams with {items_per_group} players on each team",
            f"The parking lot has {num_groups} rows with {items_per_group} cars in each row",
            f"A baker makes {num_groups} trays with {items_per_group} cookies on each tray"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}. How many in total?}}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num_groups} \\times {items_per_group} = {product}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiplicationAsEqualGroupsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
