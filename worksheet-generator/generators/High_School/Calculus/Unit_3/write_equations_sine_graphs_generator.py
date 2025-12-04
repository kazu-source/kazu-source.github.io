"""
Write Equations from Sine Graphs Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class WriteEquationsSineGraphsGenerator:
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
        a = random.randint(2, 5)

        latex = f"\\text{{Write equation for sine with amplitude }} {a}."
        solution = f"f(x) = {a}\\sin(x)"
        steps = [
            f"\\text{{Amplitude }} A = {a}",
            f"\\text{{Standard form: }} y = A\\sin(x)",
            f"f(x) = {a}\\sin(x)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 4)
        k = random.randint(1, 5)

        latex = f"\\text{{Write equation: amplitude }} {a}, \\text{{ midline }} y = {k}."
        solution = f"f(x) = {a}\\sin(x) + {k}"
        steps = [
            f"\\text{{Amplitude: }} {a}",
            f"\\text{{Midline: }} +{k}",
            f"f(x) = {a}\\sin(x) + {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(2, 4)

        latex = f"\\text{{Write equation: amplitude }} {a}, \\text{{ period }} \\frac{{2\\pi}}{{{b}}}."
        solution = f"f(x) = {a}\\sin({b}x)"
        steps = [
            f"\\text{{Amplitude: }} A = {a}",
            f"\\text{{Period }} = \\frac{{2\\pi}}{{B}} = \\frac{{2\\pi}}{{{b}}} \\Rightarrow B = {b}",
            f"f(x) = {a}\\sin({b}x)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 3)
        b = random.randint(2, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)

        latex = f"\\text{{Write equation: amp }} {a}, \\text{{ period }} \\frac{{2\\pi}}{{{b}}}, \\text{{ phase right }} {c}, \\text{{ midline }} y = {d}."
        solution = f"f(x) = {a}\\sin({b}(x - {c})) + {d}"
        steps = [
            f"\\text{{Amplitude: }} A = {a}",
            f"\\text{{Period gives: }} B = {b}",
            f"\\text{{Phase shift: }} C = {c}",
            f"\\text{{Midline: }} D = {d}",
            f"f(x) = {a}\\sin({b}(x - {c})) + {d}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = WriteEquationsSineGraphsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
