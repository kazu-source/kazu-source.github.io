"""
Slope Generator - Grade 8 Unit 3
Generates problems about finding and interpreting slope
Example: Find the slope between (2, 3) and (5, 9)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SlopeGenerator:
    """Generates slope problems."""

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
        """Generate easy problems: find slope from two points."""
        x1, x2 = random.randint(1, 5), random.randint(6, 10)
        m = random.randint(2, 6)
        y1 = random.randint(1, 8)
        y2 = y1 + m * (x2 - x1)

        latex = f"\\text{{Find the slope between }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})"
        solution = f"m = {m}"
        steps = [
            f"m = \\frac{{y_2 - y_1}}{{x_2 - x_1}}",
            f"m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}}",
            f"m = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {m}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium problems: find slope with negative values."""
        x1, x2 = random.randint(-5, 0), random.randint(1, 6)
        m = random.randint(-4, -1)
        y1 = random.randint(5, 15)
        y2 = y1 + m * (x2 - x1)

        latex = f"\\text{{Find the slope between }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})"
        solution = f"m = {m}"
        steps = [
            f"m = \\frac{{{y2} - {y1}}}{{{x2} - ({x1})}}",
            f"m = \\frac{{{y2 - y1}}}{{{x2 - x1}}}",
            f"m = {m}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard problems: fractional slopes."""
        x1, x2 = random.randint(1, 4), random.randint(7, 12)
        rise = random.choice([1, 2, 3, 5])
        run = random.choice([2, 3, 4, 6])
        if rise == run:
            run += 1

        y1 = random.randint(2, 8)
        y2 = y1 + rise
        x2 = x1 + run

        from fractions import Fraction
        slope_frac = Fraction(rise, run)

        latex = f"\\text{{Find the slope between }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})"
        solution = f"m = \\frac{{{slope_frac.numerator}}}{{{slope_frac.denominator}}}"
        steps = [
            f"m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}}",
            f"m = \\frac{{{rise}}}{{{run}}} = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: find missing coordinate given slope."""
        m = random.randint(2, 5)
        x1, y1 = random.randint(1, 5), random.randint(2, 10)
        x2 = random.randint(7, 12)
        y2 = y1 + m * (x2 - x1)

        latex = f"\\text{{If the slope between }} ({x1}, {y1}) \\text{{ and }} ({x2}, y) \\text{{ is }} {m}, \\text{{ find }} y"
        solution = f"y = {y2}"
        steps = [
            f"{m} = \\frac{{y - {y1}}}{{{x2} - {x1}}}",
            f"{m} = \\frac{{y - {y1}}}{{{x2 - x1}}}",
            f"{m * (x2 - x1)} = y - {y1}",
            f"y = {y2}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SlopeGenerator()

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
