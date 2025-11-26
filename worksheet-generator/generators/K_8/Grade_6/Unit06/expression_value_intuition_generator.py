"""Expression Value Intuition Generator - Grade 6 Unit 6"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class ExpressionValueIntuitionGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x = random.randint(2, 8)
        latex = f"\\text{{Which is greater: }} x + 5 \\text{{ or }} x \\text{{ when }} x = {x}\\text{{?}}"
        return Equation(latex=latex, solution="x + 5", steps=[f"{x} + 5 > {x}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        x = random.randint(1, 6)
        latex = f"\\text{{Which is greater: }} 2x \\text{{ or }} x \\text{{ when }} x = {x}\\text{{?}}"
        return Equation(latex=latex, solution="2x", steps=[f"2({x}) = {2*x} > {x}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x = random.randint(2, 5)
        val1, val2 = 3*x+2, 2*x+5
        comp = ">" if val1 > val2 else ("<" if val1 < val2 else "=")
        latex = f"\\text{{Compare: }} 3x+2 \\text{{ vs }} 2x+5 \\text{{ when }} x={x}"
        return Equation(latex=latex, solution=f"3x+2 {comp} 2x+5", steps=[f"{val1} {comp} {val2}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        x = random.randint(1, 4)
        vals = [(x**2, "x^2"), (2*x, "2x"), (x+3, "x+3")]
        vals.sort()
        latex = f"\\text{{Order: }} x^2, 2x, x+3 \\text{{ when }} x={x}"
        return Equation(latex=latex, solution=f"{vals[0][1]}, {vals[1][1]}, {vals[2][1]}", steps=["Ordered"], difficulty='challenge')

def main():
    gen = ExpressionValueIntuitionGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
