"""
Adding and Subtracting Decimals Word Problems Generator - Grade 6 Unit 2
Generates word problems involving adding and subtracting decimals
Example: Sarah had $15.75. She spent $8.50. How much does she have left?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AddingAndSubtractingDecimalsWordProblemsGenerator:
    """Generates adding and subtracting decimals word problems."""

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
        """Generate easy problems: simple addition word problems."""
        contexts = [
            "Sarah bought a book for ${} and a pen for ${}. How much did she spend in total?",
            "A rope is {} meters long and another rope is {} meters long. What is the total length?",
            "Tom walked {} miles on Monday and {} miles on Tuesday. How far did he walk total?",
            "A bottle has {} liters of water and another has {} liters. How much water total?"
        ]

        context = random.choice(contexts)
        num1 = round(random.uniform(1.0, 10.0), 1)
        num2 = round(random.uniform(1.0, 10.0), 1)
        result = round(num1 + num2, 1)

        latex = f"\\text{{{context.format(num1, num2)}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num1} + {num2} = {result}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: subtraction word problems."""
        contexts = [
            "Maria had ${} and spent ${}. How much money does she have left?",
            "A rope was {} meters long. After cutting {} meters off, how much is left?",
            "A container had {} liters of juice. After pouring out {} liters, how much remains?",
            "John had {} pounds of flour and used {} pounds. How much flour is left?"
        ]

        context = random.choice(contexts)
        num2 = round(random.uniform(1.0, 10.0), 2)
        num1 = round(num2 + random.uniform(5.0, 15.0), 2)
        result = round(num1 - num2, 2)

        latex = f"\\text{{{context.format(num1, num2)}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num1} - {num2} = {result}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: multi-step problems."""
        num1 = round(random.uniform(10.0, 30.0), 2)
        purchase1 = round(random.uniform(2.0, 8.0), 2)
        purchase2 = round(random.uniform(2.0, 8.0), 2)
        result = round(num1 - purchase1 - purchase2, 2)

        latex = f"\\text{{Emma had $}} {num1} \\text{{. She bought a snack for $}} {purchase1}"
        latex += f"\\text{{ and a drink for $}} {purchase2} \\text{{. How much money does she have left?}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num1} - {purchase1} - {purchase2} = {result}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: combined operations."""
        initial = round(random.uniform(20.0, 50.0), 2)
        spent = round(random.uniform(5.0, 15.0), 2)
        earned = round(random.uniform(5.0, 15.0), 2)
        result = round(initial - spent + earned, 2)

        latex = f"\\text{{Alex had $}} {initial} \\text{{. He spent $}} {spent}"
        latex += f"\\text{{ on lunch and then earned $}} {earned} \\text{{. How much money does Alex have now?}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{initial} - {spent} + {earned} = {result}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = AddingAndSubtractingDecimalsWordProblemsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 2):
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
