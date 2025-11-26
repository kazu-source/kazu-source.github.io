"""Four Quadrants Generator - Grade 6 Unit 9"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class FourQuadrantsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x, y = random.randint(1, 10), random.randint(1, 10)
        latex = f"\\text{{What quadrant is point }}({x}, {y})\\text{{ in?}}"
        return Equation(latex=latex, solution="Quadrant I", steps=["Both positive: Quadrant I"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        x, y = random.randint(-10, -1), random.randint(1, 10)
        latex = f"\\text{{What quadrant is point }}({x}, {y})\\text{{ in?}}"
        return Equation(latex=latex, solution="Quadrant II", steps=["x negative, y positive: Quadrant II"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x, y = random.randint(-10, -1), random.randint(-10, -1)
        latex = f"\\text{{What quadrant is point }}({x}, {y})\\text{{ in?}}"
        return Equation(latex=latex, solution="Quadrant III", steps=["Both negative: Quadrant III"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        x, y = random.randint(1, 10), random.randint(-10, -1)
        latex = f"\\text{{What quadrant is point }}({x}, {y})\\text{{ in?}}"
        return Equation(latex=latex, solution="Quadrant IV", steps=["x positive, y negative: Quadrant IV"], difficulty='challenge')

def main():
    gen = FourQuadrantsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
