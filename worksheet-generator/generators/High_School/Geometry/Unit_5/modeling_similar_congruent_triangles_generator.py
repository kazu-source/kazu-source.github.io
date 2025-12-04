"""
Modeling with Similar and Congruent Triangles Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ModelingSimilarCongruentTrianglesGenerator:
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
        height = random.randint(120, 180)
        shadow1 = random.randint(150, 200)
        pole = random.randint(5, 8)
        shadow2 = (pole * shadow1) / height
        latex = f"\\text{{A person }} {height} \\text{{ cm tall casts a shadow }} {shadow1} \\text{{ cm. A pole casts shadow }} {shadow2:.0f} \\text{{ cm. Find pole height.}}"
        solution = f"{pole} m or {pole*100} cm"
        steps = [f"\\frac{{{height}}}{{{shadow1}}} = \\frac{{h}}{{{shadow2:.0f}}}", f"h = {pole*100} \\text{{ cm}} = {pole} \\text{{ m}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        dist1 = random.randint(100, 150)
        height1 = random.randint(30, 50)
        dist2 = random.randint(200, 300)
        height2 = (height1 * dist2) / dist1
        latex = f"\\text{{A ramp rises }} {height1} \\text{{ m over }} {dist1} \\text{{ m. How high does similar ramp rise over }} {dist2} \\text{{ m?}}"
        solution = f"{height2:.1f} m"
        steps = [f"\\frac{{{height1}}}{{{dist1}}} = \\frac{{h}}{{{dist2}}}", f"h = {height2:.1f} \\text{{ m}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        lake_width = random.randint(80, 120)
        d1 = random.randint(20, 40)
        d2 = random.randint(30, 50)
        measured = (lake_width * d1) / d2
        latex = f"\\text{{To measure lake width indirectly, triangulation gives ratio }} {d1}:{d2}. \\text{{ Measured distance }} {measured:.0f} \\text{{ m. Find lake width.}}"
        solution = f"{lake_width} m"
        steps = [f"\\frac{{w}}{{{measured:.0f}}} = \\frac{{{d2}}}{{{d1}}}", f"w = {lake_width} \\text{{ m}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        building = random.randint(40, 80)
        mirror_to_person = random.randint(2, 4)
        mirror_to_building = random.randint(30, 50)
        eye_height = (building * mirror_to_person) / mirror_to_building
        latex = f"\\text{{Using mirror method: mirror is }} {mirror_to_person} \\text{{ m from person, }} {mirror_to_building} \\text{{ m from building. Eye height }} {eye_height:.1f} \\text{{ m. Find building height.}}"
        solution = f"{building} m"
        steps = ["\\text{By similar triangles (angle of incidence = angle of reflection)}",
                f"\\frac{{h}}{{{mirror_to_building}}} = \\frac{{{eye_height:.1f}}}{{{mirror_to_person}}}",
                f"h = {building} \\text{{ m}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ModelingSimilarCongruentTrianglesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
