"""
Solving and Graphing Factored Form Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingGraphingFactoredFormGenerator:
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
        r1 = random.randint(-5, 5)
        r2 = random.randint(-5, 5)
        while r1 == r2:
            r2 = random.randint(-5, 5)
        latex = f"\\text{{Find the x-intercepts of }} y = (x {'-' if r1 < 0 else '+'} {abs(r1)})(x {'-' if r2 < 0 else '+'} {abs(r2)})"
        solution = f"x = {r1}, x = {r2}"
        steps = [
            "Set y = 0",
            f"(x {'-' if r1 < 0 else '+'} {abs(r1)})(x {'-' if r2 < 0 else '+'} {abs(r2)}) = 0",
            f"x {'-' if r1 < 0 else '+'} {abs(r1)} = 0 or x {'-' if r2 < 0 else '+'} {abs(r2)} = 0",
            f"x = {r1} or x = {r2}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 4)
        r1 = random.randint(-4, 4)
        r2 = random.randint(-4, 4)
        while r1 == r2:
            r2 = random.randint(-4, 4)
        latex = f"\\text{{Find the x-intercepts of }} y = {a}(x {'-' if r1 < 0 else '+'} {abs(r1)})(x {'-' if r2 < 0 else '+'} {abs(r2)})"
        solution = f"x = {r1}, x = {r2}"
        steps = [
            "Set y = 0",
            f"{a}(x {'-' if r1 < 0 else '+'} {abs(r1)})(x {'-' if r2 < 0 else '+'} {abs(r2)}) = 0",
            "Divide both sides by {a}",
            f"x = {r1} or x = {r2}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(1, 3)
        r1 = random.randint(-4, 4)
        r2 = random.randint(-4, 4)
        while r1 == r2:
            r2 = random.randint(-4, 4)
        vertex_x = (r1 + r2) / 2
        vertex_y = a * (vertex_x - r1) * (vertex_x - r2)
        latex = f"\\text{{Find vertex and x-intercepts of }} y = {a}(x {'-' if r1 < 0 else '+'} {abs(r1)})(x {'-' if r2 < 0 else '+'} {abs(r2)})"
        solution = f"Vertex: ({vertex_x}, {vertex_y:.2f}), x-intercepts: {r1}, {r2}"
        steps = [
            f"x-intercepts: x = {r1}, x = {r2}",
            f"Vertex x-coordinate: ({r1} + {r2})/2 = {vertex_x}",
            f"Vertex y-coordinate: {a}({vertex_x} - {r1})({vertex_x} - {r2}) = {vertex_y:.2f}",
            f"Vertex: ({vertex_x}, {vertex_y:.2f})"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(1, 3)
        r1 = random.randint(-5, 5)
        r2 = random.randint(-5, 5)
        while r1 == r2:
            r2 = random.randint(-5, 5)
        vertex_x = (r1 + r2) / 2
        vertex_y = a * (vertex_x - r1) * (vertex_x - r2)
        y_int = a * (-r1) * (-r2)
        latex = f"\\text{{Find vertex, x-intercepts, and y-intercept of }} y = {a}(x {'-' if r1 < 0 else '+'} {abs(r1)})(x {'-' if r2 < 0 else '+'} {abs(r2)})"
        solution = f"Vertex: ({vertex_x}, {vertex_y:.2f}), x-int: {r1}, {r2}, y-int: {y_int}"
        steps = [
            f"x-intercepts: {r1}, {r2}",
            f"Vertex: ({vertex_x}, {vertex_y:.2f})",
            f"y-intercept: y = {a}(0 - {r1})(0 - {r2}) = {y_int}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingGraphingFactoredFormGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
