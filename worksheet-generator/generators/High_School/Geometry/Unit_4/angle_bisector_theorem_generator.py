"""
Angle Bisector Theorem Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class AngleBisectorTheoremGenerator:
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
        latex = "\\text{State the Angle Bisector Theorem.}"
        solution = "Angle bisector divides opposite side in ratio of adjacent sides"
        steps = ["\\text{In triangle ABC, if AD bisects angle A}",
                "\\frac{BD}{DC} = \\frac{AB}{AC}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        ab, ac = random.randint(6, 12), random.randint(8, 14)
        bd = random.randint(3, 7)
        dc = (ac * bd) / ab
        latex = f"\\text{{In triangle ABC, AB = }} {ab}, \\text{{ AC = }} {ac}. \\text{{ Angle bisector from A creates BD = }} {bd}. \\text{{ Find DC.}}"
        solution = f"{dc:.2f}"
        steps = [f"\\frac{{BD}}{{DC}} = \\frac{{AB}}{{AC}} = \\frac{{{ab}}}{{{ac}}}",
                f"DC = \\frac{{{ac} \\times {bd}}}{{{ab}}} = {dc:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        ab = random.randint(8, 14)
        ac = random.randint(10, 16)
        bc = random.randint(12, 20)
        bd = (ab * bc) / (ab + ac)
        dc = bc - bd
        latex = f"\\text{{Triangle ABC: AB = }} {ab}, \\text{{ AC = }} {ac}, \\text{{ BC = }} {bc}. \\text{{ Angle bisector from A divides BC. Find BD and DC.}}"
        solution = f"BD = {bd:.2f}, DC = {dc:.2f}"
        steps = [f"BD + DC = {bc}", f"\\frac{{BD}}{{DC}} = \\frac{{{ab}}}{{{ac}}}",
                f"BD = {bd:.2f}, DC = {dc:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Prove the Angle Bisector Theorem using similar triangles.}"
        solution = "Construct parallel to bisector through vertex"
        steps = ["\\text{Draw line through C parallel to AD (bisector)}",
                "\\text{Extend AB to meet this line at E}",
                "\\text{By alternate interior angles, angle CAE = angle DAC}",
                "\\text{Triangle ACE is isosceles, so AE = AC}",
                "\\text{By similar triangles: } \\frac{BD}{DC} = \\frac{AB}{AE} = \\frac{AB}{AC}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = AngleBisectorTheoremGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
