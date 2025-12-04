"""
Constructing a Line Tangent to a Circle Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ConstructingLineTangentCircleGenerator:
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
        latex = "\\text{What angle does a tangent line make with the radius at the point of tangency?}"
        solution = "90° (perpendicular)"
        steps = ["\\text{A tangent line is perpendicular to the radius}",
                "\\text{at the point where it touches the circle}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        latex = "\\text{Describe how to construct a tangent to a circle at a given point on the circle.}"
        solution = "Draw radius, then perpendicular at endpoint"
        steps = ["\\text{1. Draw radius from center O to point P on circle}",
                "\\text{2. Construct perpendicular to OP at point P}",
                "\\text{3. This perpendicular is the tangent line}",
                "\\text{(Tangent is perpendicular to radius)}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Describe how to construct a tangent to a circle from an external point.}"
        solution = "Connect to center, find midpoint, draw circle, find intersections"
        steps = ["\\text{1. Let P be external point, O be center}",
                "\\text{2. Draw segment OP and find its midpoint M}",
                "\\text{3. Draw circle with center M and radius MP}",
                "\\text{4. This circle intersects original circle at two points}",
                "\\text{5. Lines from P to these points are tangents}",
                "\\text{(Uses right angle in semicircle)}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Prove: The construction from external point creates tangent lines using the perpendicularity property.}"
        solution = "Angle in semicircle is 90°, making PA perpendicular to OA"
        steps = ["\\text{Let P be external point, O center, A point where circles intersect}",
                "\\text{Circle with diameter OP means } \\angle OAP = 90^\\circ",
                "\\text{(angle in semicircle)}",
                "OA \\text{ is radius, PA makes } 90^\\circ \\text{ with it}",
                "\\text{Therefore PA is tangent (perpendicular to radius)}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ConstructingLineTangentCircleGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
