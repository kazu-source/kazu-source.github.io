"""Volume with Fractions Generator - Grade 6 Unit 10"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class VolumeWithFractionsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        l, w = random.randint(2, 6), random.randint(2, 6)
        h_num, h_denom = 1, 2
        volume_num = l * w * h_num
        latex = f"\\text{{Prism: }}{l} \\times {w} \\times \\frac{{{h_num}}}{{{h_denom}}}\\text{{. Volume?}}"
        return Equation(latex=latex, solution=f"\\frac{{{volume_num}}}{{{h_denom}}} \\text{{ or }} {volume_num/h_denom}", steps=[f"{l} \\times {w} \\times \\frac{1}{2} = \\frac{{{volume_num}}}{{{h_denom}}}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        l_whole, l_num, l_denom = random.randint(2, 5), 1, 2
        w, h = random.randint(2, 5), random.randint(2, 5)
        l_improper = l_whole * l_denom + l_num
        volume_num = l_improper * w * h
        latex = f"\\text{{Box: }} {l_whole}\\frac{{{l_num}}}{{{l_denom}}} \\times {w} \\times {h}\\text{{. Volume?}}"
        return Equation(latex=latex, solution=f"\\frac{{{volume_num}}}{{{l_denom}}} \\text{{ or }} {volume_num/l_denom}", steps=[f"\\frac{{{l_improper}}}{{{l_denom}}} \\times {w} \\times {h} = \\frac{{{volume_num}}}{{{l_denom}}}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        l, w = random.choice([2, 3, 4, 6]), random.choice([2, 3, 4])
        h_num, h_denom = 3, 4
        volume_num = l * w * h_num
        latex = f"\\text{{Volume: }}{l} \\times {w} \\times \\frac{{{h_num}}}{{{h_denom}}}\\text{{?}}"
        return Equation(latex=latex, solution=f"\\frac{{{volume_num}}}{{{h_denom}}}", steps=[f"{l} \\times {w} \\times \\frac{{{h_num}}}{{{h_denom}}} = \\frac{{{volume_num}}}{{{h_denom}}}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        side_num, side_denom = random.choice([3, 5, 7]), 2
        volume_num = side_num ** 3
        volume_denom = side_denom ** 3
        latex = f"\\text{{Cube edge: }} \\frac{{{side_num}}}{{{side_denom}}}\\text{{. Volume?}}"
        return Equation(latex=latex, solution=f"\\frac{{{volume_num}}}{{{volume_denom}}}", steps=[f"\\left(\\frac{{{side_num}}}{{{side_denom}}}\\right)^3 = \\frac{{{volume_num}}}{{{volume_denom}}}"], difficulty='challenge')

def main():
    gen = VolumeWithFractionsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
