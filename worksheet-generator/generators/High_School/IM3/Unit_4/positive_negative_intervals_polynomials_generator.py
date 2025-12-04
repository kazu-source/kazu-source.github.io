"""
Positive and Negative Intervals of Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PositiveNegativeIntervalsPolynomialsGenerator:
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
        # Simple quadratic opening upward
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        if a < b:
            latex = f"\\text{{Where is }} f(x) = (x - {a})(x - {b}) \\text{{ positive?}}"
            solution = f"x < {a} \\text{{ or }} x > {b}"
        else:
            latex = f"\\text{{Where is }} f(x) = (x - {b})(x - {a}) \\text{{ positive?}}"
            solution = f"x < {b} \\text{{ or }} x > {a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Where is polynomial negative
        a = random.randint(1, 5)
        b = random.randint(6, 9)

        latex = f"\\text{{Where is }} f(x) = (x - {a})(x - {b}) \\text{{ negative?}}"
        solution = f"{a} < x < {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Cubic function intervals
        a = random.randint(1, 3)
        b = random.randint(4, 6)
        c = random.randint(7, 9)

        latex = f"\\text{{Where is }} f(x) = (x - {a})(x - {b})(x - {c}) \\text{{ positive?}}"
        solution = f"{a} < x < {b} \\text{{ or }} x > {c}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # With multiplicity
        a = random.randint(1, 4)
        b = random.randint(5, 9)

        latex = f"\\text{{Where is }} f(x) = (x - {a})^2(x - {b}) \\text{{ negative?}}"
        solution = f"x < {b}, x \\neq {a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = PositiveNegativeIntervalsPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
