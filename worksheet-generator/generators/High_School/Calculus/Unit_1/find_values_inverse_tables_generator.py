"""
Find Values of Inverse Functions from Tables Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FindValuesInverseTablesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        x_val = random.randint(1, 5)
        y_val = random.randint(1, 8)

        latex = f"\\text{{Given }} f({x_val}) = {y_val}, \\text{{ find }} f^{{-1}}({y_val})."
        solution = f"{x_val}"
        steps = [
            f"\\text{{If }} f({x_val}) = {y_val},",
            f"\\text{{then }} f^{{-1}}({y_val}) = {x_val}",
            "\\text{The inverse reverses input and output}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x1, y1 = random.randint(1, 5), random.randint(1, 8)
        x2, y2 = random.randint(6, 10), random.randint(9, 15)

        latex = f"\\text{{From a table: }} f({x1}) = {y1}, f({x2}) = {y2}. \\text{{ Find }} f^{{-1}}({y1}) + f^{{-1}}({y2})."
        result = x1 + x2
        solution = f"{result}"
        steps = [
            f"f^{{-1}}({y1}) = {x1}",
            f"f^{{-1}}({y2}) = {x2}",
            f"f^{{-1}}({y1}) + f^{{-1}}({y2}) = {x1} + {x2} = {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(2, 6), random.randint(2, 8)
        x2, y2 = random.randint(7, 12), random.randint(9, 15)

        latex = f"\\text{{Given }} f({x1}) = {y1}, f({x2}) = {y2}. \\text{{ Find }} f^{{-1}}(f({x1}))."
        solution = f"{x1}"
        steps = [
            f"f({x1}) = {y1}",
            f"f^{{-1}}(f({x1})) = f^{{-1}}({y1})",
            f"f^{{-1}}({y1}) = {x1}",
            f"\\therefore f^{{-1}}(f({x1})) = {x1}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x1, y1 = random.randint(2, 5), random.randint(3, 7)
        x2, y2 = random.randint(6, 9), random.randint(8, 12)

        latex = f"\\text{{If }} f({x1}) = {y1}, f({x2}) = {y2}, \\text{{ find }} f(f^{{-1}}({y2}))."
        solution = f"{y2}"
        steps = [
            f"f^{{-1}}({y2}) = {x2}",
            f"f(f^{{-1}}({y2})) = f({x2})",
            f"f({x2}) = {y2}",
            f"\\therefore f(f^{{-1}}({y2})) = {y2}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FindValuesInverseTablesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
