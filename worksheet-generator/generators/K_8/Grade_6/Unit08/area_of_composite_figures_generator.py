"""Area of Composite Figures Generator - Grade 6 Unit 8"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class AreaOfCompositeFiguresGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        w1, h1 = random.randint(4, 10), random.randint(3, 8)
        w2, h2 = random.randint(3, 8), random.randint(2, 6)
        area = w1 * h1 + w2 * h2
        latex = f"\\text{{Two rectangles: }}{w1}\\times{h1}\\text{{ and }}{w2}\\times{h2}\\text{{. Total area?}}"
        return Equation(latex=latex, solution=f"{area} \\text{{ sq units}}", steps=[f"{w1*h1} + {w2*h2} = {area}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        rect_w, rect_h = random.randint(8, 14), random.randint(6, 12)
        tri_b, tri_h = random.randint(4, 10) * 2, random.randint(3, 8)
        area = rect_w * rect_h + (tri_b * tri_h) // 2
        latex = f"\\text{{Rectangle }}{rect_w}\\times{rect_h}\\text{{ + triangle (b={tri_b}, h={tri_h}). Total area?}}"
        return Equation(latex=latex, solution=f"{area} \\text{{ sq units}}", steps=[f"{rect_w*rect_h} + {(tri_b*tri_h)//2} = {area}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        large_w, large_h = random.randint(10, 15), random.randint(8, 12)
        small_w, small_h = random.randint(3, 6), random.randint(2, 5)
        area = large_w * large_h - small_w * small_h
        latex = f"\\text{{Rectangle }}{large_w}\\times{large_h}\\text{{ with }}{small_w}\\times{small_h}\\text{{ cutout. Area?}}"
        return Equation(latex=latex, solution=f"{area} \\text{{ sq units}}", steps=[f"{large_w*large_h} - {small_w*small_h} = {area}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        side = random.randint(8, 14)
        radius = side // 2
        # Approximate: square - circle (using pi ≈ 3.14)
        sq_area = side * side
        latex = f"\\text{{Square (side {side}) with inscribed circle. Approx. area outside circle?}}"
        approx_circle = int(3.14 * radius * radius)
        area = sq_area - approx_circle
        return Equation(latex=latex, solution=f"\\approx {area} \\text{{ sq units}}", steps=[f"{sq_area} - {approx_circle} \\approx {area}"], difficulty='challenge')

def main():
    gen = AreaOfCompositeFiguresGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
