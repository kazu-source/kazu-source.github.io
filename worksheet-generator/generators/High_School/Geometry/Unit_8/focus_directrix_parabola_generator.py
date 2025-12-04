"""
Focus and Directrix of a Parabola Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class FocusDirectrixParabolaGenerator:
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
        latex = "\\text{Define: What is the focus of a parabola?}"
        solution = "Fixed point that parabola curves around"
        steps = ["\\text{A parabola is set of all points equidistant from focus and directrix}",
                "\\text{Focus is the fixed point inside the curve}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        p = random.randint(2, 6)
        latex = f"\\text{{For parabola }} y = \\frac{{1}}{{4p}}x^2 \\text{{ with }} p = {p}, \\text{{ find focus.}}"
        solution = f"(0, {p})"
        steps = [f"\\text{{For }} y = \\frac{{1}}{{4p}}x^2, \\text{{ focus is at }} (0, p)",
                f"\\text{{Focus: }} (0, {p})"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        p = random.randint(3, 7)
        latex = f"\\text{{Find focus and directrix of }} x^2 = {4*p}y."
        solution = f"Focus (0,{p}), directrix y = {-p}"
        steps = [f"x^2 = 4py \\text{{ where }} 4p = {4*p}",
                f"p = {p}",
                f"\\text{{Focus: }} (0,{p}), \\text{{ directrix: }} y = {-p}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        h, k = random.randint(-3, 3), random.randint(-3, 3)
        p = random.randint(2, 5)
        latex = f"\\text{{Find focus of }} (x - {h})^2 = {4*p}(y - {k})."
        solution = f"({h}, {k + p})"
        steps = [f"\\text{{Vertex: }} ({h},{k})",
                f"4p = {4*p}, \\text{{ so }} p = {p}",
                f"\\text{{Focus: }} ({h}, {k} + {p}) = ({h},{k + p})"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = FocusDirectrixParabolaGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
