"""
Square and Cube Roots Generator - Grade 8 Unit 1
Generates problems finding square roots and cube roots
Example: √64 = 8, ∛27 = 3
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SquareAndCubeRootsGenerator:
    """Generates square and cube roots problems."""

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
        """Generate easy problems: perfect squares up to 100."""
        perfect_squares = [(1, 1), (4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (49, 7), (64, 8), (81, 9), (100, 10)]

        square, root = random.choice(perfect_squares)

        latex = f"\\sqrt{{{square}}}"
        solution = str(root)
        steps = [f"\\sqrt{{{square}}} = {root}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: mix of square roots and cube roots."""
        if random.choice([True, False]):
            # Square roots of larger perfect squares
            perfect_squares = [(121, 11), (144, 12), (169, 13), (196, 14), (225, 15), (256, 16), (289, 17), (324, 18)]
            square, root = random.choice(perfect_squares)
            latex = f"\\sqrt{{{square}}}"
            solution = str(root)
            steps = [f"\\sqrt{{{square}}} = {root}"]
        else:
            # Cube roots
            perfect_cubes = [(1, 1), (8, 2), (27, 3), (64, 4), (125, 5), (216, 6), (343, 7), (512, 8), (729, 9), (1000, 10)]
            cube, root = random.choice(perfect_cubes)
            latex = f"\\sqrt[3]{{{cube}}}"
            solution = str(root)
            steps = [f"\\sqrt[3]{{{cube}}} = {root}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: expressions involving roots."""
        problem_type = random.choice(['add', 'multiply', 'power'])

        if problem_type == 'add':
            # √a + √b
            squares1 = [(4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (49, 7)]
            squares2 = [(4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (49, 7)]
            sq1, root1 = random.choice(squares1)
            sq2, root2 = random.choice(squares2)

            latex = f"\\sqrt{{{sq1}}} + \\sqrt{{{sq2}}}"
            solution = str(root1 + root2)
            steps = [f"\\sqrt{{{sq1}}} = {root1}", f"\\sqrt{{{sq2}}} = {root2}", f"{root1} + {root2} = {root1 + root2}"]

        elif problem_type == 'multiply':
            # √a × √b = √(ab)
            roots = [2, 3, 4, 5, 6]
            root1 = random.choice(roots)
            root2 = random.choice(roots)

            sq1 = root1 ** 2
            sq2 = root2 ** 2
            product = root1 * root2

            latex = f"\\sqrt{{{sq1}}} \\times \\sqrt{{{sq2}}}"
            solution = str(product)
            steps = [f"\\sqrt{{{sq1}}} \\times \\sqrt{{{sq2}}} = \\sqrt{{{sq1 * sq2}}}", f"\\sqrt{{{sq1 * sq2}}} = {product}"]

        else:  # power
            # (√a)²
            squares = [(4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (49, 7), (64, 8)]
            sq, root = random.choice(squares)

            latex = f"(\\sqrt{{{sq}}})^2"
            solution = str(sq)
            steps = [f"(\\sqrt{{{sq}}})^2 = {sq}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex expressions and solving equations."""
        problem_type = random.choice(['equation', 'nested', 'expression'])

        if problem_type == 'equation':
            # x² = a, solve for x
            perfect_squares = [(4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (49, 7), (64, 8), (81, 9), (100, 10)]
            square, root = random.choice(perfect_squares)

            latex = f"x^2 = {square}"
            solution = f"x = \\pm {root}"
            steps = [f"x = \\pm\\sqrt{{{square}}}", f"x = \\pm {root}"]

        elif problem_type == 'nested':
            # √(√a)
            values = [(16, 4, 2), (81, 9, 3), (256, 16, 4)]
            outer, middle, inner = random.choice(values)

            latex = f"\\sqrt{{\\sqrt{{{outer}}}}}"
            solution = str(inner)
            steps = [f"\\sqrt{{{outer}}} = {middle}", f"\\sqrt{{{middle}}} = {inner}"]

        else:  # complex expression
            # ∛a + √b
            cubes = [(8, 2), (27, 3), (64, 4), (125, 5)]
            squares = [(4, 2), (9, 3), (16, 4), (25, 5)]

            cube, cube_root = random.choice(cubes)
            square, square_root = random.choice(squares)

            latex = f"\\sqrt[3]{{{cube}}} + \\sqrt{{{square}}}"
            solution = str(cube_root + square_root)
            steps = [f"\\sqrt[3]{{{cube}}} = {cube_root}", f"\\sqrt{{{square}}} = {square_root}", f"{cube_root} + {square_root} = {cube_root + square_root}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = SquareAndCubeRootsGenerator()

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
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
