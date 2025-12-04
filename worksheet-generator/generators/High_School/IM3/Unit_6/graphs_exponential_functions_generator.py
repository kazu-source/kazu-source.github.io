"""
Graphs of Exponential Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphsExponentialFunctionsGenerator:
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
        # Basic exponential shift
        b = random.choice([2, 3])
        k = random.randint(1, 5)

        latex = f"\\text{{Describe: }} f(x) = {b}^x + {k}"
        solution = f"Exponential base {b} shifted up {k}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Horizontal shift
        b = random.choice([2, 3])
        h = random.randint(1, 5)

        latex = f"\\text{{Describe: }} f(x) = {b}^{{x - {h}}}"
        solution = f"Exponential base {b} shifted right {h}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Reflection and shift
        b = random.choice([2, 3])
        k = random.randint(1, 5)

        latex = f"\\text{{Describe: }} f(x) = -{b}^x + {k}"
        solution = f"Reflected over x-axis, shifted up {k}, asymptote at y = {k}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Multiple transformations
        a = random.randint(2, 4)
        b = random.choice([2, 3])
        h = random.randint(1, 5)
        k = random.randint(1, 5)

        latex = f"\\text{{Describe: }} f(x) = {a} \\cdot {b}^{{x - {h}}} + {k}"
        solution = f"Stretch by {a}, right {h}, up {k}, asymptote at y = {k}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = GraphsExponentialFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
