"""
Estimate to Subtract Multi-Digit Numbers Generator - Grade 3 Unit 3
Generates problems for estimating differences by rounding before subtracting
Focuses on rounding to nearest 10 or 100, then subtracting the rounded numbers
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EstimateToSubtractMultiDigitNumbersGenerator:
    """Generates estimation subtraction problems."""

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

    def _round_to_nearest(self, number: int, round_to: int) -> int:
        """Round a number to the nearest 10 or 100."""
        if round_to == 10:
            ones = number % 10
            if ones < 5:
                return (number // 10) * 10
            else:
                return ((number // 10) + 1) * 10
        else:  # round to 100
            tens_digit = (number // 10) % 10
            if tens_digit < 5:
                return (number // 100) * 100
            else:
                return ((number // 100) + 1) * 100

    def _generate_easy(self) -> Equation:
        """Generate easy problems: 2-digit - 2-digit, round to nearest 10."""
        num1 = random.randint(30, 98)
        num2 = random.randint(12, num1 - 5)  # Ensure positive result

        rounded1 = self._round_to_nearest(num1, 10)
        rounded2 = self._round_to_nearest(num2, 10)

        # Ensure estimate is positive
        if rounded1 <= rounded2:
            rounded1 = rounded1 + 10

        estimate = rounded1 - rounded2

        latex = f"\\text{{Estimate: }} {num1} - {num2} \\text{{ (round to nearest 10)}}"
        solution = str(estimate)

        steps = [
            f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
            f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
            f"\\text{{Subtract: }} {rounded1} - {rounded2} = {estimate}",
            f"\\text{{Estimate: }} {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 3-digit - 3-digit or 2-digit, round to nearest 10."""
        num1 = random.randint(200, 999)
        num2 = random.randint(50, num1 - 20)

        rounded1 = self._round_to_nearest(num1, 10)
        rounded2 = self._round_to_nearest(num2, 10)
        estimate = rounded1 - rounded2

        latex = f"\\text{{Estimate: }} {num1} - {num2} \\text{{ (round to nearest 10)}}"
        solution = str(estimate)

        steps = [
            f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
            f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
            f"\\text{{Subtract: }} {rounded1} - {rounded2} = {estimate}",
            f"\\text{{Estimate: }} {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 3-digit - 3-digit, round to nearest 100."""
        num1 = random.randint(300, 950)
        num2 = random.randint(150, num1 - 50)

        rounded1 = self._round_to_nearest(num1, 100)
        rounded2 = self._round_to_nearest(num2, 100)

        # Ensure estimate is positive
        if rounded1 <= rounded2:
            rounded1 = rounded1 + 100

        estimate = rounded1 - rounded2

        latex = f"\\text{{Estimate: }} {num1} - {num2} \\text{{ (round to nearest 100)}}"
        solution = str(estimate)

        steps = [
            f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
            f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
            f"\\text{{Subtract: }} {rounded1} - {rounded2} = {estimate}",
            f"\\text{{Estimate: }} {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: word problems with estimation."""
        num1 = random.randint(250, 900)
        num2 = random.randint(125, num1 - 50)
        round_to = random.choice([10, 100])

        contexts = [
            f"A store had {num1} items. They sold {num2} items",
            f"A school has {num1} students. {num2} students went on a field trip",
            f"A farmer had {num1} apples. He gave away {num2} apples",
            f"The library had {num1} books. {num2} books were checked out",
            f"A factory produced {num1} toys. {num2} toys were shipped"
        ]

        context = random.choice(contexts)

        rounded1 = self._round_to_nearest(num1, round_to)
        rounded2 = self._round_to_nearest(num2, round_to)

        # Ensure estimate is positive
        if rounded1 <= rounded2:
            if round_to == 10:
                rounded1 = rounded1 + 10
            else:
                rounded1 = rounded1 + 100

        estimate = rounded1 - rounded2

        latex = f"\\text{{{context}. Estimate how many are left (round to nearest {round_to})}}."
        solution = str(estimate)

        steps = [
            f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
            f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
            f"\\text{{Subtract: }} {rounded1} - {rounded2} = {estimate}",
            f"\\text{{Estimated amount left: }} {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = EstimateToSubtractMultiDigitNumbersGenerator()

    print("Easy (2-digit - 2-digit, round to nearest 10):")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print(f"  Steps: {problem.steps[0]}, {problem.steps[1]}")
        print()

    print("\nMedium (3-digit - 3-digit, round to nearest 10):")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()

    print("\nHard (3-digit - 3-digit, round to nearest 100):")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()

    print("\nChallenge (Word problems with estimation):")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()


if __name__ == '__main__':
    main()
