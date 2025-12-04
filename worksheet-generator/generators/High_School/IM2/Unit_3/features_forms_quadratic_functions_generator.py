"""
Features and Forms of Quadratic Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FeaturesFormsQuadraticFunctionsGenerator:
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
        a = random.choice([1, 2, -1, -2])
        h = random.randint(-4, 4)
        k = random.randint(-4, 4)
        latex = f"\\text{{Identify the form: }} y = {'' if a == 1 else a}(x {'-' if h < 0 else '+'} {abs(h)})^2 {'+' if k >= 0 else ''}{k}"
        solution = f"Vertex form: vertex ({h}, {k})"
        steps = [
            "This is vertex form: y = a(x - h)² + k",
            f"Vertex: ({h}, {k})",
            f"a = {a}, opens {'up' if a > 0 else 'down'}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        r1 = random.randint(-4, 4)
        r2 = random.randint(-4, 4)
        while r1 == r2:
            r2 = random.randint(-4, 4)
        a = random.choice([1, 2, -1])
        latex = f"\\text{{Identify the form: }} y = {'' if a == 1 else a}(x {'-' if r1 < 0 else '+'} {abs(r1)})(x {'-' if r2 < 0 else '+'} {abs(r2)})"
        solution = f"Factored form: x-intercepts at {r1} and {r2}"
        steps = [
            "This is factored form: y = a(x - r₁)(x - r₂)",
            f"x-intercepts: x = {r1} and x = {r2}",
            f"Vertex x = ({r1} + {r2})/2 = {(r1 + r2) / 2}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(1, 3)
        b = random.randint(-8, 8)
        c = random.randint(-8, 8)
        h = -b / (2 * a)
        k = a * h ** 2 + b * h + c
        latex = f"\\text{{Find all key features of }} y = {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}"
        solution = f"Vertex: ({h}, {k:.1f}), y-int: {c}, axis: x = {h}"
        steps = [
            f"Standard form: y = {a}x² {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}",
            f"Vertex x: h = -b/(2a) = -{b}/(2·{a}) = {h}",
            f"Vertex y: k = {a}({h})² {'+' if b >= 0 else ''}{b}({h}) {'+' if c >= 0 else ''}{c} = {k:.1f}",
            f"y-intercept: {c}",
            f"Axis of symmetry: x = {h}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        form = random.choice(['standard_to_vertex', 'vertex_to_factored'])
        if form == 'standard_to_vertex':
            a = random.randint(1, 3)
            b = random.randint(-6, 6)
            c = random.randint(-6, 6)
            h = -b / (2 * a)
            k = c - (b ** 2) / (4 * a)
            latex = f"\\text{{Convert to vertex form: }} y = {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}"
            solution = f"y = {a}(x {'-' if h < 0 else '+'} {abs(h):.1f})^2 {'+' if k >= 0 else ''}{k:.1f}"
            steps = [
                "Complete the square",
                f"h = -b/(2a) = {h:.1f}",
                f"k = {k:.1f}",
                solution
            ]
        else:
            h = random.randint(-3, 3)
            k = random.randint(-4, 4)
            if k >= 0:
                import math
                sqrt_k = math.sqrt(k)
                r1 = h - sqrt_k
                r2 = h + sqrt_k
                latex = f"\\text{{Convert to factored form: }} y = (x {'-' if h < 0 else '+'} {abs(h)})^2 - {k}"
                solution = f"y = (x {'-' if r1 < 0 else '+'} {abs(r1):.2f})(x {'-' if r2 < 0 else '+'} {abs(r2):.2f})"
                steps = [
                    "Vertex form to factored form",
                    f"Find roots: (x {'-' if h < 0 else '+'} {abs(h)})² = {k}",
                    f"x {'-' if h < 0 else '+'} {abs(h)} = ±{sqrt_k:.2f}",
                    solution
                ]
            else:
                latex = f"\\text{{Can you convert to factored form: }} y = (x {'-' if h < 0 else '+'} {abs(h)})^2 + {abs(k)}"
                solution = "No real factored form (no real roots)"
                steps = [
                    f"Vertex at ({h}, {k})",
                    f"Since k = {k} and parabola opens up, no x-intercepts",
                    "Cannot factor over real numbers"
                ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FeaturesFormsQuadraticFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
