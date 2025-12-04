"""
Adding and Subtracting Complex Numbers Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class AddingSubtractingComplexNumbersGenerator:
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
        a, b = random.randint(1, 8), random.randint(1, 8)
        c, d = random.randint(1, 8), random.randint(1, 8)
        real_sum = a + c
        imag_sum = b + d
        latex = f"({a} + {b}i) + ({c} + {d}i)"
        solution = f"{real_sum} + {imag_sum}i"
        steps = [
            f"Add real parts: {a} + {c} = {real_sum}",
            f"Add imaginary parts: {b} + {d} = {imag_sum}",
            f"Result: {real_sum} + {imag_sum}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a, b = random.randint(-6, 6), random.randint(-6, 6)
        c, d = random.randint(-6, 6), random.randint(-6, 6)
        real_diff = a - c
        imag_diff = b - d
        latex = f"({a} {'+' if b >= 0 else ''} {b}i) - ({c} {'+' if d >= 0 else ''} {d}i)"
        solution = f"{real_diff} {'+' if imag_diff >= 0 else ''} {imag_diff}i"
        steps = [
            f"Subtract real parts: {a} - ({c}) = {real_diff}",
            f"Subtract imaginary parts: {b} - ({d}) = {imag_diff}",
            f"Result: {real_diff} {'+' if imag_diff >= 0 else ''} {imag_diff}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a, b = random.randint(-8, 8), random.randint(-8, 8)
        c, d = random.randint(-8, 8), random.randint(-8, 8)
        e, f = random.randint(-8, 8), random.randint(-8, 8)
        real_total = a + c - e
        imag_total = b + d - f
        latex = f"({a} {'+' if b >= 0 else ''} {b}i) + ({c} {'+' if d >= 0 else ''} {d}i) - ({e} {'+' if f >= 0 else ''} {f}i)"
        solution = f"{real_total} {'+' if imag_total >= 0 else ''} {imag_total}i"
        steps = [
            f"Real parts: {a} + {c} - {e} = {real_total}",
            f"Imaginary parts: {b} + {d} - {f} = {imag_total}",
            f"Result: {real_total} {'+' if imag_total >= 0 else ''} {imag_total}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a, b = random.randint(-5, 5), random.randint(-5, 5)
        c, d = random.randint(-5, 5), random.randint(-5, 5)
        k = random.randint(2, 4)
        real_result = a + k * c
        imag_result = b + k * d
        latex = f"({a} {'+' if b >= 0 else ''} {b}i) + {k}({c} {'+' if d >= 0 else ''} {d}i)"
        solution = f"{real_result} {'+' if imag_result >= 0 else ''} {imag_result}i"
        steps = [
            f"Distribute {k}: {k}({c} {'+' if d >= 0 else ''} {d}i) = {k*c} {'+' if k*d >= 0 else ''} {k*d}i",
            f"Real parts: {a} + {k*c} = {real_result}",
            f"Imaginary parts: {b} + {k*d} = {imag_result}",
            f"Result: {real_result} {'+' if imag_result >= 0 else ''} {imag_result}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = AddingSubtractingComplexNumbersGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
