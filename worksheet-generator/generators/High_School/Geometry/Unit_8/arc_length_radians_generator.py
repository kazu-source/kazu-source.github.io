"""
Arc Length in Radians Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ArcLengthRadiansGenerator:
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
        theta = random.choice([math.pi/6, math.pi/4, math.pi/3, math.pi/2])
        r = random.randint(6, 12)
        arc = r * theta
        theta_str = {math.pi/6: "π/6", math.pi/4: "π/4", math.pi/3: "π/3", math.pi/2: "π/2"}
        latex = f"\\text{{Arc length with }} \\theta = {theta_str[theta]} \\text{{ rad, }} r = {r}."
        solution = f"{arc:.2f}"
        steps = [f"s = r\\theta = {r} \\times {theta_str[theta]} = {arc:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        theta = random.uniform(1, 3)
        r = random.randint(8, 15)
        arc = r * theta
        latex = f"\\text{{Find arc length: }} \\theta = {theta:.2f} \\text{{ rad, }} r = {r}."
        solution = f"{arc:.2f}"
        steps = [f"s = r\\theta = {r} \\times {theta:.2f} = {arc:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        r = random.randint(10, 20)
        arc = random.randint(15, 35)
        theta = arc / r
        latex = f"\\text{{Arc length }} {arc} \\text{{ in circle radius }} {r}. \\text{{ Find }} \\theta \\text{{ in radians.}}"
        solution = f"{theta:.3f} rad"
        steps = [f"s = r\\theta \\Rightarrow \\theta = \\frac{{s}}{{r}}",
                f"\\theta = \\frac{{{arc}}}{{{r}}} = {theta:.3f} \\text{{ rad}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        theta = random.uniform(0.8, 2.5)
        arc = random.randint(20, 45)
        r = arc / theta
        latex = f"\\text{{Arc length }} {arc} \\text{{ with central angle }} {theta:.2f} \\text{{ rad. Find radius.}}"
        solution = f"{r:.2f}"
        steps = [f"s = r\\theta \\Rightarrow r = \\frac{{s}}{{\\theta}}",
                f"r = \\frac{{{arc}}}{{{theta:.2f}}} = {r:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ArcLengthRadiansGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
