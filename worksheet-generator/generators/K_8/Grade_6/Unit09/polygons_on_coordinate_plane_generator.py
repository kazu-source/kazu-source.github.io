"""Polygons on Coordinate Plane Generator - Grade 6 Unit 9"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class PolygonsOnCoordinatePlaneGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x, y, w, h = random.randint(1, 5), random.randint(1, 5), random.randint(3, 6), random.randint(3, 6)
        perimeter = 2 * (w + h)
        latex = f"\\text{{Rectangle vertices: }}({x},{y}), ({x+w},{y}), ({x+w},{y+h}), ({x},{y+h})\\text{{. Perimeter?}}"
        return Equation(latex=latex, solution=f"{perimeter} \\text{{ units}}", steps=[f"2({w} + {h}) = {perimeter}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        x, y, w, h = random.randint(-5, 5), random.randint(-5, 5), random.randint(4, 8), random.randint(4, 8)
        area = w * h
        latex = f"\\text{{Rectangle: }}({x},{y}), ({x+w},{y}), ({x+w},{y+h}), ({x},{y+h})\\text{{. Area?}}"
        return Equation(latex=latex, solution=f"{area} \\text{{ sq units}}", steps=[f"{w} \\times {h} = {area}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x, y, base, height = random.randint(-6, 6), random.randint(-6, 6), random.randint(4, 10) * 2, random.randint(3, 8)
        area = (base * height) // 2
        latex = f"\\text{{Triangle vertices: }}({x},{y}), ({x+base},{y}), ({x+base//2},{y+height})\\text{{. Area?}}"
        return Equation(latex=latex, solution=f"{area} \\text{{ sq units}}", steps=[f"\\frac{1}{2} \\times {base} \\times {height} = {area}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        x, y = random.randint(-4, 4), random.randint(-4, 4)
        side = random.randint(5, 10)
        perimeter = 4 * side
        latex = f"\\text{{Square with one vertex at }}({x},{y})\\text{{ and side }}{side}\\text{{. Perimeter?}}"
        return Equation(latex=latex, solution=f"{perimeter} \\text{{ units}}", steps=[f"4 \\times {side} = {perimeter}"], difficulty='challenge')

def main():
    gen = PolygonsOnCoordinatePlaneGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
