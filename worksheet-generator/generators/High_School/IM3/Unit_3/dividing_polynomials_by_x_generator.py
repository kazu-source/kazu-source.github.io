"""
Dividing Polynomials by x Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DividingPolynomialsByXGenerator:
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
        # Simple division by x
        a = random.randint(2, 9)
        b = random.randint(1, 9)

        latex = f"\\frac{{{a}x^2 + {b}x}}{{x}}"
        solution = f"{a}x + {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Division by x with remainder
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)

        latex = f"\\frac{{{a}x^2 + {b}x + {c}}}{{x}}"
        solution = f"{a}x + {b} + \\frac{{{c}}}{{x}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Cubic divided by x
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)

        latex = f"\\frac{{{a}x^3 + {b}x^2 + {c}x + {d}}}{{x}}"
        solution = f"{a}x^2 + {b}x + {c} + \\frac{{{d}}}{{x}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Division by ax
        a = random.randint(2, 5)
        b = random.randint(2, 9)
        c = random.randint(1, 9)
        d = random.randint(1, 9)

        coef1 = a * b
        coef2 = a * c

        latex = f"\\frac{{{coef1}x^3 + {coef2}x^2 + {d}x}}{{{a}x}}"
        solution = f"{b}x^2 + {c}x + \\frac{{{d}}}{{{a}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = DividingPolynomialsByXGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
