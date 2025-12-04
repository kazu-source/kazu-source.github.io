"""
Solving Similar and Congruent Triangles Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SolvingSimilarCongruentTrianglesGenerator:
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
        s1, s2, s3 = random.randint(6, 10), random.randint(7, 11), random.randint(8, 12)
        latex = f"\\text{{If }} \\triangle ABC \\cong \\triangle DEF \\text{{ and AB = }} {s1}, \\text{{ what is DE?}}"
        solution = f"{s1}"
        steps = ["\\text{Congruent triangles have equal corresponding parts}", f"DE = AB = {s1}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        s1 = random.randint(5, 10)
        k = random.choice([2, 3, 4])
        s2 = s1 * k
        x = random.randint(6, 12)
        y = x * k
        latex = f"\\text{{Similar triangles with sides }} {s1} \\text{{ and }} {s2}. \\text{{ If one side is }} {x} \\text{{ in smaller, find corresponding side.}}"
        solution = f"{y}"
        steps = [f"k = \\frac{{{s2}}}{{{s1}}} = {k}", f"\\text{{Corresponding side}} = {x} \\times {k} = {y}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        s1, s2 = random.randint(8, 14), random.randint(10, 16)
        t1 = random.randint(12, 20)
        t2 = (s2 * t1) / s1
        latex = f"\\text{{Two similar triangles have corresponding sides }} {s1} \\text{{ and }} {t1}. \\text{{ If another side is }} {s2}, \\text{{ find its corresponding side.}}"
        solution = f"{t2:.1f}"
        steps = [f"k = \\frac{{{t1}}}{{{s1}}} = {t1/s1:.2f}", f"\\text{{Corresponding}} = {s2} \\times {t1/s1:.2f} = {t2:.1f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        h1 = random.randint(6, 12)
        k = random.choice([2, 3])
        h2 = h1 * k
        latex = f"\\text{{Two similar triangles have altitudes }} {h1} \\text{{ and }} {h2}. \\text{{ If the smaller has area 20, find area of larger.}}"
        area = 20 * k * k
        solution = f"{area}"
        steps = [f"k = \\frac{{{h2}}}{{{h1}}} = {k}", f"\\text{{Area ratio}} = {k}^2 = {k*k}", f"\\text{{Area}} = 20 \\times {k*k} = {area}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = SolvingSimilarCongruentTrianglesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
