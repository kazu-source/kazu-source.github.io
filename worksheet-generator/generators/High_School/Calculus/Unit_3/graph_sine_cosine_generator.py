"""
Graph Sine and Cosine Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphSineCosineGenerator:
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
        a = random.randint(2, 4)
        func = random.choice(['sin', 'cos'])

        latex = f"\\text{{Graph }} f(x) = {a}\\{func}(x). \\text{{ State key points.}}"
        solution = f"Amplitude {a}, standard {func} shape"
        steps = [
            f"\\text{{Amplitude: }} {a}",
            f"\\text{{Period: }} 2\\pi",
            f"\\text{{Max: }} {a}, \\text{{ Min: }} -{a}",
            f"\\text{{Plot standard }} \\{func} \\text{{ with these values}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 3)
        k = random.randint(1, 4)
        func = random.choice(['sin', 'cos'])

        latex = f"\\text{{Graph }} f(x) = {a}\\{func}(x) + {k}."
        solution = f"Shifted up {k}, amplitude {a}"
        steps = [
            f"\\text{{Amplitude: }} {a}",
            f"\\text{{Midline: }} y = {k}",
            f"\\text{{Max: }} {a + k}, \\text{{ Min: }} {k - a}",
            f"\\text{{Center around }} y = {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 3)
        b = random.randint(2, 3)
        func = random.choice(['sin', 'cos'])

        latex = f"\\text{{Graph }} f(x) = {a}\\{func}({b}x)."
        solution = f"Amplitude {a}, period \\frac{{2\\pi}}{{{b}}}"
        steps = [
            f"\\text{{Amplitude: }} {a}",
            f"\\text{{Period: }} \\frac{{2\\pi}}{{{b}}}",
            f"\\text{{Compressed horizontally by factor }} {b}",
            f"\\text{{Max: }} {a}, \\text{{ Min: }} -{a}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 3)
        b = random.randint(2, 3)
        c = random.randint(1, 2)
        d = random.randint(1, 3)
        func = random.choice(['sin', 'cos'])

        latex = f"\\text{{Graph }} f(x) = {a}\\{func}({b}(x - {c})) + {d}."
        solution = f"Full transformation with all parameters"
        steps = [
            f"\\text{{Amplitude: }} {a}",
            f"\\text{{Period: }} \\frac{{2\\pi}}{{{b}}}",
            f"\\text{{Phase shift: right }} {c}",
            f"\\text{{Vertical shift: }} y = {d}",
            f"\\text{{Max: }} {a + d}, \\text{{ Min: }} {d - a}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = GraphSineCosineGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
