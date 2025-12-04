"""
Interpreting Features of Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class InterpretingFeaturesFunctionsGenerator:
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
        # Identify domain
        a = random.randint(1, 5)

        latex = f"\\text{{Find domain of }} f(x) = \\sqrt{{x - {a}}}"
        solution = f"x \\geq {a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Identify range
        a = random.randint(1, 5)
        k = random.randint(1, 5)

        latex = f"\\text{{Find range of }} f(x) = {a}x^2 + {k}"
        solution = f"y \\geq {k}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Identify intercepts
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Find x and y intercepts of }} f(x) = {a}x + {b}"
        solution = f"x-intercept: (-\\frac{{{b}}}{{{a}}}, 0), y-intercept: (0, {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Identify increasing/decreasing intervals
        a = random.randint(1, 5)

        latex = f"\\text{{Where is }} f(x) = -x^2 + {a} \\text{{ increasing?}}"
        solution = f"x < 0"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = InterpretingFeaturesFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
