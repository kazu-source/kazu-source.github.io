"""
Graphing Slope-Intercept Form Generator - Grade 8 Unit 3
Generates problems about graphing lines in slope-intercept form
Example: Graph y = 2x + 3
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class GraphingSlopeInterceptFormGenerator:
    """Generates graphing slope-intercept form problems."""

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
        """Generate easy problems: graph simple positive slope."""
        m = random.randint(1, 4)
        b = random.randint(1, 6)

        latex = f"\\text{{Graph }} y = {m}x + {b}"
        solution = f"\\text{{Start at (0, {b}), rise {m}, run 1}}"
        steps = [
            f"\\text{{Y-intercept: (0, {b})}}",
            f"\\text{{Slope: }} {m} = \\frac{{{m}}}{{1}}",
            f"\\text{{From (0, {b}), go up {m}, right 1}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium problems: graph negative slope."""
        m = random.randint(-4, -1)
        b = random.randint(2, 8)

        latex = f"\\text{{Graph }} y = {m}x + {b}"
        solution = f"\\text{{Start at (0, {b}), down {abs(m)}, right 1}}"
        steps = [
            f"\\text{{Y-intercept: (0, {b})}}",
            f"\\text{{Slope: }} {m} = \\frac{{{m}}}{{1}}",
            f"\\text{{From (0, {b}), go down {abs(m)}, right 1}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard problems: fractional slope."""
        num = random.choice([1, 2, 3])
        den = random.choice([2, 3, 4])
        if num == den:
            den += 1
        b = random.randint(1, 6)

        latex = f"\\text{{Graph }} y = \\frac{{{num}}}{{{den}}}x + {b}"
        solution = f"\\text{{Start at (0, {b}), rise {num}, run {den}}}"
        steps = [
            f"\\text{{Y-intercept: (0, {b})}}",
            f"\\text{{Slope: }} \\frac{{{num}}}{{{den}}}",
            f"\\text{{From (0, {b}), go up {num}, right {den}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: find points on line."""
        m = random.randint(2, 5)
        b = random.randint(1, 8)

        x1, x2 = random.randint(1, 4), random.randint(5, 8)
        y1, y2 = m * x1 + b, m * x2 + b

        latex = f"\\text{{Find two points on }} y = {m}x + {b}"
        solution = f"({x1}, {y1}), ({x2}, {y2})"
        steps = [
            f"\\text{{When }} x = {x1}: y = {m}({x1}) + {b} = {y1}",
            f"\\text{{When }} x = {x2}: y = {m}({x2}) + {b} = {y2}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = GraphingSlopeInterceptFormGenerator()

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
