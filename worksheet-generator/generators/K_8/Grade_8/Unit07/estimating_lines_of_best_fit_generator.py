"""
Estimating Lines of Best Fit Generator - Grade 8 Unit 7
Generates problems about lines of best fit
Example: Given points, estimate the line of best fit.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EstimatingLinesOfBestFitGenerator:
    """Generates estimating lines of best fit problems."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        latex = "\\text{What is the line of best fit?}"
        solution = "\\text{A line that best represents the trend in data}"
        steps = [solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 5)
        b = random.randint(3, 8)

        latex = f"\\text{{Data points roughly follow }} y = {m}x + {b}. \\text{{ Estimate }} y \\text{{ when }} x = 10."
        y = m * 10 + b
        solution = f"y \\approx {y}"
        steps = [
            f"y = {m}(10) + {b}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        points = [(1, 3), (2, 5), (3, 7), (4, 9)]

        latex = f"\\text{{Data: }} {points}. \\text{{ Estimate line of best fit.}}"
        solution = "y = 2x + 1"
        steps = [
            "\\text{Points follow linear pattern}",
            "\\text{Slope } m = 2, \\text{ intercept } b = 1",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        m = random.randint(2, 4)
        b = random.randint(5, 10)
        x = random.randint(15, 25)

        latex = f"\\text{{Line of best fit: }} y = {m}x + {b}. \\text{{ Predict }} y \\text{{ when }} x = {x}."
        y = m * x + b
        solution = f"y \\approx {y}"
        steps = [
            f"y = {m}({x}) + {b}",
            f"y = {y}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = EstimatingLinesOfBestFitGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
