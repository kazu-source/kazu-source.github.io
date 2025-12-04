"""
Inscribed Shapes Problem Solving Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class InscribedShapesProblemSolvingGenerator:
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
        a1 = random.randint(60, 100)
        a2 = 180 - a1
        latex = f"\\text{{Quadrilateral inscribed in circle has one angle }} {a1}^\\circ. \\text{{ Find opposite angle.}}"
        solution = f"{a2}°"
        steps = ["\\text{In inscribed quadrilateral, opposite angles are supplementary}",
                f"{a1}^\\circ + \\angle = 180^\\circ",
                f"\\angle = {a2}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        side = random.randint(6, 12)
        area_square = side * side
        r = (side * math.sqrt(2)) / 2
        area_circle = math.pi * r * r
        latex = f"\\text{{Square with side }} {side} \\text{{ inscribed in circle. Find circle area.}}"
        solution = f"{area_circle:.2f}"
        steps = [f"\\text{{Diagonal of square}} = {side}\\sqrt{{2}}",
                f"\\text{{Diagonal = diameter, so }} r = \\frac{{{side}\\sqrt{{2}}}}{{2}}",
                f"A = \\pi r^2 = {area_circle:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        side = random.randint(8, 16)
        r = side * math.sqrt(3) / 3
        latex = f"\\text{{Equilateral triangle with side }} {side} \\text{{ inscribed in circle. Find radius.}}"
        solution = f"{r:.2f}"
        steps = [f"\\text{{For equilateral triangle, }} r = \\frac{{s}}{{\\sqrt{{3}}}}",
                f"r = \\frac{{{side}}}{{\\sqrt{{3}}}} = \\frac{{{side}\\sqrt{{3}}}}{{3}} = {r:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        r = random.randint(8, 14)
        side = r * math.sqrt(2)
        area = side * side
        latex = f"\\text{{Circle has radius }} {r}. \\text{{ Find area of inscribed square.}}"
        solution = f"{area:.2f}"
        steps = [f"\\text{{Diagonal of square}} = 2r = {2*r}",
                f"\\text{{Side}} = \\frac{{2r}}{{\\sqrt{{2}}}} = r\\sqrt{{2}} = {side:.2f}",
                f"\\text{{Area}} = s^2 = {area:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = InscribedShapesProblemSolvingGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
