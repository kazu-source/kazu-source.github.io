"""
Discontinuities in Rational Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DiscontinuitiesRationalFunctionsGenerator:
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
        # Vertical asymptote
        a = random.randint(1, 9)

        latex = f"\\text{{Find vertical asymptote: }} f(x) = \\frac{{1}}{{x - {a}}}"
        solution = f"x = {a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Multiple vertical asymptotes
        a = random.randint(1, 5)
        b = random.randint(6, 9)

        latex = f"\\text{{Find vertical asymptotes: }} f(x) = \\frac{{1}}{{(x - {a})(x - {b})}}"
        solution = f"x = {a}, x = {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Hole vs asymptote
        a = random.randint(1, 5)
        b = random.randint(6, 9)

        latex = f"\\text{{Find holes and asymptotes: }} f(x) = \\frac{{(x - {a})(x - {b})}}{{x - {a}}}"
        solution = f"Hole at x = {a}, no vertical asymptote"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complete discontinuity analysis
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Analyze: }} f(x) = \\frac{{x^2 - {a**2}}}{{x - {a}}}"
        solution = f"Hole at x = {a} (removable discontinuity)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = DiscontinuitiesRationalFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
