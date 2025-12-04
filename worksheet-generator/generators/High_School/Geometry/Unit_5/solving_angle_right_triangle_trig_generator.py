"""
Solving for an Angle in Right Triangle Using Trig Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SolvingAngleRightTriangleTrigGenerator:
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
        opp, hyp = 3, 5
        angle = math.degrees(math.asin(opp/hyp))
        latex = f"\\text{{Right triangle: opposite }} {opp}, \\text{{ hypotenuse }} {hyp}. \\text{{ Find the angle.}}"
        solution = f"{angle:.1f}°"
        steps = [f"\\sin(\\theta) = \\frac{{{opp}}}{{{hyp}}}",
                f"\\theta = \\sin^{{-1}}\\left(\\frac{{{opp}}}{{{hyp}}}\\right) = {angle:.1f}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        adj, hyp = random.randint(8, 12), random.randint(14, 18)
        if adj >= hyp:
            adj = hyp - random.randint(2, 5)
        angle = math.degrees(math.acos(adj/hyp))
        latex = f"\\text{{Right triangle: adjacent }} {adj}, \\text{{ hypotenuse }} {hyp}. \\text{{ Find the angle.}}"
        solution = f"{angle:.1f}°"
        steps = [f"\\cos(\\theta) = \\frac{{{adj}}}{{{hyp}}}",
                f"\\theta = \\cos^{{-1}}\\left(\\frac{{{adj}}}{{{hyp}}}\\right) = {angle:.1f}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        opp = random.randint(6, 12)
        adj = random.randint(8, 14)
        angle = math.degrees(math.atan(opp/adj))
        latex = f"\\text{{Right triangle: opposite }} {opp}, \\text{{ adjacent }} {adj}. \\text{{ Find the angle.}}"
        solution = f"{angle:.1f}°"
        steps = [f"\\tan(\\theta) = \\frac{{{opp}}}{{{adj}}}",
                f"\\theta = \\tan^{{-1}}\\left(\\frac{{{opp}}}{{{adj}}}\\right) = {angle:.1f}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a, b, c = 5, 12, 13
        angle_a = math.degrees(math.asin(a/c))
        angle_b = 90 - angle_a
        latex = f"\\text{{Right triangle with sides }} {a}, {b}, {c}. \\text{{ Find both acute angles.}}"
        solution = f"{angle_a:.1f}° and {angle_b:.1f}°"
        steps = [f"\\sin(\\alpha) = \\frac{{{a}}}{{{c}}}, \\quad \\alpha = {angle_a:.1f}^\\circ",
                f"\\beta = 90^\\circ - {angle_a:.1f}^\\circ = {angle_b:.1f}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = SolvingAngleRightTriangleTrigGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
