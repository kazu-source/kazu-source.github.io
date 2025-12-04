"""
Graphs of Rational Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphsRationalFunctionsGenerator:
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
        # Basic hyperbola
        a = random.randint(1, 9)

        latex = f"\\text{{Sketch }} f(x) = \\frac{{{a}}}{{x}}"
        solution = f"Vertical asymptote: x = 0, Horizontal asymptote: y = 0"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Shifted hyperbola
        h = random.randint(1, 5)
        k = random.randint(1, 5)

        latex = f"\\text{{Sketch }} f(x) = \\frac{{1}}{{x - {h}}} + {k}"
        solution = f"VA: x = {h}, HA: y = {k}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # More complex rational function
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Graph }} f(x) = \\frac{{x + {a}}}{{x - {b}}}"
        solution = f"VA: x = {b}, HA: y = 1, x-intercept: x = -{a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complete graph analysis
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Completely analyze and sketch }} f(x) = \\frac{{x^2}}{{x^2 - {a**2}}}"
        solution = f"VA: x = \\pm{a}, HA: y = 1, Even function"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = GraphsRationalFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
