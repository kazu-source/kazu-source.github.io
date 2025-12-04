"""
Cavalieri's Principle Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class CavalierisPrincipleGenerator:
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
        latex = "\\text{State Cavalieri's Principle.}"
        solution = "If cross-sectional areas at every height are equal, volumes are equal"
        steps = ["\\text{Cavalieri's Principle: Two solids with equal height}",
                "\\text{have equal volume if all parallel cross-sections}",
                "\\text{at equal heights have equal areas}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        r = random.randint(4, 10)
        h = random.randint(8, 15)
        vol_cylinder = math.pi * r * r * h
        latex = f"\\text{{A right cylinder and an oblique cylinder both have radius }} {r} \\text{{ and height }} {h}. "
        latex += "\\text{Compare their volumes using Cavalieri's Principle.}"
        solution = f"Both have volume {vol_cylinder:.2f}"
        steps = ["\\text{By Cavalieri's Principle:}",
                "\\text{At any height, both cross-sections are circles with same radius}",
                f"\\text{{Both volumes}} = \\pi r^2 h = \\pi({r})^2({h}) = {vol_cylinder:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        r = random.randint(5, 10)
        h = random.randint(10, 18)
        vol_cone = (1/3) * math.pi * r * r * h
        vol_pyramid = (1/3) * r * r * h  # square base
        latex = f"\\text{{Use Cavalieri's Principle to explain why cone volume formula is }} \\frac{{1}}{{3}}\\pi r^2 h."
        solution = "Cross-sections proportionally shrink from base to apex"
        steps = ["\\text{At height } x \\text{ from base, radius is } r(1 - x/h)",
                "\\text{Cross-section area} = \\pi [r(1-x/h)]^2",
                "\\text{Integrating from 0 to h gives } \\frac{1}{3}\\pi r^2 h",
                "\\text{Similar to pyramid with square base}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        r = random.randint(6, 12)
        vol_sphere = (4/3) * math.pi * r**3
        vol_cylinder = math.pi * r**2 * (2*r)
        vol_cones = 2 * (1/3) * math.pi * r**2 * r
        vol_diff = vol_cylinder - vol_cones
        latex = f"\\text{{Use Cavalieri's Principle to derive sphere volume. Hint: compare sphere radius }} {r} "
        latex += f"\\text{{to cylinder minus two cones.}}"
        solution = f"V = (4/3)πr³ = {vol_sphere:.2f}"
        steps = [f"\\text{{Cylinder: radius }} {r}, \\text{{ height }} {2*r}, \\text{{ volume }} = {vol_cylinder:.2f}",
                f"\\text{{Two cones: same base/height, volume}} = {vol_cones:.2f}",
                f"\\text{{Difference}} = {vol_diff:.2f}",
                f"\\text{{At height }} y, \\text{{ both have equal cross-sections}}",
                f"\\text{{Therefore sphere volume}} = {vol_sphere:.2f} = \\frac{{4}}{{3}}\\pi({r})^3"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = CavalierisPrincipleGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
