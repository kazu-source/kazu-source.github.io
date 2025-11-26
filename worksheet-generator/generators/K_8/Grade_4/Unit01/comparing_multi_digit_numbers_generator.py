"""
Comparing Multi-Digit Numbers Generator - Grade 4 Unit 1
Generates problems comparing multi-digit whole numbers
Example: Compare: 3,527 __ 3,572 (>, <, or =)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingMultiDigitNumbersGenerator:
    """Generates comparing multi-digit numbers problems."""

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
        """Generate easy problems: 3-digit numbers with clear differences."""
        num1 = random.randint(100, 999)
        # Make sure num2 is clearly different
        difference = random.randint(50, 200)
        if random.choice([True, False]):
            num2 = num1 + difference
        else:
            num2 = max(100, num1 - difference)

        if num1 > num2:
            comparison = ">"
        else:
            comparison = "<"

        latex = f"\\text{{Compare: }} {num1:,} \\quad \\text{{and}} \\quad {num2:,}"
        solution = f"{num1:,} {comparison} {num2:,}"

        steps = [
            f"\\text{{Compare the numbers}}",
            f"{num1:,} {comparison} {num2:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 4-digit numbers."""
        num1 = random.randint(1000, 9999)
        # Create num2 by changing one digit
        num1_str = str(num1)
        digits = list(num1_str)
        pos = random.randint(0, len(digits) - 1)
        old_digit = int(digits[pos])
        new_digit = random.choice([d for d in range(10) if d != old_digit])
        digits[pos] = str(new_digit)
        num2 = int(''.join(digits))

        if num1 > num2:
            comparison = ">"
        elif num1 < num2:
            comparison = "<"
        else:
            comparison = "="

        latex = f"\\text{{Compare: }} {num1:,} \\quad \\text{{and}} \\quad {num2:,}"
        solution = f"{num1:,} {comparison} {num2:,}"

        steps = [
            f"\\text{{Compare digit by digit from left to right}}",
            f"{num1:,} {comparison} {num2:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 5-6 digit numbers with close values."""
        num1 = random.randint(10000, 999999)
        # Create a close number
        difference = random.randint(1, 100)
        if random.choice([True, False]):
            num2 = num1 + difference
        else:
            num2 = num1 - difference

        if num1 > num2:
            comparison = ">"
        elif num1 < num2:
            comparison = "<"
        else:
            comparison = "="

        latex = f"\\text{{Compare: }} {num1:,} \\quad \\text{{and}} \\quad {num2:,}"
        solution = f"{num1:,} {comparison} {num2:,}"

        steps = [
            f"\\text{{Compare place by place}}",
            f"{num1:,} {comparison} {num2:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: ordering multiple numbers."""
        # Generate 3 different numbers
        numbers = random.sample(range(1000, 9999), 3)

        latex = f"\\text{{Order from least to greatest: }} {numbers[0]:,}, {numbers[1]:,}, {numbers[2]:,}"
        sorted_nums = sorted(numbers)
        solution = f"{sorted_nums[0]:,}, {sorted_nums[1]:,}, {sorted_nums[2]:,}"

        steps = [
            f"\\text{{Compare the numbers}}",
            f"\\text{{Ordered: }} {solution}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ComparingMultiDigitNumbersGenerator()

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
