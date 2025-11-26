"""
Order of Operations Introduction Generator - Grade 6 Unit 4
Generates problems introducing order of operations (PEMDAS)
Example: Evaluate 3 + 4 × 2
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class OrderOfOperationsIntroductionGenerator:
    """Generates order of operations introduction problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
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
        """Generate easy problems: addition/subtraction and multiplication."""
        a = random.randint(2, 10)
        b = random.randint(2, 9)
        c = random.randint(2, 9)

        if random.choice([True, False]):
            # a + b × c
            result = a + (b * c)
            latex = f"{a} + {b} \\times {c}"
            steps = [
                f"\\text{{Multiply first: }} {b} \\times {c} = {b*c}",
                f"\\text{{Then add: }} {a} + {b*c} = {result}"
            ]
        else:
            # a × b + c
            result = (a * b) + c
            latex = f"{a} \\times {b} + {c}"
            steps = [
                f"\\text{{Multiply first: }} {a} \\times {b} = {a*b}",
                f"\\text{{Then add: }} {a*b} + {c} = {result}"
            ]

        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: with parentheses."""
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        c = random.randint(2, 9)

        if random.choice([True, False]):
            # (a + b) × c
            result = (a + b) * c
            latex = f"({a} + {b}) \\times {c}"
            steps = [
                f"\\text{{Parentheses first: }} {a} + {b} = {a+b}",
                f"\\text{{Then multiply: }} {a+b} \\times {c} = {result}"
            ]
        else:
            # (a - b) × c
            if a <= b:
                a, b = b, a
            result = (a - b) * c
            latex = f"({a} - {b}) \\times {c}"
            steps = [
                f"\\text{{Parentheses first: }} {a} - {b} = {a-b}",
                f"\\text{{Then multiply: }} {a-b} \\times {c} = {result}"
            ]

        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: division and multiplication."""
        a = random.randint(4, 12) * 2
        b = random.randint(2, 4)
        c = random.randint(2, 5)
        d = random.randint(2, 5)

        if random.choice([True, False]):
            # a ÷ b × c
            result = (a // b) * c
            latex = f"{a} \\div {b} \\times {c}"
            steps = [
                f"\\text{{Left to right: }} {a} \\div {b} = {a//b}",
                f"\\text{{Then multiply: }} {a//b} \\times {c} = {result}"
            ]
        else:
            # a × b ÷ c + d
            product = a * b
            quotient = product // c
            result = quotient + d
            latex = f"{a} \\times {b} \\div {c} + {d}"
            steps = [
                f"\\text{{Multiply: }} {a} \\times {b} = {product}",
                f"\\text{{Divide: }} {product} \\div {c} = {quotient}",
                f"\\text{{Add: }} {quotient} + {d} = {result}"
            ]

        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multiple operations with parentheses."""
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(2, 5)
        d = random.randint(2, 5)

        # (a + b) × c - d
        sum_val = a + b
        product = sum_val * c
        result = product - d

        latex = f"({a} + {b}) \\times {c} - {d}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Parentheses: }} {a} + {b} = {sum_val}",
                f"\\text{{Multiply: }} {sum_val} \\times {c} = {product}",
                f"\\text{{Subtract: }} {product} - {d} = {result}"
            ],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = OrderOfOperationsIntroductionGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex} = {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex} = {problem.solution}\n")


if __name__ == '__main__':
    main()
