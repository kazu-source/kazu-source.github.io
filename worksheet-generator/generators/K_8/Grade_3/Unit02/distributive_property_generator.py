"""
Distributive Property Generator - Grade 3 Unit 2
Generates problems focused on the distributive property with multiplication
Examples: 3 × 12 = 3 × (10 + 2) = (3 × 10) + (3 × 2) = 30 + 6 = 36
Focuses on breaking apart numbers using 2s/5s and 3s/6s
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DistributivePropertyGenerator:
    """Generates distributive property problems for multiplication."""

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
        """Generate easy problems: simple distributive property with 2s and 5s."""
        # Use 2 or 5 as the multiplier
        multiplier = random.choice([2, 5])

        # Create a number that can be broken down (e.g., 6 = 5 + 1, 8 = 5 + 3)
        if multiplier == 2:
            # Numbers that break nicely with 2: use even numbers split in half
            base = random.randint(2, 4)
            part1 = base
            part2 = base
            number = part1 + part2
        else:  # multiplier == 5
            # Break into 5 + something
            part1 = 5
            part2 = random.randint(1, 3)
            number = part1 + part2

        product = multiplier * number
        product1 = multiplier * part1
        product2 = multiplier * part2

        latex = f"{multiplier} \\times {number} = {multiplier} \\times ({part1} + {part2})"
        solution = str(product)

        steps = [
            f"{multiplier} \\times {number} = {multiplier} \\times ({part1} + {part2})",
            f"= ({multiplier} \\times {part1}) + ({multiplier} \\times {part2})",
            f"= {product1} + {product2}",
            f"= {product}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: distributive property with 3s and 6s."""
        # Use 3 or 6 as the multiplier
        multiplier = random.choice([3, 6])

        if multiplier == 3:
            # Break into friendly numbers
            part1 = random.choice([3, 4, 5])
            part2 = random.randint(2, 4)
        else:  # multiplier == 6
            # Break into 5 + something or 6 + something
            part1 = random.choice([5, 6])
            part2 = random.randint(1, 3)

        number = part1 + part2
        product = multiplier * number
        product1 = multiplier * part1
        product2 = multiplier * part2

        latex = f"{multiplier} \\times {number} = {multiplier} \\times ({part1} + {part2})"
        solution = str(product)

        steps = [
            f"{multiplier} \\times {number} = {multiplier} \\times ({part1} + {part2})",
            f"= ({multiplier} \\times {part1}) + ({multiplier} \\times {part2})",
            f"= {product1} + {product2}",
            f"= {product}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems using distributive property."""
        multiplier = random.choice([2, 3, 5, 6])

        # Create a scenario that naturally breaks apart
        part1 = random.randint(5, 8)
        part2 = random.randint(2, 4)
        number = part1 + part2

        product = multiplier * number
        product1 = multiplier * part1
        product2 = multiplier * part2

        contexts = [
            f"A store has {number} shelves ({part1} + {part2}). Each shelf has {multiplier} books. Use the distributive property to find the total number of books.",
            f"There are {number} groups ({part1} + {part2}). Each group has {multiplier} students. Break apart the groups to find the total.",
            f"A baker makes {number} trays ({part1} + {part2}). Each tray has {multiplier} cookies. Use the distributive property to find the total cookies.",
            f"There are {number} boxes ({part1} + {part2}). Each box has {multiplier} toys. Break it apart to find the total."
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(product)

        steps = [
            f"{multiplier} \\times {number} = {multiplier} \\times ({part1} + {part2})",
            f"= ({multiplier} \\times {part1}) + ({multiplier} \\times {part2})",
            f"= {product1} + {product2}",
            f"= {product}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: larger numbers and multiple strategies."""
        multiplier = random.choice([3, 4, 6, 7, 8])

        # Use 10-based decomposition for challenge
        ones_digit = random.randint(2, 8)
        tens = random.randint(1, 2) * 10
        number = tens + ones_digit

        product = multiplier * number
        product1 = multiplier * tens
        product2 = multiplier * ones_digit

        # Sometimes show it with 10s, sometimes with other breakdowns
        if random.choice([True, False]):
            latex = f"{multiplier} \\times {number}"
            steps = [
                f"\\text{{Break apart }} {number} \\text{{ into }} {tens} + {ones_digit}",
                f"{multiplier} \\times {number} = {multiplier} \\times ({tens} + {ones_digit})",
                f"= ({multiplier} \\times {tens}) + ({multiplier} \\times {ones_digit})",
                f"= {product1} + {product2}",
                f"= {product}"
            ]
        else:
            contexts = [
                f"A school has {number} classrooms. Each has {multiplier} computers. Use distributive property with tens ({tens}) and ones ({ones_digit}).",
                f"There are {number} students. Each needs {multiplier} pencils. Break into {tens} and {ones_digit} to calculate.",
                f"A store has {number} boxes. Each has {multiplier} items. Use {tens} + {ones_digit} to find the total."
            ]
            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            steps = [
                f"{multiplier} \\times {number} = {multiplier} \\times ({tens} + {ones_digit})",
                f"= ({multiplier} \\times {tens}) + ({multiplier} \\times {ones_digit})",
                f"= {product1} + {product2}",
                f"= {product}"
            ]

        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = DistributivePropertyGenerator()

    print("Easy (2s and 5s):")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
        print(f"    Steps: {problem.steps[0]}")

    print("\nMedium (3s and 6s):")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")
        print(f"    Steps: {problem.steps[0]}")

    print("\nHard (Word problems):")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        for step in problem.steps:
            print(f"    {step}")

    print("\nChallenge (Larger numbers with tens):")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        for step in problem.steps:
            print(f"    {step}")


if __name__ == '__main__':
    main()
