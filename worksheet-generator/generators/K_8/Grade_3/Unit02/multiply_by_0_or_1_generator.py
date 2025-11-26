"""
Multiplication by 0 or 1 Generator - Grade 3 Unit 2
Generates problems focused on multiplication by 0 and 1
Examples: 5 × 0 = 0, 7 × 1 = 7
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplyBy0Or1Generator:
    """Generates multiplication by 0 or 1 problems."""

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
        """Generate easy problems: basic multiplication by 0 or 1 (numbers 1-5)."""
        multiplier = random.choice([0, 1])
        number = random.randint(1, 5)

        # Randomly decide order
        if random.choice([True, False]):
            latex = f"{number} \\times {multiplier}"
            product = number * multiplier
        else:
            latex = f"{multiplier} \\times {number}"
            product = multiplier * number

        solution = str(product)

        if multiplier == 0:
            explanation = "\\text{Any number times 0 equals 0}"
        else:
            explanation = f"\\text{{Any number times 1 equals itself}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[explanation, f"{latex} = {product}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: multiplication by 0 or 1 (numbers up to 10)."""
        multiplier = random.choice([0, 1])
        number = random.randint(1, 10)

        # Randomly decide order
        if random.choice([True, False]):
            latex = f"{number} \\times {multiplier}"
            product = number * multiplier
        else:
            latex = f"{multiplier} \\times {number}"
            product = multiplier * number

        solution = str(product)

        if multiplier == 0:
            explanation = "\\text{Any number times 0 equals 0}"
        else:
            explanation = f"\\text{{Any number times 1 equals itself}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[explanation, f"{latex} = {product}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with 0 or 1."""
        multiplier = random.choice([0, 1])
        number = random.randint(3, 10)
        product = number * multiplier

        if multiplier == 0:
            contexts = [
                f"There are {number} plates with 0 cookies on each plate",
                f"A store has {number} shelves with 0 books on each shelf",
                f"There are {number} baskets with 0 apples in each basket",
                f"A classroom has {number} desks with 0 pencils on each desk"
            ]
        else:
            contexts = [
                f"There are {number} bags with 1 apple in each bag",
                f"A store has {number} boxes with 1 toy in each box",
                f"There are {number} students with 1 pencil each",
                f"A garden has {number} pots with 1 flower in each pot"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}. How many in total?}}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{number} \\times {multiplier} = {product}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: larger numbers and multi-step contexts."""
        multiplier = random.choice([0, 1])
        number = random.randint(10, 20)
        product = number * multiplier

        if multiplier == 0:
            contexts = [
                f"A farmer has {number} fields. Each field has 0 cows because they were moved. How many cows are in the fields?",
                f"There are {number} jars. Each jar had cookies but now has 0. How many cookies are there?",
                f"A library has {number} sections with 0 new books in each section. How many new books total?",
                f"There are {number} boxes that are empty (0 items each). How many items total?"
            ]
        else:
            contexts = [
                f"A teacher has {number} students. Each student brings 1 book. How many books total?",
                f"There are {number} teams. Each team has 1 captain. How many captains total?",
                f"A store has {number} shelves. Each shelf displays 1 special item. How many special items?",
                f"There are {number} cars. Each car has 1 driver. How many drivers total?"
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
    generator = MultiplyBy0Or1Generator()

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
