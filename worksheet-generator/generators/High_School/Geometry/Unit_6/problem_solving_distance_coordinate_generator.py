"""
Problem Solving with Distance on the Coordinate Plane Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ProblemSolvingDistanceCoordinateGenerator:
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
        x1, y1 = random.randint(1, 6), random.randint(1, 6)
        x2, y2 = random.randint(7, 12), random.randint(7, 12)
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        latex = f"\\text{{Find distance between }} ({x1},{y1}) \\text{{ and }} ({x2},{y2})."
        solution = f"{dist:.2f}"
        steps = [f"d = \\sqrt{{({x2}-{x1})^2 + ({y2}-{y1})^2}}",
                f"d = \\sqrt{{{(x2-x1)**2} + {(y2-y1)**2}}} = \\sqrt{{{(x2-x1)**2 + (y2-y1)**2}}} = {dist:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x1, y1 = 0, 0
        x2, y2 = random.randint(6, 12), random.randint(8, 15)
        dist = math.sqrt(x2**2 + y2**2)
        latex = f"\\text{{A point }} ({x2},{y2}) \\text{{ is how far from the origin?}}"
        solution = f"{dist:.2f}"
        steps = [f"d = \\sqrt{{{x2}^2 + {y2}^2}}",
                f"d = \\sqrt{{{x2**2} + {y2**2}}} = {dist:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(2, 6), random.randint(2, 6)
        x2, y2 = random.randint(8, 14), random.randint(8, 14)
        x3, y3 = random.randint(2, 6), random.randint(8, 14)
        d1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        d2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
        d3 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
        perim = d1 + d2 + d3
        latex = f"\\text{{Find perimeter of triangle with vertices }} ({x1},{y1}), ({x2},{y2}), ({x3},{y3})."
        solution = f"{perim:.2f}"
        steps = [f"d_1 = \\sqrt{{({x2}-{x1})^2 + ({y2}-{y1})^2}} = {d1:.2f}",
                f"d_2 = \\sqrt{{({x3}-{x2})^2 + ({y3}-{y2})^2}} = {d2:.2f}",
                f"d_3 = \\sqrt{{({x3}-{x1})^2 + ({y3}-{y1})^2}} = {d3:.2f}",
                f"\\text{{Perimeter}} = {d1:.2f} + {d2:.2f} + {d3:.2f} = {perim:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Circle problem
        h, k = random.randint(3, 8), random.randint(3, 8)
        r = random.randint(4, 10)
        x, y = random.randint(0, 5), random.randint(0, 5)
        dist = math.sqrt((x - h)**2 + (y - k)**2)
        on_circle = abs(dist - r) < 0.1
        latex = f"\\text{{Is point }} ({x},{y}) \\text{{ on circle with center }} ({h},{k}) \\text{{ and radius }} {r}?"
        solution = "Yes" if on_circle else "No"
        steps = [f"\\text{{Distance from }} ({x},{y}) \\text{{ to }} ({h},{k}):",
                f"d = \\sqrt{{({x}-{h})^2 + ({y}-{k})^2}} = {dist:.2f}",
                f"\\text{{Radius}} = {r}",
                f"\\text{{Since }} {dist:.2f} {'=' if on_circle else '\\neq'} {r}, \\text{{ answer is {solution}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ProblemSolvingDistanceCoordinateGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
