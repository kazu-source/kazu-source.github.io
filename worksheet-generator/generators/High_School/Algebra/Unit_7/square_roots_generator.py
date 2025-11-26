"""
Square Roots Generator - Introduction to square roots
Generates problems about evaluating square root expressions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class SquareRootsGenerator:
    """Generates problems for evaluating square root expressions."""

    def __init__(self, seed=None):
        """Initialize the square roots generator."""
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
        """Generate a single square root problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate perfect square roots: √a where a is a perfect square"""
        # Perfect squares from 1 to 144
        perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
        value = random.choice(perfect_squares)

        latex = f"\\sqrt{{{value}}}"
        solution = int(value ** 0.5)

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate square root with multiplication: √a × √b"""
        # Use smaller perfect squares
        perfect_squares = [4, 9, 16, 25, 36, 49]
        a = random.choice(perfect_squares)
        b = random.choice(perfect_squares)

        latex = f"\\sqrt{{{a}}} \\times \\sqrt{{{b}}}"
        solution = int((a * b) ** 0.5)

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate square root of a product: √(a × b)"""
        # Use values that multiply to a perfect square
        perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
        product = random.choice(perfect_squares)

        # Find two factors
        factors = []
        for i in range(2, int(product ** 0.5) + 1):
            if product % i == 0:
                factors.append((i, product // i))

        if factors:
            a, b = random.choice(factors)
        else:
            a, b = 1, product

        latex = f"\\sqrt{{{a} \\times {b}}}"
        solution = int(product ** 0.5)

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate nested square roots: √(√a)² or √(a² + b²) where result is integer"""
        choice = random.choice(['nested', 'pythagorean'])

        if choice == 'nested':
            # √(√a)² = √a
            perfect_squares = [4, 9, 16, 25, 36, 49]
            value = random.choice(perfect_squares)

            latex = f"\\sqrt{{(\\sqrt{{{value}}})^2}}"
            solution = int(value ** 0.5)
        else:
            # Pythagorean triples
            triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
            a, b, c = random.choice(triples)

            latex = f"\\sqrt{{{a}^2 + {b}^2}}"
            solution = c

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = SquareRootsGenerator()

    print("Testing Square Roots Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")
