"""
Rounding Decimals Generator - Grade 5 Unit 1
Generates problems rounding decimals to various places
Example: Round 3.456 to the nearest tenth: 3.5
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RoundingDecimalsGenerator:
    """Generates rounding decimals problems."""

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
        """Generate easy problems: round to nearest whole number."""
        ones = random.randint(1, 9)
        tenths = random.randint(0, 9)

        number = f"{ones}.{tenths}"

        if tenths >= 5:
            rounded = ones + 1
        else:
            rounded = ones

        latex = f"\\text{{{{Round to the nearest whole number: }}}} {number}"
        solution = str(rounded)
        steps = [
            f"{number}",
            f"\\text{{{{Look at tenths place: }}}} {tenths}",
            f"{tenths} {'≥' if tenths >= 5 else '<'} 5, \\text{{{{ so round {'up' if tenths >= 5 else 'down'}}}}}",
            str(rounded)
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: round to nearest tenth."""
        ones = random.randint(1, 9)
        tenths = random.randint(0, 9)
        hundredths = random.randint(0, 9)

        number = f"{ones}.{tenths}{hundredths}"

        if hundredths >= 5:
            if tenths == 9:
                rounded = f"{ones + 1}.0"
            else:
                rounded = f"{ones}.{tenths + 1}"
        else:
            rounded = f"{ones}.{tenths}"

        latex = f"\\text{{{{Round to the nearest tenth: }}}} {number}"
        solution = rounded
        steps = [
            f"{number}",
            f"\\text{{{{Look at hundredths place: }}}} {hundredths}",
            f"{hundredths} {'≥' if hundredths >= 5 else '<'} 5, \\text{{{{ so round {'up' if hundredths >= 5 else 'down'}}}}}",
            rounded
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: round to nearest hundredth."""
        ones = random.randint(1, 9)
        tenths = random.randint(0, 9)
        hundredths = random.randint(0, 9)
        thousandths = random.randint(0, 9)

        number = f"{ones}.{tenths}{hundredths}{thousandths}"

        if thousandths >= 5:
            if hundredths == 9:
                if tenths == 9:
                    rounded = f"{ones + 1}.00"
                else:
                    rounded = f"{ones}.{tenths + 1}0"
            else:
                rounded = f"{ones}.{tenths}{hundredths + 1}"
        else:
            rounded = f"{ones}.{tenths}{hundredths}"

        latex = f"\\text{{{{Round to the nearest hundredth: }}}} {number}"
        solution = rounded
        steps = [
            f"{number}",
            f"\\text{{{{Look at thousandths place: }}}} {thousandths}",
            f"{thousandths} {'≥' if thousandths >= 5 else '<'} 5, \\text{{{{ so round {'up' if thousandths >= 5 else 'down'}}}}}",
            rounded
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: round to multiple places."""
        ones = random.randint(2, 9)
        tenths = random.randint(0, 9)
        hundredths = random.randint(0, 9)
        thousandths = random.randint(0, 9)

        number = f"{ones}.{tenths}{hundredths}{thousandths}"

        # Round to whole number
        if tenths >= 5:
            rounded_whole = ones + 1
        else:
            rounded_whole = ones

        # Round to tenth
        if hundredths >= 5:
            if tenths == 9:
                rounded_tenth = f"{ones + 1}.0"
            else:
                rounded_tenth = f"{ones}.{tenths + 1}"
        else:
            rounded_tenth = f"{ones}.{tenths}"

        latex = f"\\text{{{{Round }}}} {number} \\text{{{{ to the nearest whole number and to the nearest tenth.}}}}"
        solution = f"\\text{{{{Whole: }}}} {rounded_whole}, \\text{{{{ Tenth: }}}} {rounded_tenth}"
        steps = [
            f"{number}",
            f"\\text{{{{To whole: look at {tenths}, round to }}}} {rounded_whole}",
            f"\\text{{{{To tenth: look at {hundredths}, round to }}}} {rounded_tenth}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = RoundingDecimalsGenerator()

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
