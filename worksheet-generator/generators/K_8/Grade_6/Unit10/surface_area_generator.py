"""Surface Area Generator - Grade 6 Unit 10"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class SurfaceAreaGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        side = random.randint(3, 8)
        sa = 6 * side * side
        latex = f"\\text{{Cube with edge }}{side}\\text{{. Surface area?}}"
        return Equation(latex=latex, solution=f"{sa} \\text{{ sq units}}", steps=[f"6 \\times {side}^2 = {sa}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        l, w, h = random.randint(4, 10), random.randint(3, 8), random.randint(2, 6)
        sa = 2 * (l*w + l*h + w*h)
        latex = f"\\text{{Rectangular prism: }}{l}\\times{w}\\times{h}\\text{{. Surface area?}}"
        return Equation(latex=latex, solution=f"{sa} \\text{{ sq units}}", steps=[f"2({l*w} + {l*h} + {w*h}) = {sa}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        sa = random.randint(90, 200)
        side_sq = sa // 6
        side = int(side_sq ** 0.5)
        if side * side * 6 == sa:
            latex = f"\\text{{Cube surface area is }}{sa}\\text{{. Edge length?}}"
            return Equation(latex=latex, solution=f"{side} \\text{{ units}}", steps=[f"\\sqrt{{{sa} \\div 6}} = {side}"], difficulty='hard')
        else:
            side = random.randint(3, 8)
            sa = 6 * side * side
            latex = f"\\text{{Cube surface area is }}{sa}\\text{{. Edge length?}}"
            return Equation(latex=latex, solution=f"{side} \\text{{ units}}", steps=[f"\\sqrt{{{sa} \\div 6}} = {side}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        l, w, h = random.randint(5, 12), random.randint(4, 10), random.randint(3, 8)
        sa = 2 * (l*w + l*h + w*h)
        latex = f"\\text{{Rectangular prism: length }}{l}\\text{{, width }}{w}\\text{{, height }}{h}\\text{{. Surface area?}}"
        return Equation(latex=latex, solution=f"{sa} \\text{{ sq units}}", steps=[f"2({l}\\times{w} + {l}\\times{h} + {w}\\times{h}) = {sa}"], difficulty='challenge')

def main():
    gen = SurfaceAreaGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
