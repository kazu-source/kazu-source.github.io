"""
Subtracting Multi-Digit Numbers Generator - Grade 4 Unit 2
Generates subtraction problems with multi-digit numbers
Example: 5,527 - 1,845 = ?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SubtractingMultiDigitNumbersGenerator:
    """Generates subtracting multi-digit numbers problems."""

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
        """Generate easy problems: 3-digit subtraction, no regrouping."""
        num2 = random.randint(100, 400)
        num1 = num2 + random.randint(100, 400)

        # Ensure no regrouping needed
        n1_str = str(num1)
        n2_str = str(num2)
        digits1 = [int(d) for d in n1_str]
        digits2 = [int(d) for d in n2_str]

        # Adjust to avoid borrowing
        for i in range(len(digits1)):
            if digits1[i] < digits2[i]:
                digits2[i] = random.randint(0, digits1[i])

        num2 = int(''.join(map(str, digits2)))
        difference = num1 - num2

        latex = f"{num1:,} - {num2:,} = ?"
        solution = f"{difference:,}"

        steps = [
            f"{num1:,} - {num2:,} = {difference:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 4-digit subtraction with regrouping."""
        num2 = random.randint(1000, 5000)
        num1 = num2 + random.randint(1000, 4999)
        difference = num1 - num2

        latex = f"{num1:,} - {num2:,} = ?"
        solution = f"{difference:,}"

        steps = [
            f"{num1:,} - {num2:,} = {difference:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 5-digit subtraction."""
        num2 = random.randint(10000, 50000)
        num1 = num2 + random.randint(10000, 49999)
        difference = num1 - num2

        latex = f"{num1:,} - {num2:,} = ?"
        solution = f"{difference:,}"

        steps = [
            f"\\text{{Subtract from right to left, regrouping as needed}}",
            f"{num1:,} - {num2:,} = {difference:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: word problems with subtraction."""
        num1 = random.randint(5000, 9999)
        num2 = random.randint(1500, num1 - 100)
        difference = num1 - num2

        contexts = [
            f"A store had {num1:,} items. {num2:,} were sold. How many items remain?",
            f"A school has {num1:,} students. {num2:,} are in elementary. How many are in other grades?",
            f"A library had {num1:,} books. {num2:,} were checked out. How many books remain?",
            f"A town had {num1:,} residents. {num2:,} moved away. What's the new population?"
        ]

        context = random.choice(contexts)

        latex = f"\\text{{{context}}}"
        solution = f"{difference:,}"

        steps = [
            f"{num1:,} - {num2:,} = {difference:,}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = SubtractingMultiDigitNumbersGenerator()

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
