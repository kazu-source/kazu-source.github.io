"""Greatest Common Factor Generator - Grade 6 Unit 6"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation
from math import gcd

class GreatestCommonFactorGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        factor = random.randint(2, 6)
        a, b = factor * random.randint(2, 5), factor * random.randint(2, 5)
        gcf = gcd(a, b)
        latex = f"\\text{{Find GCF of }}{a}\\text{{ and }}{b}"
        return Equation(latex=latex, solution=str(gcf), steps=[f"\\text{{GCF}} = {gcf}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        a, b = random.randint(6, 24), random.randint(6, 24)
        gcf = gcd(a, b)
        latex = f"\\text{{Find GCF of }}{a}\\text{{ and }}{b}"
        return Equation(latex=latex, solution=str(gcf), steps=[f"\\text{{GCF}} = {gcf}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        a, b, c = random.randint(8, 30), random.randint(8, 30), random.randint(8, 30)
        gcf = gcd(gcd(a, b), c)
        latex = f"\\text{{Find GCF of }}{a}, {b}, \\text{{ and }}{c}"
        return Equation(latex=latex, solution=str(gcf), steps=[f"\\text{{GCF}} = {gcf}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        a, b = random.randint(12, 48), random.randint(12, 48)
        gcf = gcd(a, b)
        latex = f"\\text{{Find GCF of }}{a}\\text{{ and }}{b}"
        return Equation(latex=latex, solution=str(gcf), steps=[f"\\text{{GCF}} = {gcf}"], difficulty='challenge')

def main():
    gen = GreatestCommonFactorGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex} = {p.solution}")
if __name__ == '__main__': main()
