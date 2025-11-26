"""
Intro to Slope-Intercept Form Generator - Grade 8 Unit 3
Generates problems introducing slope-intercept form y = mx + b
Example: Identify the slope and y-intercept in y = 3x + 5
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IntroToSlopeInterceptFormGenerator:
    """Generates intro to slope-intercept form problems."""

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
        """Generate easy problems: identify slope and y-intercept."""
        m = random.randint(1, 8)
        b = random.randint(1, 10)

        latex = f"\\text{{Find the slope and y-intercept of }} y = {m}x + {b}"
        solution = f"\\text{{Slope: }} {m}, \\text{{ y-intercept: }} {b}"
        steps = [
            f"y = {m}x + {b}",
            f"\\text{{Slope (m) = }} {m}",
            f"\\text{{Y-intercept (b) = }} {b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium problems: identify slope/intercept with negative values."""
        m = random.randint(-6, -1)
        b = random.randint(-8, 8)

        b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        latex = f"\\text{{Find the slope and y-intercept of }} y = {m}x {b_str}"
        solution = f"\\text{{Slope: }} {m}, \\text{{ y-intercept: }} {b}"
        steps = [
            f"y = {m}x {b_str}",
            f"\\text{{Slope (m) = }} {m}",
            f"\\text{{Y-intercept (b) = }} {b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard problems: identify from non-standard form."""
        m = random.randint(2, 6)
        b = random.randint(1, 10)

        # Present as x term after constant
        latex = f"\\text{{Write in slope-intercept form: }} y = {b} + {m}x"
        solution = f"y = {m}x + {b}"
        steps = [
            f"y = {b} + {m}x",
            f"\\text{{Rearrange: }} y = {m}x + {b}",
            f"\\text{{Slope: }} {m}, \\text{{ y-intercept: }} {b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: convert from standard form."""
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(6, 20)

        m = -a / b
        y_int = c / b

        m_str = f"-\\frac{{{a}}}{{{b}}}" if c % b != 0 else f"{int(m)}"
        b_str = f"\\frac{{{c}}}{{{b}}}" if c % b != 0 else f"{int(y_int)}"

        latex = f"\\text{{Convert to slope-intercept form: }} {a}x + {b}y = {c}"
        solution = f"y = {m_str}x + {b_str}"
        steps = [
            f"{a}x + {b}y = {c}",
            f"{b}y = -{a}x + {c}",
            f"y = {m_str}x + {b_str}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = IntroToSlopeInterceptFormGenerator()

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
