"""
Intro to Radians Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class IntroRadiansGenerator:
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
        degrees = random.choice([30, 45, 60, 90, 180])
        rads = degrees * math.pi / 180
        latex = f"\\text{{Convert }} {degrees}^\\circ \\text{{ to radians.}}"
        solution = f"{rads:.3f} rad or {degrees}π/180"
        steps = [f"\\text{{radians}} = \\text{{degrees}} \\times \\frac{{\\pi}}{{180}}",
                f"= {degrees} \\times \\frac{{\\pi}}{{180}} = {rads:.3f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        rads = random.choice([math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi])
        degrees = rads * 180 / math.pi
        rad_str = {math.pi/6: "π/6", math.pi/4: "π/4", math.pi/3: "π/3", math.pi/2: "π/2", math.pi: "π"}
        latex = f"\\text{{Convert }} {rad_str.get(rads, f'{rads:.3f}')} \\text{{ radians to degrees.}}"
        solution = f"{degrees:.0f}°"
        steps = [f"\\text{{degrees}} = \\text{{radians}} \\times \\frac{{180}}{{\\pi}}",
                f"= {rad_str.get(rads, f'{rads:.3f}')} \\times \\frac{{180}}{{\\pi}} = {degrees:.0f}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        degrees = random.randint(10, 170)
        rads = degrees * math.pi / 180
        latex = f"\\text{{Convert }} {degrees}^\\circ \\text{{ to radians (exact and decimal).}}"
        solution = f"{degrees}π/180 ≈ {rads:.4f} rad"
        steps = [f"= {degrees} \\times \\frac{{\\pi}}{{180}} = \\frac{{{degrees}\\pi}}{{180}}",
                f"\\approx {rads:.4f} \\text{{ rad}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{How many radians are in a full circle? Explain.}"
        solution = "2π radians"
        steps = ["\\text{Full circle} = 360^\\circ",
                "360^\\circ \\times \\frac{\\pi}{180} = 2\\pi \\text{ radians}",
                "\\text{Alternatively: circumference/radius} = 2\\pi r / r = 2\\pi"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = IntroRadiansGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
