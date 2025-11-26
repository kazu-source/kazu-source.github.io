"""
Multiplication by 2 or 4 Generator - Grade 3 Unit 2
Generates problems focused on multiplication by 2 and 4
Examples: 6 × 2 = 12, 5 × 4 = 20
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplyBy2Or4Generator:
    """Generates multiplication by 2 or 4 problems."""

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
        """Generate easy problems: basic multiplication by 2 or 4 (numbers 1-5)."""
        multiplier = random.choice([2, 4])
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
        """Generate medium problems: multiplication by 2 or 4 (numbers up to 10)."""
        multiplier = random.choice([2, 4])
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
        """Generate hard problems: word problems with 2 or 4."""
        multiplier = random.choice([2, 4])
        number = random.randint(3, 10)
        product = number * multiplier

        if multiplier == 2:
            contexts = [
                f"There are {number} pairs of shoes. How many shoes total?",
                f"A bicycle has {number} wheels (2 per bike). How many bikes are there?",
                f"There are {number} students. Each student has 2 pencils. How many pencils total?",
                f"A teacher has {number} bags with 2 books in each bag. How many books total?"
            ]
        else:  # multiplier == 4
            contexts = [
                f"There are {number} tables. Each table has 4 legs. How many legs total?",
                f"A store has {number} boxes with 4 toys in each box. How many toys total?",
                f"There are {number} cars. Each car has 4 wheels. How many wheels total?",
                f"A classroom has {number} groups with 4 students in each group. How many students total?"
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
        """Generate challenge problems: larger numbers and multi-step reasoning."""
        multiplier = random.choice([2, 4])
        number = random.randint(10, 15)
        product = number * multiplier

        if multiplier == 2:
            contexts = [
                f"A store sells gloves in pairs. If they have {number} pairs, how many individual gloves are there?",
                f"There are {number} teams playing basketball. Each team needs 2 basketballs. How many basketballs needed?",
                f"A baker makes {number} trays of cookies with 2 cookies per tray. How many cookies total?",
                f"There are {number} boxes with 2 books in each box. How many books are there in all?"
            ]
        else:  # multiplier == 4
            contexts = [
                f"A pet store has {number} fish tanks with 4 fish in each tank. How many fish total?",
                f"There are {number} packs of markers with 4 markers in each pack. How many markers total?",
                f"A parking lot has {number} rows with 4 cars in each row. How many cars total?",
                f"A restaurant has {number} tables with 4 chairs at each table. How many chairs total?"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{number} \\times {multiplier} = {product}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiplyBy2Or4Generator()

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
