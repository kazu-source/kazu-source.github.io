"""
Parallel and Perpendicular Lines on Coordinate Plane Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ParallelPerpendicularLinesCoordinateGenerator:
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
        m = random.randint(2, 6)
        b = random.randint(-5, 5)
        latex = f"\\text{{What is the slope of a line parallel to }} y = {m}x + {b}?"
        solution = f"{m}"
        steps = ["\\text{Parallel lines have equal slopes}",
                f"\\text{{Slope}} = {m}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 6)
        b = random.randint(-5, 5)
        perp_m = -1 / m
        latex = f"\\text{{What is the slope of a line perpendicular to }} y = {m}x + {b}?"
        solution = f"{perp_m:.2f}" if perp_m != int(perp_m) else f"{int(perp_m)}"
        steps = ["\\text{Perpendicular lines have slopes that are negative reciprocals}",
                f"m_{{\\perp}} = -\\frac{{1}}{{{m}}} = {perp_m:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(2, 6), random.randint(2, 6)
        x2, y2 = random.randint(8, 12), random.randint(8, 12)
        m = (y2 - y1) / (x2 - x1)
        x3, y3 = random.randint(1, 5), random.randint(10, 15)
        b = y3 - m * x3
        latex = f"\\text{{Find equation of line through }} ({x3},{y3}) \\text{{ parallel to line through }} ({x1},{y1}) \\text{{ and }} ({x2},{y2})."
        solution = f"y = {m:.2f}x + {b:.2f}"
        steps = [f"\\text{{Slope of original line: }} m = \\frac{{{y2}-{y1}}}{{{x2}-{x1}}} = {m:.2f}",
                f"\\text{{Parallel line has same slope: }} m = {m:.2f}",
                f"\\text{{Using point-slope: }} y - {y3} = {m:.2f}(x - {x3})",
                f"y = {m:.2f}x + {b:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x1, y1 = random.randint(2, 6), random.randint(2, 6)
        x2, y2 = random.randint(8, 12), random.randint(8, 12)
        m = (y2 - y1) / (x2 - x1)
        perp_m = -1 / m
        x3, y3 = random.randint(1, 5), random.randint(10, 15)
        b = y3 - perp_m * x3
        latex = f"\\text{{Find equation of line through }} ({x3},{y3}) \\text{{ perpendicular to line through }} ({x1},{y1}) \\text{{ and }} ({x2},{y2})."
        solution = f"y = {perp_m:.2f}x + {b:.2f}"
        steps = [f"\\text{{Slope of original line: }} m = \\frac{{{y2}-{y1}}}{{{x2}-{x1}}} = {m:.2f}",
                f"\\text{{Perpendicular slope: }} m_{{\\perp}} = -\\frac{{1}}{{{m:.2f}}} = {perp_m:.2f}",
                f"\\text{{Using point-slope: }} y - {y3} = {perp_m:.2f}(x - {x3})",
                f"y = {perp_m:.2f}x + {b:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ParallelPerpendicularLinesCoordinateGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
