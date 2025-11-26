"""
Decimals on Number Line Generator - Grade 5 Unit 1
Generates problems placing decimals on a number line
Example: Where is 0.6 on a number line from 0 to 1?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DecimalsOnNumberLineGenerator:
    """Generates decimals on number line problems."""

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
        """Generate easy problems: locate tenths on 0 to 1 number line."""
        tenths = random.randint(1, 9)
        decimal = tenths / 10

        latex = f"\\text{{{{Locate }}}} {decimal} \\text{{{{ on a number line from 0 to 1.}}}}"
        solution = f"\\text{{{{At the {tenths}th mark (counting from 0)}}}}"
        steps = [
            f"{decimal} = \\frac{{{tenths}}}{{10}}",
            f"\\text{{{{Divide the number line into 10 equal parts}}}}",
            f"\\text{{{{Count {tenths} marks from 0}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: locate hundredths on number line."""
        tenths = random.randint(1, 8)
        hundredths = random.randint(1, 9)
        decimal = tenths + hundredths / 10

        latex = f"\\text{{{{Locate }}}} {decimal} \\text{{{{ on a number line from {tenths} to {tenths + 1}.}}}}"
        solution = f"\\text{{{{At position {decimal}}}}}"
        steps = [
            f"{decimal} = {tenths}.{hundredths}",
            f"\\text{{{{Start at {tenths}, move {hundredths} tenths toward {tenths + 1}}}}}",
            f"\\text{{{{Position: {decimal}}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: identify decimal at a specific position."""
        start = random.randint(0, 5)
        end = start + 1
        divisions = 10
        position = random.randint(1, 9)

        decimal_value = start + position / divisions

        latex = f"\\text{{{{A number line from {start} to {end} is divided into {divisions} equal parts. What decimal is at the {position}th mark from {start}?}}}}"
        solution = str(decimal_value)
        steps = [
            f"\\text{{{{Each division = }}}} \\frac{{1}}{{{divisions}}} = 0.1",
            f"{position} \\text{{{{ marks from {start} = }}}} {start} + {position}(0.1)",
            f"{decimal_value}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: compare positions on number line."""
        tenths1 = random.randint(2, 7)
        hundredths1 = random.randint(0, 9)
        decimal1 = tenths1 / 10 + hundredths1 / 100

        tenths2 = random.randint(2, 7)
        hundredths2 = random.randint(0, 9)
        while tenths2 == tenths1 and hundredths2 == hundredths1:
            tenths2 = random.randint(2, 7)
            hundredths2 = random.randint(0, 9)
        decimal2 = tenths2 / 10 + hundredths2 / 100

        latex = f"\\text{{{{Which is farther from 0 on a number line: }}}} {decimal1} \\text{{{{ or }}}} {decimal2}?"

        if decimal1 > decimal2:
            solution = str(decimal1)
            comparison = ">"
        else:
            solution = str(decimal2)
            comparison = "<"

        steps = [
            f"{decimal1} {comparison} {decimal2}",
            f"\\text{{{{Therefore, }}}} {solution} \\text{{{{ is farther from 0}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = DecimalsOnNumberLineGenerator()

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
