"""
Intercepts Generator - Grade 8 Unit 3
Generates problems about finding x and y intercepts
Example: Find the intercepts of y = 2x + 6
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class InterceptsGenerator:
    """Generates intercepts problems."""

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
        """Generate easy problems: find y-intercept."""
        m = random.randint(1, 6)
        b = random.randint(1, 10)

        latex = f"\\text{{Find the y-intercept of }} y = {m}x + {b}"
        solution = f"(0, {b})"
        steps = [
            f"\\text{{Y-intercept occurs when }} x = 0",
            f"y = {m}(0) + {b} = {b}",
            f"(0, {b})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium problems: find both intercepts."""
        m = random.randint(1, 6)
        b = random.randint(2, 12)

        x_int = -b / m if b % m == 0 else -b / m
        x_int_display = f"{-b // m}" if b % m == 0 else f"-\\frac{{{b}}}{{{m}}}"

        latex = f"\\text{{Find both intercepts of }} y = {m}x + {b}"
        solution = f"\\text{{x-int: }} ({x_int_display}, 0), \\text{{ y-int: }} (0, {b})"
        steps = [
            f"\\text{{Y-intercept: }} x = 0 \\Rightarrow y = {b}",
            f"\\text{{X-intercept: }} y = 0 \\Rightarrow 0 = {m}x + {b}",
            f"x = {x_int_display}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard problems: find intercepts from standard form."""
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(6, 20)

        latex = f"\\text{{Find both intercepts of }} {a}x + {b}y = {c}"
        x_int = c / a
        y_int = c / b

        x_int_str = f"{c // a}" if c % a == 0 else f"\\frac{{{c}}}{{{a}}}"
        y_int_str = f"{c // b}" if c % b == 0 else f"\\frac{{{c}}}{{{b}}}"

        solution = f"\\text{{x-int: }} ({x_int_str}, 0), \\text{{ y-int: }} (0, {y_int_str})"
        steps = [
            f"\\text{{X-intercept (y=0): }} {a}x = {c} \\Rightarrow x = {x_int_str}",
            f"\\text{{Y-intercept (x=0): }} {b}y = {c} \\Rightarrow y = {y_int_str}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: write equation given intercepts."""
        x_int = random.randint(2, 8)
        y_int = random.randint(2, 10)

        m = -y_int / x_int
        m_display = f"-\\frac{{{y_int}}}{{{x_int}}}" if y_int % x_int != 0 else f"{int(m)}"

        latex = f"\\text{{Write equation with x-int }} ({x_int}, 0) \\text{{ and y-int }} (0, {y_int})"
        solution = f"y = {m_display}x + {y_int}"
        steps = [
            f"\\text{{Use }} y = mx + b",
            f"\\text{{b = {y_int} (y-intercept)}}",
            f"\\text{{Slope: }} m = \\frac{{{y_int} - 0}}{{0 - {x_int}}} = {m_display}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = InterceptsGenerator()

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
