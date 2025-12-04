"""
2D vs 3D Objects Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class TwoDVs3DObjectsGenerator:
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
        shape = random.choice(['cube', 'cylinder', 'sphere', 'cone'])
        cross_sections = {
            'cube': 'square, rectangle, triangle, hexagon',
            'cylinder': 'circle, rectangle',
            'sphere': 'circle',
            'cone': 'circle, ellipse, triangle, parabola'
        }
        latex = f"\\text{{Name a possible cross-section of a {shape}.}}"
        solution = cross_sections[shape]
        steps = [f"\\text{{Possible cross-sections of {shape}:}}",
                f"\\text{{{cross_sections[shape]}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        solid = random.choice(['prism', 'pyramid', 'cylinder', 'cone'])
        latex = f"\\text{{Describe how to obtain a triangular cross-section of a {solid}.}}"
        if solid == 'prism':
            solution = "Cut at an angle through edges"
        elif solid == 'pyramid':
            solution = "Cut parallel to triangular face"
        elif solid == 'cylinder':
            solution = "Cut at an angle through axis"
        else:  # cone
            solution = "Cut through vertex and base"
        steps = [f"\\text{{For {solid}:}}", f"\\text{{{solution}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{What 3D solid is formed by rotating a rectangle around one of its sides?}"
        solution = "Cylinder"
        steps = ["\\text{Rotating a rectangle around a side creates a cylinder}",
                "\\text{The rotating rectangle sweeps out a circular cross-section}",
                "\\text{Height = side of rectangle, radius = other dimension}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{A plane intersects a double cone (two cones joined at vertices). What curves can result?}"
        solution = "Circle, ellipse, parabola, hyperbola (conic sections)"
        steps = ["\\text{These are the conic sections:}",
                "\\text{- Perpendicular to axis: circle}",
                "\\text{- Angled (intersects one cone): ellipse}",
                "\\text{- Parallel to slant: parabola}",
                "\\text{- Steep angle (both cones): hyperbola}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = TwoDVs3DObjectsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
