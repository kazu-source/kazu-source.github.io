"""
Find Values of Inverse Functions from Graphs Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FindValuesInverseGraphsGenerator:
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
        x = random.randint(1, 6)
        y = random.randint(1, 8)

        latex = f"\\text{{The graph of }} f(x) \\text{{ passes through }} ({x}, {y}). \\text{{ Find }} f^{{-1}}({y})."
        solution = f"{x}"
        steps = [
            f"\\text{{Point on }} f: ({x}, {y})",
            f"\\text{{Point on }} f^{{-1}}: ({y}, {x})",
            f"\\therefore f^{{-1}}({y}) = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x = random.randint(2, 7)
        y = random.randint(3, 9)

        latex = f"\\text{{If }} ({x}, {y}) \\text{{ is on the graph of }} f, \\text{{ what point is on }} f^{{-1}}?"
        solution = f"({y}, {x})"
        steps = [
            "\\text{The inverse function swaps x and y}",
            f"\\text{{Point on }} f: ({x}, {y})",
            f"\\text{{Point on }} f^{{-1}}: ({y}, {x})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(1, 5), random.randint(2, 7)
        x2, y2 = random.randint(6, 10), random.randint(8, 12)

        latex = f"\\text{{Graph of }} f \\text{{ has points }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2}). "
        latex += f"\\text{{Find }} f^{{-1}}({y1}) \\cdot f^{{-1}}({y2})."
        result = x1 * x2
        solution = f"{result}"
        steps = [
            f"f^{{-1}}({y1}) = {x1}",
            f"f^{{-1}}({y2}) = {x2}",
            f"f^{{-1}}({y1}) \\cdot f^{{-1}}({y2}) = {x1} \\cdot {x2} = {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x = random.randint(2, 6)
        y = random.randint(3, 8)

        latex = f"\\text{{If }} ({x}, {y}) \\text{{ is on }} f, \\text{{ find }} (f^{{-1}} \\circ f)({x})."
        solution = f"{x}"
        steps = [
            f"(f^{{-1}} \\circ f)(x) = f^{{-1}}(f(x))",
            f"\\text{{This always equals }} x",
            f"(f^{{-1}} \\circ f)({x}) = {x}",
            "\\text{Inverse composition property}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FindValuesInverseGraphsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
