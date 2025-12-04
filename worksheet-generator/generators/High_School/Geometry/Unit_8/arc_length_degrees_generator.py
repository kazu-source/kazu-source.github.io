"""
Arc Length in Degrees Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ArcLengthDegreesGenerator:
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
        angle = random.choice([60, 90, 120, 180])
        r = random.randint(6, 12)
        arc = (angle / 360) * 2 * math.pi * r
        latex = f"\\text{{Arc with central angle }} {angle}^\\circ \\text{{ in circle radius }} {r}. \\text{{ Find arc length.}}"
        solution = f"{arc:.2f}"
        steps = [f"\\text{{Arc length}} = \\frac{{\\theta}}{{360}} \\times 2\\pi r",
                f"= \\frac{{{angle}}}{{360}} \\times 2\\pi({r}) = {arc:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        angle = random.randint(30, 150)
        r = random.randint(8, 15)
        arc = (angle / 360) * 2 * math.pi * r
        latex = f"\\text{{Find arc length: }} \\theta = {angle}^\\circ, r = {r}."
        solution = f"{arc:.2f}"
        steps = [f"L = \\frac{{{angle}}}{{360}} \\times 2\\pi({r}) = {arc:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        r = random.randint(10, 18)
        arc = random.randint(15, 30)
        angle = (arc / (2 * math.pi * r)) * 360
        latex = f"\\text{{Arc length }} {arc} \\text{{ in circle radius }} {r}. \\text{{ Find central angle.}}"
        solution = f"{angle:.1f}°"
        steps = [f"\\frac{{\\theta}}{{360}} \\times 2\\pi r = {arc}",
                f"\\theta = \\frac{{{arc} \\times 360}}{{2\\pi({r})}} = {angle:.1f}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        angle = random.randint(45, 135)
        arc = random.randint(20, 40)
        r = (arc * 360) / (angle * 2 * math.pi)
        latex = f"\\text{{Arc length }} {arc} \\text{{ with central angle }} {angle}^\\circ. \\text{{ Find radius.}}"
        solution = f"{r:.2f}"
        steps = [f"\\frac{{{angle}}}{{360}} \\times 2\\pi r = {arc}",
                f"r = \\frac{{{arc} \\times 360}}{{{angle} \\times 2\\pi}} = {r:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ArcLengthDegreesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
