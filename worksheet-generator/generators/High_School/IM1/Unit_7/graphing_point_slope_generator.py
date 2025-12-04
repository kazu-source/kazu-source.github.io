"""
Graphing Point Slope Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphingPointSlopeGenerator:
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
        m = random.randint(1, 4)
        x1 = random.randint(1, 5)
        y1 = random.randint(1, 8)

        latex = f"\\text{{Graph }} y - {y1} = {m}(x - {x1})"
        solution = f"Start at ({x1}, {y1}), slope {m}"
        steps = [f"Point: ({x1}, {y1})", f"Slope: {m}", f"From ({x1}, {y1}), rise {m}, run 1"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(-4, -1)
        x1 = random.randint(0, 5)
        y1 = random.randint(3, 10)

        latex = f"\\text{{Graph }} y - {y1} = {m}(x - {x1})"
        solution = f"Start at ({x1}, {y1}), slope {m}"
        steps = [f"Point: ({x1}, {y1})", f"Slope: {m} (down {abs(m)}, right 1)", f"Plot and draw line"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        num = random.randint(2, 4)
        den = random.randint(3, 5)
        x1 = random.randint(0, 4)
        y1 = random.randint(2, 8)

        latex = f"\\text{{Graph }} y - {y1} = \\frac{{{num}}}{{{den}}}(x - {x1})"
        solution = f"Start at ({x1}, {y1}), rise {num}, run {den}"
        steps = [f"Point: ({x1}, {y1})", f"Slope: rise {num}, run {den}", f"From ({x1}, {y1}), up {num}, right {den}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        m = random.randint(2, 5)
        x1 = random.randint(1, 4)
        y1 = random.randint(2, 8)
        b = y1 - m * x1

        latex = f"\\text{{Graph }} y - {y1} = {m}(x - {x1}) \\text{{ and find y-intercept}}"
        solution = f"y-intercept: {b}"
        steps = [f"Convert to y = mx + b", f"y = {m}x + {b}", f"Y-intercept: {b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = GraphingPointSlopeGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
