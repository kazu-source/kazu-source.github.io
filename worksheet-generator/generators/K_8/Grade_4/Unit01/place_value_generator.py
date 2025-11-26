"""
Place Value Generator - Grade 4 Unit 1
Generates problems on understanding place value in multi-digit numbers
Example: What is the value of the digit 5 in 3,527?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PlaceValueGenerator:
    """Generates place value problems."""

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
        """Generate easy problems: 3-digit numbers."""
        number = random.randint(100, 999)
        digits = [int(d) for d in str(number)]
        place = random.choice(['hundreds', 'tens', 'ones'])

        if place == 'hundreds':
            digit = digits[0]
            value = digit * 100
        elif place == 'tens':
            digit = digits[1]
            value = digit * 10
        else:
            digit = digits[2]
            value = digit

        latex = f"\\text{{What is the value of the digit }} {digit} \\text{{ in }} {number:,}?"
        solution = str(value)

        steps = [
            f"\\text{{The number is }} {number:,}",
            f"\\text{{The digit }} {digit} \\text{{ is in the {place} place}}",
            f"\\text{{Value: }} {value}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 4-digit numbers."""
        number = random.randint(1000, 9999)
        digits = [int(d) for d in str(number)]
        place = random.choice(['thousands', 'hundreds', 'tens', 'ones'])

        place_map = {
            'thousands': (digits[0], digits[0] * 1000),
            'hundreds': (digits[1], digits[1] * 100),
            'tens': (digits[2], digits[2] * 10),
            'ones': (digits[3], digits[3])
        }

        digit, value = place_map[place]

        latex = f"\\text{{What is the value of the digit }} {digit} \\text{{ in }} {number:,}?"
        solution = str(value)

        steps = [
            f"\\text{{The number is }} {number:,}",
            f"\\text{{The digit }} {digit} \\text{{ is in the {place} place}}",
            f"\\text{{Value: }} {value:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 5-6 digit numbers."""
        number = random.randint(10000, 999999)
        num_str = str(number)
        digits = [int(d) for d in num_str]

        # Determine place values based on number length
        if len(num_str) == 5:
            places = ['ten thousands', 'thousands', 'hundreds', 'tens', 'ones']
            multipliers = [10000, 1000, 100, 10, 1]
        else:
            places = ['hundred thousands', 'ten thousands', 'thousands', 'hundreds', 'tens', 'ones']
            multipliers = [100000, 10000, 1000, 100, 10, 1]

        idx = random.randint(0, len(digits) - 1)
        digit = digits[idx]
        place = places[idx]
        value = digit * multipliers[idx]

        latex = f"\\text{{What is the value of the digit }} {digit} \\text{{ in }} {number:,}?"
        solution = str(value)

        steps = [
            f"\\text{{The number is }} {number:,}",
            f"\\text{{The digit }} {digit} \\text{{ is in the {place} place}}",
            f"\\text{{Value: }} {value:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: comparing values of different digits."""
        number = random.randint(10000, 999999)
        num_str = str(number)
        digits = [int(d) for d in num_str]

        # Pick two different positions
        idx1, idx2 = random.sample(range(len(digits)), 2)

        if len(num_str) == 5:
            places = ['ten thousands', 'thousands', 'hundreds', 'tens', 'ones']
            multipliers = [10000, 1000, 100, 10, 1]
        else:
            places = ['hundred thousands', 'ten thousands', 'thousands', 'hundreds', 'tens', 'ones']
            multipliers = [100000, 10000, 1000, 100, 10, 1]

        value1 = digits[idx1] * multipliers[idx1]
        value2 = digits[idx2] * multipliers[idx2]

        latex = f"\\text{{In }} {number:,}, \\text{{ how many times greater is the value of the }} {digits[idx1]} \\text{{ than the }} {digits[idx2]}?"

        if value1 > value2:
            times = value1 // value2 if value2 != 0 else value1
        else:
            times = value2 // value1 if value1 != 0 else value2

        solution = str(times) if times > 0 else "0"

        steps = [
            f"\\text{{Value of }} {digits[idx1]}: {value1:,}",
            f"\\text{{Value of }} {digits[idx2]}: {value2:,}",
            f"\\text{{Ratio: }} {value1:,} \\div {value2:,} = {solution}" if value1 > value2 else f"\\text{{Ratio: }} {value2:,} \\div {value1:,} = {solution}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = PlaceValueGenerator()

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
