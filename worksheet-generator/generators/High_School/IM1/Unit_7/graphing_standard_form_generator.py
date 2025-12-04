"""
Graphing Standard Form Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphingStandardFormGenerator:
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
        c = random.randint(10, 20)

        x_int = c / a
        y_int = c / b

        latex = f"\\text{{Graph }} {a}x + {b}y = {c} \\text{{ using intercepts}}"
        solution = f"({x_int:.1f}, 0) \\text{{ and }} (0, {y_int:.1f})"
        steps = [f"X-intercept: ({x_int:.1f}, 0)", f"Y-intercept: (0, {y_int:.1f})", "Plot both points and draw line"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(12, 30)

        x_int = c / a
        y_int = c / b

        latex = f"\\text{{Graph }} {a}x + {b}y = {c}"
        solution = f"Intercepts: ({x_int:.1f}, 0), (0, {y_int:.1f})"
        steps = [f"Find x-intercept: set y=0, x = {x_int:.1f}", f"Find y-intercept: set x=0, y = {y_int:.1f}", "Connect the points"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(-5, -2)
        b = random.randint(2, 6)
        c = random.randint(10, 25)

        x_int = c / a
        y_int = c / b

        latex = f"\\text{{Graph }} {a}x + {b}y = {c}"
        solution = f"Intercepts: ({x_int:.1f}, 0), (0, {y_int:.1f})"
        steps = [f"X-intercept: {a}x = {c}, x = {x_int:.1f}", f"Y-intercept: {b}y = {c}, y = {y_int:.1f}", "Plot and connect"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        c = random.randint(15, 30)

        x_int = c / a
        y_int = c / b
        m = -a / b

        latex = f"\\text{{Graph }} {a}x + {b}y = {c} \\text{{ and find its slope}}"
        solution = f"Slope: {m:.1f}"
        steps = [f"Convert to y = mx + b", f"{b}y = -{a}x + {c}", f"y = {m:.1f}x + {y_int:.1f}", f"Slope: {m:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = GraphingStandardFormGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
