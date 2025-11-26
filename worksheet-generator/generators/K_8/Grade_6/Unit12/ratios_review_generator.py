"""Ratios Review Generator - Grade 6 Unit 12"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class RatiosReviewGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        a, b = random.randint(2, 8), random.randint(2, 8)
        latex = f"\\text{{Write ratio of {a} to {b}.}}"
        return Equation(latex=latex, solution=f"{a}:{b}", steps=[f"{a}:{b}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        a, b = random.randint(4, 12), random.randint(4, 12)
        from math import gcd
        g = gcd(a, b)
        latex = f"\\text{{Simplify ratio {a}:{b}.}}"
        return Equation(latex=latex, solution=f"{a//g}:{b//g}", steps=[f"GCD={g}, simplified: {a//g}:{b//g}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        distance, time = random.randint(60, 180), random.randint(2, 6)
        rate = distance / time
        latex = f"\\text{{Rate: {distance} miles in {time} hours. Miles per hour?}}"
        return Equation(latex=latex, solution=f"{rate:.0f} mph", steps=[f"{distance} \\div {time} = {rate:.0f}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        ratio_a, ratio_b = random.randint(2, 5), random.randint(2, 5)
        total_parts = ratio_a + ratio_b
        total = total_parts * random.randint(5, 10)
        part_a = (ratio_a * total) // total_parts
        latex = f"\\text{{Ratio is {ratio_a}:{ratio_b}. If total is {total}, find first part.}}"
        return Equation(latex=latex, solution=str(part_a), steps=[f"Part A = {ratio_a}/{total_parts} \\times {total} = {part_a}"], difficulty='challenge')

def main():
    gen = RatiosReviewGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
