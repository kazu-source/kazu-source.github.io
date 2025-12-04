"""
Putting It All Together - Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PuttingItAllTogetherPolynomialsGenerator:
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
        # Complete analysis of simple polynomial
        a = random.randint(1, 5)
        b = random.randint(6, 9)

        latex = f"\\text{{Find zeros and end behavior of }} f(x) = (x - {a})(x - {b})"
        solution = f"Zeros: {a}, {b}; End behavior: up on both sides"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Sketch polynomial given properties
        a = random.randint(1, 5)
        b = random.randint(6, 9)

        latex = f"\\text{{Analyze }} f(x) = -(x - {a})(x - {b}): \\text{{ zeros, end behavior, sign}}"
        solution = f"Zeros: {a}, {b}; Negative on ends; Positive between zeros"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Complete cubic analysis
        a = random.randint(1, 3)
        b = random.randint(4, 6)
        c = random.randint(7, 9)

        latex = f"\\text{{Analyze }} f(x) = (x - {a})(x - {b})(x - {c}): \\text{{ zeros, intervals, end behavior}}"
        solution = f"Zeros: {a}, {b}, {c}; Negative: x<{a}, {b}<x<{c}; Positive: {a}<x<{b}, x>{c}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Write polynomial given properties
        a = random.randint(1, 5)
        b = random.randint(6, 9)

        latex = f"\\text{{Write a polynomial with zeros at }} x = {a}, {b} \\text{{ and end behavior down on both sides}}"
        solution = f"f(x) = -(x - {a})(x - {b}) \\text{{ or any negative leading coefficient}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = PuttingItAllTogetherPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
