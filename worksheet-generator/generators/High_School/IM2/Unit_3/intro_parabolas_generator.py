"""
Introduction to Parabolas Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class IntroParabolasGenerator:
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
        a = random.choice([1, 2, 3, -1, -2])
        latex = f"\\text{{Identify the vertex and direction of }} y = {a if a != 1 else ''}x^2"
        solution = f"Vertex: (0, 0), Opens {'up' if a > 0 else 'down'}"
        steps = [
            f"Standard form: y = ax²",
            f"Vertex is at origin: (0, 0)",
            f"a = {a}",
            f"Since a {'> 0' if a > 0 else '< 0'}, parabola opens {'up' if a > 0 else 'down'}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.choice([1, 2, -1, -2, 0.5, -0.5])
        h = random.randint(-4, 4)
        k = random.randint(-4, 4)
        latex = f"\\text{{Find the vertex of }} y = {'' if a == 1 else a}(x {'-' if h < 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else ''} {k}"
        solution = f"({h}, {k})"
        steps = [
            f"Vertex form: y = a(x - h)² + k",
            f"Vertex is at (h, k)",
            f"From y = {'' if a == 1 else a}(x {'-' if h < 0 else '+'} {abs(h)})² {'+' if k >= 0 else ''} {k}",
            f"h = {h}, k = {k}",
            f"Vertex: ({h}, {k})"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.choice([1, 2, 3, -1, -2])
        h = random.randint(-5, 5)
        k = random.randint(-5, 5)
        latex = f"\\text{{Find vertex, axis of symmetry, and direction for }} y = {a if a != 1 else ''}(x {'-' if h < 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else ''} {k}"
        solution = f"Vertex: ({h}, {k}), Axis: x = {h}, Opens {'up' if a > 0 else 'down'}"
        steps = [
            f"Vertex form: y = a(x - h)² + k",
            f"Vertex: ({h}, {k})",
            f"Axis of symmetry: x = {h}",
            f"a = {a} {'> 0' if a > 0 else '< 0'}, opens {'up' if a > 0 else 'down'}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(1, 3)
        b = random.randint(-8, 8)
        c = random.randint(-8, 8)
        h = -b / (2 * a)
        k = a * h**2 + b * h + c
        latex = f"\\text{{Convert to vertex form: }} y = {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}"
        solution = f"y = {a}(x {'-' if h < 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else ''}{k:.2f}"
        steps = [
            f"Complete the square for y = {a}x² {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}",
            f"h = -b/(2a) = -{b}/(2·{a}) = {h}",
            f"k = a(h)² + b(h) + c = {k:.2f}",
            f"Vertex form: y = {a}(x - {h})² + {k:.2f}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = IntroParabolasGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
