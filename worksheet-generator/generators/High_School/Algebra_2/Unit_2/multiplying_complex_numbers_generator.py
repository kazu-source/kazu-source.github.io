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
        a = random.randint(2, 8)
        b = random.randint(1, 6)

        latex = f"{a}i \\cdot {b}i"
        result = -a * b  # i * i = -1
        solution = f"{result}"
        steps = [
            f"{a}i \\cdot {b}i = {a} \\cdot {b} \\cdot i \\cdot i",
            f"= {a*b} \\cdot i^2",
            f"= {a*b} \\cdot (-1)",
            f"= {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a, b = random.randint(1, 6), random.randint(1, 8)
        c, d = random.randint(1, 6), random.randint(1, 8)

        latex = f"({a} + {b}i)({c} + {d}i)"
        # (a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i
        real = a * c - b * d
        imag = a * d + b * c
        solution = f"{real} + {imag}i" if imag >= 0 else f"{real} - {abs(imag)}i"

        steps = [
            f"Use FOIL method",
            f"First: {a} \\cdot {c} = {a*c}",
            f"Outer: {a} \\cdot {d}i = {a*d}i",
            f"Inner: {b}i \\cdot {c} = {b*c}i",
            f"Last: {b}i \\cdot {d}i = {b*d}i^2 = {-b*d}",
            f"Combine: ({a*c} - {b*d}) + ({a*d} + {b*c})i = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a, b = random.randint(-6, 6), random.randint(-6, 6)
        c, d = random.randint(-6, 6), random.randint(-6, 6)

        sign1 = '+' if b >= 0 else '-'
        sign2 = '+' if d >= 0 else '-'

        latex = f"({a} {sign1} {abs(b)}i)({c} {sign2} {abs(d)}i)"
        real = a * c - b * d
        imag = a * d + b * c
        solution = f"{real} + {imag}i" if imag >= 0 else f"{real} - {abs(imag)}i"

        steps = [
            f"({a})({c}) = {a*c}",
            f"({a})({d}i) = {a*d}i",
            f"({b}i)({c}) = {b*c}i",
            f"({b}i)({d}i) = {b*d}i^2 = {-b*d}",
            f"Real part: {a*c} + ({-b*d}) = {real}",
            f"Imaginary part: {a*d} + {b*c} = {imag}",
            f"Result: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        problem_type = random.choice(['conjugate_multiply', 'triple_product'])

        if problem_type == 'conjugate_multiply':
            # (a + bi)(a - bi) = a^2 + b^2
            a = random.randint(2, 8)
            b = random.randint(2, 8)

            latex = f"({a} + {b}i)({a} - {b}i)"
            result = a * a + b * b
            solution = f"{result}"
            steps = [
                f"This is a conjugate pair: (a + bi)(a - bi) = a^2 + b^2",
                f"a = {a}, b = {b}",
                f"a^2 = {a*a}",
                f"b^2 = {b*b}",
                f"Result: {a*a} + {b*b} = {result}"
            ]
        else:
            # (a + bi)^2
            a = random.randint(1, 5)
            b = random.randint(1, 5)

            latex = f"({a} + {b}i)^2"
            real = a*a - b*b
            imag = 2*a*b
            solution = f"{real} + {imag}i"

            steps = [
                f"({a} + {b}i)^2 = ({a} + {b}i)({a} + {b}i)",
                f"= {a}^2 + 2({a})({b}i) + ({b}i)^2",
                f"= {a*a} + {2*a*b}i + {b*b}i^2",
                f"= {a*a} + {2*a*b}i - {b*b}",
                f"= ({a*a} - {b*b}) + {2*a*b}i",
                f"Result: {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = MultiplyingComplexNumbersGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
