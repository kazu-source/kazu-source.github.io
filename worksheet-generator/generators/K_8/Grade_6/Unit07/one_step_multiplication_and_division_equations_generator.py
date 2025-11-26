"""One Step Multiplication and Division Equations Generator - Grade 6 Unit 7"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class OneStepMultiplicationAndDivisionEquationsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x, a = random.randint(2, 12), random.randint(2, 9)
        latex = f"\\text{{Solve: }} {a}x = {a*x}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"x = {a*x} \\div {a} = {x}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        a = random.randint(2, 8)
        x = random.randint(2, 15)
        result = a * x
        latex = f"\\text{{Solve: }} \\frac{{x}}{{{a}}} = {x}"
        return Equation(latex=latex, solution=f"x = {result}", steps=[f"x = {x} \\times {a} = {result}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x, a = random.randint(3, 18), random.randint(2, 9)
        latex = f"\\text{{Solve: }} {a}x = {a*x}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"x = {a*x} \\div {a} = {x}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        a = random.randint(3, 8)
        quotient = random.randint(4, 12)
        x = a * quotient
        latex = f"\\text{{Solve: }} \\frac{{x}}{{{a}}} = {quotient}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"x = {quotient} \\times {a} = {x}"], difficulty='challenge')

def main():
    gen = OneStepMultiplicationAndDivisionEquationsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex} -> {p.solution}")
if __name__ == '__main__': main()
