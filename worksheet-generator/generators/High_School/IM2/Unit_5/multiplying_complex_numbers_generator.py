"""
Multiplying Complex Numbers Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MultiplyingComplexNumbersGenerator:
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
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        latex = f"{a}i \\cdot {b}i"
        product = -a * b
        solution = f"{product}"
        steps = [
            f"{a}i · {b}i = {a * b}i²",
            f"= {a * b}(-1)",
            f"= {product}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a, b = random.randint(1, 5), random.randint(1, 5)
        c, d = random.randint(1, 5), random.randint(1, 5)
        real = a * c - b * d
        imag = a * d + b * c
        latex = f"({a} + {b}i)({c} + {d}i)"
        solution = f"{real} {'+' if imag >= 0 else ''} {imag}i"
        steps = [
            "Use FOIL method:",
            f"First: {a} · {c} = {a*c}",
            f"Outer: {a} · {d}i = {a*d}i",
            f"Inner: {b}i · {c} = {b*c}i",
            f"Last: {b}i · {d}i = {b*d}i² = -{b*d}",
            f"Combine: {a*c} + {a*d}i + {b*c}i - {b*d}",
            f"= {real} {'+' if imag >= 0 else ''} {imag}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a, b = random.randint(-5, 5), random.randint(-5, 5)
        c, d = random.randint(-5, 5), random.randint(-5, 5)
        real = a * c - b * d
        imag = a * d + b * c
        latex = f"({a} {'+' if b >= 0 else ''} {b}i)({c} {'+' if d >= 0 else ''} {d}i)"
        solution = f"{real} {'+' if imag >= 0 else ''} {imag}i"
        steps = [
            f"Real part: {a}·{c} - {b}·{d} = {a*c} - {b*d} = {real}",
            f"Imaginary part: {a}·{d} + {b}·{c} = {a*d} + {b*c} = {imag}",
            f"Result: {real} {'+' if imag >= 0 else ''} {imag}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a, b = random.randint(1, 4), random.randint(1, 4)
        real = a**2 - b**2
        imag = 2 * a * b
        latex = f"({a} + {b}i)^2"
        solution = f"{real} {'+' if imag >= 0 else ''} {imag}i"
        steps = [
            f"({a} + {b}i)² = ({a} + {b}i)({a} + {b}i)",
            f"= {a}² + 2·{a}·{b}i + ({b}i)²",
            f"= {a**2} + {2*a*b}i + {b**2}i²",
            f"= {a**2} + {2*a*b}i - {b**2}",
            f"= {real} {'+' if imag >= 0 else ''} {imag}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = MultiplyingComplexNumbersGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
