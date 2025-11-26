"""Geometric Solids 3D Shapes Generator - Grade 6 Unit 10"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class GeometricSolids3dShapesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        faces = random.choice([("cube", 6), ("rectangular prism", 6)])
        latex = f"\\text{{How many faces does a {faces[0]} have?}}"
        return Equation(latex=latex, solution=str(faces[1]), steps=[f"{faces[0]}: {faces[1]} faces"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        shape = random.choice([("triangular prism", 5, 9), ("rectangular pyramid", 5, 8)])
        latex = f"\\text{{How many faces and edges does a {shape[0]} have?}}"
        return Equation(latex=latex, solution=f"{shape[1]} faces, {shape[2]} edges", steps=[f"{shape[0]}: {shape[1]} faces, {shape[2]} edges"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        latex = f"\\text{{What 3D shape has 1 circular base and 1 vertex?}}"
        return Equation(latex=latex, solution="Cone", steps=["Cone"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        latex = f"\\text{{How many vertices does a rectangular prism have?}}"
        return Equation(latex=latex, solution="8", steps=["Rectangular prism: 8 vertices"], difficulty='challenge')

def main():
    gen = GeometricSolids3dShapesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
