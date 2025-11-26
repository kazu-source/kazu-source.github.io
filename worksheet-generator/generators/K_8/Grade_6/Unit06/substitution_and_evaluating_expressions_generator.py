"""
Substitution and Evaluating Expressions Generator - Grade 6 Unit 6
Generates problems evaluating expressions with substitution
Example: Evaluate 3x + 5 when x = 4
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SubstitutionAndEvaluatingExpressionsGenerator:
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problems.append(self._generate_problem(difficulty))
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
        coef, const, x_val = random.randint(2, 9), random.randint(1, 10), random.randint(1, 5)
        result = coef * x_val + const
        latex = f"\\text{{Evaluate }} {coef}x + {const} \\text{{ when }} x = {x_val}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{coef}({x_val}) + {const} = {coef*x_val} + {const} = {result}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        coef, const, x_val = random.randint(3, 12), random.randint(5, 20), random.randint(2, 8)
        result = coef * x_val - const
        latex = f"\\text{{Evaluate }} {coef}x - {const} \\text{{ when }} x = {x_val}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{coef}({x_val}) - {const} = {coef*x_val} - {const} = {result}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        coef, exp_val, x_val = random.randint(2, 5), 2, random.randint(2, 5)
        power = x_val ** exp_val
        result = coef * power
        latex = f"\\text{{Evaluate }} {coef}x^{{2}} \\text{{ when }} x = {x_val}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{coef}({x_val})^2 = {coef}({power}) = {result}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        coef1, coef2, const = random.randint(2, 6), random.randint(2, 6), random.randint(3, 10)
        x_val, y_val = random.randint(2, 5), random.randint(2, 5)
        result = coef1 * x_val + coef2 * y_val + const
        latex = f"\\text{{Evaluate }} {coef1}x + {coef2}y + {const} \\text{{ when }} x = {x_val}, y = {y_val}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{coef1}({x_val}) + {coef2}({y_val}) + {const} = {coef1*x_val} + {coef2*y_val} + {const} = {result}"], difficulty='challenge')


def main():
    generator = SubstitutionAndEvaluatingExpressionsGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
