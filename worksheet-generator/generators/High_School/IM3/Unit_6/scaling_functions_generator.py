"""
Scaling Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ScalingFunctionsGenerator:
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
        # Vertical stretch
        a = random.randint(2, 5)

        latex = f"\\text{{Describe: }} f(x) = {a}x^2"
        solution = f"Vertical stretch by factor of {a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Vertical compression
        a = random.randint(2, 5)

        latex = f"\\text{{Describe: }} f(x) = \\frac{{1}}{{{a}}}x^2"
        solution = f"Vertical compression by factor of {a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Horizontal stretch/compression
        a = random.randint(2, 5)

        latex = f"\\text{{Describe: }} f(x) = ({a}x)^2"
        solution = f"Horizontal compression by factor of {a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Combined scaling and other transformations
        a = random.randint(2, 4)
        h = random.randint(1, 5)
        k = random.randint(1, 5)

        latex = f"\\text{{Describe all transformations: }} f(x) = {a}(x - {h})^2 + {k}"
        solution = f"Stretch by {a}, shift right {h}, shift up {k}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ScalingFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
