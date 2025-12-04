"""
Ratios in Right Triangles Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class RatiosInRightTrianglesGenerator:
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
        a, b, c = 3, 4, 5
        latex = f"\\text{{In a }} {a}-{b}-{c} \\text{{ right triangle, find sin of the smallest angle.}}"
        solution = f"{a}/{c}"
        steps = [f"\\text{{Smallest angle is opposite shortest side }} ({a})",
                f"\\sin(\\theta) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}} = \\frac{{{a}}}{{{c}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a, b, c = 5, 12, 13
        latex = f"\\text{{In right triangle with legs }} {a}, {b} \\text{{ and hypotenuse }} {c}, \\text{{ find cos of larger acute angle.}}"
        solution = f"{a}/{c}"
        steps = ["\\text{Larger acute angle is opposite longer leg}",
                f"\\text{{But we want cos, so use adjacent leg}}: \\frac{{{a}}}{{{c}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{In a right triangle, the altitude to the hypotenuse creates two smaller triangles. Prove they are similar to the original.}"
        solution = "All three triangles share acute angles"
        steps = ["\\text{Let altitude from C meet hypotenuse AB at D}",
                "\\text{Triangle ACD has right angle at D, acute angle at A}",
                "\\text{Triangle CBD has right angle at D, acute angle at B}",
                "\\text{Original triangle ABC has acute angles A and B}",
                "\\text{By AA similarity, all three triangles are similar}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        h = random.randint(8, 15)
        latex = f"\\text{{In right triangle, altitude to hypotenuse is }} {h}. \\text{{ If it divides hypotenuse into segments 6 and 8, find the legs.}}"
        import math
        leg1 = math.sqrt(6 * (6+8))
        leg2 = math.sqrt(8 * (6+8))
        solution = f"{leg1:.1f} and {leg2:.1f}"
        steps = ["\\text{Use geometric mean: } a^2 = m \\cdot c \\text{ and } b^2 = n \\cdot c",
                f"a^2 = 6 \\times 14 = 84, \\quad a = {leg1:.1f}",
                f"b^2 = 8 \\times 14 = 112, \\quad b = {leg2:.1f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = RatiosInRightTrianglesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
