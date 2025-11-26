"""
Multiplication by 3 or 6 Generator - Grade 3 Unit 2
Generates problems focused on multiplication by 3 and 6
Examples: 5 × 3 = 15, 7 × 6 = 42
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplyBy3Or6Generator:
    """Generates multiplication by 3 or 6 problems."""

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
        """Generate easy problems: basic multiplication by 3 or 6 (numbers 1-5)."""
        multiplier = random.choice([3, 6])
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
        """Generate medium problems: multiplication by 3 or 6 (numbers up to 10)."""
        multiplier = random.choice([3, 6])
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
        """Generate hard problems: word problems with 3 or 6."""
        multiplier = random.choice([3, 6])
        number = random.randint(3, 10)
        product = number * multiplier

        if multiplier == 3:
            contexts = [
                f"There are {number} tricycles. Each tricycle has 3 wheels. How many wheels total?",
                f"A store has {number} boxes with 3 toys in each box. How many toys total?",
                f"There are {number} triangles. Each triangle has 3 sides. How many sides total?",
                f"A teacher has {number} groups with 3 students in each group. How many students total?"
            ]
        else:  # multiplier == 6
            contexts = [
                f"There are {number} boxes with 6 eggs in each box. How many eggs total?",
                f"A store has {number} packs of juice with 6 juice boxes in each pack. How many juice boxes total?",
                f"There are {number} groups with 6 students in each group. How many students total?",
                f"A classroom has {number} tables with 6 pencils on each table. How many pencils total?"
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
        """Generate challenge problems: larger numbers and relationship between 3 and 6."""
        multiplier = random.choice([3, 6])
        number = random.randint(10, 15)
        product = number * multiplier

        if multiplier == 3:
            contexts = [
                f"A store has {number} shelves with 3 books on each shelf. How many books total?",
                f"There are {number} teams. Each team has 3 players. How many players total?",
                f"A baker makes {number} trays with 3 muffins on each tray. How many muffins total?",
                f"A garden has {number} rows with 3 plants in each row. How many plants total?"
            ]
        else:  # multiplier == 6
            contexts = [
                f"A store sells {number} cartons with 6 eggs in each carton. How many eggs total?",
                f"There are {number} boxes with 6 markers in each box. How many markers total?",
                f"A parking lot has {number} rows with 6 cars in each row. How many cars total?",
                f"A school has {number} classrooms with 6 computers in each. How many computers total?"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(product)

        # Sometimes add a hint about the relationship between 3 and 6
        hint = ""
        if multiplier == 6 and random.choice([True, False]):
            hint = "\\text{Remember: 6 is double 3}"

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
    generator = MultiplyBy3Or6Generator()

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
