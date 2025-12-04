"""
Constructing Circumcircles and Incircles Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ConstructingCircumcirclesIncirclesGenerator:
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
        latex = "\\text{What is the circumcircle of a triangle?}"
        solution = "Circle passing through all three vertices"
        steps = ["\\text{Circumcircle passes through all vertices of triangle}",
                "\\text{Center is circumcenter (intersection of perpendicular bisectors)}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        latex = "\\text{How do you construct the incircle of a triangle?}"
        solution = "Find incenter using angle bisectors, draw perpendicular to side"
        steps = ["\\text{1. Construct angle bisectors of triangle}",
                "\\text{2. Incenter I is where they intersect}",
                "\\text{3. Draw perpendicular from I to any side}",
                "\\text{4. Circle with center I and radius = perpendicular distance}",
                "\\text{5. This incircle is tangent to all three sides}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a, b, c = 6, 8, 10  # Right triangle
        s = (a + b + c) / 2
        area = 0.5 * a * b
        r = area / s
        latex = f"\\text{{Triangle with sides }} {a}, {b}, {c}. \\text{{ Find inradius.}}"
        solution = f"{r}"
        steps = [f"s = \\frac{{{a}+{b}+{c}}}{{2}} = {s}",
                f"\\text{{Area}} = \\frac{{1}}{{2}} \\times {a} \\times {b} = {area}",
                f"r = \\frac{{\\text{{Area}}}}{{s}} = \\frac{{{area}}}{{{s}}} = {r}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a, b, c = 5, 12, 13  # Right triangle
        R = c / 2
        latex = f"\\text{{Triangle with sides }} {a}, {b}, {c}. \\text{{ Find circumradius.}}"
        solution = f"{R}"
        steps = [f"\\text{{This is a right triangle (}} {a}^2 + {b}^2 = {c}^2)",
                "\\text{For right triangles, circumradius = } \\frac{\\text{hypotenuse}}{2}",
                f"R = \\frac{{{c}}}{{2}} = {R}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ConstructingCircumcirclesIncirclesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
