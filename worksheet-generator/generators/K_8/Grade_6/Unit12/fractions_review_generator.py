"""Fractions Review Generator - Grade 6 Unit 12"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class FractionsReviewGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        num1, denom = random.randint(1, 5), random.choice([4, 6, 8])
        num2 = random.randint(1, 5)
        result_num = num1 + num2
        latex = f"\\text{{Add: }} \\frac{{{num1}}}{{{denom}}} + \\frac{{{num2}}}{{{denom}}}"
        from math import gcd
        g = gcd(result_num, denom)
        return Equation(latex=latex, solution=f"\\frac{{{result_num//g}}}{{{denom//g}}}", steps=[f"\\frac{{{result_num}}}{{{denom}}} = \\frac{{{result_num//g}}}{{{denom//g}}}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        num1, denom1 = random.randint(1, 4), random.choice([3, 4, 5])
        num2, denom2 = random.randint(1, 4), random.choice([3, 4, 5])
        result_num = num1 * num2
        result_denom = denom1 * denom2
        from math import gcd
        g = gcd(result_num, result_denom)
        latex = f"\\text{{Multiply: }} \\frac{{{num1}}}{{{denom1}}} \\times \\frac{{{num2}}}{{{denom2}}}"
        return Equation(latex=latex, solution=f"\\frac{{{result_num//g}}}{{{result_denom//g}}}", steps=[f"\\frac{{{result_num}}}{{{result_denom}}} = \\frac{{{result_num//g}}}{{{result_denom//g}}}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        num1, denom1 = random.randint(1, 4), random.choice([2, 3, 4])
        num2, denom2 = random.randint(1, 3), random.choice([2, 3, 4])
        result_num = num1 * denom2
        result_denom = denom1 * num2
        from math import gcd
        g = gcd(result_num, result_denom)
        latex = f"\\text{{Divide: }} \\frac{{{num1}}}{{{denom1}}} \\div \\frac{{{num2}}}{{{denom2}}}"
        return Equation(latex=latex, solution=f"\\frac{{{result_num//g}}}{{{result_denom//g}}}", steps=[f"\\frac{{{num1}}}{{{denom1}}} \\times \\frac{{{denom2}}}{{{num2}}} = \\frac{{{result_num//g}}}{{{result_denom//g}}}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        whole, num, denom = random.randint(2, 5), 1, random.choice([2, 3, 4])
        decimal = whole + num/denom
        latex = f"\\text{{Convert }} {whole}\\frac{{{num}}}{{{denom}}} \\text{{ to decimal.}}"
        return Equation(latex=latex, solution=str(decimal), steps=[f"{whole} + {num}/{denom} = {decimal}"], difficulty='challenge')

def main():
    gen = FractionsReviewGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
