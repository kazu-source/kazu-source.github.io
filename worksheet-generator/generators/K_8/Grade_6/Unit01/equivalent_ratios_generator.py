"""
Equivalent Ratios Generator - Grade 6 Unit 1
Generates problems about equivalent ratios
Example: Are 2:3 and 4:6 equivalent ratios?
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EquivalentRatiosGenerator:
    """Generates equivalent ratios problems."""

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
        """Generate easy problems: identifying equivalent ratios."""
        num1 = random.randint(1, 4)
        num2 = random.randint(1, 4)
        multiplier = random.choice([2, 3])

        new_num1 = num1 * multiplier
        new_num2 = num2 * multiplier

        # Randomly decide if they are equivalent
        is_equivalent = random.choice([True, False])

        if not is_equivalent:
            new_num2 += random.choice([1, -1]) * random.choice([1, 2])
            if new_num2 <= 0:
                new_num2 = num2 * multiplier + 1

        latex = f"\\text{{Are {num1}:{num2} and {new_num1}:{new_num2} equivalent ratios?}}"
        solution = "Yes" if is_equivalent else "No"

        if is_equivalent:
            steps = [f"\\text{{{num1} \\times {multiplier} = {new_num1} and {num2} \\times {multiplier} = {new_num2}, so Yes}}"]
        else:
            steps = [f"\\text{{The ratios are not equivalent}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: finding missing values in equivalent ratios."""
        num1 = random.randint(2, 6)
        num2 = random.randint(2, 6)
        multiplier = random.choice([2, 3, 4, 5])

        # Randomly pick which value to hide
        hide_first = random.choice([True, False])

        if hide_first:
            known = num2 * multiplier
            latex = f"\\text{{If {num1}:{num2} is equivalent to ?:{known}, find the missing number.}}"
            solution = str(num1 * multiplier)
        else:
            known = num1 * multiplier
            latex = f"\\text{{If {num1}:{num2} is equivalent to {known}:?, find the missing number.}}"
            solution = str(num2 * multiplier)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Multiply by {multiplier}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: creating tables of equivalent ratios."""
        num1 = random.randint(2, 5)
        num2 = random.randint(2, 5)
        multiplier = random.choice([3, 4])

        result1 = num1 * multiplier
        result2 = num2 * multiplier

        latex = f"\\text{{Create an equivalent ratio to {num1}:{num2} where the first number is {result1}.}}"
        solution = f"{result1}:{result2}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Multiply both by {multiplier}: {num1} \\times {multiplier} = {result1}, {num2} \\times {multiplier} = {result2}}}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: word problems with equivalent ratios."""
        contexts = [
            ("cups of flour", "cups of sugar"),
            ("red paint", "blue paint"),
            ("boys", "girls"),
            ("apples", "oranges")
        ]

        item1, item2 = random.choice(contexts)
        num1 = random.randint(2, 4)
        num2 = random.randint(2, 4)
        multiplier = random.choice([2, 3])

        new_num1 = num1 * multiplier

        latex = f"\\text{{A recipe uses {num1} {item1} for every {num2} {item2}.}}"
        latex += f"\\text{{ If you use {new_num1} {item1}, how many {item2} do you need?}}"
        solution = str(num2 * multiplier)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Ratio {num1}:{num2}, multiply by {multiplier} to get {new_num1}:{num2 * multiplier}}}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = EquivalentRatiosGenerator()

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
