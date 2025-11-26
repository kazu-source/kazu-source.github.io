"""Volume with Mini Cubes Generator - Grade 6 Unit 10"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class VolumeWithMiniCubesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        l, w, h = random.randint(2, 5), random.randint(2, 5), random.randint(2, 5)
        volume = l * w * h
        latex = f"\\text{{Rectangular prism: }}{l}\\times{w}\\times{h}\\text{{ unit cubes. Volume?}}"
        return Equation(latex=latex, solution=f"{volume} \\text{{ cubic units}}", steps=[f"{l} \\times {w} \\times {h} = {volume}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        l, w, h = random.randint(3, 8), random.randint(3, 8), random.randint(3, 8)
        volume = l * w * h
        latex = f"\\text{{How many unit cubes fit in }}{l}\\times{w}\\times{h}\\text{{ box?}}"
        return Equation(latex=latex, solution=str(volume), steps=[f"{l} \\times {w} \\times {h} = {volume}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        volume = random.randint(30, 100)
        l = random.randint(3, 8)
        w = random.randint(2, 6)
        h = volume // (l * w)
        if volume % (l * w) != 0:
            h = random.randint(2, 6)
            volume = l * w * h
        latex = f"\\text{{Volume is }}{volume}\\text{{ cubes. Base is }}{l}\\times{w}\\text{{. Height?}}"
        return Equation(latex=latex, solution=f"{h} \\text{{ units}}", steps=[f"h = {volume} \\div ({l} \\times {w}) = {h}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        side = random.randint(4, 10)
        volume = side ** 3
        latex = f"\\text{{Cube with edge }}{side}\\text{{ units. Volume?}}"
        return Equation(latex=latex, solution=f"{volume} \\text{{ cubic units}}", steps=[f"{side}^3 = {volume}"], difficulty='challenge')

def main():
    gen = VolumeWithMiniCubesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
