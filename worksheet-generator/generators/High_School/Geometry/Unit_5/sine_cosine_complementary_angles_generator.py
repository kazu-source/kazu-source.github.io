"""
Sine and Cosine of Complementary Angles Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SineCosineComplementaryAnglesGenerator:
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
        angle = random.randint(20, 70)
        comp = 90 - angle
        latex = f"\\text{{If }} \\sin({angle}^\\circ) = x, \\text{{ what is }} \\cos({comp}^\\circ)?"
        solution = "x"
        steps = [f"\\text{{Complementary angles: }} {angle}^\\circ + {comp}^\\circ = 90^\\circ",
                f"\\sin({angle}^\\circ) = \\cos({comp}^\\circ)",
                "\\text{Therefore, answer is } x"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        angle = random.randint(25, 65)
        comp = 90 - angle
        latex = f"\\text{{Verify that }} \\sin({angle}^\\circ) = \\cos({comp}^\\circ) \\text{{ using a right triangle.}}"
        solution = "Both equal opposite/hypotenuse in complementary triangles"
        steps = [f"\\text{{In right triangle with angle }} {angle}^\\circ:",
                f"\\sin({angle}^\\circ) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}}",
                f"\\text{{Other acute angle is }} {comp}^\\circ",
                f"\\cos({comp}^\\circ) = \\frac{{\\text{{adjacent to }} {comp}^\\circ}}{{\\text{{hypotenuse}}}}",
                f"\\text{{Adjacent to }} {comp}^\\circ \\text{{ = opposite to }} {angle}^\\circ",
                f"\\text{{Therefore }} \\sin({angle}^\\circ) = \\cos({comp}^\\circ)"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        angle = random.randint(30, 60)
        comp = 90 - angle
        val = math.sin(math.radians(angle))
        latex = f"\\text{{If }} \\sin({angle}^\\circ) = {val:.3f}, \\text{{ find }} \\cos({comp}^\\circ) \\text{{ and }} \\sin({comp}^\\circ)."
        sin_comp = math.sin(math.radians(comp))
        solution = f"cos({comp}°) = {val:.3f}, sin({comp}°) = {sin_comp:.3f}"
        steps = [f"\\cos({comp}^\\circ) = \\sin({angle}^\\circ) = {val:.3f}",
                f"\\sin({comp}^\\circ) = \\cos({angle}^\\circ) = {sin_comp:.3f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Prove the cofunction identity: } \\sin(\\theta) = \\cos(90^\\circ - \\theta)."
        solution = "Use right triangle and definition of complementary angles"
        steps = ["\\text{In right triangle with angle } \\theta:",
                "\\sin(\\theta) = \\frac{a}{c} \\text{ where } a \\text{ is opposite, } c \\text{ is hypotenuse}",
                "\\text{The other acute angle is } 90^\\circ - \\theta",
                "\\cos(90^\\circ - \\theta) = \\frac{\\text{adjacent to } (90^\\circ - \\theta)}{c}",
                "\\text{Adjacent to } (90^\\circ - \\theta) \\text{ is opposite to } \\theta \\text{, which is } a",
                "\\text{Therefore } \\sin(\\theta) = \\frac{a}{c} = \\cos(90^\\circ - \\theta)"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = SineCosineComplementaryAnglesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
