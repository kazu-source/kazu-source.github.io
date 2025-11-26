"""One Step Addition and Subtraction Equations Generator - Grade 6 Unit 7"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class OneStepAdditionAndSubtractionEquationsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x, b = random.randint(1, 15), random.randint(3, 12)
        latex = f"\\text{{Solve: }} x + {b} = {x+b}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"x = {x+b} - {b} = {x}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        x, b = random.randint(5, 20), random.randint(2, 10)
        latex = f"\\text{{Solve: }} x - {b} = {x-b}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"x = {x-b} + {b} = {x}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x, b = random.randint(-10, 20), random.randint(3, 15)
        latex = f"\\text{{Solve: }} {b} + x = {b+x}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"x = {b+x} - {b} = {x}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        x, b = random.randint(-15, 15), random.randint(5, 20)
        latex = f"\\text{{Solve: }} {b} - x = {b-x}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"x = {b} - {b-x} = {x}"], difficulty='challenge')

def main():
    gen = OneStepAdditionAndSubtractionEquationsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex} -> {p.solution}")
if __name__ == '__main__': main()
