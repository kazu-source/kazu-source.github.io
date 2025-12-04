"""
Solving Quadratics by Factoring Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingQuadraticsFactoringGenerator:
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
        p = random.randint(1, 6)
        q = random.randint(1, 6)
        b = p + q
        c = p * q
        latex = f"\\text{{Solve: }} x^2 + {b}x + {c} = 0"
        solution = f"x = -{p}, x = -{q}"
        steps = [
            f"Factor: x² + {b}x + {c} = 0",
            f"(x + {p})(x + {q}) = 0",
            f"x + {p} = 0 or x + {q} = 0",
            f"x = -{p} or x = -{q}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        p = random.randint(1, 5)
        q = random.randint(1, 5)
        sign_choice = random.choice(['both_neg', 'mixed'])
        if sign_choice == 'both_neg':
            b = -(p + q)
            c = p * q
            latex = f"\\text{{Solve: }} x^2 - {p+q}x + {c} = 0"
            solution = f"x = {p}, x = {q}"
            steps = [
                f"Factor: (x - {p})(x - {q}) = 0",
                f"x = {p} or x = {q}"
            ]
        else:
            b = p - q
            c = -p * q
            latex = f"\\text{{Solve: }} x^2 + {b}x - {p*q} = 0"
            solution = f"x = -{p}, x = {q}"
            steps = [
                f"Factor: (x + {p})(x - {q}) = 0",
                f"x = -{p} or x = {q}"
            ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        p = random.randint(1, 4)
        q = random.randint(1, 4)
        b = a * q + p
        c = p * q
        latex = f"\\text{{Solve: }} {a}x^2 + {b}x + {c} = 0"
        solution = f"x = -{p}/{a}, x = -{q}"
        steps = [
            f"{a}x² + {b}x + {c} = 0",
            f"Factor: ({a}x + {p})(x + {q}) = 0",
            f"{a}x + {p} = 0 or x + {q} = 0",
            f"x = -{p}/{a} or x = -{q}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)
        r1 = random.randint(-3, 3)
        r2 = random.randint(-3, 3)
        while r1 == r2:
            r2 = random.randint(-3, 3)
        b = -a * (r1 + r2)
        c = a * r1 * r2
        latex = f"\\text{{Solve: }} {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c} = 0"
        solution = f"x = {r1}, x = {r2}"
        steps = [
            f"Factor out {a} if possible or use grouping",
            f"Solutions: x = {r1}, x = {r2}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingQuadraticsFactoringGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
