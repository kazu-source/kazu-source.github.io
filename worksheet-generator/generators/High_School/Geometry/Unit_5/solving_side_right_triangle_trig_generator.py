"""
Solving for a Side in Right Triangle Using Trig Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SolvingSideRightTriangleTrigGenerator:
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
        angle = random.choice([30, 45, 60])
        hyp = random.randint(10, 20)
        opp = hyp * math.sin(math.radians(angle))
        latex = f"\\text{{Right triangle: angle }} {angle}^\\circ, \\text{{ hypotenuse }} {hyp}. \\text{{ Find opposite side.}}"
        solution = f"{opp:.2f}"
        steps = [f"\\sin({angle}^\\circ) = \\frac{{\\text{{opp}}}}{{{hyp}}}",
                f"\\text{{opp}} = {hyp} \\times \\sin({angle}^\\circ) = {opp:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        angle = random.randint(25, 65)
        adj = random.randint(8, 16)
        opp = adj * math.tan(math.radians(angle))
        latex = f"\\text{{Right triangle: angle }} {angle}^\\circ, \\text{{ adjacent side }} {adj}. \\text{{ Find opposite side.}}"
        solution = f"{opp:.2f}"
        steps = [f"\\tan({angle}^\\circ) = \\frac{{\\text{{opp}}}}{{{adj}}}",
                f"\\text{{opp}} = {adj} \\times \\tan({angle}^\\circ) = {opp:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        angle = random.randint(30, 60)
        opp = random.randint(10, 20)
        hyp = opp / math.sin(math.radians(angle))
        latex = f"\\text{{Right triangle: angle }} {angle}^\\circ, \\text{{ opposite side }} {opp}. \\text{{ Find hypotenuse.}}"
        solution = f"{hyp:.2f}"
        steps = [f"\\sin({angle}^\\circ) = \\frac{{{opp}}}{{\\text{{hyp}}}}",
                f"\\text{{hyp}} = \\frac{{{opp}}}{{\\sin({angle}^\\circ)}} = {hyp:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        angle1 = random.randint(30, 50)
        angle2 = 90 - angle1
        side = random.randint(12, 20)
        x = side * math.tan(math.radians(angle1))
        latex = f"\\text{{Right triangle with angles }} {angle1}^\\circ \\text{{ and }} {angle2}^\\circ. \\text{{ Side adjacent to }} {angle1}^\\circ \\text{{ is }} {side}. \\text{{ Find other leg.}}"
        solution = f"{x:.2f}"
        steps = [f"\\text{{Other leg is opposite to }} {angle1}^\\circ",
                f"\\tan({angle1}^\\circ) = \\frac{{x}}{{{side}}}",
                f"x = {side} \\times \\tan({angle1}^\\circ) = {x:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = SolvingSideRightTriangleTrigGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
