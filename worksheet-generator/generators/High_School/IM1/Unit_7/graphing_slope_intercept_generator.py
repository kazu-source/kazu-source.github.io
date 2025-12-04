"""
Graphing Slope Intercept Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphingSlopeInterceptGenerator:
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
        m = random.randint(1, 5)
        b = random.randint(-5, 5)

        latex = f"\\text{{Graph }} y = {m}x + {b}"
        solution = f"Start at (0, {b}), slope = {m}"
        steps = [f"Y-intercept: (0, {b})", f"Slope: rise {m}, run 1", f"Plot points and draw line"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(-4, -1)
        b = random.randint(-6, 6)

        latex = f"\\text{{Graph }} y = {m}x + {b}"
        solution = f"Start at (0, {b}), slope = {m}"
        steps = [f"Y-intercept: (0, {b})", f"Slope: rise {m}, run 1 (down {abs(m)}, right 1)", f"Plot points and draw line"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        num = random.randint(1, 4)
        den = random.randint(2, 5)
        b = random.randint(-5, 5)

        latex = f"\\text{{Graph }} y = \\frac{{{num}}}{{{den}}}x + {b}"
        solution = f"Start at (0, {b}), rise {num}, run {den}"
        steps = [f"Y-intercept: (0, {b})", f"Slope: rise {num}, run {den}", f"From (0,{b}), go up {num}, right {den}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        m = random.randint(2, 5)
        b = random.randint(-4, 4)
        x_val = random.randint(1, 3)
        y_val = m * x_val + b

        latex = f"\\text{{Graph }} y = {m}x + {b} \\text{{ and identify point when }} x = {x_val}"
        solution = f"Point: ({x_val}, {y_val})"
        steps = [f"Y-intercept: (0, {b})", f"When x = {x_val}: y = {m}({x_val}) + {b} = {y_val}", f"Point: ({x_val}, {y_val})"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = GraphingSlopeInterceptGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
