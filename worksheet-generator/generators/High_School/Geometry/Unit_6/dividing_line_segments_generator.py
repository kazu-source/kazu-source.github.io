"""
Dividing Line Segments Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class DividingLineSegmentsGenerator:
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
        x1, y1 = random.randint(2, 8), random.randint(2, 8)
        x2, y2 = random.randint(10, 16), random.randint(10, 16)
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        latex = f"\\text{{Find midpoint of segment from }} ({x1},{y1}) \\text{{ to }} ({x2},{y2})."
        solution = f"({mx},{my})"
        steps = [f"M = \\left(\\frac{{{x1}+{x2}}}{{2}}, \\frac{{{y1}+{y2}}}{{2}}\\right)",
                f"M = ({mx}, {my})"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x1, y1 = random.randint(0, 6), random.randint(0, 6)
        x2, y2 = random.randint(8, 14), random.randint(8, 14)
        ratio = random.choice([1, 2])
        total = ratio + 1
        px = (total * x2 + ratio * x1) / (2 * total) if ratio == 1 else (x1 + 2 * x2) / 3
        py = (total * y2 + ratio * y1) / (2 * total) if ratio == 1 else (y1 + 2 * y2) / 3
        if ratio == 1:
            px = (x1 + x2) / 2
            py = (y1 + y2) / 2
        else:
            px = (x1 + 2 * x2) / 3
            py = (y1 + 2 * y2) / 3
        latex = f"\\text{{Divide segment from }} ({x1},{y1}) \\text{{ to }} ({x2},{y2}) \\text{{ in ratio }} {ratio}:1."
        solution = f"({px:.1f},{py:.1f})"
        steps = [f"P = \\left(\\frac{{{ratio} \\cdot {x2} + 1 \\cdot {x1}}}{{{ratio}+1}}, \\frac{{{ratio} \\cdot {y2} + 1 \\cdot {y1}}}{{{ratio}+1}}\\right)",
                f"P = ({px:.1f}, {py:.1f})"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(2, 6), random.randint(2, 6)
        x2, y2 = random.randint(10, 16), random.randint(10, 16)
        m = random.randint(2, 4)
        n = random.randint(1, 3)
        px = (n * x1 + m * x2) / (m + n)
        py = (n * y1 + m * y2) / (m + n)
        latex = f"\\text{{Find point that divides segment from }} ({x1},{y1}) \\text{{ to }} ({x2},{y2}) \\text{{ in ratio }} {m}:{n}."
        solution = f"({px:.2f},{py:.2f})"
        steps = [f"P = \\left(\\frac{{{m} \\cdot {x2} + {n} \\cdot {x1}}}{{{m}+{n}}}, \\frac{{{m} \\cdot {y2} + {n} \\cdot {y1}}}{{{m}+{n}}}\\right)",
                f"P = ({px:.2f}, {py:.2f})"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x1, y1 = random.randint(0, 5), random.randint(0, 5)
        x2, y2 = random.randint(9, 15), random.randint(9, 15)
        # Point that divides segment in golden ratio
        phi = (1 + math.sqrt(5)) / 2
        px = (x1 + phi * x2) / (1 + phi)
        py = (y1 + phi * y2) / (1 + phi)
        import math
        latex = f"\\text{{Find trisection points (divide into 3 equal parts) of segment from }} ({x1},{y1}) \\text{{ to }} ({x2},{y2})."
        p1x = (2 * x1 + x2) / 3
        p1y = (2 * y1 + y2) / 3
        p2x = (x1 + 2 * x2) / 3
        p2y = (y1 + 2 * y2) / 3
        solution = f"({p1x:.2f},{p1y:.2f}) and ({p2x:.2f},{p2y:.2f})"
        steps = [f"P_1 = \\left(\\frac{{2 \\cdot {x1} + {x2}}}{{3}}, \\frac{{2 \\cdot {y1} + {y2}}}{{3}}\\right) = ({p1x:.2f}, {p1y:.2f})",
                f"P_2 = \\left(\\frac{{{x1} + 2 \\cdot {x2}}}{{3}}, \\frac{{{y1} + 2 \\cdot {y2}}}{{3}}\\right) = ({p2x:.2f}, {p2y:.2f})"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = DividingLineSegmentsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
