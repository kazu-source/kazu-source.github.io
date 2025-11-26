"""
Writing Slope-Intercept Equations Generator - Grade 8 Unit 3
Generates problems about writing equations in slope-intercept form
Example: Write an equation with slope 3 and y-intercept 5
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class WritingSlopeInterceptEquationsGenerator:
    """Generates writing slope-intercept equations problems."""

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
        """Generate easy problems: given slope and y-intercept."""
        m = random.randint(1, 8)
        b = random.randint(1, 10)

        latex = f"\\text{{Write an equation with slope }} {m} \\text{{ and y-intercept }} {b}"
        solution = f"y = {m}x + {b}"
        steps = [
            f"\\text{{Use }} y = mx + b",
            f"\\text{{Substitute }} m = {m}, b = {b}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium problems: given two points."""
        x1, x2 = random.randint(1, 5), random.randint(6, 10)
        m = random.randint(2, 5)
        y1 = random.randint(3, 12)
        y2 = y1 + m * (x2 - x1)
        b = y1 - m * x1

        latex = f"\\text{{Write an equation through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})"
        solution = f"y = {m}x + {b}"
        steps = [
            f"m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {m}",
            f"\\text{{Use point }} ({x1}, {y1}): {y1} = {m}({x1}) + b",
            f"b = {b}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard problems: given point and slope."""
        x = random.randint(1, 8)
        y = random.randint(5, 20)
        m = random.randint(-4, 6)
        if m == 0:
            m = 1
        b = y - m * x

        b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        latex = f"\\text{{Write an equation with slope }} {m} \\text{{ through }} ({x}, {y})"
        solution = f"y = {m}x {b_str}"
        steps = [
            f"y = mx + b",
            f"{y} = {m}({x}) + b",
            f"{y} = {m * x} + b",
            f"b = {b}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: parallel or perpendicular lines."""
        problem_type = random.choice(['parallel', 'perpendicular'])

        m1 = random.randint(2, 6)
        b1 = random.randint(1, 8)
        x = random.randint(1, 6)
        y = random.randint(5, 15)

        if problem_type == 'parallel':
            m2 = m1
            b2 = y - m2 * x

            b2_str = f"+ {b2}" if b2 >= 0 else f"- {abs(b2)}"
            latex = f"\\text{{Write equation parallel to }} y = {m1}x + {b1} \\text{{ through }} ({x}, {y})"
            solution = f"y = {m2}x {b2_str}"
            steps = [
                f"\\text{{Parallel lines have same slope: }} m = {m1}",
                f"{y} = {m2}({x}) + b",
                f"b = {b2}",
                solution
            ]
        else:  # perpendicular
            m2_num = -1
            m2_den = m1

            b2 = y - (m2_num / m2_den) * x
            b2_int = int(b2) if b2 == int(b2) else b2

            latex = f"\\text{{Write equation perpendicular to }} y = {m1}x + {b1} \\text{{ through }} ({x}, {y})"
            solution = f"y = -\\frac{{1}}{{{m1}}}x + {b2_int}"
            steps = [
                f"\\text{{Perpendicular slope: }} m = -\\frac{{1}}{{{m1}}}",
                f"{y} = -\\frac{{1}}{{{m1}}}({x}) + b",
                f"b = {b2_int}",
                solution
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = WritingSlopeInterceptEquationsGenerator()

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
