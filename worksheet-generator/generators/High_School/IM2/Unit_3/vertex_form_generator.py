"""
Vertex Form Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class VertexFormGenerator:
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
        h = random.randint(-5, 5)
        k = random.randint(-5, 5)
        latex = f"\\text{{Find the vertex of }} y = (x {'-' if h < 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else ''}{k}"
        solution = f"({h}, {k})"
        steps = [
            f"Vertex form: y = a(x - h)² + k",
            f"Vertex is (h, k)",
            f"From y = (x {'-' if h < 0 else '+'} {abs(h)})² {'+' if k >= 0 else ''}{k}",
            f"Vertex: ({h}, {k})"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(1, 3)
        b = random.randint(-8, 8)
        c = random.randint(-8, 8)
        h = -b / (2 * a)
        k = c - (b ** 2) / (4 * a)
        latex = f"\\text{{Convert to vertex form: }} y = {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}"
        solution = f"y = {a}(x - {h:.1f})^2 + {k:.1f}"
        steps = [
            f"Complete the square",
            f"h = -b/(2a) = -{b}/(2·{a}) = {h:.1f}",
            f"k = c - b²/(4a) = {c} - {b**2}/(4·{a}) = {k:.1f}",
            f"y = {a}(x - {h:.1f})² + {k:.1f}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        h = random.randint(-4, 4)
        k = random.randint(-6, 6)
        latex = f"\\text{{Expand to standard form: }} y = {a}(x {'-' if h < 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else ''}{k}"
        a_coef = a
        b_coef = -2 * a * h
        c_coef = a * h ** 2 + k
        solution = f"y = {a_coef}x^2 {'+' if b_coef >= 0 else ''}{b_coef}x {'+' if c_coef >= 0 else ''}{c_coef}"
        steps = [
            f"Expand (x {'-' if h < 0 else '+'} {abs(h)})²",
            f"= x² {'-' if h < 0 else '+'} {2*abs(h)}x + {h**2}",
            f"y = {a}(x² {'-' if h < 0 else '+'} {2*abs(h)}x + {h**2}) {'+' if k >= 0 else ''}{k}",
            f"y = {a_coef}x² {'+' if b_coef >= 0 else ''}{b_coef}x {'+' if c_coef >= 0 else ''}{c_coef}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        h = random.randint(-3, 3)
        k = random.randint(-5, 5)
        x_val = h + random.randint(1, 3)
        a = random.randint(1, 3)
        y_val = a * (x_val - h) ** 2 + k
        latex = f"\\text{{Write equation with vertex }} ({h}, {k}) \\text{{ passing through }} ({x_val}, {y_val})"
        solution = f"y = {a}(x {'-' if h < 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else ''}{k}"
        steps = [
            f"Use vertex form: y = a(x - h)² + k",
            f"Vertex ({h}, {k}): y = a(x {'-' if h < 0 else '+'} {abs(h)})² {'+' if k >= 0 else ''}{k}",
            f"Substitute ({x_val}, {y_val}):",
            f"{y_val} = a({x_val} {'-' if h < 0 else '+'} {abs(h)})² {'+' if k >= 0 else ''}{k}",
            f"a = {a}",
            solution
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = VertexFormGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
