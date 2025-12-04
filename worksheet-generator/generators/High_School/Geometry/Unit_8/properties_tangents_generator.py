"""
Properties of Tangents Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class PropertiesTangentsGenerator:
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
        latex = "\\text{What is the relationship between a tangent line and the radius at the point of tangency?}"
        solution = "Perpendicular (90° angle)"
        steps = ["\\text{A tangent line is perpendicular to the radius}",
                "\\text{at the point of tangency}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        r = random.randint(6, 12)
        dist = random.randint(10, 20)
        tangent = math.sqrt(dist**2 - r**2)
        latex = f"\\text{{From external point }} {dist} \\text{{ units from center of circle (radius }} {r}), \\text{{ find tangent length.}}"
        solution = f"{tangent:.2f}"
        steps = ["\\text{Use Pythagorean theorem (tangent } \\perp \\text{ radius)}",
                f"t^2 + {r}^2 = {dist}^2",
                f"t = \\sqrt{{{dist**2} - {r**2}}} = {tangent:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        t1 = random.randint(8, 15)
        latex = f"\\text{{Two tangent segments from external point have lengths }} {t1} \\text{{ and }} x. \\text{{ Find }} x."
        solution = f"{t1}"
        steps = ["\\text{Two tangent segments from same external point are congruent}",
                f"x = {t1}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Prove: Two tangent segments from an external point to a circle are congruent.}"
        solution = "Use congruent right triangles"
        steps = ["\\text{Let P be external point, A and B be points of tangency}",
                "\\text{OA } \\perp \\text{ PA and OB } \\perp \\text{ PB (tangent } \\perp \\text{ radius)}",
                "\\text{In right triangles OAP and OBP:}",
                "OP = OP \\text{ (common)}, OA = OB \\text{ (radii)}",
                "\\text{By HL theorem, triangles are congruent}",
                "\\text{Therefore PA} = \\text{PB (CPCTC)}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = PropertiesTangentsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
