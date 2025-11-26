"""
Evaluating Expressions with Multiple Variables Generator - Grade 6 Unit 6
Example: Evaluate 2x + 3y when x = 4, y = 5
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EvaluatingExpressionsWithMultipleVariablesGenerator:
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()

    def _generate_easy(self) -> Equation:
        a, b, x, y = random.randint(2, 6), random.randint(2, 6), random.randint(1, 5), random.randint(1, 5)
        result = a * x + b * y
        latex = f"\\text{{Evaluate }} {a}x + {b}y \\text{{ when }} x = {x}, y = {y}"
        return Equation(latex=latex, solution=str(result), steps=[f"{a}({x}) + {b}({y}) = {result}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a, b, c, x, y = random.randint(2, 5), random.randint(2, 5), random.randint(1, 10), random.randint(2, 6), random.randint(2, 6)
        result = a * x + b * y - c
        latex = f"\\text{{Evaluate }} {a}x + {b}y - {c} \\text{{ when }} x = {x}, y = {y}"
        return Equation(latex=latex, solution=str(result), steps=[f"{a}({x}) + {b}({y}) - {c} = {result}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a, b, x, y = random.randint(2, 4), random.randint(2, 4), random.randint(2, 4), random.randint(2, 4)
        result = a * (x ** 2) + b * y
        latex = f"\\text{{Evaluate }} {a}x^2 + {b}y \\text{{ when }} x = {x}, y = {y}"
        return Equation(latex=latex, solution=str(result), steps=[f"{a}({x})^2 + {b}({y}) = {a}({x**2}) + {b*y} = {result}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a, b, c, x, y, z = random.randint(2, 4), random.randint(2, 4), random.randint(2, 4), random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)
        result = a * x + b * y + c * z
        latex = f"\\text{{Evaluate }} {a}x + {b}y + {c}z \\text{{ when }} x = {x}, y = {y}, z = {z}"
        return Equation(latex=latex, solution=str(result), steps=[f"{a}({x}) + {b}({y}) + {c}({z}) = {result}"], difficulty='challenge')


def main():
    generator = EvaluatingExpressionsWithMultipleVariablesGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
