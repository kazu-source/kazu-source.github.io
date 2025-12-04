"""
Add, Subtract, Multiply, and Divide Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class AddSubtractMultiplyDivideFunctionsGenerator:
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
        b = random.randint(1, 5)
        operation = random.choice(['add', 'subtract'])

        if operation == 'add':
            latex = f"f(x) = {a}x, g(x) = {b}x. \\text{{ Find }} (f + g)(x)."
            solution = f"{a + b}x"
            steps = [
                f"(f + g)(x) = f(x) + g(x)",
                f"= {a}x + {b}x",
                f"= {a + b}x"
            ]
        else:
            latex = f"f(x) = {a}x, g(x) = {b}x. \\text{{ Find }} (f - g)(x)."
            solution = f"{a - b}x"
            steps = [
                f"(f - g)(x) = f(x) - g(x)",
                f"= {a}x - {b}x",
                f"= {a - b}x"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(1, 4)
        b = random.randint(1, 6)
        c = random.randint(1, 4)
        d = random.randint(1, 6)
        operation = random.choice(['add', 'subtract', 'multiply'])

        if operation == 'add':
            latex = f"f(x) = {a}x + {b}, g(x) = {c}x + {d}. \\text{{ Find }} (f + g)(x)."
            solution = f"{a + c}x + {b + d}"
            steps = [
                f"(f + g)(x) = ({a}x + {b}) + ({c}x + {d})",
                f"= {a + c}x + {b + d}"
            ]
        elif operation == 'subtract':
            latex = f"f(x) = {a}x + {b}, g(x) = {c}x + {d}. \\text{{ Find }} (f - g)(x)."
            solution = f"{a - c}x + {b - d}" if b - d >= 0 else f"{a - c}x - {abs(b - d)}"
            steps = [
                f"(f - g)(x) = ({a}x + {b}) - ({c}x + {d})",
                f"= {a - c}x + {b - d}"
            ]
        else:
            latex = f"f(x) = {a}x, g(x) = {c}x. \\text{{ Find }} (f \\cdot g)(x)."
            solution = f"{a * c}x^2"
            steps = [
                f"(f \\cdot g)(x) = f(x) \\cdot g(x)",
                f"= {a}x \\cdot {c}x",
                f"= {a * c}x^2"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(1, 3)
        b = random.randint(1, 5)
        c = random.randint(1, 3)
        operation = random.choice(['multiply', 'divide'])

        if operation == 'multiply':
            latex = f"f(x) = {a}x + {b}, g(x) = {c}x. \\text{{ Find }} (f \\cdot g)(x)."
            solution = f"{a * c}x^2 + {b * c}x"
            steps = [
                f"(f \\cdot g)(x) = ({a}x + {b})({c}x)",
                f"= {a * c}x^2 + {b * c}x"
            ]
        else:
            latex = f"f(x) = {a}x, g(x) = {c}x. \\text{{ Find }} \\left(\\frac{{f}}{{g}}\\right)(x)."
            solution = f"\\frac{{{a}}}{{{c}}}"
            steps = [
                f"\\left(\\frac{{f}}{{g}}\\right)(x) = \\frac{{f(x)}}{{g(x)}}",
                f"= \\frac{{{a}x}}{{{c}x}}",
                f"= \\frac{{{a}}}{{{c}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(1, 3)
        b = random.randint(1, 4)
        c = random.randint(1, 3)
        d = random.randint(1, 4)

        latex = f"f(x) = {a}x + {b}, g(x) = {c}x + {d}. \\text{{ Find }} (f \\cdot g)(x)."
        solution = f"{a * c}x^2 + {a * d + b * c}x + {b * d}"
        steps = [
            f"(f \\cdot g)(x) = ({a}x + {b})({c}x + {d})",
            f"= {a * c}x^2 + {a * d}x + {b * c}x + {b * d}",
            f"= {a * c}x^2 + {a * d + b * c}x + {b * d}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = AddSubtractMultiplyDivideFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
