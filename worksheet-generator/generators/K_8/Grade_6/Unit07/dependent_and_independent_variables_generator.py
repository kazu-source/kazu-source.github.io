"""Dependent and Independent Variables Generator - Grade 6 Unit 7"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class DependentAndIndependentVariablesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        cost = random.randint(3, 12)
        latex = f"\\text{{Total cost = }}\\${cost} \\times \\text{{number of items. Which is independent?}}"
        return Equation(latex=latex, solution="number of items", steps=["Independent: number of items"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        rate = random.randint(40, 70)
        latex = f"\\text{{Distance = }}{rate} \\times \\text{{time. Which is dependent?}}"
        return Equation(latex=latex, solution="distance", steps=["Dependent: distance"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        latex = f"\\text{{Temperature depends on time of day. Identify dependent variable.}}"
        return Equation(latex=latex, solution="temperature", steps=["Dependent: temperature"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        latex = f"\\text{{Plant height depends on weeks of growth. Identify independent variable.}}"
        return Equation(latex=latex, solution="weeks", steps=["Independent: weeks"], difficulty='challenge')

def main():
    gen = DependentAndIndependentVariablesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
