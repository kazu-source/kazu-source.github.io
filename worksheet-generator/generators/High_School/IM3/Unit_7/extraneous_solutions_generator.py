"""
Extraneous Solutions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ExtraneousSolutionsGenerator:
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
        # Check if solution is extraneous
        a = random.randint(1, 5)

        latex = f"\\text{{Check if }} x = {a} \\text{{ solves }} \\sqrt{{x}} = -{a}"
        solution = "Extraneous (square root cannot equal negative)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Solve and check for extraneous
        a = random.randint(2, 5)

        latex = f"\\text{{Solve and check: }} \\sqrt{{x + {a}}} = x - {a}"
        solution = f"x = {a+1} \\text{{ (check: both sides positive)}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Rational equation with restriction
        a = random.randint(2, 5)

        latex = f"\\text{{Solve: }} \\frac{{1}}{{x - {a}}} = \\frac{{1}}{{x - {a}}}"
        solution = f"\\text{{All real numbers except }} x = {a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex equation with potential extraneous solution
        a = random.randint(1, 5)

        latex = f"\\text{{Solve and identify extraneous solutions: }} \\sqrt{{2x + {a}}} = x - {a}"
        solution = "Solve algebraically, check both solutions in original equation"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ExtraneousSolutionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
