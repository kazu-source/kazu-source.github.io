"""
Ratio Application Generator - Grade 6 Unit 1
Generates problems applying ratios to real-world contexts
Example: A recipe calls for ingredients in a 3:2 ratio. If you have 12 cups of the first ingredient, how much of the second do you need?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RatioApplicationGenerator:
    """Generates ratio application problems."""

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
        """Generate easy problems: simple ratio applications."""
        contexts = [
            ("apples", "oranges"),
            ("red marbles", "blue marbles"),
            ("boys", "girls"),
            ("pencils", "pens")
        ]

        item1, item2 = random.choice(contexts)
        ratio1 = random.randint(1, 4)
        ratio2 = random.randint(1, 4)
        multiplier = random.choice([2, 3])

        actual1 = ratio1 * multiplier
        actual2 = ratio2 * multiplier

        latex = f"\\text{{The ratio of {item1} to {item2} is {ratio1}:{ratio2}.}}"
        latex += f"\\text{{ If there are {actual1} {item1}, how many {item2} are there?}}"
        solution = str(actual2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{actual1} \\div {ratio1} = {multiplier}, so {ratio2} \\times {multiplier} = {actual2}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: recipe and mixture problems."""
        contexts = [
            ("cups of flour", "cups of sugar", "cookies"),
            ("red paint", "blue paint", "purple paint"),
            ("cups of water", "cups of concentrate", "juice"),
            ("tablespoons of oil", "tablespoons of vinegar", "dressing")
        ]

        item1, item2, product = random.choice(contexts)
        ratio1 = random.randint(2, 5)
        ratio2 = random.randint(2, 5)
        multiplier = random.choice([2, 3, 4])

        actual1 = ratio1 * multiplier

        latex = f"\\text{{A recipe for {product} uses {ratio1} {item1} and {ratio2} {item2}.}}"
        latex += f"\\text{{ If you have {actual1} {item1}, how many {item2} do you need?}}"
        solution = str(ratio2 * multiplier)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Multiplier: {actual1} \\div {ratio1} = {multiplier}, so {ratio2} \\times {multiplier} = {ratio2 * multiplier}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: finding total from ratio."""
        contexts = [
            ("red marbles", "blue marbles"),
            ("girls", "boys"),
            ("cats", "dogs"),
            ("fiction books", "non-fiction books")
        ]

        item1, item2 = random.choice(contexts)
        ratio1 = random.randint(2, 5)
        ratio2 = random.randint(2, 5)
        multiplier = random.choice([2, 3, 4])

        actual1 = ratio1 * multiplier
        actual2 = ratio2 * multiplier
        total = actual1 + actual2

        latex = f"\\text{{The ratio of {item1} to {item2} is {ratio1}:{ratio2}.}}"
        latex += f"\\text{{ If there are {actual1} {item1}, what is the total number of items?}}"
        solution = str(total)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{item2}: {ratio2} \\times {multiplier} = {actual2}, Total: {actual1} + {actual2} = {total}}}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: finding parts from total."""
        contexts = [
            ("red flowers", "yellow flowers"),
            ("small boxes", "large boxes"),
            ("cats", "dogs"),
            ("mystery books", "adventure books")
        ]

        item1, item2 = random.choice(contexts)
        ratio1 = random.randint(2, 4)
        ratio2 = random.randint(2, 4)
        multiplier = random.choice([2, 3])

        actual1 = ratio1 * multiplier
        actual2 = ratio2 * multiplier
        total = actual1 + actual2

        latex = f"\\text{{A group has {item1} and {item2} in a ratio of {ratio1}:{ratio2}.}}"
        latex += f"\\text{{ If there are {total} items total, how many are {item1}?}}"
        solution = str(actual1)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Total parts: {ratio1} + {ratio2} = {ratio1 + ratio2}, Multiplier: {total} \\div {ratio1 + ratio2} = {multiplier}, {item1}: {ratio1} \\times {multiplier} = {actual1}}}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = RatioApplicationGenerator()

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
