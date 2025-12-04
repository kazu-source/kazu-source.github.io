"""
Factoring Monomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FactoringMonomialsGenerator:
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
        # Factor out a simple monomial
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)

        latex = f"\\text{{Factor: }} {a*b}x + {a*c}"
        solution = f"{a}({b}x + {c})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Factor out x from polynomial
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)

        latex = f"\\text{{Factor: }} {a}x^2 + {b}x"
        solution = f"x({a}x + {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Factor out complex monomial
        gcf = random.randint(2, 5)
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        coef1 = gcf * a
        coef2 = gcf * b
        coef3 = gcf * c

        latex = f"\\text{{Factor: }} {coef1}x^3 + {coef2}x^2 + {coef3}x"
        solution = f"{gcf}x({a}x^2 + {b}x + {c})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Factor out monomial with multiple variables
        gcf = random.randint(2, 5)
        a = random.randint(2, 5)
        b = random.randint(1, 5)

        coef1 = gcf * a
        coef2 = gcf * b

        latex = f"\\text{{Factor: }} {coef1}x^2y^2 + {coef2}xy"
        solution = f"{gcf}xy({a}xy + {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = FactoringMonomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
