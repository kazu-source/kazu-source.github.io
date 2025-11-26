"""
Adding Multi-Digit Numbers Generator - Grade 4 Unit 2
Generates addition problems with multi-digit numbers
Example: 3,527 + 1,845 = ?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AddingMultiDigitNumbersGenerator:
    """Generates adding multi-digit numbers problems."""

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
        """Generate easy problems: 3-digit addition, no regrouping."""
        # Ensure no regrouping by controlling digit sums
        num1 = random.randint(100, 400)
        num2 = random.randint(100, 400)

        # Adjust to avoid regrouping
        n1_str = str(num1)
        n2_str = str(num2)
        digits1 = [int(d) for d in n1_str]
        digits2 = [int(d) for d in n2_str]

        # Adjust ones place
        if digits1[2] + digits2[2] >= 10:
            digits2[2] = random.randint(0, 9 - digits1[2])

        # Adjust tens place
        if digits1[1] + digits2[1] >= 10:
            digits2[1] = random.randint(0, 9 - digits1[1])

        num2 = int(''.join(map(str, digits2)))
        sum_result = num1 + num2

        latex = f"{num1:,} + {num2:,} = ?"
        solution = f"{sum_result:,}"

        steps = [
            f"{num1:,} + {num2:,} = {sum_result:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 4-digit addition with regrouping."""
        num1 = random.randint(1000, 9999)
        num2 = random.randint(1000, 9999)
        sum_result = num1 + num2

        latex = f"{num1:,} + {num2:,} = ?"
        solution = f"{sum_result:,}"

        steps = [
            f"{num1:,} + {num2:,} = {sum_result:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 5-digit addition."""
        num1 = random.randint(10000, 99999)
        num2 = random.randint(10000, 99999)
        sum_result = num1 + num2

        latex = f"{num1:,} + {num2:,} = ?"
        solution = f"{sum_result:,}"

        steps = [
            f"\\text{{Add from right to left, regrouping as needed}}",
            f"{num1:,} + {num2:,} = {sum_result:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: word problems with addition."""
        num1 = random.randint(1500, 9999)
        num2 = random.randint(1500, 9999)
        sum_result = num1 + num2

        contexts = [
            f"A store sold {num1:,} items in January and {num2:,} items in February. How many items total?",
            f"One school has {num1:,} students and another has {num2:,} students. How many students in all?",
            f"A library has {num1:,} fiction books and {num2:,} non-fiction books. How many books total?",
            f"In 2020, a city had {num1:,} residents. {num2:,} more moved in. What's the new population?"
        ]

        context = random.choice(contexts)

        latex = f"\\text{{{context}}}"
        solution = f"{sum_result:,}"

        steps = [
            f"{num1:,} + {num2:,} = {sum_result:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = AddingMultiDigitNumbersGenerator()

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
