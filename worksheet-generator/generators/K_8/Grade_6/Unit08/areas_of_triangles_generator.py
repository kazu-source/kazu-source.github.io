"""Areas of Triangles Generator - Grade 6 Unit 8"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class AreasOfTrianglesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        base, height = random.randint(4, 12) * 2, random.randint(3, 10)
        area = (base * height) // 2
        latex = f"\\text{{Triangle: base = }}{base}\\text{{, height = }}{height}\\text{{. Area?}}"
        return Equation(latex=latex, solution=f"{area} \\text{{ square units}}", steps=[f"\\frac{1}{2} \\times {base} \\times {height} = {area}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        base, height = random.randint(6, 16) * 2, random.randint(5, 12)
        area = (base * height) // 2
        latex = f"\\text{{Find area: base }}{base}\\text{{ cm, height }}{height}\\text{{ cm}}"
        return Equation(latex=latex, solution=f"{area} \\text{{ cm}}^2", steps=[f"A = \\frac{1}{2} \\times {base} \\times {height} = {area}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        area = random.randint(20, 80)
        base = random.randint(4, 12)
        height = (2 * area) // base
        if (2 * area) % base != 0:
            area = (base * random.randint(5, 12)) // 2
            height = (2 * area) // base
        latex = f"\\text{{Triangle area is }}{area}\\text{{ sq units, base is }}{base}\\text{{. Height?}}"
        return Equation(latex=latex, solution=f"{height} \\text{{ units}}", steps=[f"h = 2 \\times {area} \\div {base} = {height}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        base, height = round(random.uniform(6.0, 14.0), 1), round(random.uniform(4.0, 10.0), 1)
        area = round((base * height) / 2, 1)
        latex = f"\\text{{Triangle: base }}{base}\\text{{ m, height }}{height}\\text{{ m. Area?}}"
        return Equation(latex=latex, solution=f"{area} \\text{{ m}}^2", steps=[f"\\frac{1}{2} \\times {base} \\times {height} = {area}"], difficulty='challenge')

def main():
    gen = AreasOfTrianglesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
