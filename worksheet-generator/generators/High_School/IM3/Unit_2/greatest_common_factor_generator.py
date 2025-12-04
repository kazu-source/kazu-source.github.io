"""
Greatest Common Factor Generator
"""
import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GreatestCommonFactorGenerator:
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
        # Find GCF of two terms
        gcf = random.randint(2, 9)
        a = random.randint(2, 9)
        b = random.randint(2, 9)

        term1 = gcf * a
        term2 = gcf * b

        latex = f"\\text{{Find the GCF of }} {term1} \\text{{ and }} {term2}"
        solution = f"{gcf}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Find GCF and factor
        gcf = random.randint(2, 6)
        a = random.randint(2, 5)
        b = random.randint(1, 5)

        term1 = gcf * a
        term2 = gcf * b

        latex = f"\\text{{Factor using GCF: }} {term1}x^2 + {term2}x"
        solution = f"{gcf}x({a}x + {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Find GCF of three terms
        gcf = random.randint(2, 5)
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        term1 = gcf * a
        term2 = gcf * b
        term3 = gcf * c

        latex = f"\\text{{Factor using GCF: }} {term1}x^3 + {term2}x^2 + {term3}x"
        solution = f"{gcf}x({a}x^2 + {b}x + {c})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # GCF with coefficients and variables
        gcf = random.randint(2, 5)
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        term1 = gcf * a
        term2 = gcf * b
        term3 = gcf * c

        latex = f"\\text{{Factor using GCF: }} {term1}x^2y^3 + {term2}xy^2 + {term3}xy"
        solution = f"{gcf}xy({a}xy^2 + {b}y + {c})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = GreatestCommonFactorGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
