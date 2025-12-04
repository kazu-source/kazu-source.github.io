"""
Sectors Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SectorsGenerator:
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
        angle = random.choice([60, 90, 120, 180])
        r = random.randint(6, 12)
        area = (angle / 360) * math.pi * r * r
        latex = f"\\text{{Find area of sector: }} \\theta = {angle}^\\circ, r = {r}."
        solution = f"{area:.2f}"
        steps = [f"A = \\frac{{\\theta}}{{360}} \\times \\pi r^2",
                f"= \\frac{{{angle}}}{{360}} \\times \\pi({r})^2 = {area:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        theta = random.choice([math.pi/6, math.pi/4, math.pi/3, math.pi/2])
        r = random.randint(8, 14)
        area = 0.5 * r * r * theta
        theta_str = {math.pi/6: "π/6", math.pi/4: "π/4", math.pi/3: "π/3", math.pi/2: "π/2"}
        latex = f"\\text{{Find sector area: }} \\theta = {theta_str[theta]} \\text{{ rad, }} r = {r}."
        solution = f"{area:.2f}"
        steps = [f"A = \\frac{{1}}{{2}}r^2\\theta = \\frac{{1}}{{2}}({r})^2 \\times {theta_str[theta]}",
                f"= {area:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        angle = random.randint(40, 160)
        r = random.randint(10, 18)
        sector_area = (angle / 360) * math.pi * r * r
        circle_area = math.pi * r * r
        ratio = sector_area / circle_area
        latex = f"\\text{{Sector with }} {angle}^\\circ \\text{{ in circle radius }} {r}. \\text{{ What fraction of circle is sector?}}"
        solution = f"{ratio:.3f} or {angle}/360"
        steps = [f"\\text{{Fraction}} = \\frac{{\\theta}}{{360}} = \\frac{{{angle}}}{{360}} = {ratio:.3f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        r = random.randint(10, 16)
        area = random.randint(50, 120)
        theta_rad = (2 * area) / (r * r)
        theta_deg = theta_rad * 180 / math.pi
        latex = f"\\text{{Sector area }} {area} \\text{{ in circle radius }} {r}. \\text{{ Find central angle in degrees.}}"
        solution = f"{theta_deg:.1f}°"
        steps = [f"A = \\frac{{1}}{{2}}r^2\\theta \\Rightarrow \\theta = \\frac{{2A}}{{r^2}}",
                f"\\theta = \\frac{{2 \\times {area}}}{{{r}^2}} = {theta_rad:.3f} \\text{{ rad}}",
                f"= {theta_deg:.1f}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = SectorsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
