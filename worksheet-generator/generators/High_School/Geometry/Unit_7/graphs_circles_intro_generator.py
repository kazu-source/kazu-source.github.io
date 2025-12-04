"""
Graphs of Circles Intro Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class GraphsCirclesIntroGenerator:
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
        r = random.randint(3, 10)
        latex = f"\\text{{Write equation of circle centered at origin with radius }} {r}."
        solution = f"x² + y² = {r**2}"
        steps = [f"\\text{{Standard form: }} x^2 + y^2 = r^2",
                f"x^2 + y^2 = {r}^2 = {r**2}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        h, k = random.randint(-5, 5), random.randint(-5, 5)
        r = random.randint(4, 10)
        latex = f"\\text{{Write equation of circle with center }} ({h},{k}) \\text{{ and radius }} {r}."
        solution = f"(x - {h})² + (y - {k})² = {r**2}"
        steps = [f"\\text{{Standard form: }} (x - h)^2 + (y - k)^2 = r^2",
                f"(x - ({h}))^2 + (y - ({k}))^2 = {r}^2",
                f"(x - {h})^2 + (y - {k})^2 = {r**2}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        h, k = random.randint(-6, 6), random.randint(-6, 6)
        r_sq = random.choice([16, 25, 36, 49])
        r = int(math.sqrt(r_sq))
        latex = f"\\text{{Find center and radius: }} (x - {h})^2 + (y - {k})^2 = {r_sq}."
        solution = f"Center ({h},{k}), radius {r}"
        steps = [f"\\text{{Compare to }} (x - h)^2 + (y - k)^2 = r^2",
                f"h = {h}, k = {k}, r^2 = {r_sq}",
                f"\\text{{Center: }} ({h},{k}), \\text{{ radius: }} {r}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x1, y1 = random.randint(-4, 4), random.randint(-4, 4)
        x2, y2 = random.randint(-4, 4), random.randint(-4, 4)
        h = (x1 + x2) / 2
        k = (y1 + y2) / 2
        r = math.sqrt((x2 - h)**2 + (y2 - k)**2)
        latex = f"\\text{{Circle has diameter with endpoints }} ({x1},{y1}) \\text{{ and }} ({x2},{y2}). \\text{{ Write equation.}}"
        solution = f"(x - {h:.1f})² + (y - {k:.1f})² = {r**2:.2f}"
        steps = [f"\\text{{Center (midpoint): }} ({h:.1f},{k:.1f})",
                f"\\text{{Radius (half diameter): }} r = {r:.2f}",
                f"(x - {h:.1f})^2 + (y - {k:.1f})^2 = {r**2:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = GraphsCirclesIntroGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
