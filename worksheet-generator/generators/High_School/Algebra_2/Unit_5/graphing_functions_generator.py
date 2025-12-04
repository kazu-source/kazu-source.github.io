"""
Graphing Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphingFunctionsGenerator:
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
                b = random.randint(-5, 5)
                latex = f"\\text{{Graph: }} y = {a}x + {b}"
                solution = f"\\text{{Linear function, slope = {a}, y-intercept = {b}}}"
                steps = [f"Slope: {a}", f"Y-intercept: {b}", f"Plot points and draw line"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                a = random.randint(1, 4)
                h = random.randint(-3, 3)
                k = random.randint(-3, 3)
                latex = f"\\text{{Graph: }} y = {a}(x - {h})^2 + {k}"
                solution = f"\\text{{Parabola, vertex at ({h}, {k}), opens {'up' if a > 0 else 'down'}}}"
                steps = [f"Vertex form", f"Vertex: ({h}, {k})", f"Opens: {'up' if a > 0 else 'down'}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                a = random.randint(2, 5)
                latex = f"\\text{{Graph: }} y = \\frac{{{a}}}{{x}}"
                solution = f"\\text{{Hyperbola with vertical asymptote x=0, horizontal asymptote y=0}}"
                steps = [f"Rational function", f"Vertical asymptote: x = 0", f"Horizontal asymptote: y = 0"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                a = random.randint(1, 3)
                b = random.randint(1, 4)
                c = random.randint(-5, 5)
                latex = f"\\text{{Graph: }} y = {a}|x - {b}| + {c}"
                solution = f"\\text{{Absolute value, vertex at ({b}, {c}), V-shape}}"
                steps = [f"Absolute value function", f"Vertex: ({b}, {c})", f"Opens {'up' if a > 0 else 'down'}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = GraphingFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
