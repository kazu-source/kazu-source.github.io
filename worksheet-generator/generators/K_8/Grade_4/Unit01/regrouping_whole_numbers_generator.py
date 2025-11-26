"""
Regrouping Whole Numbers Generator - Grade 4 Unit 1
Generates problems on regrouping and decomposing numbers
Example: Regroup 3,527 as 35 hundreds and 27 ones
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RegroupingWholeNumbersGenerator:
    """Generates regrouping problems."""

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
        """Generate easy problems: regroup 3-digit numbers."""
        number = random.randint(100, 999)

        # Regroup into tens and ones
        tens = number // 10
        ones = number % 10

        latex = f"\\text{{Regroup }} {number:,} \\text{{ as tens and ones}}"
        solution = f"{tens} tens and {ones} ones" if ones > 0 else f"{tens} tens"

        steps = [
            f"\\text{{Number: }} {number:,}",
            f"\\text{{Tens: }} {number:,} \\div 10 = {tens}",
            f"\\text{{Ones: }} {number:,} - ({tens} \\times 10) = {ones}",
            f"\\text{{Answer: }} {solution}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: regroup 4-digit numbers into different units."""
        number = random.randint(1000, 9999)

        regroup_type = random.choice(['hundreds', 'tens'])

        if regroup_type == 'hundreds':
            hundreds = number // 100
            remainder = number % 100
            latex = f"\\text{{Regroup }} {number:,} \\text{{ as hundreds and ones}}"
            solution = f"{hundreds} hundreds and {remainder} ones" if remainder > 0 else f"{hundreds} hundreds"
        else:
            tens = number // 10
            ones = number % 10
            latex = f"\\text{{Regroup }} {number:,} \\text{{ as tens and ones}}"
            solution = f"{tens} tens and {ones} ones" if ones > 0 else f"{tens} tens"

        steps = [
            f"\\text{{Number: }} {number:,}",
            f"\\text{{Regrouped: }} {solution}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: regroup with specific constraints."""
        number = random.randint(1000, 9999)

        # Ask to regroup in a specific way
        choices = [
            ('hundreds and tens', lambda n: f"{n // 100} hundreds and {(n % 100) // 10} tens"),
            ('thousands and hundreds', lambda n: f"{n // 1000} thousands and {(n % 1000) // 100} hundreds"),
            ('tens', lambda n: f"{n // 10} tens")
        ]

        choice_name, choice_func = random.choice(choices)
        latex = f"\\text{{Regroup }} {number:,} \\text{{ as }} {choice_name}"
        solution = choice_func(number)

        steps = [
            f"\\text{{Number: }} {number:,}",
            f"\\text{{Regrouped: }} {solution}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multiple regroupings or word problems."""
        number = random.randint(2000, 9999)

        # Regroup in unusual ways
        hundreds = number // 100
        tens = number // 10

        problem_type = random.choice(['unusual', 'comparison'])

        if problem_type == 'unusual':
            latex = f"\\text{{How many tens are in }} {number:,}?"
            solution = str(tens)
            steps = [
                f"\\text{{Number: }} {number:,}",
                f"\\text{{Tens: }} {number:,} \\div 10 = {tens}"
            ]
        else:
            latex = f"\\text{{How many hundreds are in }} {number:,}?"
            solution = str(hundreds)
            steps = [
                f"\\text{{Number: }} {number:,}",
                f"\\text{{Hundreds: }} {number:,} \\div 100 = {hundreds}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = RegroupingWholeNumbersGenerator()

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
