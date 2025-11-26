"""
Solutions to Linear Equations Generator - Grade 8 Unit 3
Generates problems about determining if a point is a solution to a linear equation
Example: Is (2, 5) a solution to y = 2x + 1?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SolutionsToLinearEquationsGenerator:
    """Generates solutions to linear equations problems."""

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
        """Generate easy problems: check if point is solution."""
        m = random.randint(1, 5)
        b = random.randint(1, 8)
        x = random.randint(1, 6)
        y = m * x + b

        is_solution = random.choice([True, False])
        if not is_solution:
            y += random.randint(1, 3)

        latex = f"\\text{{Is }} ({x}, {y}) \\text{{ a solution to }} y = {m}x + {b}?"
        solution = "\\text{Yes}" if is_solution else "\\text{No}"

        check_y = m * x + b
        steps = [
            f"\\text{{Substitute }} x = {x}",
            f"y = {m}({x}) + {b} = {check_y}",
            f"\\text{{Given point has }} y = {y}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium problems: find missing coordinate."""
        m = random.randint(2, 6)
        b = random.randint(-5, 8)

        if random.choice([True, False]):
            x = random.randint(1, 8)
            y = m * x + b
            latex = f"\\text{{Find y if }} ({x}, y) \\text{{ is on }} y = {m}x + {b}"
            solution = f"y = {y}"
            steps = [f"y = {m}({x}) + {b}", f"y = {y}"]
        else:
            y = random.randint(5, 30)
            x = (y - b) // m if (y - b) % m == 0 else random.randint(1, 8)
            y = m * x + b
            latex = f"\\text{{Find x if }} (x, {y}) \\text{{ is on }} y = {m}x + {b}"
            solution = f"x = {x}"
            steps = [f"{y} = {m}x + {b}", f"{y - b} = {m}x", f"x = {x}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard problems: determine if multiple points are solutions."""
        m = random.randint(2, 5)
        b = random.randint(-3, 5)

        x1, x2 = random.randint(1, 5), random.randint(6, 10)
        y1, y2 = m * x1 + b, m * x2 + b + random.randint(1, 3)

        latex = f"\\text{{Which points are on }} y = {m}x + {b}: ({x1}, {y1}) \\text{{ or }} ({x2}, {y2})?"
        solution = f"({x1}, {y1})"
        steps = [
            f"\\text{{Check }} ({x1}, {y1}): {m}({x1}) + {b} = {m * x1 + b} = {y1} \\checkmark",
            f"\\text{{Check }} ({x2}, {y2}): {m}({x2}) + {b} = {m * x2 + b} \\neq {y2}",
            f"\\text{{Only }} ({x1}, {y1})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: work backwards from solution."""
        x, y = random.randint(2, 8), random.randint(10, 30)
        m = random.randint(2, 5)
        b = y - m * x

        latex = f"\\text{{If }} ({x}, {y}) \\text{{ is on }} y = {m}x + b, \\text{{ find }} b"
        solution = f"b = {b}"
        steps = [
            f"{y} = {m}({x}) + b",
            f"{y} = {m * x} + b",
            f"b = {y} - {m * x}",
            f"b = {b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SolutionsToLinearEquationsGenerator()

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
