"""
Polynomial Remainder Theorem Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PolynomialRemainderTheoremGenerator:
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
        a = random.randint(1, 5)
        k = random.randint(2, 8)
        latex = f"\\text{{Find remainder when }} x^2 + {k} \\text{{ is divided by }} x - {a}"
        remainder = a*a + k
        solution = f"{remainder}"
        steps = [f"Use remainder theorem: P({a})", f"P({a}) = {a}^2 + {k} = {remainder}", f"Remainder: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(1, 4)
        b = random.randint(2, 6)
        c = random.randint(2, 8)
        latex = f"\\text{{Find remainder: }} (x^2 + {b}x + {c}) \\div (x - {a})"
        remainder = a*a + b*a + c
        solution = f"{remainder}"
        steps = [f"P(x) = x^2 + {b}x + {c}", f"P({a}) = {a}^2 + {b}({a}) + {c}", f"= {remainder}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(1, 3)
        b = random.randint(1, 4)
        c = random.randint(1, 5)
        d = random.randint(1, 6)
        latex = f"\\text{{Remainder: }} (x^3 + {b}x^2 + {c}x + {d}) \\div (x - {a})"
        remainder = a**3 + b*a*a + c*a + d
        solution = f"{remainder}"
        steps = [f"P({a}) = {a}^3 + {b}({a})^2 + {c}({a}) + {d}", f"= {remainder}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(1, 4)
        c = random.randint(1, 5)
        d = random.randint(1, 6)
        latex = f"\\text{{For what k does }} (x^3 + {b}x^2 + kx + {d}) \\text{{ have remainder {c} when divided by }} (x - {a})?"
        k_val = (c - a**3 - b*a*a - d) // a
        solution = f"k = {k_val}"
        steps = [f"P({a}) = {c}", f"{a}^3 + {b}({a})^2 + k({a}) + {d} = {c}", f"Solve for k: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PolynomialRemainderTheoremGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
