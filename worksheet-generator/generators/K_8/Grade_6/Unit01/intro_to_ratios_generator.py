"""
Intro to Ratios Generator - Grade 6 Unit 1
Generates problems introducing basic ratio concepts
Example: There are 3 apples and 5 oranges. What is the ratio of apples to oranges?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IntroToRatiosGenerator:
    """Generates intro to ratios problems."""

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
        """Generate easy problems: simple ratios with small numbers."""
        contexts = [
            ("apples", "oranges"),
            ("boys", "girls"),
            ("red marbles", "blue marbles"),
            ("cats", "dogs"),
            ("pencils", "pens")
        ]

        item1, item2 = random.choice(contexts)
        num1 = random.randint(2, 5)
        num2 = random.randint(2, 5)

        latex = f"\\text{{There are {num1} {item1} and {num2} {item2}. What is the ratio of {item1} to {item2}?}}"
        solution = f"{num1}:{num2}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Ratio of {item1} to {item2} is {num1}:{num2}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: ratios with larger numbers."""
        contexts = [
            ("red flowers", "yellow flowers"),
            ("fiction books", "non-fiction books"),
            ("students", "teachers"),
            ("triangles", "circles"),
            ("basketballs", "soccer balls")
        ]

        item1, item2 = random.choice(contexts)
        num1 = random.randint(5, 12)
        num2 = random.randint(5, 12)

        latex = f"\\text{{A classroom has {num1} {item1} and {num2} {item2}. Write the ratio of {item1} to {item2}.}}"
        solution = f"{num1}:{num2}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Ratio is {num1}:{num2}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: three-part ratios."""
        contexts = [
            ("red", "blue", "green"),
            ("apples", "oranges", "bananas"),
            ("fiction", "non-fiction", "reference"),
            ("small", "medium", "large")
        ]

        item1, item2, item3 = random.choice(contexts)
        num1 = random.randint(2, 8)
        num2 = random.randint(2, 8)
        num3 = random.randint(2, 8)

        latex = f"\\text{{A bag contains {num1} {item1}, {num2} {item2}, and {num3} {item3} items.}}"
        latex += f"\\text{{ Write the ratio of {item1} to {item2} to {item3}.}}"
        solution = f"{num1}:{num2}:{num3}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Ratio is {num1}:{num2}:{num3}}}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: ratios with part-to-whole relationships."""
        contexts = [
            ("red marbles", "marbles"),
            ("girls", "students"),
            ("apples", "fruits"),
            ("fiction books", "books")
        ]

        part_name, whole_name = random.choice(contexts)
        part = random.randint(3, 10)
        other_part = random.randint(3, 10)
        total = part + other_part

        latex = f"\\text{{Out of {total} {whole_name}, {part} are {part_name}.}}"
        latex += f"\\text{{ What is the ratio of {part_name} to total {whole_name}?}}"
        solution = f"{part}:{total}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Ratio is {part}:{total}}}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = IntroToRatiosGenerator()

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
