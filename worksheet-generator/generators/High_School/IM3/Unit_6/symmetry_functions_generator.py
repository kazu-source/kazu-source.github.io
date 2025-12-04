"""
Symmetry of Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SymmetryFunctionsGenerator:
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
        # Even function
        a = random.randint(1, 5)

        latex = f"\\text{{Is }} f(x) = {a}x^2 \\text{{ even, odd, or neither?}}"
        solution = "Even (symmetric about y-axis)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Odd function
        a = random.randint(1, 5)

        latex = f"\\text{{Is }} f(x) = {a}x^3 \\text{{ even, odd, or neither?}}"
        solution = "Odd (symmetric about origin)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Neither even nor odd
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Is }} f(x) = x^2 + {b}x \\text{{ even, odd, or neither?}}"
        solution = "Neither"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Test for even/odd algebraically
        a = random.randint(1, 5)

        latex = f"\\text{{Verify that }} f(x) = {a}x^4 + x^2 \\text{{ is even}}"
        solution = f"f(-x) = {a}(-x)^4 + (-x)^2 = {a}x^4 + x^2 = f(x)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = SymmetryFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
