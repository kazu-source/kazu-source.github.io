"""
Shifting Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ShiftingFunctionsGenerator:
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
        # Vertical shift
        k = random.randint(1, 9)

        latex = f"\\text{{Describe the transformation: }} f(x) = x^2 + {k}"
        solution = f"Vertical shift up {k} units"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Horizontal shift
        h = random.randint(1, 9)

        latex = f"\\text{{Describe the transformation: }} f(x) = (x - {h})^2"
        solution = f"Horizontal shift right {h} units"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Both shifts
        h = random.randint(1, 5)
        k = random.randint(1, 5)

        latex = f"\\text{{Describe the transformation: }} f(x) = (x - {h})^2 + {k}"
        solution = f"Shift right {h}, shift up {k}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Write transformed function
        h = random.randint(1, 5)
        k = random.randint(1, 5)

        latex = f"\\text{{Write }} f(x) = x^3 \\text{{ shifted left {h} and down {k}}}"
        solution = f"f(x) = (x + {h})^3 - {k}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ShiftingFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
