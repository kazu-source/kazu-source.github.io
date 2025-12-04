"""
End Behavior of Rational Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EndBehaviorRationalFunctionsGenerator:
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
        # Same degree
        a = random.randint(2, 9)
        b = random.randint(1, 9)

        latex = f"\\text{{Find horizontal asymptote: }} f(x) = \\frac{{{a}x}}{{{b}x + 1}}"
        solution = f"y = \\frac{{{a}}}{{{b}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Numerator degree less
        a = random.randint(1, 9)
        b = random.randint(1, 5)

        latex = f"\\text{{Find horizontal asymptote: }} f(x) = \\frac{{{a}}}{{x^2 + {b}}}"
        solution = "y = 0"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Numerator degree greater
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Describe end behavior: }} f(x) = \\frac{{{a}x^2}}{{{b}x + 1}}"
        solution = "No horizontal asymptote (oblique asymptote)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Find slant asymptote
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Find slant asymptote: }} f(x) = \\frac{{x^2 + {a}x}}{{x + {b}}}"
        solution = f"\\text{{Divide: }} y = x + {a-b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = EndBehaviorRationalFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
