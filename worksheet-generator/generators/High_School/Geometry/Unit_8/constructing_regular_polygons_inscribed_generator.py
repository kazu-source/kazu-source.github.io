"""
Constructing Regular Polygons Inscribed in Circles Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ConstructingRegularPolygonsInscribedGenerator:
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
        n = random.choice([3, 4, 6, 8])
        angle = 360 / n
        latex = f"\\text{{What is the central angle for a regular {n}-gon inscribed in a circle?}}"
        solution = f"{angle}°"
        steps = [f"\\text{{Central angle}} = \\frac{{360^\\circ}}{{{n}}} = {angle}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        n = random.choice([5, 6, 8])
        interior = ((n - 2) * 180) / n
        latex = f"\\text{{Find interior angle of regular {n}-gon.}}"
        solution = f"{interior}°"
        steps = [f"\\text{{Interior angle}} = \\frac{{(n-2) \\times 180^\\circ}}{{n}}",
                f"= \\frac{{({n}-2) \\times 180^\\circ}}{{{n}}} = {interior}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        n = random.choice([6, 8, 12])
        r = random.randint(8, 15)
        central = 360 / n
        central_rad = math.radians(central)
        side = 2 * r * math.sin(central_rad / 2)
        latex = f"\\text{{Regular {n}-gon inscribed in circle radius }} {r}. \\text{{ Find side length.}}"
        solution = f"{side:.2f}"
        steps = [f"\\text{{Central angle}} = \\frac{{360^\\circ}}{{{n}}} = {central}^\\circ",
                f"\\text{{Side}} = 2r\\sin\\left(\\frac{{\\theta}}{{2}}\\right)",
                f"= 2({r})\\sin({central/2}^\\circ) = {side:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Describe how to construct a regular hexagon inscribed in a circle using compass and straightedge.}"
        solution = "Use radius to mark 6 equal arcs around circle"
        steps = ["\\text{1. Draw circle with center O}",
                "\\text{2. Mark point A on circle}",
                "\\text{3. With compass set to radius, mark arc from A to get B}",
                "\\text{4. Repeat from B to get C, then D, E, F}",
                "\\text{5. Connect consecutive points to form hexagon}",
                "\\text{Works because radius = side length for hexagon}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ConstructingRegularPolygonsInscribedGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
