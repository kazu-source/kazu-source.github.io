"""Nets of 3D Figures Generator - Grade 6 Unit 10"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class NetsOf3dFiguresGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        latex = f"\\text{{How many squares are in the net of a cube?}}"
        return Equation(latex=latex, solution="6", steps=["Cube has 6 faces, so 6 squares"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        latex = f"\\text{{A net has 2 triangles and 3 rectangles. What 3D shape?}}"
        return Equation(latex=latex, solution="Triangular prism", steps=["Triangular prism"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        l, w, h = random.randint(3, 8), random.randint(2, 6), random.randint(2, 5)
        faces = [l*w, l*w, l*h, l*h, w*h, w*h]
        total_area = sum(faces)
        latex = f"\\text{{Rectangular prism net: }}{l}\\times{w}\\times{h}\\text{{. Total area of net?}}"
        return Equation(latex=latex, solution=f"{total_area} \\text{{ sq units}}", steps=[f"2({l*w} + {l*h} + {w*h}) = {total_area}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        latex = f"\\text{{What 3D shape has a net with 1 circle and 1 sector (pie slice)?}}"
        return Equation(latex=latex, solution="Cone", steps=["Cone"], difficulty='challenge')

def main():
    gen = NetsOf3dFiguresGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
