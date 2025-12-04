"""
Proving Relationships Using Similarity Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ProvingRelationshipsSimilarityGenerator:
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
        a1, a2 = random.randint(55, 75), random.randint(60, 80)
        latex = f"\\text{{Two triangles have angles }} {a1}^\\circ, {a2}^\\circ. \\text{{ Prove they are similar.}}"
        solution = "AA similarity - two angles match"
        steps = [f"\\text{{Both triangles have }} {a1}^\\circ \\text{{ and }} {a2}^\\circ", "\\text{By AA, triangles are similar}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        latex = "\\text{Prove that a line parallel to one side of a triangle divides the other two sides proportionally.}"
        solution = "Use AA similarity"
        steps = ["\\text{Let line DE be parallel to BC}", "\\text{Angles ADE = ABC (corresponding)}",
                "\\text{Angle A is common}", "\\text{Triangles ADE and ABC are similar by AA}",
                "\\text{Therefore } \\frac{AD}{AB} = \\frac{AE}{AC}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{In right triangle ABC with altitude to hypotenuse, prove the altitude creates two similar triangles.}"
        solution = "All three triangles are similar"
        steps = ["\\text{Let altitude from C meet AB at D}", "\\text{Triangles ACD and CBD are both right triangles}",
                "\\text{Angle A is common to ABC and ACD}", "\\text{Angle B is common to ABC and CBD}",
                "\\text{All three triangles are similar by AA}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Prove the Pythagorean theorem using similar triangles.}"
        solution = "Use altitude to hypotenuse creating similar triangles"
        steps = ["\\text{Right triangle ABC with altitude CD to hypotenuse AB}",
                "\\text{Triangle ACD ~ ABC and CBD ~ ABC}",
                "\\text{From similarity: } a^2 = c \\cdot m \\text{ and } b^2 = c \\cdot n",
                "\\text{where } m, n \\text{ are segments of hypotenuse}",
                "a^2 + b^2 = c(m + n) = c \\cdot c = c^2"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ProvingRelationshipsSimilarityGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
