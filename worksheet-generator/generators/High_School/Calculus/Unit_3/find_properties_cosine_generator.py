"""
Find Properties of Cosine Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FindPropertiesCosineGenerator:
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
        a = random.randint(2, 6)

        latex = f"\\text{{Find the amplitude of }} f(x) = {a}\\cos(x)."
        solution = f"{a}"
        steps = [
            f"\\text{{Form: }} y = A\\cos(x)",
            f"\\text{{Amplitude }} = |A| = {a}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        b = random.randint(2, 5)

        latex = f"\\text{{Find the period of }} f(x) = \\cos({b}x)."
        solution = f"\\frac{{2\\pi}}{{{b}}}"
        steps = [
            f"\\text{{Form: }} y = \\cos(Bx)",
            f"\\text{{Period }} = \\frac{{2\\pi}}{{B}} = \\frac{{2\\pi}}{{{b}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 4)
        k = random.randint(-3, 3)
        k_str = f"+ {k}" if k >= 0 else f"- {abs(k)}"

        latex = f"\\text{{Find amplitude, period, and midline of }} f(x) = {a}\\cos({b}x) {k_str}."
        solution = f"Amp: {a}, Period: \\frac{{2\\pi}}{{{b}}}, Midline: y = {k}"
        steps = [
            f"\\text{{Amplitude: }} {a}",
            f"\\text{{Period: }} \\frac{{2\\pi}}{{{b}}}",
            f"\\text{{Midline: }} y = {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(2, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)

        latex = f"\\text{{Find all properties of }} f(x) = {a}\\cos({b}(x + {c})) - {d}."
        solution = f"Amp: {a}, Period: \\frac{{2\\pi}}{{{b}}}, Phase left: {c}, Midline: -{d}"
        steps = [
            f"\\text{{Amplitude: }} {a}",
            f"\\text{{Period: }} \\frac{{2\\pi}}{{{b}}}",
            f"\\text{{Phase shift: left }} {c}",
            f"\\text{{Vertical shift: }} y = -{d}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FindPropertiesCosineGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
