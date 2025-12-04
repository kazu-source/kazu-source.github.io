"""
Multiplying and Dividing Rational Expressions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MultiplyingDividingRationalExpressionsGenerator:
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
        # Simple multiplication
        a = random.randint(2, 9)
        b = random.randint(2, 9)

        latex = f"\\frac{{{a}x}}{{y}} \\cdot \\frac{{y}}{{{b}x}}"
        solution = f"\\frac{{{a}}}{{{b}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Division
        a = random.randint(2, 9)
        b = random.randint(2, 9)

        latex = f"\\frac{{{a}x}}{{y}} \\div \\frac{{{b}x}}{{y}}"
        solution = f"\\frac{{{a}}}{{{b}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # With factoring
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\frac{{x + {a}}}{{x + {b}}} \\cdot \\frac{{x + {b}}}{{x + {a}}}"
        solution = f"1, x \\neq -{a}, -{b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex expression
        a = random.randint(1, 5)

        latex = f"\\frac{{x^2 - {a**2}}}{{x + {a}}} \\div \\frac{{x - {a}}}{{1}}"
        solution = f"1, x \\neq \\pm{a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = MultiplyingDividingRationalExpressionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
