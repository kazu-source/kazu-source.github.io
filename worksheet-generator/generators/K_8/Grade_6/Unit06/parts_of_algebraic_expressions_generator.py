"""
Parts of Algebraic Expressions Generator - Grade 6 Unit 6
Generates problems identifying terms, coefficients, and constants
Example: In 3x + 5, what is the coefficient?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PartsOfAlgebraicExpressionsGenerator:
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
        coef = random.randint(2, 9)
        const = random.randint(1, 10)
        latex = f"\\text{{In }} {coef}x + {const}, \\text{{ what is the coefficient of }} x\\text{{?}}"
        solution = str(coef)
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Coefficient: }} {coef}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        coef = random.randint(2, 9)
        const = random.randint(1, 10)
        latex = f"\\text{{In }} {coef}x + {const}, \\text{{ what is the constant term?}}"
        solution = str(const)
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Constant: }} {const}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        coef1, coef2 = random.randint(2, 9), random.randint(2, 9)
        const = random.randint(1, 10)
        latex = f"\\text{{How many terms in }} {coef1}x + {coef2}y + {const}\\text{{?}}"
        solution = "3"
        return Equation(latex=latex, solution=solution, steps=["Three terms: " + f"{coef1}x, {coef2}y, {const}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        coef1, coef2, coef3 = random.randint(2, 7), random.randint(2, 7), random.randint(2, 7)
        const = random.randint(1, 10)
        latex = f"\\text{{List all coefficients in }} {coef1}x^2 + {coef2}x + {coef3}y + {const}"
        solution = f"{coef1}, {coef2}, {coef3}"
        return Equation(latex=latex, solution=solution, steps=[f"\\text{{Coefficients: }} {solution}"], difficulty='challenge')


def main():
    generator = PartsOfAlgebraicExpressionsGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
