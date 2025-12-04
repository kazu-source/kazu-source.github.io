"""
Rational Equations Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class RationalEquationsGenerator:
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
        # Simple rational equation
        a = random.randint(2, 9)
        b = random.randint(1, 9)

        latex = f"\\frac{{{a}}}{{x}} = {b}"
        solution = f"x = \\frac{{{a}}}{{{b}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Rational equation with addition
        a = random.randint(2, 9)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        latex = f"\\frac{{{a}}}{{x}} + {b} = {c}"
        solution = f"x = \\frac{{{a}}}{{{c - b}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Two rational terms
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        c = random.randint(1, 5)

        latex = f"\\frac{{{a}}}{{x}} + \\frac{{{b}}}{{x}} = {c}"
        solution = f"x = \\frac{{{a + b}}}{{{c}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Different denominators
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        c = random.randint(1, 5)
        d = random.randint(1, 5)

        latex = f"\\frac{{{a}}}{{x}} = \\frac{{{b}}}{{x + {c}}}"
        solution = f"x = \\frac{{{a*c}}}{{{b - a}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = RationalEquationsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
