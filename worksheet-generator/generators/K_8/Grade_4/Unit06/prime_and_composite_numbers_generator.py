"""
Prime and Composite Numbers Generator - Grade 4 Unit 06
Generates problems on identifying prime and composite numbers
Example: [Problem example]
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PrimeAndCompositeNumbersGenerator:
    """Generates identifying prime and composite numbers problems."""

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
        """Generate easy problems."""
        # TODO: Implement easy problem generation
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)

        latex = f"{number1} + {number2} = ?"
        solution = str(number1 + number2)

        steps = [
            f"\\text{{Add: }} {number1} + {number2} = {number1 + number2}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems."""
        # TODO: Implement medium problem generation
        number1 = random.randint(10, 50)
        number2 = random.randint(10, 50)

        latex = f"{number1} + {number2} = ?"
        solution = str(number1 + number2)

        steps = [
            f"\\text{{Add: }} {number1} + {number2} = {number1 + number2}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems."""
        # TODO: Implement hard problem generation
        number1 = random.randint(50, 100)
        number2 = random.randint(50, 100)

        latex = f"{number1} + {number2} = ?"
        solution = str(number1 + number2)

        steps = [
            f"\\text{{Add: }} {number1} + {number2} = {number1 + number2}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems."""
        # TODO: Implement challenge problem generation
        number1 = random.randint(100, 200)
        number2 = random.randint(100, 200)

        latex = f"\\text{{Word problem with }} {number1} \\text{{ and }} {number2}"
        solution = str(number1 + number2)

        steps = [
            f"\\text{{Solve: }} {number1} + {number2} = {number1 + number2}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = PrimeAndCompositeNumbersGenerator()

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
