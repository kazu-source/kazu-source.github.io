"""Intro to Inequalities with Variables Generator - Grade 6 Unit 7"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class IntroToInequalitiesWithVariablesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        val, test = random.randint(5, 15), random.randint(1, 10)
        result = "Yes" if test < val else "No"
        latex = f"\\text{{Is }} x = {test} \\text{{ a solution to }} x < {val}\\text{{?}}"
        return Equation(latex=latex, solution=result, steps=[f"{test} < {val}: {result}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        val = random.randint(8, 20)
        latex = f"\\text{{Write an inequality: }} x \\text{{ is greater than }} {val}"
        return Equation(latex=latex, solution=f"x > {val}", steps=[f"x > {val}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        val, test = random.randint(10, 25), random.randint(5, 30)
        result = "Yes" if test >= val else "No"
        latex = f"\\text{{Is }} x = {test} \\text{{ a solution to }} x \\geq {val}\\text{{?}}"
        return Equation(latex=latex, solution=result, steps=[f"{test} \\geq {val}: {result}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        val, a = random.randint(10, 30), random.randint(2, 6)
        latex = f"\\text{{Write inequality: }} {a}x \\text{{ is less than or equal to }} {val}"
        return Equation(latex=latex, solution=f"{a}x \\leq {val}", steps=[f"{a}x \\leq {val}"], difficulty='challenge')

def main():
    gen = IntroToInequalitiesWithVariablesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
