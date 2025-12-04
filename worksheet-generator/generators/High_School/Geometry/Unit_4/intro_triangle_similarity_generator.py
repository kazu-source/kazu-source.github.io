"""
Intro to Triangle Similarity Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class IntroTriangleSimilarityGenerator:
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
        a1, a2 = random.randint(50, 70), random.randint(60, 80)
        a3 = 180 - a1 - a2
        latex = f"\\text{{Triangles with angles }} {a1}^\\circ, {a2}^\\circ, {a3}^\\circ \\text{{ and }} {a1}^\\circ, {a2}^\\circ, {a3}^\\circ \\text{{ are similar by which criterion?}}"
        solution = "AA (Angle-Angle)"
        steps = ["\\text{Two angles match}", "\\text{By AA criterion, triangles are similar}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        s1, s2, s3 = 5, 7, 9
        k = random.choice([2, 3])
        t1, t2, t3 = s1*k, s2*k, s3*k
        latex = f"\\text{{Triangle ABC: }} {s1}, {s2}, {s3}. \\text{{ Triangle DEF: }} {t1}, {t2}, {t3}. \\text{{ Similar?}}"
        solution = f"Yes, scale factor {k}"
        steps = [f"\\text{{All ratios equal }} {k}", "\\text{By SSS similarity}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        s1 = random.randint(6, 12)
        s2 = random.randint(8, 14)
        x = random.randint(3, 7)
        latex = f"\\text{{Similar triangles with sides }} {s1}, {s2} \\text{{ and }} {s1+x}, \\text{{ find fourth side.}}"
        k = (s1 + x) / s1
        s2_new = s2 * k
        solution = f"{s2_new:.1f}"
        steps = [f"k = {k:.2f}", f"\\text{{Fourth side}} = {s2} \\times {k:.2f} = {s2_new:.1f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Prove AA similarity criterion using transformations.}"
        solution = "Use dilation and rotation to map one triangle to another"
        steps = ["\\text{Given two angles equal}", "\\text{Third angle must also be equal (angle sum)}",
                "\\text{Use rotation to align angles}", "\\text{Use dilation to match side lengths}",
                "\\text{Triangles map to each other, thus similar}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = IntroTriangleSimilarityGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
