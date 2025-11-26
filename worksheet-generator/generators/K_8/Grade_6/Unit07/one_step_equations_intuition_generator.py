"""One Step Equations Intuition Generator - Grade 6 Unit 7"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class OneStepEquationsIntuitionGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x, b = random.randint(1, 10), random.randint(3, 12)
        latex = f"\\text{{What number plus }}{b}\\text{{ equals }}{x+b}\\text{{?}}"
        return Equation(latex=latex, solution=str(x), steps=[f"x + {b} = {x+b}, \\text{{ so }} x = {x}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        x, a = random.randint(2, 8), random.randint(2, 6)
        latex = f"\\text{{What number times }}{a}\\text{{ equals }}{a*x}\\text{{?}}"
        return Equation(latex=latex, solution=str(x), steps=[f"{a}x = {a*x}, \\text{{ so }} x = {x}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x, b = random.randint(5, 15), random.randint(2, 8)
        latex = f"\\text{{What number minus }}{b}\\text{{ equals }}{x-b}\\text{{?}}"
        return Equation(latex=latex, solution=str(x), steps=[f"x - {b} = {x-b}, \\text{{ so }} x = {x}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        x, a = random.randint(6, 18), random.randint(2, 6)
        while x % a != 0:
            x = random.randint(6, 18)
        latex = f"\\text{{What number divided by }}{a}\\text{{ equals }}{x//a}\\text{{?}}"
        return Equation(latex=latex, solution=str(x), steps=[f"x \\div {a} = {x//a}, \\text{{ so }} x = {x}"], difficulty='challenge')

def main():
    gen = OneStepEquationsIntuitionGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex} = {p.solution}")
if __name__ == '__main__': main()
