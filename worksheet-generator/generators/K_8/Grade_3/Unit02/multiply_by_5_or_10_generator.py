"""
Multiplication by 5 or 10 Generator - Grade 3 Unit 2
Generates problems focused on multiplication by 5 and 10
Examples: 7 × 5 = 35, 8 × 10 = 80
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplyBy5Or10Generator:
    """Generates multiplication by 5 or 10 problems."""

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
        """Generate easy problems: basic multiplication by 5 or 10 (numbers 1-5)."""
        multiplier = random.choice([5, 10])
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
        """Generate medium problems: multiplication by 5 or 10 (numbers up to 10)."""
        multiplier = random.choice([5, 10])
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
        """Generate hard problems: word problems with 5 or 10."""
        multiplier = random.choice([5, 10])
        number = random.randint(3, 10)
        product = number * multiplier

        if multiplier == 5:
            contexts = [
                f"There are {number} hands. Each hand has 5 fingers. How many fingers total?",
                f"A store has {number} bags with 5 apples in each bag. How many apples total?",
                f"There are {number} students. Each student has 5 pencils. How many pencils total?",
                f"A teacher has {number} boxes with 5 books in each box. How many books total?"
            ]
        else:  # multiplier == 10
            contexts = [
                f"There are {number} boxes with 10 crayons in each box. How many crayons total?",
                f"A student has {number} groups of 10 stickers. How many stickers total?",
                f"There are {number} bags with 10 marbles in each bag. How many marbles total?",
                f"A classroom has {number} tables with 10 chairs at each table. How many chairs total?"
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
        """Generate challenge problems: larger numbers and pattern recognition."""
        multiplier = random.choice([5, 10])
        number = random.randint(10, 15)
        product = number * multiplier

        if multiplier == 5:
            contexts = [
                f"A school has {number} classrooms. Each classroom has 5 computers. How many computers total?",
                f"There are {number} teams. Each team has 5 players. How many players total?",
                f"A baker makes {number} trays with 5 cookies on each tray. How many cookies total?",
                f"A store sells {number} packs of pencils with 5 pencils in each pack. How many pencils total?"
            ]
        else:  # multiplier == 10
            contexts = [
                f"A library has {number} shelves with 10 books on each shelf. How many books total?",
                f"There are {number} boxes with 10 toys in each box. How many toys total?",
                f"A farmer has {number} baskets with 10 eggs in each basket. How many eggs total?",
                f"A store has {number} packages with 10 markers in each package. How many markers total?"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(product)

        hint = ""
        if multiplier == 10:
            hint = "\\text{Hint: Multiplying by 10 adds a zero to the number}"

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
    generator = MultiplyBy5Or10Generator()

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
