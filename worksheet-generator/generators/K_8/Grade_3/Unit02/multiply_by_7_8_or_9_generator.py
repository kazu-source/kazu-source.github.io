"""
Multiplication by 7, 8, or 9 Generator - Grade 3 Unit 2
Generates problems focused on multiplication by 7, 8, and 9
Examples: 6 × 7 = 42, 5 × 8 = 40, 4 × 9 = 36
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplyBy7_8Or9Generator:
    """Generates multiplication by 7, 8, or 9 problems."""

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
        """Generate easy problems: basic multiplication by 7, 8, or 9 (numbers 1-5)."""
        multiplier = random.choice([7, 8, 9])
        number = random.randint(1, 5)

        # Randomly decide order
        if random.choice([True, False]):
            latex = f"{number} \\times {multiplier}"
        else:
            latex = f"{multiplier} \\times {number}"

        product = number * multiplier
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{latex} = {product}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: multiplication by 7, 8, or 9 (numbers up to 10)."""
        multiplier = random.choice([7, 8, 9])
        number = random.randint(1, 10)

        # Randomly decide order
        if random.choice([True, False]):
            latex = f"{number} \\times {multiplier}"
        else:
            latex = f"{multiplier} \\times {number}"

        product = number * multiplier
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{latex} = {product}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with 7, 8, or 9."""
        multiplier = random.choice([7, 8, 9])
        number = random.randint(3, 10)
        product = number * multiplier

        if multiplier == 7:
            contexts = [
                f"There are {number} weeks. Each week has 7 days. How many days total?",
                f"A store has {number} boxes with 7 toys in each box. How many toys total?",
                f"There are {number} tables with 7 chairs at each table. How many chairs total?",
                f"A teacher has {number} groups with 7 students in each group. How many students total?"
            ]
        elif multiplier == 8:
            contexts = [
                f"There are {number} spiders. Each spider has 8 legs. How many legs total?",
                f"A store has {number} boxes with 8 crayons in each box. How many crayons total?",
                f"There are {number} groups with 8 students in each group. How many students total?",
                f"A classroom has {number} tables with 8 pencils on each table. How many pencils total?"
            ]
        else:  # multiplier == 9
            contexts = [
                f"There are {number} boxes with 9 markers in each box. How many markers total?",
                f"A store sells {number} packs with 9 cards in each pack. How many cards total?",
                f"There are {number} teams with 9 players on each team. How many players total?",
                f"A baker makes {number} trays with 9 cookies on each tray. How many cookies total?"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{number} \\times {multiplier} = {product}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: larger numbers and strategies."""
        multiplier = random.choice([7, 8, 9])
        number = random.randint(10, 12)
        product = number * multiplier

        if multiplier == 7:
            contexts = [
                f"A school has {number} classrooms. Each classroom has 7 computers. How many computers total?",
                f"There are {number} shelves with 7 books on each shelf. How many books total?",
                f"A parking lot has {number} rows with 7 cars in each row. How many cars total?",
                f"A store sells {number} packages with 7 pencils in each package. How many pencils total?"
            ]
        elif multiplier == 8:
            contexts = [
                f"A library has {number} shelves with 8 books on each shelf. How many books total?",
                f"There are {number} boxes with 8 toys in each box. How many toys total?",
                f"A farmer has {number} baskets with 8 apples in each basket. How many apples total?",
                f"A school has {number} tables with 8 chairs at each table. How many chairs total?"
            ]
        else:  # multiplier == 9
            contexts = [
                f"A store has {number} boxes with 9 markers in each box. How many markers total?",
                f"There are {number} teams with 9 players on each team. How many players total?",
                f"A baker makes {number} trays with 9 muffins on each tray. How many muffins total?",
                f"A garden has {number} rows with 9 plants in each row. How many plants total?"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(product)

        # Sometimes add a strategy hint
        hint = ""
        if multiplier == 9 and random.choice([True, False]):
            hint = f"\\text{{Strategy: }} {number} \\times 10 = {number * 10}, \\text{{ then subtract }} {number}"
        elif multiplier == 8 and random.choice([True, False]):
            hint = f"\\text{{Strategy: Double, double, double! }} {number} \\times 2 \\times 2 \\times 2"

        steps = [f"{number} \\times {multiplier} = {product}"]
        if hint:
            steps.insert(0, hint)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiplyBy7_8Or9Generator()

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

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
