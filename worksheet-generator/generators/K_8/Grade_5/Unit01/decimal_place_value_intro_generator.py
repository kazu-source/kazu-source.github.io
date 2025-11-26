"""
Decimal Place Value Intro Generator - Grade 5 Unit 1
Generates problems introducing decimal place value
Example: What digit is in the tenths place in 3.456? Answer: 4
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DecimalPlaceValueIntroGenerator:
    """Generates decimal place value introduction problems."""

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
        """Generate easy problems: identify digit in tenths place."""
        ones = random.randint(0, 9)
        tenths = random.randint(1, 9)

        number = f"{ones}.{tenths}"

        latex = f"\\text{{{{What digit is in the tenths place in }}}} {number}?"
        solution = str(tenths)
        steps = [
            f"{number}",
            f"\\text{{{{The digit after the decimal point is in the tenths place}}}}",
            f"\\text{{{{Answer: }}}} {tenths}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: identify digit in various places with hundredths."""
        ones = random.randint(0, 9)
        tenths = random.randint(0, 9)
        hundredths = random.randint(1, 9)

        number = f"{ones}.{tenths}{hundredths}"

        place = random.choice(['tenths', 'hundredths'])

        if place == 'tenths':
            digit = tenths
            place_name = "tenths"
        else:
            digit = hundredths
            place_name = "hundredths"

        latex = f"\\text{{{{What digit is in the {place_name} place in }}}} {number}?"
        solution = str(digit)
        steps = [
            f"{number}",
            f"\\text{{{{The {place_name} place is position {2 if place == 'hundredths' else 1} after the decimal}}}}",
            f"\\text{{{{Answer: }}}} {digit}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: identify place value of a specific digit."""
        ones = random.randint(1, 9)
        tenths = random.randint(1, 9)
        hundredths = random.randint(1, 9)

        # Make sure all digits are different for clarity
        while tenths == ones:
            tenths = random.randint(1, 9)
        while hundredths == ones or hundredths == tenths:
            hundredths = random.randint(1, 9)

        number = f"{ones}.{tenths}{hundredths}"

        digit_choice = random.choice([ones, tenths, hundredths])

        if digit_choice == ones:
            place_value = "ones"
        elif digit_choice == tenths:
            place_value = "tenths"
        else:
            place_value = "hundredths"

        latex = f"\\text{{{{In the number }}}} {number}\\text{{{{, what place value does the digit }}}} {digit_choice} \\text{{{{ occupy?}}}}"
        solution = f"\\text{{{{{place_value}}}}}"
        steps = [
            f"{number}",
            f"\\text{{{{The digit }}}} {digit_choice} \\text{{{{ is in the {place_value} place}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: identify value represented by a digit."""
        ones = random.randint(2, 9)
        tenths = random.randint(1, 9)
        hundredths = random.randint(1, 9)
        thousandths = random.randint(1, 9)

        number = f"{ones}.{tenths}{hundredths}{thousandths}"

        place_choice = random.choice(['ones', 'tenths', 'hundredths', 'thousandths'])

        if place_choice == 'ones':
            digit = ones
            value = ones
        elif place_choice == 'tenths':
            digit = tenths
            value = f"0.{tenths}"
        elif place_choice == 'hundredths':
            digit = hundredths
            value = f"0.0{hundredths}"
        else:
            digit = thousandths
            value = f"0.00{thousandths}"

        latex = f"\\text{{{{In the number }}}} {number}\\text{{{{, what is the value of the digit }}}} {digit} \\text{{{{ in the {place_choice} place?}}}}"
        solution = str(value)
        steps = [
            f"{number}",
            f"\\text{{{{The digit }}}} {digit} \\text{{{{ in the {place_choice} place represents }}}} {value}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = DecimalPlaceValueIntroGenerator()

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
