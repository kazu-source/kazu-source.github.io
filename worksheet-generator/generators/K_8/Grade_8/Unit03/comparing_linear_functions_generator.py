"""
Comparing Linear Functions Generator - Grade 8 Unit 3
Generates problems about comparing different representations of linear functions
Example: Which function has a greater rate of change?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingLinearFunctionsGenerator:
    """Generates comparing linear functions problems."""

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
        m1 = random.randint(2, 8)
        m2 = random.randint(2, 8)
        while m1 == m2:
            m2 = random.randint(2, 8)

        b1 = random.randint(1, 8)
        b2 = random.randint(1, 8)

        greater = m1 if m1 > m2 else m2
        latex = f"\\text{{Which has a greater slope: }} f(x) = {m1}x + {b1} \\text{{ or }} g(x) = {m2}x + {b2}?"
        solution = f"f(x)" if m1 > m2 else f"g(x)"
        steps = [
            f"\\text{{Slope of f(x): }} {m1}",
            f"\\text{{Slope of g(x): }} {m2}",
            f"{m1} {'>' if m1 > m2 else '<'} {m2}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m1 = random.randint(2, 6)
        m2 = random.randint(2, 6)
        while m1 == m2:
            m2 = random.randint(2, 6)

        b1 = random.randint(1, 10)
        b2 = random.randint(1, 10)

        latex = f"\\text{{Compare y-intercepts: }} y = {m1}x + {b1} \\text{{ and }} y = {m2}x + {b2}"
        solution = f"{b1} {'>' if b1 > b2 else '<' if b1 < b2 else '='} {b2}"
        steps = [
            f"\\text{{Y-intercept 1: }} {b1}",
            f"\\text{{Y-intercept 2: }} {b2}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        m1 = random.randint(3, 7)
        b1 = random.randint(5, 15)

        x1, x2 = 0, random.randint(3, 6)
        m2 = random.randint(2, 8)
        y1, y2 = random.randint(3, 10), random.randint(15, 30)

        latex = f"\\text{{Function A: }} y = {m1}x + {b1}. \\text{{ Function B passes through }} ({x1}, {y1}), ({x2}, {y2}). \\text{{ Which is steeper?}}"
        m2_calc = (y2 - y1) / (x2 - x1)
        solution = "A" if m1 > m2_calc else "B"
        steps = [
            f"\\text{{Slope of A: }} {m1}",
            f"\\text{{Slope of B: }} \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = {m2_calc}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        m1 = random.randint(3, 8)
        b1 = random.randint(10, 30)
        m2 = random.randint(2, 7)
        b2 = random.randint(15, 40)

        x_intersect = (b2 - b1) / (m1 - m2) if m1 != m2 else 0

        latex = f"\\text{{At what x-value do }} y = {m1}x + {b1} \\text{{ and }} y = {m2}x + {b2} \\text{{ intersect?}}"
        solution = f"x = {x_intersect:.1f}" if x_intersect != int(x_intersect) else f"x = {int(x_intersect)}"
        steps = [
            f"{m1}x + {b1} = {m2}x + {b2}",
            f"{m1 - m2}x = {b2 - b1}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = ComparingLinearFunctionsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
