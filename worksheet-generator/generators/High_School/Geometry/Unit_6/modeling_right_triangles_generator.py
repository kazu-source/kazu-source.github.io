"""
Modeling with Right Triangles Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ModelingRightTrianglesGenerator:
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
        height = random.randint(20, 40)
        distance = random.randint(15, 30)
        angle = math.degrees(math.atan(height/distance))
        latex = f"\\text{{A ladder reaches }} {height} \\text{{ ft up a wall, base }} {distance} \\text{{ ft from wall. Find angle with ground.}}"
        solution = f"{angle:.1f}°"
        steps = [f"\\tan(\\theta) = \\frac{{{height}}}{{{distance}}}",
                f"\\theta = \\tan^{{-1}}\\left(\\frac{{{height}}}{{{distance}}}\\right) = {angle:.1f}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        angle = random.randint(30, 60)
        base = random.randint(50, 100)
        height = base * math.tan(math.radians(angle))
        latex = f"\\text{{A ramp at }} {angle}^\\circ \\text{{ angle extends }} {base} \\text{{ ft horizontally. Find vertical rise.}}"
        solution = f"{height:.1f} ft"
        steps = [f"\\tan({angle}^\\circ) = \\frac{{h}}{{{base}}}",
                f"h = {base} \\times \\tan({angle}^\\circ) = {height:.1f} \\text{{ ft}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        angle = random.randint(35, 55)
        height = random.randint(100, 200)
        distance = height / math.tan(math.radians(angle))
        latex = f"\\text{{From angle of elevation }} {angle}^\\circ, \\text{{ you see top of }} {height} \\text{{ ft building. How far are you from base?}}"
        solution = f"{distance:.1f} ft"
        steps = [f"\\tan({angle}^\\circ) = \\frac{{{height}}}{{d}}",
                f"d = \\frac{{{height}}}{{\\tan({angle}^\\circ)}} = {distance:.1f} \\text{{ ft}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        angle1 = random.randint(30, 45)
        angle2 = random.randint(50, 65)
        dist = random.randint(40, 80)
        h1 = dist * math.tan(math.radians(angle1))
        h2 = dist * math.tan(math.radians(angle2))
        height_diff = h2 - h1
        latex = f"\\text{{Two observers }} {dist} \\text{{ ft from tower see top at }} {angle1}^\\circ \\text{{ and }} {angle2}^\\circ. \\text{{ They are at different heights. Find difference.}}"
        solution = f"{height_diff:.1f} ft"
        steps = [f"h_1 = {dist} \\times \\tan({angle1}^\\circ) = {h1:.1f}",
                f"h_2 = {dist} \\times \\tan({angle2}^\\circ) = {h2:.1f}",
                f"\\text{{Difference}} = {h2:.1f} - {h1:.1f} = {height_diff:.1f} \\text{{ ft}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ModelingRightTrianglesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
