"""
Linear and Nonlinear Functions Generator - Grade 8 Unit 4
Generates problems identifying linear vs nonlinear functions
Example: Is y = x² a linear or nonlinear function?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class LinearAndNonlinearFunctionsGenerator:
    """Generates linear and nonlinear functions problems."""

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
        is_linear = random.choice([True, False])

        if is_linear:
            m = random.randint(1, 6)
            b = random.randint(1, 10)
            latex = f"\\text{{Is }} y = {m}x + {b} \\text{{ linear or nonlinear?}}"
            solution = "\\text{Linear}"
            steps = ["\\text{Highest power of x is 1}", solution]
        else:
            exp = random.choice([2, 3])
            latex = f"\\text{{Is }} y = x^{{{exp}}} \\text{{ linear or nonlinear?}}"
            solution = "\\text{Nonlinear}"
            steps = [f"\\text{{Highest power of x is {exp}}}", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x_vals = [0, 1, 2, 3]
        is_linear = random.choice([True, False])

        if is_linear:
            m, b = random.randint(2, 5), random.randint(1, 6)
            y_vals = [m * x + b for x in x_vals]
            latex = f"\\text{{Is this table linear? x: }} {x_vals}; \\text{{ y: }} {y_vals}"
            solution = "\\text{Linear (constant rate of change)}"
        else:
            y_vals = [x ** 2 for x in x_vals]
            latex = f"\\text{{Is this table linear? x: }} {x_vals}; \\text{{ y: }} {y_vals}"
            solution = "\\text{Nonlinear (rate of change varies)}"

        steps = ["\\text{Check if rate of change is constant}", solution]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        func_type = random.choice(['abs', 'reciprocal', 'linear_complex'])

        if func_type == 'abs':
            latex = "\\text{Is } y = |x| \\text{ linear or nonlinear?}"
            solution = "\\text{Nonlinear}"
            steps = ["\\text{Absolute value creates V-shape, not straight line}", solution]
        elif func_type == 'reciprocal':
            latex = "\\text{Is } y = \\frac{1}{x} \\text{ linear or nonlinear?}"
            solution = "\\text{Nonlinear}"
            steps = ["\\text{Reciprocal function is not linear}", solution]
        else:
            m, b, c = random.randint(2, 5), random.randint(1, 4), random.randint(1, 6)
            latex = f"\\text{{Is }} y = {m}(x + {b}) - {c} \\text{{ linear or nonlinear?}}"
            solution = "\\text{Linear}"
            steps = [f"y = {m}(x + {b}) - {c} = {m}x + {m * b - c}", "\\text{Linear}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Is } y = 2x^2 - 3x^2 + x^2 + 5x \\text{ linear or nonlinear?}"
        solution = "\\text{Linear}"
        steps = [
            "\\text{Simplify: } 2x^2 - 3x^2 + x^2 = 0x^2 = 0",
            "y = 5x",
            "\\text{Linear}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = LinearAndNonlinearFunctionsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
