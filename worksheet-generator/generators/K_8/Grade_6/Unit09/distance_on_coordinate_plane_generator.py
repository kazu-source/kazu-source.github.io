"""Distance on Coordinate Plane Generator - Grade 6 Unit 9"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class DistanceOnCoordinatePlaneGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x, y1, y2 = random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)
        dist = abs(y2 - y1)
        latex = f"\\text{{Distance between }}({x}, {y1})\\text{{ and }}({x}, {y2})\\text{{?}}"
        return Equation(latex=latex, solution=f"{dist} \\text{{ units}}", steps=[f"|{y2} - {y1}| = {dist}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        x1, x2, y = random.randint(-8, 8), random.randint(-8, 8), random.randint(1, 8)
        dist = abs(x2 - x1)
        latex = f"\\text{{Distance between }}({x1}, {y})\\text{{ and }}({x2}, {y})\\text{{?}}"
        return Equation(latex=latex, solution=f"{dist} \\text{{ units}}", steps=[f"|{x2} - {x1}| = {dist}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
        x2, y2 = x1, y1 + random.randint(5, 12)
        dist = abs(y2 - y1)
        latex = f"\\text{{Distance from }}({x1}, {y1})\\text{{ to }}({x2}, {y2})\\text{{?}}"
        return Equation(latex=latex, solution=f"{dist} \\text{{ units}}", steps=[f"|{y2} - {y1}| = {dist}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        x1, y1 = random.randint(-8, 8), random.randint(-8, 8)
        x2, y2 = x1 + random.randint(3, 9), y1 + random.randint(4, 10)
        # Using Pythagorean theorem
        dx, dy = abs(x2 - x1), abs(y2 - y1)
        dist_sq = dx**2 + dy**2
        dist = round(dist_sq ** 0.5, 1)
        latex = f"\\text{{Approximate distance: }}({x1}, {y1})\\text{{ to }}({x2}, {y2})\\text{{?}}"
        return Equation(latex=latex, solution=f"\\approx {dist} \\text{{ units}}", steps=[f"\\sqrt{{{dx}^2 + {dy}^2}} \\approx {dist}"], difficulty='challenge')

def main():
    gen = DistanceOnCoordinatePlaneGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
