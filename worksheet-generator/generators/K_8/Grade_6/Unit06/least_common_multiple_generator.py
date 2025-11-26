"""Least Common Multiple Generator - Grade 6 Unit 6"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation
from math import gcd

class LeastCommonMultipleGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        a, b = random.randint(2, 6), random.randint(2, 6)
        lcm = abs(a * b) // gcd(a, b)
        latex = f"\\text{{Find LCM of }}{a}\\text{{ and }}{b}"
        return Equation(latex=latex, solution=str(lcm), steps=[f"\\text{{LCM}} = {lcm}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        a, b = random.randint(4, 12), random.randint(4, 12)
        lcm = abs(a * b) // gcd(a, b)
        latex = f"\\text{{Find LCM of }}{a}\\text{{ and }}{b}"
        return Equation(latex=latex, solution=str(lcm), steps=[f"\\text{{LCM}} = {lcm}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        a, b, c = random.randint(2, 8), random.randint(2, 8), random.randint(2, 8)
        lcm_ab = abs(a * b) // gcd(a, b)
        lcm = abs(lcm_ab * c) // gcd(lcm_ab, c)
        latex = f"\\text{{Find LCM of }}{a}, {b}, \\text{{ and }}{c}"
        return Equation(latex=latex, solution=str(lcm), steps=[f"\\text{{LCM}} = {lcm}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        a, b = random.randint(6, 15), random.randint(6, 15)
        lcm = abs(a * b) // gcd(a, b)
        latex = f"\\text{{Find LCM of }}{a}\\text{{ and }}{b}"
        return Equation(latex=latex, solution=str(lcm), steps=[f"\\text{{LCM}} = {lcm}"], difficulty='challenge')

def main():
    gen = LeastCommonMultipleGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex} = {p.solution}")
if __name__ == '__main__': main()
