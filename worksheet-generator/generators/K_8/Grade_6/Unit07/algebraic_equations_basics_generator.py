"""Algebraic Equations Basics Generator - Grade 6 Unit 7"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class AlgebraicEquationsBasicsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x, b = random.randint(1, 10), random.randint(3, 12)
        latex = f"\\text{{Is }} x = {x} \\text{{ a solution to }} x + {b} = {x+b}\\text{{?}}"
        return Equation(latex=latex, solution="Yes", steps=[f"{x} + {b} = {x+b}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        x, a = random.randint(2, 8), random.randint(2, 6)
        latex = f"\\text{{Is }} x = {x} \\text{{ a solution to }} {a}x = {a*x}\\text{{?}}"
        return Equation(latex=latex, solution="Yes", steps=[f"{a}({x}) = {a*x}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x, a, b = random.randint(2, 7), random.randint(2, 5), random.randint(3, 9)
        wrong_x = x + 1
        latex = f"\\text{{Is }} x = {wrong_x} \\text{{ a solution to }} {a}x + {b} = {a*x+b}\\text{{?}}"
        return Equation(latex=latex, solution="No", steps=[f"{a}({wrong_x}) + {b} = {a*wrong_x+b} \\neq {a*x+b}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        x, a, b, c = random.randint(2, 6), random.randint(2, 4), random.randint(2, 5), random.randint(1, 5)
        latex = f"\\text{{Find }} x \\text{{ if }} {a}x + {b} = {a*x+b}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"x = {x}"], difficulty='challenge')

def main():
    gen = AlgebraicEquationsBasicsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
