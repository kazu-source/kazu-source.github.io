"""
Complex Numbers Introduction Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ComplexNumbersIntroGenerator:
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
        a = random.randint(1, 8)
        b = random.randint(1, 8)
        latex = f"\\text{{Write in standard form a + bi: }} {a} + {b}i"
        solution = f"{a} + {b}i"
        steps = [
            f"Already in standard form a + bi",
            f"Real part: {a}",
            f"Imaginary part: {b}",
            f"Answer: {a} + {b}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(-6, 6)
        b = random.randint(-6, 6)
        sign = '+' if b >= 0 else ''
        latex = f"\\text{{Identify real and imaginary parts: }} {a} {sign} {b}i"
        solution = f"Real: {a}, Imaginary: {b}"
        steps = [
            f"Standard form: a + bi",
            f"Real part (a): {a}",
            f"Imaginary part (b): {b}",
            f"Answer: Real = {a}, Imaginary = {b}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(1, 5)
        n = random.randint(1, 12)
        latex = f"\\text{{Write in standard form: }} {a} + \\sqrt{{-{n}}}"
        import math
        solution = f"{a} + i\\sqrt{{{n}}}"
        steps = [
            f"{a} + √(-{n})",
            f"= {a} + √{n} · √(-1)",
            f"= {a} + i√{n}",
            solution
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(-5, 5)
        b = random.randint(1, 8)
        c = random.randint(1, 8)
        latex = f"\\text{{Write in standard form: }} {a} + {b}i + {c}i"
        total_imag = b + c
        solution = f"{a} + {total_imag}i"
        steps = [
            f"{a} + {b}i + {c}i",
            f"Combine like terms: {a} + ({b} + {c})i",
            f"= {a} + {total_imag}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ComplexNumbersIntroGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
