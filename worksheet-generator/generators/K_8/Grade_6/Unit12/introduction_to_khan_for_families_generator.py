"""Introduction to Khan for Families Generator - Grade 6 Unit 12"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class IntroductionToKhanForFamiliesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        num = random.randint(10, 50)
        latex = f"\\text{{Practice problem: What is }} {num} \\div 5\\text{{?}}"
        return Equation(latex=latex, solution=str(num//5), steps=[f"{num} \\div 5 = {num//5}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        a, b = random.randint(2, 9), random.randint(2, 9)
        latex = f"\\text{{Review: Solve }} {a}x = {a*b}"
        return Equation(latex=latex, solution=f"x = {b}", steps=[f"x = {a*b} \\div {a} = {b}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        num, denom = random.randint(1, 5), random.choice([2, 4, 5])
        latex = f"\\text{{Convert }} \\frac{{{num}}}{{{denom}}} \\text{{ to decimal.}}"
        return Equation(latex=latex, solution=str(num/denom), steps=[f"{num} \\div {denom} = {num/denom}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        percent = random.choice([25, 50, 75])
        num = random.randint(20, 100)
        result = (percent * num) // 100
        latex = f"\\text{{What is {percent}\\% of {num}?}}"
        return Equation(latex=latex, solution=str(result), steps=[f"{percent}\\% \\times {num} = {result}"], difficulty='challenge')

def main():
    gen = IntroductionToKhanForFamiliesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
