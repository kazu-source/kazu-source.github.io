"""
Adding and Subtracting Complex Numbers Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class AddSubComplexNumbersGenerator:
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
        operation = random.choice(['add', 'subtract'])
        a1, b1 = random.randint(1, 10), random.randint(1, 10)
        a2, b2 = random.randint(1, 10), random.randint(1, 10)

        if operation == 'add':
            latex = f"({a1} + {b1}i) + ({a2} + {b2}i)"
            real = a1 + a2
            imag = b1 + b2
            solution = f"{real} + {imag}i"
            steps = [
                f"Add real parts: {a1} + {a2} = {real}",
                f"Add imaginary parts: {b1}i + {b2}i = {imag}i",
                f"Result: {solution}"
            ]
        else:
            latex = f"({a1} + {b1}i) - ({a2} + {b2}i)"
            real = a1 - a2
            imag = b1 - b2
            solution = f"{real} + {imag}i" if imag >= 0 else f"{real} - {abs(imag)}i"
            steps = [
                f"Subtract real parts: {a1} - {a2} = {real}",
                f"Subtract imaginary parts: {b1}i - {b2}i = {imag}i",
                f"Result: {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        operation = random.choice(['add', 'subtract', 'mixed'])
        a1, b1 = random.randint(-10, 10), random.randint(-10, 10)
        a2, b2 = random.randint(-10, 10), random.randint(-10, 10)

        sign1 = '+' if b1 >= 0 else '-'
        sign2 = '+' if b2 >= 0 else '-'

        if operation == 'add':
            latex = f"({a1} {sign1} {abs(b1)}i) + ({a2} {sign2} {abs(b2)}i)"
            real = a1 + a2
            imag = b1 + b2
        elif operation == 'subtract':
            latex = f"({a1} {sign1} {abs(b1)}i) - ({a2} {sign2} {abs(b2)}i)"
            real = a1 - a2
            imag = b1 - b2
        else:
            a3, b3 = random.randint(-8, 8), random.randint(-8, 8)
            sign3 = '+' if b3 >= 0 else '-'
            latex = f"({a1} {sign1} {abs(b1)}i) + ({a2} {sign2} {abs(b2)}i) - ({a3} {sign3} {abs(b3)}i)"
            real = a1 + a2 - a3
            imag = b1 + b2 - b3

        solution = f"{real} + {imag}i" if imag >= 0 else f"{real} - {abs(imag)}i"
        steps = [
            f"Combine real parts: {real}",
            f"Combine imaginary parts: {imag}i",
            f"Result: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Include coefficients and nested operations
        a1, b1 = random.randint(-8, 8), random.randint(-8, 8)
        a2, b2 = random.randint(-8, 8), random.randint(-8, 8)
        k = random.randint(2, 5)

        sign1 = '+' if b1 >= 0 else '-'
        sign2 = '+' if b2 >= 0 else '-'

        latex = f"{k}({a1} {sign1} {abs(b1)}i) + ({a2} {sign2} {abs(b2)}i)"
        real = k * a1 + a2
        imag = k * b1 + b2

        solution = f"{real} + {imag}i" if imag >= 0 else f"{real} - {abs(imag)}i"
        steps = [
            f"Distribute {k}: {k*a1} {'+' if k*b1 >= 0 else '-'} {abs(k*b1)}i",
            f"Add: ({k*a1} {'+' if k*b1 >= 0 else '-'} {abs(k*b1)}i) + ({a2} {sign2} {abs(b2)}i)",
            f"Real: {k*a1} + {a2} = {real}",
            f"Imaginary: {k*b1} + {b2} = {imag}",
            f"Result: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex expression with multiple terms and coefficients
        a1, b1 = random.randint(-6, 6), random.randint(-6, 6)
        a2, b2 = random.randint(-6, 6), random.randint(-6, 6)
        a3, b3 = random.randint(-6, 6), random.randint(-6, 6)
        k1, k2 = random.randint(2, 4), random.randint(2, 4)

        sign1 = '+' if b1 >= 0 else '-'
        sign2 = '+' if b2 >= 0 else '-'
        sign3 = '+' if b3 >= 0 else '-'

        latex = f"{k1}({a1} {sign1} {abs(b1)}i) - {k2}({a2} {sign2} {abs(b2)}i) + ({a3} {sign3} {abs(b3)}i)"
        real = k1 * a1 - k2 * a2 + a3
        imag = k1 * b1 - k2 * b2 + b3

        solution = f"{real} + {imag}i" if imag >= 0 else f"{real} - {abs(imag)}i"
        steps = [
            f"Distribute {k1}: {k1*a1} {'+' if k1*b1 >= 0 else '-'} {abs(k1*b1)}i",
            f"Distribute {k2}: {k2*a2} {'+' if k2*b2 >= 0 else '-'} {abs(k2*b2)}i",
            f"Combine all terms",
            f"Real: {k1*a1} - {k2*a2} + {a3} = {real}",
            f"Imaginary: {k1*b1} - {k2*b2} + {b3} = {imag}",
            f"Result: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = AddSubComplexNumbersGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
